# SPIKE Decisions — visual narrative pivot

**Date**: 2026-08-09
**Wave**: SPIKE (second probe → promotion gate → walking skeleton)
**Relates to**: `findings-visual-narrative.md`. The first spike (`findings.md` / `wave-decisions.md`) validated the Marp authoring loop; this one validated programmatic image sourcing and executed the narrative restructure.

## Assumption Tested

- Can a wordless "evolution of transportation" image sequence be sourced programmatically — real photographs, permissively licensed, with attribution metadata — compressed and base64-embedded into the single-file Marp house style?

## Probe Verdict

- **WORKS.** Wikimedia Commons search API → license filter → download → ImageMagick compress → base64 data URI. 14/14 images landed at ~4.0 MB total. Full pipeline reproducible via `tools/fetch-commons-images.py`.
- Three mechanism defects were found and fixed during the probe, none of which were predictable by reasoning: see "Constraints Discovered".

## Promotion Decision

- **PROMOTE.** The mechanism worked and the narrative pivot had somewhere concrete to go. The deck was restructured in place.

## Interactive decisions captured

| Decision | Answer | Consequence |
|---|---|---|
| The two opening slides (Ferrari honesty hook, CNCF prior-art disclosure) | **Cut both entirely** | Deck opens cold on the montage. Created two dangling references that had to be repaired — see Back-propagation. |
| Visual treatment | **Full-bleed image + era badge** | New `section.visual` theme component; 13-slide wordless montage |
| Healthcare case study placement | **Replace Part Twelve** | Resolves the "unowned content" defect flagged in the first `wave-decisions.md` |
| Slide budget | **Add now, propose a ranked cut list** | Nothing removed silently. Cut list below. |

## Walking Skeleton

- **Driving adapter**: `marp --no-stdin platform-engineering-talk.md --pdf -o platform-engineering-talk.pdf`
- **User-visible output**: `platform-engineering-talk.pdf` (4.5 MB, 86 slides) and `.html` (4.5 MB)
- **Acceptance evidence**: all 86 slides rendered to PNG and a representative sample visually inspected — montage slides 2/6/10/14, the reveal (15), the road↔software map (16), and case study slides 74–80 and 85. Full-bleed backgrounds, gradient scrim, era badges, `.cards-grid`, `.timeline`, `.pillars-grid`, `.takeaway`, `.cite` and the two-column `.credits` all render with no overflow.
- **Demo command**:
  ```bash
  marp --no-stdin -s .
  ```
- **Commit**: **still blocked** — this directory is not a git repository. The deck is now 4.1 MB and represents substantially more work than at the first spike. `git init` is overdue.

## What changed in the deck

| # | Change | Slides |
|---|---|---|
| 1 | New `section.visual` full-bleed component + 14 `.bg-*` background classes in the inline `<style>` block | theme |
| 2 | 13-slide wordless transportation montage, cover → Waymo | 2–14 |
| 3 | Reveal statement: *"You have just watched the history of software engineering."* | 15 |
| 4 | Road ↔ organisation mapping via existing `.map-grid` | 16 |
| 5 | Ferrari honesty hook + CNCF prior-art slide **removed** | — |
| 6 | Part Twelve replaced with the homecare / FHIR / ABP.io case study | 73–80 |
| 7 | Image credits slide (all 14 attributions) | 85 |

## Back-propagation — contradictions the skeleton revealed

Cutting the opening broke two downstream slides that depended on it. Both are **fixed**, not merely noted:

1. **Part Eleven's headline** was *"I promised you a thesis I had to abandon"* — a promise made only by the deleted Ferrari slide. Reworded to *"The tidy conclusion — and why I had to abandon it"* with a standalone subtitle, so the reversal survives without the setup.
2. **"The claim I was going to make"** → *"The claim I nearly made"*, for the same reason.
3. **The CNCF prior-art inoculation was lost with its slide.** Rather than silently dropping it, the disclosure now lives as a scripted one-line verbal aside in the speaker notes of slide 16, with an explicit warning about what the first Q&A question will otherwise be. **This is a deliberate downgrade from a slide to a sentence, made on the author's instruction — it is a real reduction in cover, not an equivalent substitution.**
4. **The cover speaker note** still instructed "Do NOT open with a Ferrari" and carried a timing budget for the old structure. Rewritten with montage pacing (8–12 s/slide) and a revised 60-minute budget.

## ~~Slide budget — the ranked cut list~~ (SUPERSEDED by Revision 2 below)

The deck is **86 slides** against a 45–55 target. It may still fit: 13 montage slides run 8–12 s and ~15 `statement` slides run 10–15 s, so a rough estimate lands near **52 minutes** plus Q&A. That is an estimate, not a measurement — **it needs one timed rehearsal before it can be trusted.**

