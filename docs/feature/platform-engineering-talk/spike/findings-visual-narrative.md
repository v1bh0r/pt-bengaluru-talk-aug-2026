# SPIKE Findings — visual narrative pivot

**Date**: 2026-08-09
**Wave**: SPIKE (probe → promotion gate)
**Supersedes nothing** — this is a second probe against a new assumption, run after the deck's first walking skeleton already shipped. See `findings.md` for the first probe (Marp render loop).

## Assumption tested

> Can a wordless "evolution of transportation" image sequence be sourced programmatically — real photographs, permissively licensed, with attribution metadata — compressed and base64-embedded into the single-file Marp house style without blowing up the deck?

The narrative pivot itself is not the risky part. The **images** are: the house style forbids external asset paths (everything is a data URI), the deck currently contains **zero images**, and a Pixar-style opening is worthless with placeholder boxes.

## Probe verdict

**WORKS.**

| Step | Mechanism | Result |
|---|---|---|
| Resolve image by guessed filename | `commons.wikimedia.org/w/api.php?titles=File:...` | **Unreliable — 3/13 hit.** Guessing titles fails. |
| Resolve by **search** | `action=query&list=search&srnamespace=6` | **8/14 first pass, 13/14 after a retry with better terms** |
| License metadata | `iiprop=extmetadata` → `LicenseShortName` | Returned inline. Filterable to PD/CC0/CC-BY automatically. |
| Download | `upload.wikimedia.org` direct + custom User-Agent | **200 OK.** Default UA → **HTTP 400**; the UA header is mandatory. |
| Compress | `magick -resize 1200x -quality 82 -strip` | 580 KB → **281 KB**; base64 ≈ **375 KB/image** |
| `sips -Z` (macOS built-in) | rejected | *Increased* size on re-encode (829 KB b64). Use ImageMagick. |

Timing: full 14-image resolve pass ≈ **21 s**. Download + compress ≈ **1 s/image**.

## Edge cases discovered

1. **User-Agent is load-bearing.** `upload.wikimedia.org` returns HTTP 400 with an HTML error body — not a 403, and not an image — when the UA is curl's default. Silent failure mode: you get a 2 KB "image" that is an HTML document.
2. **Search relevance ≠ semantic correctness.** The API cheerfully returned `File:Joint Operations Centre Cannerberg.jpg` (a NATO bunker) for "traffic control centre" and an Australian town hall for "traffic congestion". **Every image needs a human/visual look before it goes in the deck.** This is the one step that cannot be automated away.
3. **Weight budget.** At ~375 KB base64/image, a 13-image sequence adds **~4.9 MB** to the `.md`. The deck is currently 58 KB. This changes the file's character: targeted edits become mandatory, not merely preferred.
4. **`--allow-local-files` still not needed** — data URIs keep the single-file portability property intact.
5. **Licensing is free here.** Historical transportation imagery on Commons is overwhelmingly public domain or CC-BY/CC0. Filtering to permissive licenses cost nothing and removed the question entirely, so the deck ships with clean provenance and a credits slide rather than an unresolved risk.

## Resolved image set (13/14)

| Slot | Commons file | License |
|---|---|---|
| Cart / the wheel | `Girl on bullock cart, Umaria district, MP, India.jpg` | CC BY-SA 4.0 |
| Roman road | `Via Appia Antica map.jpg` | Public domain |
| Stagecoach | `Fotoreproductie van het Wagentje van Dieges…jpg` | CC0 |
| Locomotive | `Stephenson Rocket at the National Railway Museum York.jpg` | CC0 |
| Motorwagen | `Patent-Motorwagen Nr.1 Benz 2.jpg` | CC BY-SA 3.0 |
| Bertha Benz | `Berthabenzportrait.jpg` | Public domain |
| Model T line | `Assembly line Ford T, 1923.jpg` | CC BY-SA 4.0 |
| Early motoring | `Charles Rolls driving a Peugeot 1896.jpg` | Public domain |
| Congestion | *weak match — needs re-curation* | CC BY-SA 2.0 |
| Interstate | `Interstate 75, Pontiac, Michigan.jpg` | CC BY-SA 2.0 |
| Autobahn | `Autobahn-RAB4-03-Rudolf-Knobloch-1935.jpg` | CC0 |
| Traffic control | *weak match — needs re-curation* | CC0 |
| Waymo | `Waymo self-driving car. (52194843144).jpg` | CC BY 2.0 |
| Lane markings | **unresolved** | — |

Two weak matches and one miss remain. All three are curation, not mechanism.

## Design implications

- **A full-bleed image slide type does not exist in the current theme.** The inline `<style>` block has no `section.visual` / `.full-bleed` component. The visual opening needs one new component (image as `background-image` on `section`, with an optional caption and era badge overlaid). This is the single largest CSS addition since the theme was written.
- **Slide budget is now the binding constraint.** The deck is already **69 slides against a 45–55 target**. A 10–13 slide visual opening plus a healthcare case study lands it near **90**. Something has to give, and that is a decision for the author, not an inference.
- **The healthcare case study resolves an open defect.** `wave-decisions.md` flags Part Twelve (People/Process/Mindset) as *"unowned content — my inference, highest-priority section to rewrite."* The author's FHIR/ABP.io homecare story is the real version of exactly that section.
- **Attribution needs a home.** CC-BY and CC-BY-SA images require credit. One end-of-deck credits slide covers all of them and costs nothing.

## Constraints discovered

- Image curation cannot be fully automated — semantic mismatches pass the license and resolution filters.
- No probe of *presentation timing* was run. Whether 90 slides fits 60 minutes is unknown and cannot be settled by reasoning; it needs a rehearsal.
- The repository is **still not a git repo**, so a 58 KB deck about to grow to ~5 MB remains unversioned.

## Promotion

**PROMOTED on 2026-08-09.** The probe was refactored into the deck itself: `section.visual` theme component, a 13-slide montage, the reveal, the road↔organisation map, and the homecare case study replacing Part Twelve. Probe directory `/tmp/spike_transport_deck/` deleted; the reusable half survives as `tools/fetch-commons-images.py`. See `wave-decisions-visual-narrative.md` for the decisions, the back-propagation fixes, and the ranked cut list.
