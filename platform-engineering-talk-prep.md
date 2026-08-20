# Platform Thinking in the Real World — speaker prep

*People, Process & Mindset. The title you announced to the meetup group.*

Companion to `platform-engineering-talk.md`. Everything here used to live *on* slides or in verification cites; it is for your learning and preparation, not for the screen. Slides are referenced by title because numbers shift as the deck evolves.

---

## 0. The room (read this first)

**ProductTank Bengaluru**, at the meetup themed *"Product vs Platform: The Mindset Shift Every PM Needs"*. Hosted at Booking Holdings, RMZ Ecoworld, Bellandur. You are **one of three talks** in the 10:30–12:30 block, alongside speakers from Booking Holdings and Atlassian, with a separate hands-on workshop after lunch.

**The audience is mixed product managers and engineering leaders — not the platform-engineering audience this deck was originally written for.**

**Current running order** (so this does not have to be reconstructed from scattered notes again): Act 1, road history ending on the thesis ("Ahead of the scale") → the case study ("Then it was my system, behind the scale" through "We stopped re-deciding problems that were already solved") → the new-driver / AI-agent section ("What happens when the driver changes?" through "Somewhere around 1905") → Close ("What to do on Monday" → five questions → Thank you → Image credits). The case study now precedes the AI turn, not the other way round.

Three consequences, all already applied to the deck:

1. **From the two-column turn onwards, every engineer-facing claim has a product-facing twin in the same sentence or grid.** "Spec review *and* code review." "Quarterly roadmaps." "Estimates." "Approvals, sign-offs, review meetings." Read both halves and do not announce that you are doing it — the pairing works because nobody notices it happening.
2. **The case study keeps its engineering spine** (FHIR, ABP.io, the strangler fig, the five graduates) **and gains a translation into the currency a PM budgets in** — budget, velocity, and brownfield. The three lines that carry it:
   - *"Finance saw four bids for budget; the roadmap saw every estimate quietly growing."* — the whole product translation of the diagnosis. If a PM remembers one sentence from the case study, make it this one.
   - *"...your delivery estimates stop depending on which five people happen to be free."* — pays off the "estimates" assumption planted earlier.
   - *"...instead of the big-bang rewrite you keep being asked to fund."* — the single most valuable sentence in the deck for a PM on a legacy product. Say it slowly.
3. **Act 1 now runs 15 slides instead of 27** (deck: 50 → 37), for the same reason as the pairing above: you are talking to product managers rather than civil engineers. It came down in three passes.

   **Cut.** The Roman road cross-section diagram (the Appian Way keeps its takeaway), the **Macadam** slide and its construction diagram, the 1896 bridge photograph, the **MUTCD 1935 convergence** slide, and the **1903 driver-licences** slide. Every slide that stayed pays off later: Bertha sets up Monday question 4, the red flag question 2, eleven signs question 1, the centreline question 5, the capacity horizon question 3.

   **Folded in.** "A line painted on a road" (its own slide for the 1911 centreline) is gone — the reveal, the Hines credit, and the coordination mechanism it explained now open "Then, in twelve years" and its speaker note, so the room gets the same beats without a fourth consecutive content slide. The `04-coordination` diagram it carried is no longer embedded; its source stays in `assets/diagrams/` alongside the other cut diagrams.

   **Merged.** Seven photo beats now sit on the same slide as the detail that followed them — the Appian Way, Bertha, the scale curve, eleven signs, the Interstate, the interchange, and the 1911→1923 timeline with the sign shapes. The red-flag slide regained the early-car photograph as its hero band. Deliver a merged slide as one beat: headline over the photograph, a pause, then the body. Reading it as two costs you the merge.

   The interchange slide runs the other way round — the fatality numbers first, the photograph beneath them — because *"no driver out there is thinking about drainage"* has to be the last thing the room reads before the turn. Say the stats, land that sentence, then advance without a word.

   **Resequenced, twice.** The lag timeline and the thesis used to sit *behind* five slides of AI-agent material, so the room was asked to accept the parallel before it was told what the road record proves. They were moved to close Act 1. "And then a new participant arrived" was cut with that move; the two-column slide names the agents in its closing sentence, and its speaker note holds the five capability characteristics. The AI-agent section (now seven slides) was then moved a second time, from directly after the thesis to directly after the case study — see the running order above. It now follows the case study rather than the thesis, applying the same lesson a second time instead of extending the first argument.

   **Re-homed rather than dropped.** The 1903 ordering ("build the road first, encode the rules second, ask the driver to be competent third") is a takeaway on the timeline slide; the MUTCD's stated purpose is a clause in the sign-shapes caption. Three lines left the screen and belong to you now: "eight thousand to twenty-six point seven million, in thirty years"; "in roughly a decade the road went from carrying no information to carrying instructions a stranger could read at speed, in the dark, in a language they did not speak"; and the three Interstate standards (controlled access with grade-separated intersections, standardised lane widths, design speeds matched to terrain). §4's ledger still backs all of it.

