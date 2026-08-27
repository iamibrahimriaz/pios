# Engineering Presentation — slide plan

<!-- fill: This template is the REQUIRED STRUCTURE of the deck, not the deck. The artifact
     delivered is `presentation/engineering-kickoff.pptx`. Fill this plan first — it is where
     the thinking happens — then generate the file per engine/presentation.md.

     Do not deliver this markdown file as the artifact. It is a working document. Whether it
     is kept alongside the .pptx is the operator's choice; the .pptx is what the manifest
     requires. -->

| | |
| --- | --- |
| Run | «slug» |
| Date | «date» |
| Audience | Engineering manager · tech lead · engineers · QA · product. AI coding agents as supporting material |
| Duration | 10–15 minutes |
| Slides | 10–15 |
| Setting | Internal engineering kickoff |

---

# The rule this deck is built on

> **Derived, never re-researched.** Every figure here already exists in `deliverables/`. The
> deck selects and arranges; it establishes nothing.

**And one that is specific to this audience:**

> **What NOT to build gets equal weight to what to build.** An engineering audience will
> reconstruct the excluded scope from first principles within a month unless each exclusion
> arrives with its reason attached. A cut list without reasons is read as a backlog.

**If the run's verdict blocks the build, the first slide says so and the last slide says so.**
An engineering kickoff for work that is not authorized is a normal thing to hold — the team
needs to know what is coming — but a deck that does not say the gate is closed will be
remembered as approval.

---

# Slide plan

<!-- fill: one block per slide. `Says` is the single thing the slide must land. `Carries` is
     the content. `Notes` is what the presenter says out loud and does not put on the slide.

     Speaker notes are required on every slide. Write them as speech, not as a summary of the
     slide — a note that repeats the slide is a note nobody reads twice. -->

## 1 — Cover

| | |
| --- | --- |
| Says | «project name», «the research verdict verbatim», «confidence level» |
| Carries | The verdict as the largest text on the slide. Confidence, validation status, and whether any code exists |
| Notes | «open by saying whether this is authorized work or not — that is the single most important thing to land in the first minute» |

## 2 — Executive summary

| | |
| --- | --- |
| Says | «what the research changed» |
| Carries | What we found, beside what it means for us. Two columns |
| Notes | «» |

## 3 — Problem statement

| | |
| --- | --- |
| Says | «the root cause, not the symptom» |
| Carries | The causal chain as a visual. The cost of the problem, and whether it is established |
| Notes | «name the feature request this slide is the answer to — every project has one» |

## 4 — Research highlights

| | |
| --- | --- |
| Says | «the findings that changed the build» |
| Carries | A table: finding, evidence tag, what it changed. Not a list of facts — a list of consequences |
| Notes | «point at three rows; do not read the table» |

## 5 — Market and competitor summary

| | |
| --- | --- |
| Says | «who we are against, including the status quo» |
| Carries | Sizing with its standing. The competitor set. **The defensibility verdict, stated plainly** |
| Notes | «if the gap is not defensible, say the words. Engineers who learn it later stop trusting the deck» |

## 6 — Key findings

| | |
| --- | --- |
| Says | «the one insight the product is built on» |
| Carries | Where independent lines of research converged, and the metric that follows from it |
| Notes | «» |

## 7 — Product direction

| | |
| --- | --- |
| Says | «the product in one sentence» |
| Carries | The design principles, numbered. Each one decides an argument that will actually happen |
| Notes | «name the principle that overrules the others when they conflict» |

## 8 — MVP scope

| | |
| --- | --- |
| Says | «what we build, and what we refuse to build» |
| Carries | Two columns of equal size. **Every exclusion carries its reason** |
| Notes | «defend the two exclusions that will be argued with. Name them» |

## 9 — High-level system architecture

| | |
| --- | --- |
| Says | «the one structural property everything else follows from» |
| Carries | A diagram. Boundaries, the write path, and where state lives |
| Notes | «draw attention to the boundary, not the boxes» |

## 10 — Technical stack and engineering considerations

| | |
| --- | --- |
| Says | «each choice, with what it costs us» |
| Carries | Layer, choice, why and what it is worse at. Plus the rejected list with reasons |
| Notes | «the rejected list matters as much as the chosen list — it is where the next argument starts» |

## 11 — Risks and assumptions

| | |
| --- | --- |
| Says | «what would kill this, and which of it is behavioral rather than technical» |
| Carries | Risks with likelihood and position. Then the load-bearing assumptions with what happens if each is false |
| Notes | «if a risk is accepted rather than mitigated, say so in those words» |

## 12 — «the validation step» (Milestone Zero or equivalent)

| | |
| --- | --- |
| Says | «this is the gate on everything else in this deck» |
| Carries | The tests, the method, the days. The stop conditions, verbatim |
| Notes | «read the stop conditions out loud. They were set before the data was gathered, which is the only moment that can be done honestly» |

## 13 — Roadmap and development phases

| | |
| --- | --- |
| Says | «the sequence, and what gates each step» |
| Carries | A timeline visual, then a table of gates |
| Notes | «say which durations are estimates and which are counted. Treat the estimated ones as sequence, not schedule» |

## 14 — Open decisions

| | |
| --- | --- |
| Says | «what no amount of engineering produces» |
| Carries | Blocked work with an owner and the moment each bites |
| Notes | «these are things to ask about, not decide» |

## 15 — Engineering next steps

| | |
| --- | --- |
| Says | «what happens after this meeting» |
| Carries | What may be done now, what must wait, and what the entry file is for |
| Notes | «close on where the bottleneck actually is. If it is validation rather than engineering, say that as the last sentence of the meeting» |

---

# Visual requirements

**These are not decoration. Each replaces a paragraph nobody would read on a slide.**

| Required | Why |
| --- | --- |
| **A system diagram** | The architecture slide is unreadable as prose, and an engineer will redraw it on a whiteboard within a day anyway |
| **A milestone timeline** | Sequence and duration are spatial. A table of dates hides which things are parallel |
| **A workflow or critical-path diagram** | If the product has one interaction that everything else reads or writes, it gets drawn |
| **Tables instead of paragraphs** | Comparative content on a slide is a table. Prose on a slide is read instead of listened to |

---

# What this deck does not do

- **It does not re-open the research.** If it cannot be built honestly from `deliverables/`,
  the run is not finished — go back to the run.
- **It does not soften the verdict for its audience.** The framework's value is that its output
  is the same document whoever is reading it.
- **It does not replace the build handoff.** It points at it. An engineer who watched the deck
  and did not read `12-Build-Handoff.md` is not ready to build.
- **It does not edit a deliverable.** If building it shows a deliverable is wrong, say so and
  stop.

---

<!-- ACCEPTANCE — remove before delivery.

  [ ] 10–15 slides, sized for 10–15 minutes
  [ ] Cover states project, verdict and confidence
  [ ] What NOT to build has equal weight, and every exclusion carries its reason
  [ ] A system diagram and a milestone timeline are present as visuals
  [ ] Tables rather than paragraphs
  [ ] Risks and load-bearing assumptions named, with what happens if each is false
  [ ] The validation step is a slide of its own, with stop conditions verbatim
  [ ] Blocked work listed as things to ask about, not decide
  [ ] Every slide carries speaker notes, written as speech
  [ ] No shape falls outside the slide bounds — checked, not assumed
  [ ] Every figure traces to a deliverable
  [ ] Nothing in deliverables/ was edited to match the deck
-->
