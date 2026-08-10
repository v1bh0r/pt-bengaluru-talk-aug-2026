# SPIKE Decisions — platform-engineering-talk

**Date**: 2026-08-09

## Assumption Tested

- Can a 60-minute conference deck be authored in the established Marp house style (single self-contained `.md`, inline CSS design system) and rendered to a viewable artifact fast enough to iterate on while drafting?

## Probe Verdict

- **WORKS**: Marp renders the full 69-slide deck to HTML in 1.2 s and to PDF in 3.3 s. The single-file + inline-CSS house style holds at full talk scale. See `findings.md`.
- No `/tmp/spike_*` probe directory was created — the mechanism had already been measured in the preceding session, and re-probing would have been waste. This is a deliberate deviation from the skill's default and is recorded here rather than hidden.

## Promotion Decision

- **PROMOTE**. The mechanism works and the content had somewhere to go: a rendered deck is exactly the artifact needed to evaluate narrative flow, which no amount of outline review substitutes for.

## Interactive decisions captured

| Decision | Answer | Consequence |
|---|---|---|
| Slot length | **60 min** | Slide budget ~45–55; actual draft came in at **69** (over budget — see Constraints) |
| Draft scope | **Full talk skeleton** | Every section exists end-to-end; no section left as a bare stub |
| Missing content (People/Process/Mindset, takeaways) | **Draft my best guess** | Part Twelve + the Monday slide are my inference, visibly flagged with a `.guess` badge on-slide |

## Walking Skeleton

- **Driving adapter (entry point)**: `marp --no-stdin platform-engineering-talk.md --pdf -o platform-engineering-talk.pdf`
- **User-visible output**: `platform-engineering-talk.pdf` (1.0 MB, 69 slides) and `platform-engineering-talk.html` (194 KB)
- **Acceptance evidence**: rendered PNGs of slides 1, 3, 61, 67 visually inspected — cover gradient, `.cards-grid`, `.cite` footer, `.era` badge, `.guess` flag, pagination and the 5-item compact recap all render correctly with no overflow.
- **Demo command**:
  ```bash
  marp --no-stdin -s .
  ```
- **Commit**: not committed — this directory is **not a git repository**. `git init` is a prerequisite before the conventional-commit step in the skill's checklist can be satisfied.

## Deviation from the skill's Definition of Done

The skill's Phase 3 DoD assumes a software feature: a `.feature` acceptance test under `tests/`, code under `src/`, a conventional commit. None of those map onto a presentation deliverable. Substituted equivalents:

| Skill DoD item | Substituted evidence |
|---|---|
| `@walking_skeleton` acceptance test green | Deck renders to PDF + HTML with exit 0; four representative slides visually verified |
| Code in `src/` | Deck at repo root per house style (`CLAUDE.md`: exports sit alongside the `.md`) |
| Committed with conventional message | **Blocked** — not a git repo |
| Probe directory deleted | N/A — no probe directory created |

## Design Implications for DESIGN

- **Slide count is over budget**: 69 slides against a 45–55 target. Many are `section.statement` punchlines that consume 10–20 s, so the deck may still land inside 60 min — but this needs a timed rehearsal, not an estimate. DESIGN should decide what to cut; candidates are the Part Two "what does not exist yet" slide, the "remember this shape" slide (redundant with the statement before it), and one of the two guardrail contrast slides.
- **Part Twelve is unowned content.** People/Process/Mindset and the four Monday questions are my inference. They are structurally sound but not the author's argument. This is the highest-priority section to rewrite.
- **Four new theme components** were added beyond the reference decks: `.cite`, `section.statement`, `.era`, `.map-grid`, plus `.takeaway`/`.takeaway.compact` and `.guess`. If a second deck ever needs this look, extract the style block to a shared theme at that point — not before.
- **Evidence lives in speaker notes**, not on slides. Every corrected claim carries its correction and reasoning in the presenter notes, so the deck stays clean while the author retains the citation at the podium.

## Constraints Discovered

- **Three claims cannot be strengthened**: the 1915 Detroit STOP sign, the 1935 compulsory-driving-test detail, and the 1931 Highway Code have zero trusted sources. The 1915 stop sign was **removed** from the deck and replaced with the well-sourced 1923 shape standardisation; the other two are stated without dates. No further research will fix this.
- **Cover assets missing**: no event logo exists as a base64 data URI, so the cover uses a text lockup. Slides link and contact details are `TODO`.
- **Not a git repository**, so nothing in this project is version-controlled yet — including a 58 KB deck that now represents several hours of work.
- **PDF export depends on local Chrome.** Fine on this machine; a headless/CI render would need `--browser-path` or a bundled Chromium.

## Research corrections applied

All nine corrections from `docs/research/platform-history/road-infrastructure-platform-analogy-research.md` are baked into the draft:

1. Bertha Benz — **106 km one way**, not a 180 km round trip
2. Red flag — reframed as **stale, not strict** control; 1865 Act predates the Benz patent by 21 years, targeted steam traction engines, red flag repealed 1878
3. Sign shapes — **1923, Mississippi Valley Association**, not 1922 AASHO
4. 1956 Act — **called for** uniform standards; **AASHO wrote them**; median separation and rail-crossing removal dropped
5. Benz power — **"less than one horsepower"**
6. Cleveland 1914 — qualified as **"first permanent electric… in the United States"**
7. 1915 STOP sign **removed**; UK testing/Highway Code dates **hedged**
8. Uniformity rationale — replaced with verbatim **MUTCD §1A.06** quote
9. AI-agent claims — **no statistics quoted**; argument rests on capability characteristics, per thin evidence base

Plus two additions research surfaced that the original narrative lacked: the **1900 baseline of 8,000 vehicles** (making the scale curve far stronger spoken aloud) and the **1956 capacity horizon** designed for 1975 traffic.

## Next Wave

**Handoff to**: DESIGN (`nw-design`) — the deck is a fait accompli. DESIGN decides the cut list to hit 60 minutes and owns rewriting Part Twelve.
