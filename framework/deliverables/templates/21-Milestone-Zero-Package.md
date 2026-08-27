# Template — Milestone Zero Execution Package

<!-- Usage
     Write to projects/<slug>/milestone-zero/. A DIRECTORY, not one file.
     Method: framework/engine/milestone-zero.md. Read it before filling this in.

     Required whenever outputs.roadmap.milestone_zero_present is true. Absent otherwise,
     and its absence is then correct.

     Shape:
       milestone-zero/
         CHECKLIST.md              the one-pager — write it LAST
         M0-1-«slug».md            one working document per test
         M0-2-«slug».md
         M0-3-«slug».md
         results/                  empty, with pre-headed data files

     Every threshold here is REPRODUCED from state.outputs.stop_conditions. Never
     re-derived, never softened, never rounded. If a threshold looks wrong while writing
     this, record that it looks wrong — do not change it.

     Remove every «placeholder» and every HTML comment before finishing.
-->

---

# Per-test working document — `M0-«n»-«slug».md`

<!-- One per Milestone Zero test. Sections vary by test TYPE: a technical test needs a
     corpus and a procedure; an outreach test needs the message written out; a research
     test needs a script and a score sheet. Use the sections that apply and delete the
     rest — an empty "Test corpus" heading on an email test is noise.

     The test: could the operator execute this without opening any research document? -->

| | |
| --- | --- |
| Test | **M0-«n»** |
| Answers | «assumption ids, and what each one decides» |
| Effort | «hours or days — from the roadmap, not re-estimated» |
| Cost | «money, usually zero» |
| Needs | «nobody but the operator / n other people» |
| Carries | «the stop conditions this test can fire» |

## 1. Objective

«What this establishes, in two sentences. Then: what it is NOT — the adjacent question a
reader will assume it answers and it does not.»

## 2. Prerequisites

<!-- Everything that must be true before step 1. Accounts, installs, tools, access.
     Include the confounds to remove — the things that make the result unreadable if
     left in place. -->

## 3. Procedure

<!-- Numbered. Executable. Each step is an action, not a topic.

     Include the step that PROVES THE INSTRUMENT before it is used to measure anything.
     A test whose apparatus is wrong reads exactly like a strong positive result, and
     that is the most flattering false answer available. -->

## 4. Expected observations

<!-- Predictions, written BEFORE the test runs, with the evidence behind each and a
     confidence word. These are not criteria — §5 holds those. They exist so the result
     cannot be quietly read to fit.

     If the outcome differs from every prediction, that is a finding: write it down
     verbatim before interpreting it. -->

## 5. Pass / fail

**Passes when:** «the specific observable»
**Fails when:** «the specific observable — and which stop condition that is»

<!-- State the outcomes that are NEITHER. Most real results land there, and a test with
     only two branches forces an honest ambiguous result into the branch it least
     resembles. -->

## 6. Decision table

| # | Result | Verdict | Next |
| --- | --- | --- | --- |
| 1 | «observable» | «BUILD / SMALLER MVP / PIVOT / DO NOT BUILD / PROCEED» | «the action» |

<!-- Read top to bottom, first match wins. Say so on the page. -->

## 7. Evidence to collect

| # | Artefact | Format |
| --- | --- | --- |

## 8. Deliverables

<!-- Where each output lands, and the one line appended to the checklist. Require the
     findings document to NAME THE DECISION-TABLE ROW — a result described without naming
     its rule gets re-argued later by whoever preferred a different answer. -->

---

# The one-pager — `CHECKLIST.md`

<!-- Write this LAST, from the finished test documents.

     THE CONSTRAINT: it can be followed start to finish without opening anything else,
     including the research it came from. End it by saying so. -->

# Milestone Zero — one page, no other document required

**«duration». «cost». «what it can return».**

**Start date: ____________**

## Before anything

- [ ] «setup that makes the week possible»

## Day «n» — «the day's objective in four words»

- [ ] «action»

<!-- One block per day. Put the tests that depend on OTHER PEOPLE on day 1, whatever
     their effort — reply latency is the critical path, not work time. -->

## The «n» numbers

| | Value |
| --- | --- |
| «the measure» | ________ |

## The verdict table — read top to bottom, stop at the first match

| | Condition | **Verdict** |
| --- | --- | --- |
| «id» | «threshold, reproduced from stop_conditions» | **«verdict»** |

### Not stop conditions — and they will be tempting

«The bad-but-survivable results. Name them, because at the end of a hard week they read
like failure.»

### Rules that keep the table honest

1. **No threshold moves after «the day they are frozen».** If one turns out to be wrong,
   record that it was wrong — then apply it as written anyway.
2. **Thresholds read against what was actually achieved, not the target.** If a threshold
   becomes unreachable at that n, say so rather than rescaling it.

## Results

| Test | Date | Result | Verdict |
| --- | --- | --- | --- |

### **Milestone Zero verdict: ______________  Date: ____________**

## If it passes / If it fails

«The next milestone. And: write down which condition fired and stop.»

---

*Detail, if you need it: «the per-test files». You should not need it.*

---

# `results/`

<!-- Created empty, with pre-headed data files so the operator RECORDS rather than
     DESIGNS at the moment they are trying to observe something.

     A pre-headed CSV per test that produces rows. Subdirectories for artefacts.
     Nothing in this directory is written by the run. -->

<!-- COMPLETION CHECK — remove this block when done.
     - [ ] One working document per Milestone Zero test in the roadmap
     - [ ] Every threshold matches state.outputs.stop_conditions exactly
     - [ ] The checklist stands alone — no research document needed
     - [ ] Tests depending on other people start on day 1
     - [ ] Every artifact to be built is SPECIFIED, not built
     - [ ] results/ exists with pre-headed files
     - [ ] No placeholder text remains
-->