Cuts are ranked by (lowest value × highest time). Nothing here has been removed.

### Tier 1 — safe cuts, no argument lost (9 slides → 77)

| Slide | Title | Why it can go |
|---|---|---|
| 16 | Every one of those beats has a name you already use | The montage already made this visually. Its own speaker notes nominate it first. |
| 23 | What does not exist yet | Already flagged as a cut candidate in the first `wave-decisions.md`. |
| 28 | Remember this shape | Redundant with the statement slide immediately before it (27). |
| 34 | So let us be careful what we conclude | Hedging after 32 and 33 have already landed the point. |
| 43 | Then, very quickly | Timeline detail; 41 and 42 carry the argument. |
| 47 | Convergence | Overlaps 46 "Shape carries the meaning". |
| 56 | And it worked | Keep 55 "The detail nobody mentions"; this one restates it. |
| 61 | The same three generations, in platforms | The mapping appears elsewhere in the deck. |
| 71 | Where a sharp audience member will push back | Excellent material — but it is a Q&A answer, not a slide. Move to notes. |

### Tier 2 — montage trims, only if Tier 1 is not enough (3 slides → 74)

| Slide | Title | Why |
|---|---|---|
| 8 | 1896 · On infrastructure built for somebody else | Says the same thing as 6 (Motorwagen), and the reveal restates it again. |
| 4 | 1800s · Then almost nothing, for a very long time | A strong beat, but it can be narrated over slide 3 rather than shown. |
| 12 or 13 | Autobahn / interchange | Both say "mature platform". Keep whichever image plays better in the room. |

### Tier 3 — only under time pressure on the day

- 37 "Eleven signs for one route"
- 50 "Roads do not drive themselves"

**Recommendation**: take Tier 1 (→ 77 slides) as insurance, rehearse once with a timer, and only touch Tier 2 if the rehearsal runs past 55 minutes. Do not cut into the montage first — it is the part of the deck that is doing something the audience has not seen before.

## Design Implications

- **The montage is now the deck's highest-risk section.** It carries no text scaffolding, so it lives or dies on pacing. It cannot be rehearsed silently; it needs to be said out loud, once, against a clock.
- **The case study resolves the largest open defect.** Part Twelve is no longer inference — it is the author's own experience, and it is the only section of the talk that constitutes first-hand evidence.
- **Takeaway numbering shifted.** The case study introduces Takeaways #5 and #6; the pre-existing recap slide near the close still refers to "five takeaways" and must be reconciled.
- **CC BY-SA images impose share-alike on adaptations.** Presenting is unaffected; redistributing modified slides carries the same licence. The credits slide covers attribution.

## Constraints Discovered

- **Marp strips `style` attributes from inline HTML.** Per-slide background images therefore cannot be set with `<div style="background-image:...">`; they must be CSS classes in the theme block. Cost: two failed render iterations before the HTML was inspected.
- **Marp's `_backgroundImage` directive layers above `section::before`**, so a gradient scrim cannot be applied over it via pseudo-element. The working pattern is an absolutely-positioned `.vbg` div with `linear-gradient(...), url(...)` in a single `background-image`.
- **`upload.wikimedia.org` returns HTTP 400 without a custom User-Agent**, and the body is an HTML error page — so a naive fetch silently produces a 2 KB "image".
- **`sips -Z` increases file size on re-encode.** Use ImageMagick.
- **ImageMagick has no usable font in this environment** — `montage -label` and `-annotate` fail with a FreeType error. Use `+append`/`-append` for contact sheets.
- **Automated image search returns semantically wrong results that pass every mechanical filter** (a NATO bunker for "traffic control centre"). Visual review is mandatory and cannot be skipped.
- **No permissive traffic-control-room image exists on Commons** that survived filtering; a motorway interchange was substituted for that beat.
- **Still not a git repository.**

## Next Wave

**Handoff to**: DESIGN (`nw-design`). DESIGN owns (a) the timed rehearsal that settles the slide budget, (b) applying the cut list, and (c) reconciling the "five takeaways" recap against the two new ones.


---

# Revision 2 — trivia woven into Act 1, period-authentic imagery

**Date**: 2026-08-09 (same session)

## What the author asked for

1. Move the transportation trivia — previously in the detailed chapters from slide ~20 onward — **early**, interleaved between the hero images.
2. Make the software connection **subtle and obvious, using no software-engineering vocabulary** in the narrative.
3. Get into the case study directly afterwards.
4. Replace images that were not period-authentic (the modern bullock cart in particular) with historical photographs.

