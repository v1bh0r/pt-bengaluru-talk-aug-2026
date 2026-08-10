# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Marp presentation — a platform-engineering talk given at **ProductTank Bengaluru** ("Product vs Platform: The Mindset Shift Every PM Needs"), one of three expert talks in that session, hosted at Booking Holdings' Bellandur office. Not a standalone "Platform Engineering Day" — that name was an earlier placeholder and has been corrected throughout. Decks are authored as Markdown and exported to HTML/PDF/PPTX via the Marp CLI.

**Current state:** `platform-engineering-talk.md` is the deck — 50 slides, ~4.2 MB (14 base64 images + 3 base64 logos), exported alongside as `.html` and `.pdf`. It is themed to the **ProductTank 2026 template** (see below). `platform-engineering-talk-prep.md` is the speaker's prep companion — the red-flag myth correction, anticipated pushback, the verification ledger, and delivery notes all live there, **not on slides**; prep material removed from the deck goes into that file, and slide-facing `.cite` lines carry clean sources only (no "CONFIRMED/CORRECTED" chatter). Wave artifacts live in `docs/feature/platform-engineering-talk/`, research in `docs/research/`, and the image pipeline in `tools/`. The repo is now under version control and pushed to [github.com/v1bh0r/pt-bengaluru-talk-aug-2026](https://github.com/v1bh0r/pt-bengaluru-talk-aug-2026); there is still no `package.json` — do not add one unless the author asks.

Because the deck is now mostly base64, **never read or rewrite it whole**. Use targeted edits, and locate slides with `python3 -c "...split('</style>')[1].split('\n---\n')"` rather than by line number.

## Toolchain

Marp CLI is installed **globally** (`@marp-team/marp-cli` v4.4.0 w/ marp-core v4.3.0) at `/usr/local/bin/marp`. There are no local npm dependencies and no `package.json` — do not add one unless the author asks. PDF/PPTX/image export drives the locally installed Google Chrome.

## Commands

Exports sit **alongside** the `.md` file sharing its basename — there is no `dist/` or build directory. The reference decks ship as `<name>.md` + `<name>.html` + `<name>.pdf` in one folder.

```bash
marp --no-stdin deck.md -o deck.html
```

```bash
marp --no-stdin deck.md --pdf -o deck.pdf
```

HTML and PDF are the two formats the author actually ships. PPTX is available if asked for:

```bash
marp --no-stdin deck.md --pptx -o deck.pptx
```

Live-reloading preview server while writing slides (watches for changes, serves the directory):

```bash
marp --no-stdin -s .
```

Export every slide as an image (useful for social posts or embedding single slides):

```bash
marp --no-stdin deck.md --images png -o slide.png
```

### Non-obvious gotchas

- **Always pass `--no-stdin`** (or redirect `< /dev/null`) when invoking `marp` non-interactively. Marp reads stdin by default, and in an agent/CI shell where stdin never closes it hangs indefinitely with no output. This was observed here: the same command hung past a 2-minute timeout without `--no-stdin` and completed in 0.5s with it.
- The **first** `marp` invocation on a cold cache can take ~90s before it prints anything. Subsequent runs are sub-second (HTML), ~2s (PPTX), ~4s (PDF). Don't kill a first run assuming it's stuck.
- `--allow-local-files` is required for PDF/PPTX/image export **only** if the deck references local files by path. The house style embeds images as base64 data URIs (see below), which avoids needing this flag entirely — prefer that.
- Marp writes nothing to stdout on success beyond two `[ INFO ]` lines; verify the output file exists rather than parsing output.
- `ls -la` returns empty in this sandbox. Use `ls -a` when listing directories. Bare `ls` is unreliable too — prefer `find . -type f`.
- **Marp strips `style` attributes from inline HTML.** `<div style="background-image: url(...)">` silently renders as an unstyled div — the markup survives, the attribute does not. Anything visual must be a CSS class in the inline `<style>` block. Diagnose by rendering to HTML and grepping the body, not by staring at the PNG.
- **`_backgroundImage` cannot be dimmed with `section::before`.** Marp's advanced-background layer paints above the section's own pseudo-elements, so a scrim drawn that way is invisible. See the full-bleed pattern below.
- Marp's base `section` sets `flex-direction: column`, so `align-items` on a slide class controls *horizontal* alignment. To bottom-align content use `justify-content: flex-end`.
- **Content slides are vertically centred unless you say otherwise, and `justify-content` alone will not fix it.** marp-core's default theme sets `place-content: safe center center` on `section` *while `display` is still `block`*. Modern Chrome honours `align-content` on block containers, so the centring is real even though nothing is a flex container. Top-aligning needs **both** `align-content: start` and `justify-content: flex-start` on `section`. Symptom: sparse slides start a third of the way down, dense ones start at the top.
- **Inside a flex `section`, an absolutely-positioned overlay sized by offsets collapses if it also has `overflow: hidden`.** `position:absolute; left:0; right:0; top:0; bottom:0; overflow:hidden` renders nothing — the box resolves to zero and clips its own contents. Same markup with `overflow: visible` works, and so does `top:0; left:0; width:100%; height:100%; overflow:hidden`. Always size full-slide overlays with explicit `width`/`height` (see `.arcs` and `.vbg`). Diagnose this by rendering a stripped-down test deck, not by reading the CSS — the cascade looks correct.

