# Producing the Milestone Zero Execution Package

**The validation week, written out so it can be executed rather than designed.** Template:
`deliverables/templates/21-Milestone-Zero-Package.md`. Output: `projects/<slug>/milestone-zero/`.

---

## When this is required

**Whenever `state.outputs.roadmap.milestone_zero_present` is true** — that is, whenever the
strategy committed to validating before building.

**Absent otherwise, and its absence is then correct.** A run that recommends building outright,
or not building at all, has no validation week to write out.

---

## Why this exists

A run that concludes *"validate before building"* has told the operator what is unresolved and
**left them to design the validation themselves** — at exactly the moment the research stops
and their attention is lowest.

**This artifact came from operator feedback on a completed run**, where the package had to be
requested by hand after delivery and was then described as the most valuable thing the run
produced. The observation was that *"research complete"* and *"here is exactly how to resolve
what is left"* are different endings, and only the second one gets acted on.

---

## The constraint that shapes everything

> **The checklist can be followed start to finish without opening any other document,
> including the research it came from.**

Write the per-test documents first and the checklist last, from them. **Then read the checklist
alone, as someone who has forgotten the run.** Every place you reach for context that is not on
the page is a defect in the page.

---

## Reproduced, never re-derived

**Every threshold in this package already exists in `state.outputs.stop_conditions`.** Copy
them. Do not recompute them, do not round them, do not restate a 7-of-10 as "most".

**If a threshold looks wrong while you are writing this, record that it looks wrong.** Do not
change it. It was set before the evidence existed, which is the only moment it could be set
honestly — and the package is being written after, which is the moment it is easiest to adjust
toward the answer somebody wants.

---

## Five things the package must do that the roadmap does not

**1 — Prove the instrument before it measures anything.** Any test with apparatus gets an
explicit step that verifies the apparatus works, and a rule that results collected before it
passed are void. **A broken fixture reads exactly like a strong positive result**, which is the
most flattering false answer available.

**2 — Start the human-dependent tests on day one, whatever their effort.** An email answered in
four days and an interview booked in five are the critical path; a day of your own work is not.
A package that schedules by effort puts the slowest thing last.

**3 — Give every test that depends on other people a defined fallback.** What happens if the
replies never come, decided in advance, with its cost named. **Without one, a test that cannot
be run converts "do not build yet" into "do not build ever" by attrition** — a verdict nobody
chose, arrived at by nobody deciding.

**4 — Freeze the thresholds in a dated file before the first observation, and say so on the
page.** Then forbid, in writing: moving a threshold afterwards, rescaling one that became
unreachable at the n actually achieved, and counting an undecided participant as a vote.

**5 — Require every result to name the rule it was read against.** A findings document that
describes what happened without naming its decision-table row is how a completed test gets
re-argued six weeks later by whoever preferred a different answer.

---

## Every test declares what it measures, not only how

**Six fields per test, and the first one is the one runs skip.**

| Field | Content |
| --- | --- |
| **`measures`** | The claim the test establishes, stated with **no reference to method**. *"Whether a buyer will pay money for this"*, not *"ten interviews"* |
| **`claim_class`** | Which of the six claims in `evidence-policy.md`. A test that measures problem frequency says nothing about willingness to pay, and the package must not let the two be read together |
| **`instrument`** | How it is measured |
| **`criteria`** | Each marked **necessary** or **corroborating**, before collection |
| **`precedence`** | Which criterion governs when two fire with opposite implications |
| **`threshold`** | The decision rule, and the volume floor beneath which it may not be read |

**A test recorded only as a method cannot be substituted**, and substitution is the common case: the
operator says they cannot run interviews, and a package that recorded only "interview ten people"
has nothing left to judge an alternative against. `engine/instrument-substitution.md` is the
protocol; **this is the file that has to record the thing it needs.**

---

## Mixed and unreadable results are normal — decide them in advance

**Three states that a package written for pass/fail cannot express**, all three of which occurred in
a single completed validation week:

**1 — Two criteria fired with opposite implications.** One said proceed, one said stop. The document
offered no precedence rule, so which governed was decided in the write-up rather than in advance.
**Both readings were defensible, which is what makes this undetectable afterwards.**