## What changed

**Act 1 rebuilt as 30 slides** alternating full-bleed period photographs with the researched trivia, told entirely in road language:

`bullock cart → Appian Way → the Appian trivia → stagecoach → macadam → rail → Motorwagen → its stats → Bertha → her 106 km → early motoring → red flag → the red-flag correction → assembly line → the scale curve → congestion → eleven signs → the policeman → the painted line → the 1911-23 decade → sign shapes → MUTCD → licences → autobahn → interstate → the 1956 standards → the 1975 capacity horizon → the fatality numbers → the finished interchange → REVEAL`

Every researched fact from the old chapters survives — Appian drainage, McAdam-not-Telford, <1 hp, 106 km, the 1865/1886 correction, 8,000→26.7M, eleven signs, Hines 1911, the 1923 shape hierarchy, the MUTCD §1A.06 quote, 1903 licences, AASHO, the 1975 horizon, 0.85 vs 1.53. Nothing was dropped; it was **re-voiced**.

**The explicit software-mapping slides were removed**, since their whole function was to say out loud what Act 1 now leaves the audience to work out: the road↔organisation `.map-grid`, "We already know how to say this in software", "Which brings us to your change advisory board", "You have seen this before", "The software equivalent is not subtle", "Which is exactly what happens as an org scales", "So what is a transportation platform, really?", "The same three generations, in platforms", and the ten `section-header` chapter dividers.

**Vocabulary discipline is now enforced and verified.** Act 1 contains no instance of *platform, standard, deploy, team, service, pipeline, golden path, review* or *backlog*. The only survivors of an automated scan are false positives (`steam`, `encode`, `Highway Code`, `engineering body`) and one deliberate plant: **"guardrails"** on the fatality slide, used in its literal road sense so the phrase is already loaded when the closing statement reuses it.

The **cover tagline was rewritten** — it previously read "...tells us about platform engineering...", which gave the reveal away before the montage began.

**The Waymo hero moved after the reveal**, so the driverless car is on screen at the exact moment the talk starts talking about agents.

## Imagery — period authenticity

Twelve of fourteen images are now contemporaneous with the beat they illustrate. Only the last two are modern, correctly so.

| Slot | Was | Now | Licence |
|---|---|---|---|
| opening | modern colour bullock cart, MP India | **A bullock cart in India, c. 1900** | CC BY 2.0 |
| Appian Way | modern colour photo | **ViaAppiaAntica, 1900** | Public domain |
| coach | — | **McLaughlin stagecoach, c. 1880s** | Public domain |
| rail | modern museum photo of Rocket | **Bury lithograph, Liverpool & Manchester Railway, 1831** | Public domain |
| Motorwagen | modern museum photo | **1885Benz — period photograph** | Public domain |
| coordination | (none) | **London policeman directing traffic** | Public domain |
| interstate | modern colour highway | **Southern Freeway construction, Balboa Park, 1964** | Public domain |
| interchange / Waymo | unchanged — modern by design | | |

Rejected during curation: museum shots of historical objects (they read as "object in a glass case", not "moment in time"), modern historical-marker plaques, and modern colour dirt roads.

## Slide budget — RESOLVED

**86 → 57 slides.** Collapsing the chapter structure did what the Tier 1/Tier 2 cut list was meant to do, and more. The deck is now at the **top of the original 45–55 target** with no further cuts pending.

Revised timing estimate: Act 1 ≈ 22 min (13 photo slides at 8–12 s, 17 trivia slides at 45–60 s), reveal + AI turn ≈ 12 min, thesis ≈ 6 min, case study ≈ 12 min, close ≈ 5 min → **≈ 57 min**. Still an estimate. Still needs one timed rehearsal.

## Reconciliation carried out

- **Takeaway #1** reworded in Act 1; the recap slide updated to match verbatim.
- **Takeaway #2** no longer has an originating slide — its source material (the centreline and the sign shapes) is now told in road language only. It is therefore *first stated in software terms on the recap slide*, deliberately, and the speaker notes say so.
- The dangling Ferrari/prior-art repairs from Revision 1 remain in force.

## Constraints Discovered (new)

- **Commons search is poor at period authenticity.** Queries for historical subjects return modern photographs of preserved objects, because those dominate the corpus. Adding a year to the query barely helps; naming the era's *medium* ("lithograph", "engraving") or a known archival collection works better.
- No permissively-licensed period photograph of **road-line painting** was found; the London policeman image replaced that beat and is dramatically better — it shows what the line *replaced* rather than the line itself.
- Splicing slides by string offset must re-insert **both** `\n---\n` delimiters. Dropping the trailing one silently merges two slides; it renders without error and is only visible in a slide index.

