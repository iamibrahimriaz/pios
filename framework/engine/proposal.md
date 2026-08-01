# Proposal — the document the funding decision is made from

A completed run produces artifacts for the **builder**. The person who decides whether the build
happens is **not the builder**. They will not read sixteen documents, and the two the builder works
from answer a question they are not asking.

They are deciding one thing: **does this get approved, deferred, or rejected.** Nothing in the
artifact set is organized around that question, so an operator asked for "a proposal" assembles one
by hand, under time pressure, from documents written for a different reader.

**What gets dropped in that assembly is predictable**: the confidence level, the open decisions, the
stop conditions, and the gate that failed. Those are exactly the parts that make the approval honest,
and they are the parts that feel least helpful to include when you are asking for money.

This step exists so that document is produced by the same discipline as everything else in the run.

---

## When it runs

**On request only, and offered once.** At the delivery checkpoint, alongside the offer to make the
folder buildable. One sentence — do not explain it at length and do not assume it.

> *"Do you want a project proposal for whoever approves this? One HTML file, print-ready."*

**A run that reached "do not build" still gets the offer.** A decision to stop is a decision someone
has to sign off, and it is easier to sign off from a document than from a conversation.

---

## What this step produces

**One self-contained HTML file**, written to `projects/<slug>/proposal/`, plus a PDF rendered from it
where a headless browser is available.

**The HTML is the artifact; the PDF is a rendering of it.** Keep the source — a PDF that cannot be
regenerated becomes stale the first time a figure changes, and then it is wrong in the one place
outsiders read.

**Self-contained means self-contained.** No external stylesheet, font, script or image. This file gets
emailed, opened on a machine with no network, and forwarded to someone outside the organization. A
proposal that renders as unstyled text on the approver's laptop has failed at the only moment it
mattered.

**Never write into `deliverables/`, and never edit a deliverable to match the proposal.** If writing
the proposal reveals that a deliverable is wrong, say so and stop — the specification is the record of
what the run established, and a document written to win an approval is the last thing that should be
allowed to amend it.

---

## The rule that keeps it honest

> **Derived, never re-researched.**
>
> Every figure, verdict and risk in the proposal already exists in the artifact set. The proposal
> **selects and arranges**; it does not establish.

If the proposal needs a number no artifact carries, **that is a finding, not a gap to fill.** Write
that the figure is not established and what it would take to establish it. Computing one at proposal
time creates a number with no evidence tag, in the one document that will be quoted back at the team
for a year.

**Three consequences that follow from this rule:**

| | |
| --- | --- |
| **The proposal may not read better than the research reads** | Confidence appears on the first page, not in an appendix. A `low`-confidence run produces a proposal whose cover says `low`. |
| **The recommendation is the run's recommendation** | Unchanged, in force, with its qualifiers. If the run reached "do not build", the proposal proposes not building — or proposes the cheapest test that would change the verdict. |
| **A failed gate is named** | Not summarized into a risk. A gate that failed and was overridden by the operator is a fact the approver is entitled to before they sign, and concealing it is how an approval gets obtained that would not have been given. |

**The test:** would this document win approval for a run the evidence does not support? If yes, it was
written incorrectly, regardless of how good it looks.

---

## It is a decision document, not a second specification

The approver is deciding **whether**, not **how**. But "whether" for a technical project includes
enough technical substance to judge the risk — so the depth is real, and it sits at a specific level.

| Include | Exclude |
| --- | --- |
| The stack, and **why each piece**, with the trade-off accepted | Schemas, table definitions, migrations |
| The constraints that are not negotiable, **each with what breaks if it is broken** | Endpoint lists, request and response shapes |
| The scale the system is built for, and what it is deliberately **not** built for | Code, config, environment variables |
| The architecture as a diagram a non-specialist can follow | Directory layouts, naming conventions |
| The skills required to build it, and **which one is a hiring risk** | Setup commands, CI stage configuration |

**Paraphrasing a deliverable into readable prose produces a second source of truth**, and the two
disagree within a week. Reference the artifact by name for depth; do not restate it.

---

## Required content

The reader has not read the deliverables and will not. **Each section stands alone** — "see the PRD"
is never the whole answer to anything.

