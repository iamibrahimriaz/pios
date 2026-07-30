---
Title: Current Solutions
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Score the workaround dimension — the one most often omitted and the most informative.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Severity.md
Outputs:
  - Workaround within ranked_problems
Related Modules:
  - 05-competition
  - 07-strategy
Tags:
  - Problem
  - Workarounds
  - Concept
---

# Current Solutions

---

# What It Is

What the person does about the problem today — the third scoring dimension, and the one that decides whether
a high score means an opportunity.

| | 5 | 3 | 1 |
| --- | --- | --- | --- |
| **Workaround** | None — they simply suffer | Exists but poor | Exists and works |

> **The workaround dimension is the one most often omitted, and the most informative.**

A problem with a good workaround is a problem somebody already solved. It may still be worth improving, but
it is not urgent — and displacing a working workaround is much harder than solving something with no answer
at all.

A problem with **no** workaround is one of two things: extremely valuable, or not painful enough to have
provoked one. Deciding which is a judgment worth making explicitly.

---

# When It Applies

In Stage 3 (Score). It also supplies `05-competition` with the real competitive set, which usually includes
tools nobody would call competitors.

---

# How to Apply It Here

**Count everything, not just software.** A spreadsheet, a paper list, a colleague, a phone reminder, a habit,
and remembering are all current solutions. In most markets the leading alternative is a spreadsheet, and the
second is doing nothing.

**Record what the workaround costs them.** Time, duplication, risk of divergence, or the effort of
maintaining it. That cost is the gap the product has to be worth, and it is a better price anchor than any
competitor's list price.

**Say why the workaround persists.** Habit, sunk cost, control, distrust of alternatives, or genuine
sufficiency. Only the last one means the problem is solved; the others mean it is defended, which is a
different obstacle.

**Resolve the no-workaround ambiguity in writing.** If nobody has built anything, either the pain is too
diffuse to provoke action or the problem is genuinely unaddressed. `Frequency.md` and `Severity.md` usually
settle it: high on both with no workaround is a strong signal; low on both is resignation.

**Hand the list to `05-competition`.** Workarounds are competitors, and they are the ones a feature matrix
will miss.

---

# Where It Misleads

**Omitting this dimension is the module's characteristic failure.** Frequency and severity are intuitive to
score; the workaround requires knowing what people actually do, which requires `03-user` to have been done
properly. A two-dimensional score reliably over-ranks problems that are already handled.

**A working workaround is treated as a weak competitor.** It is the opposite: it is free, already installed,
fully trusted, and owned by the user. The switching cost in `03-user` is largely the cost of abandoning it.

**Poor workarounds are the strongest signal in the module and are easy to under-weight.** Someone maintaining
a bad manual process is paying repeatedly to get an outcome — that is behavioral evidence of demand, and
little else in the framework establishes it as cleanly.

**"No solution exists" is often a search that stopped early.** The same discipline `02-market` applies to
unexplained gaps applies here: absence of a solution usually has a reason, and the reason is the finding.

---

# Related

| | |
| --- | --- |
| `Frequency.md`, `Severity.md` | The other two dimensions |
| `Evidence.md` | Why a built workaround is strong evidence |
| `03-user` | Where workarounds are observed, and switching priced |
| `05-competition` | Where workarounds belong in the competitive set |

---

> **Concept Note**
>
> Score what they do about it today, or the ranking is wrong.
>
> A problem someone already solved with a spreadsheet is not an
> opportunity — it is an incumbent with no sales team and total
> trust.