---

# Revision 3 — cover, title, and the last artwork removed

**Date**: 2026-08-09 (same session)

## Cover reimagined as a full-bleed slide

The cover was a flat purple gradient, which no longer matched a deck whose first act is thirty full-bleed photographs. It now uses the same `.vbg` machinery as `section.visual`, with a **purple-tinted scrim** rather than the neutral dark one so the brand identity survives.

Image: **Charles Cooper Henderson, "Mail Coaches on the Road: the Louth-London Royal Mail progressing at Speed"** (public domain) — recovered from the discarded stagecoach candidates. Deliberately a *painting*, so the cover reads as a different register from the photographic montage that follows.

The `.logo-lockup` was restyled to the monospace cyan badge used by `.vyear`, tying the cover to the era badges in Act 1.

## Title changed: "The Road Came First. Then Everything Broke." → **"Ahead of the Scale."**

**Why it had to change.** The old title asserted the exact claim Part Eleven exists to demolish — *"the platform had to come before the Ferrari"* — and Act 1 now opens on a rut captioned *"nobody built it."* The cover was arguing against the talk.

The new title is Takeaway #4 stated verbatim: *"The platform does not have to be ahead of the innovation. It has to be ahead of the scale."*

This converts a contradiction into a **delayed payoff**: the phrase means nothing on slide 1 and resolves at Part Eleven, ~40 minutes later. Speaker notes were added at both ends — the cover note says do not explain it, the Takeaway #4 note marks the moment it lands.

## Railway image: artwork → photograph

The 1831 Bury lithograph was replaced with **`Railroad1860`** (Charles Roscoe Savage, public domain) — a real photograph of a train crossing a timber trestle over a rocky gorge. It makes the beat's point far better than the lithograph did: rail could not use the existing roads, so it carried its own across ground nothing else could cross.

**Honesty note**: practical photography did not exist when the railways opened in 1830, so no contemporaneous photograph of that moment can exist. The era badge reads **"from 1830"** rather than a specific year, and a speaker note records that the image is c.1860. This is the one slide where image and badge are deliberately not the same date.

Every image in the deck is now a photograph except the cover, which is a painting by design.

## State

- **57 slides**, 15 embedded images, 4.3 MB `.md`, 4.5 MB PDF
- Stale `rail-old` credit entry removed after the swap; credits slide carries all 15 attributions
- Still not a git repository

---

# Revision 4 — light theme, single accent

**Date**: 2026-08-09 (same session)

## Why

Projector legibility. The previous theme leaned on purple (`#5b21b6`/`#7c3aed`), cyan (`#22d3ee`), gradients, and mid-grey body text (`#334155`, `#94a3b8`) — all of which wash out under a conference projector's low contrast ratio and ambient light.

## Palette — three colours plus neutrals

| Token | Value | Role | Contrast on white |
|---|---|---|---|
| ink | `#111827` | all headings, emphasis | 16.9:1 |
| body | `#1f2937` | body copy | ~13:1 |
| muted | `#6b7280` | citations and meta **only** — never body copy | ~5:1 |
| accent | `#1d4ed8` | the single accent: rules, labels, badges, bullets, callout borders | ~6.3:1 |
| dark | `#0f172a` | statement slides and photo scrims only | — |

**Purple, cyan and every gradient on content slides are gone.** Verified by scanning the stylesheet for all 21 legacy colour values — zero remain.

## Slide-type treatment

| Type | Before | After |
|---|---|---|
| content | white, purple headings | white, **near-black headings with a blue underline rule** |
| section-header | purple gradient, white text | **white with a 14px blue left bar**, blue mono chapter label |
| statement | dark navy | **unchanged — the deck's only dark slides**, now with a blue-tinted `em` |
| cta | purple gradient | **white with the blue left bar**, matching section headers |
| visual (photos) | dark scrim | scrim **re-tinted** from `rgba(2,6,23,…)` to `rgba(15,23,42,…)` |
| cover | purple-tinted scrim | **ink scrim** — the Henderson painting's warm tones now read properly |

All 15 base64 background rules were re-tinted programmatically; the image data itself was untouched.

## Legibility changes beyond colour

- Body copy darkened `#334155` → `#1f2937`; citations `#94a3b8` → `#6b7280`; credits `#64748b` → `#4b5563`
- Coloured text on coloured backgrounds eliminated — `.failure-item` and `.good-item` keep their red/green tint but now carry **near-black text** instead of dark-red/dark-green
- Small type bumped where it was marginal: `.cite` 0.56→0.60em, `.credits` 0.53→0.56em, `.stat-key` 0.68→0.70em, card copy 0.82→0.85em
- `h2` underline strengthened to a 3px accent rule so section breaks survive projector blur
- Pagination weight raised 500→600

