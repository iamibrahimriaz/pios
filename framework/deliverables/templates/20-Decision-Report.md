# Template — Decision Report

<!-- Usage
     Write to projects/<slug>/DECISION.md, at the run root, NOT in deliverables/.
     Method: framework/engine/decision-report.md. Read it before filling this in.

     ONE PAGE. That is the constraint the artifact exists to satisfy, and every other
     instruction here is downstream of it. If a section will not fit, cut its content —
     never the section, and never the qualifier.

     Everything here already exists in deliverables/. Nothing is computed, estimated or
     researched while filling this in. A figure that is not in the artifact set does not go
     on the page; write "not established" and move on.

     Remove every «placeholder» and every HTML comment before finishing.
-->

---

# «Project Name» — Decision Report

| | |
| --- | --- |
| Date | «ISO date» |
| Confidence | **«HIGH / MEDIUM / LOW»** |
| Primary research conducted | **«YES / NO»** |
| Full package | `deliverables/` · `proposal/proposal.html` |

---

## The recommendation

<!-- The run's recommendation, in the run's words, unchanged, with its qualifiers intact.
     If the run said "do not build yet", this says "do not build yet" — not "proceed with
     caution". A softened verdict here is the single most damaging thing this page can do,
     because this is the page that gets quoted. -->

### **«THE RECOMMENDATION, VERBATIM»**

«One paragraph. What was found, and why it leads there. If the recommendation is conditional,
the condition is in this paragraph — not on another page and not behind a link.»

---

## Why the confidence is «level» and not higher

<!-- One or two sentences. A confidence word with no basis is a mood. -->

«What is unresolved, stated plainly. If confidence never moved during the run, say so —
that is a finding, not an omission.»

---

## What this rests on

<!-- ONLY the assumptions that decide the outcome. Not the register — that is
     10-Risks-and-Assumptions.md and this page must not try to be it. Three to five rows. -->

| Assumption | If it is wrong | How to find out |
| --- | --- | --- |
| «the belief, in one line» | «what collapses» | «the cheapest test, with its cost» |
| | | |

---

## What could still go wrong

<!-- Prose or three bullets. Not a risk table with likelihood and impact columns — that
     exists elsewhere and copying it here spends the page on formatting. -->

- «the thing most likely to make this fail, stated as a sentence a person would say»
- «the second»

---

## What happens next

| # | Action | Owner | Cost |
| --- | --- | --- | --- |
| 1 | «the specific first thing» | «a named person or role» | «time and money» |
| 2 | | | |

<!-- An action with no owner is not an action. If the owner is the operator, say so; if
     nobody has been named, write NOT ASSIGNED rather than leaving the cell blank. -->

**«If the recommendation is conditional: what decides it, and when.»**

---

## What only you can answer

<!-- The operator-owned open questions, if any remain. Delete the section if none do —
     an empty section on a one-page document is a wasted tenth of it. -->

| Question | Blocks | When it bites |
| --- | --- | --- |
| «the question, in plain language» | «what cannot proceed» | «the milestone» |

---

<!-- COMPLETION CHECK — remove this block when done.
     - [ ] Fits on one page
     - [ ] Recommendation is word-for-word the Executive Summary's
     - [ ] Every figure appears in deliverables/
     - [ ] Every next action has an owner
     - [ ] No placeholder text remains
     - [ ] A reader who reads only this page and acts on it has not been misled
-->
