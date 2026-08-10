# SPIKE Findings — platform-engineering-talk

**Date**: 2026-08-09
**Wave**: SPIKE (probe → walking skeleton)

## Assumption tested

> Can a full-length (60 min) conference deck be authored in the established Marp house style — single self-contained `.md`, inline CSS design system — and rendered to a viewable artifact fast enough to iterate on during drafting?

## Probe verdict

**WORKS.** The mechanism was validated in the preceding session rather than by a throwaway `/tmp/` probe, so no probe directory was created — the evidence already existed and re-probing would have been waste.

| Operation | Measured | Notes |
|---|---|---|
| `marp deck.md -o deck.html` | **0.5 s** (warm) | Sub-second — supports tight authoring loops |
| `marp deck.md --pdf` | **4.2 s** | Drives locally installed Google Chrome |
| `marp deck.md --pptx` | **2.0 s** | Available, not part of the house shipping format |
| First invocation on cold cache | **~90 s** | One-time; do not mistake for a hang |

## Edge cases discovered

1. **stdin hang** — `marp` blocks indefinitely when invoked non-interactively without `--no-stdin` (or `< /dev/null`). Observed: >2 min timeout with no output vs 0.5 s with the flag. This is the single most important operational finding; it is recorded in `CLAUDE.md`.
2. **Cold-start latency** — the first run prints nothing for ~90 s before succeeding. Killing it looks correct and is wrong.
3. **`ls -la` returns empty in this sandbox** — use `ls -a`. Unrelated to Marp but cost time twice.
4. **Base64 image weight** — the house style embeds images as data URIs. Decks reach 700–820 lines mostly base64, so whole-file reads/rewrites are wasteful; targeted edits only.
5. **No logo asset exists for this talk.** The reference decks carry base64 logo lockups. This deck uses a text lockup placeholder on the cover and `.slide-logo` is left unpopulated.

## Design implications for DESIGN

- **Single-file constraint holds** at 60-minute deck scale (~50 slides). No need to split into multiple decks or extract a shared theme; revisit only if a second deck must share the look.
- **The inline `<style>` block is the design system.** Restyling means editing that block, not adding a theme file.
- **Citation density is unusually high for this deck** (it is a history-of-evidence talk), so the theme needed a `.cite` component the reference decks do not have. Four new components were added: `.cite`, `section.statement`, `.era` year badge, `.map-grid` (road↔software mapping), plus a `.guess` flag for unverified draft content.
- **Speaker notes carry the evidence.** Fact-sensitive slides have the corrected wording and source in Marp presenter notes, keeping citations off the slides but available while presenting.
- **Research corrections are load-bearing on the content, not the mechanism.** All 9 corrections from `docs/research/platform-history/` are applied in the draft; see `wave-decisions.md`.

## Constraints discovered

- PDF export requires Chrome; it is present. A CI/headless environment would need `--browser-path` or a bundled Chromium.
- `--allow-local-files` is *not* needed while the house style embeds images as data URIs. Referencing local image paths later would introduce that flag as a new requirement.
- Three historical claims (1915 Detroit STOP sign, 1935 compulsory-test detail, Highway Code 1931) have **zero trusted sources** and are hedged or omitted in the draft. They cannot be strengthened without a source that does not appear to exist online.

## Promoted

**Promoted on 2026-08-09** into the walking skeleton — see `wave-decisions.md`.