### Full-bleed image slides (`section.visual`)

The working pattern — one absolutely-positioned div, with the scrim and the photo composited in a single `background-image`:

```css
section.visual { position: relative; padding: 0; overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end; }
section.visual .vbg { position: absolute; left:0; right:0; top:0; bottom:0;
  z-index: 0; background-size: cover; background-position: center; }
.bg-<slug> { background-image: linear-gradient(to top, rgba(15,23,42,.95), rgba(15,23,42,.04) 70%), url(data:image/jpeg;base64,...); }
```

Slide markup is then just `<div class="vbg bg-<slug>"></div>` plus a `.vcap` caption block at `z-index: 2`.

### Diagrams

Seven Excalidraw diagrams carry ideas prose could not: the platform cycle (closed loop), the Roman road cross-section, McAdam vs Telford, coordination cost before/after the centreline, the sign-shape hierarchy, the scaled lag timeline, and the strangler-fig/FHIR architecture.

- **Sources** live in `assets/diagrams/*.excalidraw` and stay editable. Render with the `excalidraw-diagram` skill:
  `cd ~/.claude/skills/excalidraw-diagram/references && uv run python render_excalidraw.py <file>`
- **Embed** with `python3 tools/embed-diagram.py [slug]`. Put `<!--DIAGRAM:slug-->` (or `<!--DIAGRAM:slug:w75-->` for a width class) where the diagram belongs; the script quantises to PNG-8 and inlines base64. Re-running refreshes already-embedded diagrams in place, so you can re-render and re-embed without touching the deck by hand.
- **Style rules so they read as part of the deck**, not imports: `roughness: 0`, `roundness: null` (the theme has no border radius anywhere), `fontFamily: 2` (sans — the skill's default `3` is mono and clashes with Montserrat), and **never cyan on white** (`#21ccfa` is the on-dark accent only). Blue `#126cff` = what persists; lavender-grey `#c6c1db`/`#f4f3f8` = what is superseded; purple `#8b4bef` = the failure being named.
- **Height is what blows the slide budget**, not width. Keep diagrams under ~3:1 aspect or the type shrinks below legibility; use `.diagram.w90/.w80/.w75/.w65` to fit. If a diagram and its slide's text cannot both fit, cut text — do not shrink the diagram.
- **The skill's renderer needed a fix**: `references/render_template.html` imported Excalidraw from esm.sh, whose dependency graph 404s (`@braintree/sanitize-url`), hanging module load until timeout. Repointed at jsDelivr's `+esm` build.
- **Declare accurate text widths.** The renderer crops to the element bounding box, so text wider than its declared `width` gets clipped at the image edge.

### Sourcing images

`tools/fetch-commons-images.py` resolves a list of Wikimedia Commons file titles to compressed base64 data URIs and emits an attribution table. Gotchas it encodes:

- **`upload.wikimedia.org` returns HTTP 400 without a custom `User-Agent`**, and the response body is an HTML error page — a naive fetch yields a 2 KB "image" that passes a file-exists check.
- Resolve titles via `action=query&list=search&srnamespace=6`; **guessing `File:` names fails roughly 75% of the time.**
- Filter on `extmetadata.LicenseShortName` for PD/CC0/CC-BY. Historical transport imagery on Commons is overwhelmingly permissive, so this costs nothing and keeps provenance clean. CC BY-SA obliges share-alike on adaptations — keep the credits slide.
- **Always eyeball the results.** Search returns semantically wrong images that pass every mechanical filter (a NATO bunker for "traffic control centre").
- Compress with `magick -resize 1280x -quality 78 -strip` (~250–400 KB base64 each). **`sips -Z` inflates files on re-encode — do not use it.**
- ImageMagick has no usable font here: `montage -label` and `-annotate` fail with a FreeType error. Build contact sheets with `+append` / `-append`.
- No Ghostscript or poppler, so PDF pages cannot be rasterised. To inspect slides, render with `marp --images png` and read the PNGs.

## Deck architecture and house style

The author's established pattern — worth understanding before writing slides, because it inverts the usual Marp theme setup:

**One deck = one self-contained `.md` file.** No external theme CSS, no asset directory. A deck is portable as a single file.

### Palette — ProductTank 2026

The deck is themed to the official **ProductTank Slide Template - 2026** (`~/Downloads/ProductTank Slide Template - 2026.pdf`), which is both spec and reference. Its two hard rules are *Montserrat only* and *only colours from the theme row*:

| Token | Value | Role |
| --- | --- | --- |
| navy | `#17044a` | dark surfaces, and headings on light |
| ink | `#060119` | body copy on light |
| medium | `#c6c1db` | light surface tint, hairlines |
| blue | `#126cff` | THE accent — chips, rules, bullets, card borders |
| cyan | `#21ccfa` | links + emphasis **on dark only** (fails contrast on white) |
| indigo | `#4546e0` | the decorative arc motif, secondary borders |
| purple | `#8b4bef` | contrast/legacy items, sparingly |
| yellow | `#ebef23` | marker underline and the draft flag — very sparingly |

The template's own guidance, which the theme encodes: black on light, white on dark, **bold blue** for emphasis, zingy cyan for links. **Dark navy carries the moments** (cover, chapter divider, statement, photo, close); **white carries the density** (everything with a grid on it). No red or green anywhere — they are outside the theme row, so the old failure/success tints are now purple (the legacy assumption) and blue (the correction).

Projector rules still hold: headings are navy rather than coloured, never coloured text on a coloured background, nothing below ~0.55em, no mid-greys for anything the audience must read.

**Typography is Montserrat and nothing else.** Inter and JetBrains Mono were both removed — the template forbids a second family, so numerals in `.stat`, `.week-badge` and `.era` are Montserrat 700/800, not a monospace.

**Frontmatter is minimal; the theme lives inline.** Every deck opens with:

```markdown
---
marp: true
theme: default
paginate: true
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');
/* ~560 lines of deck CSS */
</style>
```

`theme: default` is a base to override, not a theme to use. The real design system is the ~560-line inline `<style>` block that follows — it restyles `section`, `h1`–`h3`, `p`, `ul li` (round blue bullets via `::before`), `strong`, `hr`, `section::after` (pagination) and `section::before` (the persistent ProductTank wordmark, bottom-left, white variant on dark slides). Montserrat is pulled from Google Fonts. If you are asked to restyle the deck, edit this block; do not introduce a separate theme file or `--theme-set` unless the project grows to multiple decks that must share a look.

Two brand marks are embedded as base64 in the style block and on the cover: the **ProductTank Chandigarh** wordmark (dark + white variants, from `~/Documents/product-tank-chd.github.io/assets/logos/`) and the **Trantor** logo (SVG data URI, from `~/Documents/Trantor-Logo_Color.svg`). The Trantor mark is teal `#388DA9` on grey `#90918C` — outside the ProductTank palette by necessity, so it only ever appears on the cover's white footer bar, never on navy.

**Slide types are CSS classes applied per-slide** with `<!-- _class: name -->` (note the leading underscore — scopes it to that one slide). The established set:

| Class | Purpose |
| --- | --- |
| `cover` | Title slide, **navy, no photograph** — `.arcs` motif, `.chip` label, `h1`, `.tagline`, `.speaker` (`.sp-name` / `.sp-role`), and a white `.cov-foot` bar carrying both organisation marks. A direct port of template p5; the arcs run larger here than on interior dark slides. |
| `section-header` | Chapter divider, **navy** — `.arcs` motif, `.section-num` chip, `h1`, `.marker` yellow underline, `p` |
| `profile` | Speaker/founder bio — `.profile-avatar` + `.profile-content` + `.profile-meta` (`.name`, `.title`). *Unused in this deck.* |
| `cta` | Closing slide, **navy** — `.arcs`, `h1`, `p`, `.contact-info` / `.contact-item` |
| `visual` | Full-bleed photograph — `.vbg` + `.bg-<slug>` background, `.vcap` caption with a `.vyear` blue chip. The opening transportation montage. |
| `statement` | Punchline slide, **navy** — `.arcs`, large `h1`, optional `p` |

Slides with no `_class` are ordinary content slides: white, top-aligned, `h2` + prose/grids.

**Multi-column layout is done with inline `<div>` grids**, not Marp's column syntax. Established components, each with matching CSS in the style block:

- `.chip` — the blue uppercase label. The template's single most recognisable element; `.section-num`, `.vyear` and `.era` are the same object in different positions.
- `.arcs` (+ nested `.dot`) — the concentric indigo rings and cyan disc bleeding off the right edge. Drop it in as the first child of any navy slide. Pure CSS, no image.
- `.marker` — the hand-drawn yellow underline. **Use sparingly**, per the template.
- `.cards-grid` > `.card` (each with `h3` + `p`)
- `.pillars-grid` > `.pillar` (with `.pillar-num`, `h3`, `p`; `.pillar.cyan` is the indigo variant)
- `.failure-grid` > `.failure-item` (purple, the legacy assumption) / `.good-item` (blue, the correction)
- `.timeline` > `.week` (with `.week-badge`)
- `.stat-row` > `.stat` and `.takeaway` are **navy blocks on white slides** — they are the deck's rhythm, not decoration
- `.era` (top-right chip), `.cite` (source line, sits above the wordmark), `.guess` (yellow draft flag)

Reuse these before inventing new ones — a new component means new CSS in the inline block.

### Odd lists — a hard authoring rule

**Every list, grid or stat row on a slide carries exactly 3 or 5 items. Never 2, 4, or 6.** Odd-numbered groups read as deliberate; even ones read as a list that got padded or truncated. If a slide grows to 4, either merge the two weakest members into one or find a defensible fifth. If it grows past 5, merge until it is 5.

The grids are sized for this: `.stat-row` and `.timeline` are 3-column; `.cards-grid` is 3-column with a `.cards-grid.two` modifier so a 5-point slide lays out as a 3-row plus a 2-row instead of stranding a lone third-width card. `.failure-grid` is 2-column and auto-spans its last child when the count is odd.

When forcing a count, **never invent a fact to reach five.** Merge instead, or derive the new item from figures already on the slide (slide 30's `1.8×` is the ratio of the two published FHWA figures, and its `.cite` says so). Reaching five by combining is always safe; reaching five by inventing is never.

**Images are embedded as base64 data URIs** in `<img src="data:image/png;base64,...">`. The reference decks carry ~10 such images each. This is why the decks are single-file portable and why `--allow-local-files` is never needed, at the cost of large `.md` files (700–820 lines, mostly base64). When editing these files, use targeted edits — do not read or rewrite whole files unnecessarily.

**Typical deck arc:** `cover` → `section-header` → content slides → `section-header` → content slides → `profile` → `cta`.

### Full-bleed pattern, restated for the navy scrim

Only `section.visual` uses `.vbg` + a `.bg-<slug>` class — the cover is photo-free. The scrim is `rgba(13,2,40,…)` — a *darkened* navy, not `#17044a` itself. Using the brand navy at low opacity casts the photographs magenta; the darkened value keeps the family without the tint. Fourteen `.bg-*` rules sit at the end of the style block, one per photograph, and each is ~350 KB — if a photo slide is deleted, delete its rule too or the file carries dead weight.

**Every photograph is attributed on the image-credits slide.** Removing a photo means removing its `<div><b>slug</b> — …</div>` line there as well; a credit for an image that is no longer in the deck is worse than no credit.

## Reference decks

Two complete decks in this style live in a sibling project — read these for concrete examples of any component above:

- `/Users/personal/Documents/projects/flowcraft-systems.github.io/presentations/enterprise-ai-readiness.md` (721 lines)
- `/Users/personal/Documents/projects/flowcraft-systems.github.io/presentations/adeptiv-ai-proposal.md` (822 lines)

Grep them for a class name rather than reading them start to finish; the first ~400 lines of each are the CSS block and the rest is heavily base64.