## Title

Confirmed as **"Ahead of the Scale."** — the author reviewed alternatives (*Paved for Horses*, *The Driver Changed. The Road Didn't.*, *Built for Somebody Else.*) and kept the thesis-as-title with its delayed payoff at Takeaway #4.

## State

- **57 slides**, 15 images, 4.3 MB `.md`, 4.5 MB PDF, renders in ~1 s (HTML) / ~5 s (PDF)
- Still not a git repository

---

# Revision 5 — transition rework, and Revision 6 — diagrams

**Date**: 2026-08-09 (same session)

## Revision 5: the reveal removed, the transition rebuilt

The author cut the explicit reveal (*"You have just watched the history of software engineering"*) and the two Part Eleven setup slides, and asked for a cleaner hand-off out of Takeaway #3.

- **The turn is now gradual.** There is no announcement slide. The sequence is: *"What happens when the driver changes?"* → the driverless car → the two-column table where the word "software" first appears in print. The audience arrives before the speaker does; speaker notes at all three points say explicitly **do not announce it**.
- **New bridge slide** — *"The obvious conclusion is wrong"* names the conclusion the room is forming ("so build the road first") and refutes it with dates they watched as full slides in Act 1.
- **Thesis slide rewritten** to stand alone as *"Ahead of the scale"*, since it no longer follows a claim being retracted.
- **`Part Twelve` was orphaned** once Part Eleven was cut (Parts One–Ten had already gone in the Act 1 rebuild), so it became `The part that is mine`. **Numbered part labels do not survive structural edits** — a recurring hazard in this deck.

## Revision 6: seven diagrams

Built with the `excalidraw-diagram` skill, sources in `assets/diagrams/`, embedded via `tools/embed-diagram.py`.

| # | Diagram | Slide | Replaces |
|---|---|---|---|
| 1 | platform cycle (closed loop) | Ahead of the scale | a one-line text cycle that could not show the loop closing |
| 2 | Roman road cross-section | The Appian Way | two bullets |
| 3 | McAdam vs Telford | Macadam | the blockquote warning + two paragraphs |
| 4 | coordination cost, before/after | A line painted on a road | a closing paragraph |
| 5 | sign shape hierarchy | Shape carries the meaning | the prose description |
| 6 | lag timeline, drawn to scale | The obvious conclusion is wrong | the `.map-grid` table |
| 7 | strangler fig / FHIR R4 | Then we did it to the real product | a three-card grid |

Diagram 7 carries real FHIR resource names (`Patient`, `Encounter`, `Observation`, `CarePlan`, `Practitioner`, `Questionnaire`) plus LOINC, rather than generic boxes — the author will present it to people who know the spec.

## Incident: a slide was lost and restored

**During this work the rail slide (the 1860 trestle photograph, "Then something far faster arrived, and built its own road") was deleted from the deck.** It was caught by a slide-count check — 55 dropped to 54 — and traced by binary-comparing successive PNG renders to find the first divergent slide.

Restored in full: markup, speaker notes, the `.bg-rail` CSS rule, and the original photograph (`Construction train Bear River, Union Pacific Railroad`, Andrew J. Russell, public domain) identified by matching against the pre-loss render.

Two follow-on findings:
- **`rail` was missing from the image credits** even before the loss. Added.
- A first repair attempt **silently no-op'd**: the regex could not span the `rgba(...)` commas inside the scrim gradient, and the script printed success without verifying. Any scripted edit to this deck must **assert that the content actually changed**, not just that the script ran.

## Constraints Discovered

- **esm.sh serves a broken dependency graph for `@excalidraw/excalidraw`** (`@braintree/sanitize-url` 404s), hanging the renderer until timeout. Fixed by repointing the skill's template at jsDelivr.
- **Marp strips `data-*` attributes** from inline HTML as well as `style` — but keeps `class`, `alt` and `src`. The embed script's refresh logic therefore reads slugs from the markdown, never from the rendered HTML.
- **Diagram height, not width, is the binding constraint.** Anything past ~3:1 aspect forces the type below legibility once scaled to fit a slide.
- **Line art quantises extremely well**: PNG-8 at 64 colours is ~25–55 KB per diagram, roughly an eighth of the raw render. All seven added ~280 KB, not the ~1 MB estimated.

## State

- **56 slides**, 15 photographs + 7 diagrams, 4.3 MB `.md`, 4.5 MB PDF
- Still not a git repository