> **Where more than one criterion can fire independently, write the precedence rule before
> collecting.** A fired stop condition governing over any passing criterion is the usual answer, and
> it must be the recorded one rather than the assumed one.

**2 — A criterion was unsatisfiable for reasons unknowable beforehand.** A breadth requirement of
five independent venues met one venue that was dead in the window, one blocked outright, and one
that turned out to be a vendor backlog rather than a user corpus — while the test's primary floor
cleared by 2.1×. **Marking each criterion necessary or corroborating in advance is what lets that be
reported as a qualified pass instead of an awkward paragraph.**

**3 — A threshold that could not discriminate.** A test pre-registered a conservative coding rule
and an inconclusiveness threshold that, together, all but guaranteed "inconclusive" before a single
observation existed. **Compute the falsification value before collecting:** what value would the
measurement take if the hypothesis were false, under the coding rule that produces it? If that value
also crosses the threshold, **the test is not yet designed.** Afterwards, the same calculation is an
excuse.

**The six outcome states are in `gates.yaml` `validation_outcomes`.** The two that must never merge
are `inconclusive` — the test ran and the sample cannot carry the reading — and `blocked` — the test
could not run at all. **A blocked test is an action owed to the operator, not a finding about the
product.**

---

## The willingness-to-pay ladder

**Willingness to pay is the claim a validation week is most often built to answer and the one its
instruments are worst at.** The ladder, the equivalences and the disclosure rules for payment
instruments are in `engine/instrument-substitution.md`. Two things belong here, in the package:

**Name the rung.** A test at "would you pay $X?" and a test at "authorize a card that is never
captured" are not the same test and must not carry the same threshold. **Stated figures are
ceilings.**

**Fix the precedence before the result.** *Where stated and revealed willingness to pay disagree,
revealed governs.* Written into the package, not decided when the two numbers arrive disagreeing.

---

## Specify apparatus; never build it

**Where a test needs something built — a fixture, a corpus, a sample page — the package
specifies it and stops.** Controls, fields, constraints, and any non-obvious property it must
have, in enough detail that a builder needs nothing else.

**Do not write the application code.** `constitution/core/00-Purpose.md` draws this boundary and
it does not move because the code would be small, would be throwaway, or would be convenient.
The specification is the artifact; building it belongs to whoever executes the week.

---

## `results/`

**Created empty, with pre-headed data files** — a CSV per test that produces rows, with its
columns already named, and subdirectories for artefacts.

**The point is that the operator records rather than designs**, at the moment they are trying to
observe something. Designing a table while looking at a result is how a column that would have
been inconvenient goes unrecorded.

**Nothing in this directory is written by the run.**

---

## What a completed test must leave behind

**A validation result is only auditable if someone who disagrees with it can re-read the evidence
under the same rule and land in the same place.** Eight things, and the package's `results/` layout
should have a home for each before any of them exists:

| | What | Why it is not optional |
| --- | --- | --- |
| 1 | **Methodology** — the selection rule, the coding rule, the instrument | A rule nobody can apply is judgment wearing a procedure's name |
| 2 | **Raw evidence** — the corpus as collected, before coding | Without it the coding cannot be challenged, only believed |
| 3 | **Coding** — one row per item, with its source, date and author | The row-level record is what makes a re-code possible |
| 4 | **Assumptions** the test rests on | They are load-bearing and they disappear into the method otherwise |
| 5 | **Thresholds**, dated before the first observation | The only defense a threshold has against being adjusted afterwards |
| 6 | **Predictions** — what was expected, and why | See `state.pre_registration`. The miss is the informative case |
| 7 | **Results**, each naming the rule it was read against | A finding that does not name its decision-table row gets re-argued by whoever preferred another answer |
| 8 | **The decision taken**, including "none" | A fired stop condition that changed nothing is a finding the run walked past |

**The result is recorded in `state.validation`, not only in the package.** A validation outcome that
can overturn a delivered recommendation and lives only in a directory is invisible to every check —
and to the next session, which reads state before it reads anything else.

---

> **Milestone Zero Principle**
>
> A research run that ends in "validate this first" has not finished until the validation
> is executable by someone who has forgotten the research.