1. **The decision requested**, on the first page, with the real options — approve, approve with
   conditions, defer, reject — and **when each is the right call**. An approver handed only a
   recommendation is being asked to agree, not to decide.
2. **The recommendation**, and the conditions attached to it.
3. **The confidence level and what would raise it**, on the first page.
4. **The problem, the market, and the segment** — including what is verified and what is assumed.
5. **The business case** — unit economics, running cost, and the break-even position against what is
   attainable. Where the run could not establish a figure, say so in the table rather than omitting
   the row.
6. **Scope** — what is in, what is deferred, and **what is permanently excluded and why**. The
   permanent exclusions matter most: they are the ones someone will later propose adding.
7. **Technical architecture**, at the level defined above.
8. **The non-negotiable constraints, each with its consequence.** A rule whose reason is absent gets
   traded away by an approver looking for schedule.
9. **Team and skills required**, including what is explicitly *not* required. Over-hiring against an
   imagined system is a cost the approver is signing for.
10. **The delivery plan** — milestones, what each proves, and what gates the next. **If the run did
    not estimate durations, say why rather than inventing them.** A date in a proposal becomes a
    commitment regardless of the caveat next to it.
11. **Quality and release** — how correctness is verified, and what is deliberately not tested.
12. **Success metrics**, including the one that tests the business rather than the product.
13. **Risks**, with likelihood, impact, mitigation, and the early warning sign for each.
14. **Stop conditions**, stated as thresholds agreed in advance. **Approving the proposal is
    approving these** — say so in the document.
15. **Open decisions and blocked work**, each with an owner and the moment it bites.
16. **Evidence standing** — counts of verified, inferred and open claims, gate failures, and any
    primary research that was not conducted.

**Sections 14, 15 and 16 are the ones that get cut for length. They are the reason the document is
trustworthy.** Cut elsewhere.

---

## Length and shape

**As long as the decision needs, and no longer.** A two-page summary cannot support a funding
decision; a sixty-page document is not read, and an unread proposal is indistinguishable from one
that was never written.

The working test for every section: **what decision does this change?** A section that changes no
decision is background, and background belongs in the artifact set the proposal points at.

**Print to a page size, not to a screen.** The approver will print it or read it as a PDF. Use print
CSS, keep tables from splitting across pages where you can, and start each major section on a fresh
page so the document can be read in parts.

---

## Rendering

Render with whatever headless browser is present on the machine. If none is, **deliver the HTML and
say plainly that it prints to PDF from any browser** — do not install a toolchain to produce a file
the operator can produce with one keystroke.

**Check the rendered output before reporting it done.** A print stylesheet that looks correct in a
browser window can produce blank pages, split tables and clipped diagrams on paper, and the operator
discovers this in front of the approver.

---

## What this step does not do

- **It does not re-open the research.** If the proposal cannot be written honestly from the artifact
  set, the run is not finished — go back to the run, not to the proposal.
- **It does not soften a verdict for its audience.** The framework's value is that its output is the
  same document whoever is reading it.
- **It does not replace the artifact set.** It points at it, names it, and ends with an index of it.
- **It does not run automatically.** Offer it; do not assume it.

---

## Checklist

- [ ] Validator exits 0, and the delivery checkpoint has been presented
- [ ] The operator asked for this — it was offered, not assumed
- [ ] Written to `projects/<slug>/proposal/`; nothing in `deliverables/` was touched
- [ ] Self-contained: no external stylesheet, font, script or image
- [ ] **Every figure traces to a deliverable** — checked, not assumed
- [ ] Confidence level and the decision requested both appear on the first page
- [ ] Any failed gate is named, not summarized into a risk
- [ ] Permanent exclusions carry their reasons
- [ ] Non-negotiable constraints carry their consequences
- [ ] Stop conditions present, and stated as binding on approval
- [ ] Open decisions listed with owners and the moment each one bites
- [ ] Evidence standing present, including primary research not conducted
- [ ] The rendered output was opened and looked at, page by page
- [ ] The HTML source is kept beside the PDF

---

> **Proposal Principle**
>
> The proposal is read by the one person who can stop the project, and it is the only document
> they will read.
>
> That is an argument for making it clear. It is never an argument for making it more confident
> than the research it was drawn from.