**Act 3 gained a slide** — the re-org, between the strangler fig and the closing statement — so the case study now runs eight. It earns its place ahead of the FHIR slide for this room: it is the organisational proof that the boundaries were real, it answers the product half's "who do I go to for what", and its diagram carries it in about 40 seconds. The FHIR slide remains the pre-agreed cut.

**Slot length is unconfirmed.** Three talks in a two-hour block implies ~35–40 minutes gross each, against a deck budgeted for 60. The cover speaker note now carries both a 60-minute and a 35-minute timing plan, plus one **pre-agreed cut** — the FHIR slide, whose argument already survives on the diagnosis slide's third card and on the strangler-fig slide. Decide which plan you are running *before* you walk up, not on stage. **Confirm the real number with the organisers.**

---

## 1. The red-flag reversal (delivered verbally, no longer a slide)

The slide **"The man with the red flag"** sets up the story everyone recognises. The correction is now yours to deliver from the stage — the reversal is the most credibility-building 40 seconds in the talk, and it lands harder spoken than printed.

The popular version — "they responded to the car by making a man walk in front of it" — is **a story we tell about a thing that never happened**:

1. **The Act came 21 years *before* Benz's patent.** The Locomotives Act is 1865; the Benz Patent-Motorwagen is 1886. It was not a reaction to the automobile — the automobile did not exist yet.
2. **It targeted steam traction engines**, the heavy road locomotives of the day.
3. **Parliament had already walked it back** before the car mattered: the red flag requirement went in **1878** — eight years before the Motorwagen — and the escort and walking-pace limits went in **1896**.

Delivery: let the room enjoy the flag image for a second, then take it away. Be precise here — somebody in the room will know the real history, and being the one who corrects the myth (rather than the one caught repeating it) is the point of including it at all.

Why it earns its place: it is the talk's inoculation against "regulation strangles innovation" as a lazy reading. The lesson of 1865 is not "rules kill progress"; it is that rules written for the *previous* machine linger into the next one's era.

---

## 2. Anticipated pushback (formerly the "Where a sharp audience member will push back" slide)

Raise these yourself in Q&A if nobody else does — volunteering the strongest counter-arguments is the single highest-credibility move available in a talk like this.

- **"TCP/IP came first."** True. Standardised 1981–83; the Web arrived 1989–91. Here the platform *preceded* the innovation it enabled. Concede it cleanly.
- **"So did 1956."** Also true — AASHO completed the Interstate design standards the day the Act was signed, before anyone had built a mile of Interstate.
- **"Your model is accidents → standards."** If that were the model, it would be a terrible one — waiting for harm is not a strategy. **This is the important objection, and 1956 is the answer:** AASHO wrote the standards ahead of construction, from accumulated knowledge, without a fresh body count. You can skip the accidents.

Honest framing to keep in mind: the platform cycle *describes* what usually happens; it does not *prescribe* what should. The 1956 case is the existence proof that you can jump the queue.

---

## 3. Why "somewhere around 1905" (year verified)

The statement slide claims AI agents are at roughly **1905** in the road story. The year is deliberate and it checks out against the deck's own data:

- **After arrival, before the road answered.** The machine arrives 1886; the first piece of road-borne coordination (the centreline) is 1911. 1905 sits late in that gap.
- **Adoption compounding.** FHWA's MV-200 historical series (the same source as the scale-curve slide): ~8,000 US registrations in 1900, ~78,000 by 1905, ~458,000 by 1910 — roughly a doubling every 18–24 months. "The participant has arrived and adoption is compounding" is exactly the 1905 condition.
- **Coordination model still the previous generation's.** In 1905 the mechanism is still the policeman at the junction. Centreline 1911, electric signal 1914, sign shapes 1923.

