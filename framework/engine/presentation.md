# Presentation — the deck the engineering team is briefed from

A completed run produces a specification. **A specification is not a briefing.** An engineer
handed sixteen documents and told to start reads the first two, forms a model of the product
from them, and reconstructs the rest from assumption — and the assumptions they reconstruct are
the ones the research spent the most effort ruling out.

The specification answers *what to build*. **It does not answer, in a form a room can absorb in
fifteen minutes, why this project exists, what the research actually found, what is deliberately
excluded, and what is not yet allowed to start.** Those four things decide how a team behaves in
its first month, and none of them survives being buried in a document.

**The deck is not a summary of the handoff.** It is the briefing that makes the handoff land — a
different job for a different setting, and the two are not interchangeable.

---

## When it runs

**Every completed run, automatically.** It is a required completion artifact in
`deliverables/manifest.yaml`, alongside the proposal and the entry file. It is not offered and it
is not conditional.

**A run that reached "do not build" still produces it**, and the deck says so on the first slide
and the last. A team that will be asked to build this eventually needs to know what is coming and
why it has not started; a deck that omits the closed gate will be remembered as approval.

---

## What this step produces

**One `.pptx` file**, written to `projects/<slug>/presentation/engineering-kickoff.pptx`.

**10–15 slides, for a 10–15 minute internal kickoff.** Modern, minimal, professional. Tables
rather than paragraphs, diagrams rather than descriptions of diagrams, and **speaker notes on
every slide.**

**Fill `deliverables/templates/18-Engineering-Presentation.md` first.** It is the slide plan and
it is where the thinking happens. Generating slides directly produces a deck whose structure is
whatever came to mind in order.

**Never write into `deliverables/`, and never edit a deliverable to match the deck.** If building
it reveals that a deliverable is wrong, say so and stop.

---

## The rule that keeps it honest

> **Derived, never re-researched.**
>
> Every figure, verdict and risk in the deck already exists in the artifact set. The deck
> **selects and arranges**; it does not establish.

If a slide needs a number no artifact carries, **that is a finding, not a gap to fill.** Say the
figure is not established. A number invented at deck-building time arrives with no evidence tag,
in the artifact most likely to be screenshotted and pasted into a channel.

---

## The rule specific to this audience

> **What NOT to build gets equal weight to what to build, and every exclusion carries its
> reason.**

This is the difference between a deck that holds a scope line and one that does not. An
engineering audience given a cut list without reasons reads it as a backlog — a set of things
that are coming later, in an order somebody will decide. Within a month the smallest of them is
in a sprint, because it looked easy and nobody could remember why it was cut.

**A reason attached now is what survives that conversation**, and it survives it without the
person who wrote the specification being in the room.

**Name the two exclusions that will actually be argued with**, and defend them out loud in the
speaker notes. Every project has them: the one that looks trivial and is not, and the one that
looks obviously necessary and is a different product.

---

## Depth — where this sits

The room is deciding **how to build it**, so the depth is real. But it is a briefing, not a
second specification.

| Include | Exclude |
| --- | --- |
| The stack, and **why each piece**, with what it is worse at | Schemas, table definitions, migrations |
| The one structural property the architecture follows from | Endpoint lists, request and response shapes |
| The non-negotiables, **each with what breaks if it is broken** | Setup commands, environment variables, CI configuration |
| A system diagram, at whiteboard fidelity | Directory layouts, naming conventions |
| The milestone sequence and what gates each step | Per-task estimates |

**Paraphrasing a deliverable into slide prose creates a second source of truth**, and the two
disagree within a week. Reference the artifact by name for depth; do not restate it.

---

## Required slides

The template gives the full plan. **Five of them are the ones that get cut for time, and they are
the reason the deck is worth holding:**

| # | Slide | Why it is not optional |
| --- | --- | --- |
| **8** | **MVP scope — included and excluded** | The exclusions are the whole point. See above |
| **11** | **Risks and assumptions** | An engineering team that does not know which assumption is load-bearing will optimize the wrong thing for a quarter |
| **12** | **The validation step** | If a gate stands between the team and the first line of code, this slide is why the meeting exists |
| **14** | **Open decisions** | Blocked work is the category engineers are most likely to resolve by deciding it themselves, quietly and reasonably |
| **15** | **Engineering next steps** | A kickoff that ends without a first action is a status update |

