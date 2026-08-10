#!/usr/bin/env python3
"""Expand diagram placeholders in the deck into inline base64 <img> tags.

Put a placeholder where the diagram belongs:

    <!--DIAGRAM:01-platform-cycle-->

then run this script. It renders nothing itself — it expects
assets/diagrams/<slug>.png to already exist (produced by the excalidraw-diagram
skill's render script) — optimises it, base64-encodes it, and replaces the
placeholder in place.

Re-running is safe: already-expanded diagrams are matched by their data-slug
attribute and their base64 payload is refreshed, so you can re-render a
diagram and re-embed without hand-editing the deck.

    python3 tools/embed-diagram.py                 # expand/refresh everything
    python3 tools/embed-diagram.py 01-platform-cycle  # just one

Why quantised PNG-8: these are flat-colour line drawings, so a 64-colour
palette is visually lossless and roughly 8x smaller than the raw render
(~25 KB vs ~200 KB at 2000px wide).
"""
import base64, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "platform-engineering-talk.md"
DIAGRAMS = ROOT / "assets" / "diagrams"
WIDTH = 2000          # embedded pixel width; slides display it at ~1050 CSS px
COLORS = 64

def optimise(src: Path) -> bytes:
    out = src.with_name(src.stem + ".opt.png")
    subprocess.run(
        ["magick", str(src), "-resize", f"{WIDTH}x", "-colors", str(COLORS),
         "-strip", f"PNG8:{out}"],
        check=True, capture_output=True)
    data = out.read_bytes()
    out.unlink()
    return data

def img_tag(slug: str, b64: str, cls: str = "diagram") -> str:
    return (f'<img class="{cls}" data-slug="{slug}" alt="{slug.replace("-", " ")}" '
            f'src="data:image/png;base64,{b64}">')

def main(only: str | None = None) -> None:
    deck = DECK.read_text()
    done, missing = [], []

    # placeholders may carry extra classes: <!--DIAGRAM:slug:w75-->
    placeholders = dict(re.findall(r'<!--DIAGRAM:([a-z0-9-]+)(?::([a-z0-9 ]+))?-->', deck))
    slugs = [only] if only else sorted(
        set(placeholders)
        | set(re.findall(r'<img class="diagram[^"]*" data-slug="([a-z0-9-]+)"', deck)))

    for slug in slugs:
        png = DIAGRAMS / f"{slug}.png"
        if not png.exists():
            missing.append(slug)
            continue
        b64 = base64.b64encode(optimise(png)).decode()

        extra = placeholders.get(slug) or ""
        cls = ("diagram " + extra).strip() if extra else "diagram"
        placeholder = f'<!--DIAGRAM:{slug}:{extra}-->' if extra else f'<!--DIAGRAM:{slug}-->'
        if placeholder in deck:
            deck = deck.replace(placeholder, img_tag(slug, b64, cls))
        else:
            # refresh an already-embedded diagram, preserving its class list
            pat = re.compile(r'<img class="(diagram[^"]*)" data-slug="' + re.escape(slug) + r'"[^>]*>')
            m = pat.search(deck)
            if not m:
                missing.append(slug + " (no placeholder and not embedded)")
                continue
            deck = pat.sub(lambda mm: img_tag(slug, b64, mm.group(1)), deck, count=1)
        done.append(f"{slug}: {len(b64)//1024} KB base64")

    DECK.write_text(deck)
    for line in done:
        print("  embedded", line)
    for m in missing:
        print("  MISSING ", m)
    print(f"deck now {DECK.stat().st_size/1024/1024:.2f} MB")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