If challenged with "why not 1908?" (Model T) — 1908 works too; the claim is "somewhere around", and the point is the window between arrival and answer, not a precise year. Do not defend the digit; defend the window.

---

## 4. Verification ledger (moved off the slides)

These notes were `.cite` lines on the slides. The slides now carry clean source lines; the confidence notes live here.

| Claim | Status |
| --- | --- |
| Appian Way construction began 312 BC | Verified against 3 trusted sources — confirmed, high confidence |
| McAdam's method and its diffusion | Confirmed. **No longer on a slide.** The coach photograph makes the point in one clause ("engineers kept making roads better and cheaper… they built all of them for the same traveller"). If you tell the fuller story anyway: **this is McAdam, not Telford.** Speakers conflate the two more often than they make any other error in this story, so keep them apart |
| Benz Motorwagen power output | Figures vary by source (0.75 hp / 0.68 PS commonly cited) — say "**less than one horsepower**", never a precise figure |
| Bertha Benz's drive | Corrected: **~106 km one way**, Mannheim → Pforzheim, August 1888. The commonly repeated "180 km round trip" is not supported by trusted sources |
| Locomotives Act 1865 framing | Corrected: predates the Benz patent by 21 years; targeted steam traction engines (see §1) |
| US vehicle registrations 1900/1920/1930 | FHWA Highway Statistics historical series (MV-200), verified directly against the primary source |
| "Eleven different signs for a single route" | Located verbatim in the FHWA highway history primary source |
| 1911 centreline, Edward N. Hines | Attribution verified |
| Sign shapes 1923 | Corrected: **Mississippi Valley Association of State Highway Departments, 1923** — not "1922 AASHO". AASHO's combining report followed in 1924; its manual in 1927 |
| First MUTCD 1935 | Confirmed; the quotation is MUTCD §1A.06 verbatim. **No longer its own slide**, compressed to a clause in the sign-shapes caption. The verbatim quotation has left the screen, so either paraphrase it or quote it word for word. Do not half-remember it |
| UK licences 1903 for identification | Confirmed (3 sources, incl. Hansard). **No longer its own slide**, now the "The order" takeaway on the 1911→1923 timeline. Deliberately hedged: nobody could verify the dates for compulsory testing or the published Highway Code against trusted sources, so do not improvise them |
| 1956 Act "called for uniform geometric and construction standards" | Corrected wording verified. AASHO wrote the standards; the federal authority adopted them. **Median separation and railway-grade-crossing removal do not appear in the primary source — do not claim them** |
| 1956 capacity horizon (designing for 1975) | FHWA primary source; the single strongest unused fact surfaced in research |
| Fatality-rate 1.8× | The ratio of the two published FHWA figures, not a third source — say so if asked |
| The re-org slide ("Then the org chart stopped matching the system") | **Verify your own tense before presenting.** This is the only slide sourced from your internal charts rather than the public record, and it is the easiest place in the deck to over-claim. If the new structure is still being executed, say "the structure we are moving to". The diagram is deliberately simplified — no headcounts, no product names — so the claim you are making on stage is only *teams were sliced by activity, now they are sliced by domain, and a platform function exists that did not before*. Defend that, not the chart |
| EVV / HIPAA specifics | HIPAA Security Rule 45 CFR §164.312(b) (audit controls); EVV mandated under the 21st Century Cures Act. **Verify before presenting:** EVV deadlines and framing vary by jurisdiction and payer |

---

## 5. The chronology choice in the breakdown section

The section now runs: scale curve → policeman ("the 1900s") → congestion ("the 1920s") → eleven signs → "Then, in twelve years" (1911→1923, opening on the centreline). The photo badges were softened from hard years ("1922", "before 1911") to decades so the on-screen years stay monotonic, and that timeline slide opens with "The fix was already on the road" — turning the one backward jump into a deliberate reveal: *the answer predates the breakdown*. The centreline no longer has a slide of its own; the reveal now leads straight into the timeline it belongs to. If anyone asks: the congestion photograph is from 1922; the policeman postcard is early-1900s Raphael Tuck & Sons.

---