**If a risk is accepted rather than mitigated, say so in those words.** "No structural
mitigation. Accepted." An engineer who discovers later that a stated mitigation was aspirational
stops trusting the rest of the deck, and correctly.

---

## Visuals

**Each required visual replaces a paragraph nobody would read on a slide.**

| Required | Why |
| --- | --- |
| **A system diagram** | The architecture is unreadable as prose, and an engineer will redraw it on a whiteboard within a day anyway. Draw it once, correctly |
| **A milestone timeline** | Sequence and duration are spatial. A table of dates hides what is parallel |
| **A workflow or critical-path diagram** | If one interaction is what everything else reads or writes, it gets drawn |

**Diagrams are built from shapes, not pasted as images.** A rendered image cannot be edited by
the person who has to present a revised version, and it will be revised.

---

## Speaker notes

**Required on every slide, written as speech rather than as a summary.**

A note that restates the slide is read once and never again. A useful note carries what the
presenter says and does not put on the slide: **which row to point at, which objection to expect,
which word to say out loud.** The three that matter most:

- **On the cover** — whether this is authorized work. It is the first thing the room needs.
- **On any slide carrying a hard verdict** — say the verdict in plain words. "Not defensible."
  "This is not approved yet." Softening it at the podium undoes the artifact.
- **On the last slide** — where the bottleneck actually is. If it is validation rather than
  engineering, that is the last sentence of the meeting.

---

## Generation

**Build the file with whatever presentation library is available on the machine.** Nothing in
this framework depends on a particular one, and the deck is a normal `.pptx` afterwards.

**If no library is available, say so and deliver the filled slide plan instead** — do not install
a toolchain the operator did not ask for, and do not deliver a markdown file named as though it
were the deck.

### Check the geometry before reporting it done

**A generated deck is not visually checked by generating it.** Two failures are common and both
are invisible in the code:

1. **A shape falling outside the slide bounds.** Assert it: every shape's right edge inside the
   slide width, every bottom edge inside the height. This is cheap and it catches the majority.
2. **Text overflowing its box**, usually in a table row that grew. Presentation software grows
   rows to fit, which pushes everything below them down. **Leave vertical slack under any table
   whose cells might wrap to a second line**, and re-check the bounds after any content edit.

**If a renderer is available, open the deck and look at it.** If none is, **say plainly that the
geometry was verified programmatically and the deck was not visually rendered.** That is an
honest statement about a real limit. Reporting it as checked is not.

---

## What this step does not do

- **It does not re-open the research.** If the deck cannot be built honestly from the artifact
  set, the run is not finished — go back to the run, not to the deck.
- **It does not soften the verdict for its audience.** The framework's value is that its output
  is the same document whoever is reading it.
- **It does not replace the build handoff.** An engineer who watched the deck and did not read
  `12-Build-Handoff.md` is not ready to build, and the deck should say so.
- **It does not brief on work that is blocked** as though it were work that is starting.

---

## Checklist

- [ ] Validator exits 0, and the delivery checkpoint has been presented
- [ ] The slide plan in `18-Engineering-Presentation.md` was filled before any slide was generated
- [ ] Written to `projects/<slug>/presentation/`; nothing in `deliverables/` was touched
- [ ] 10–15 slides, sized for 10–15 minutes
- [ ] Cover states the project, the research verdict and the confidence level
- [ ] **What NOT to build has equal weight, and every exclusion carries its reason**
- [ ] The two exclusions most likely to be argued with are defended in the speaker notes
- [ ] A system diagram and a milestone timeline are present as visuals, built from shapes
- [ ] Tables rather than paragraphs
- [ ] Risks named, with accepted-not-mitigated stated in those words where it applies
- [ ] The load-bearing assumptions named, with what happens if each is false
- [ ] The validation step is a slide of its own, with stop conditions verbatim
- [ ] Blocked work listed as things to ask about, not decide
- [ ] **Every slide carries speaker notes, written as speech**
- [ ] **No shape falls outside the slide bounds — asserted, not assumed**
- [ ] Every figure traces to a deliverable — checked, not assumed
- [ ] Where the deck was not visually rendered, that was stated rather than implied

---

> **Presentation Principle**
>
> A specification tells a team what to build. A briefing tells them what not to, and why.
>
> The second one is what decides whether the scope line still exists in a month, and it is the
> one that gets dropped for time.