## 6. Delivery notes worth rehearsing

(These also remain as HTML comments on their slides.)

- **Cover:** say the title and go. Do not explain what the talk is about. The title promises *people, process and mindset*, and you settle that debt at "The part that made it work", whose three pillars are those three words. Do not signpost it in advance. *"Ahead of the scale"* is still the thesis and still a delayed payoff, resolving at the thesis slide ~40 minutes in. It is no longer the phrase on the cover.
- **Act 1 rule:** stay in road language until the interchange photograph. No "platform", no "standards", no "golden path", no "deploy". The audience starts translating on its own around the coach slide; that silent translation is the whole mechanism. There is no line where you announce "this was about software all along" — the word itself still waits for the two-column slide. But the case study now sits between Act 1 and that slide, and it is openly technical, so by the time the two-column slide arrives the room already knows the subject; treat it as a naming, not a discovery. The two slides after the interchange (the lag timeline and the thesis) are the step up in altitude that earns the word "platform".
- **Pacing:** photo slides 8–12 seconds; trivia slides 45–60 seconds.
- **"Eleven signs":** pause on "every one of them technically correct." That is the line — nobody was wrong; the whole thing was still unusable.
- **Interstate slide:** do not draw the 1956→1975 parallel out loud. Ask the question, leave a real silence, move on. If you say it for them you have taken the best moment in the talk away from the audience.
- **"The obvious conclusion is wrong":** this and the thesis behind it close Act 1. Read one row of the table aloud — 1886 to 1911 is twenty-five years — and let the gap do the work. You are taking "so build the platform first" away from them before you ask them anything about a new driver.
- **"Ahead of the scale":** the thesis lands here, and this is the last slide of Act 1. Say it plainly: "that is the only claim in this talk I am willing to defend." The case study proves it next, with no AI agent anywhere in it; the new-driver material that follows the case study applies the same lesson a second time, not a different argument — if the room banks the thesis here, both the case study and the AI half cost you nothing to sell.
- **The two statements before Close:** three navy slides run consecutively into the section header, so differentiate the pair by pace, not volume. *"When the driver becomes less predictable…"* is the slow beat — it is a top-five takeaway and gets the full pause. *"Somewhere around 1905"* is the brisk one: positioning, not a second punchline; land "we do not have to wait for the accidents" and move, because it is the hinge into Close, where "what to do on Monday" turns that line into five concrete actions.
- **Homecare slide:** keep the sector context to ~30 seconds; the audience needs just enough to feel "there is no just-ship-it path". Be honest that the diagnosis was not day-one knowledge. Land the budget line — *"Finance saw four bids for budget; the roadmap saw every estimate quietly growing"* — because that is what makes the absence of boundaries a product problem rather than an engineering aesthetic (see §0).
- **"The part that made it work":** the most transferable slide. Consult people as advisors while the outcome is genuinely open — asking for an opinion is how you transfer ownership. Contrast with the red flag: imposed control gets worked around; co-designed control gets defended.
- **"Then the org chart stopped matching the system":** the third proof in an escalating sequence — the pilot proved it could be built, the strangler fig proved it worked in the real product, and the re-org proves the boundaries were real, because nobody reorganises around an aesthetic. Read the diagram in one move ("fifteen bars on the left become one band on the right") and stop; the number worth saying out loud is that the team owning that band is **two people** — the widest box on the chart, the smallest team on it; team-by-team detail is a Q&A answer, not a slide. The five labels in the blue band are the same five words as the diagnosis slide, so the callback lands without you pointing at it. See §4 for the tense you are allowed to use.
- **"We stopped re-deciding problems that were already solved":** the closing sentence — *"Decisions that live in the environment do not care who is driving."* — is the only line in the case study that points back at the new-driver question, and it is now also the pivot into it: say it last, pause, and advance straight into "What happens when the driver changes?" without explaining it. That section makes the connection explicit; unpacking it here means saying it twice.

---

## 7. Style note: "centreline"

Not a typo. The deck is written in British/Indian English throughout — *standardised, colour, programme, kilometres, optimised* — and **centreline** is the correct spelling in that register ("centerline" is the US form). The Excalidraw coordination diagram renders the same spelling, so changing the prose alone would make the deck internally inconsistent. For a Bengaluru audience, British spelling is the expected convention.
