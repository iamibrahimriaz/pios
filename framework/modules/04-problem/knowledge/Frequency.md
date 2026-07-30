---
Title: Frequency
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the frequency dimension of the score and keep it grounded in observation.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - Frequency within ranked_problems
Related Modules:
  - 03-user
  - 12-metrics
Tags:
  - Problem
  - Frequency
  - Concept
---

# Frequency

---

# What It Is

How often the problem occurs — the first of the three scoring dimensions.

| | 5 | 3 | 1 |
| --- | --- | --- | --- |
| **Frequency** | Daily or more | Weekly | Monthly or less |

Frequency matters disproportionately because it multiplies everything else. A moderate cost paid daily
exceeds a large cost paid annually, and it also produces the behavioral evidence this module depends on:
frequent problems generate workarounds, and workarounds are the strongest evidence available.

---

# When It Applies

In Stage 3 (Score), taken from `03-user`'s observed workflow — not estimated here. `03-user`'s
`Usage-Frequency.md` establishes how often the job arises; this is how often it goes wrong.

---

# How to Apply It Here

**Count occurrences of the problem, not of the task.** A task performed twenty times a day where the
problem arises twice is a frequency of two. Conflating the two inflates every score in the table.

**Use the natural unit and show it.** Per consultation, per claim, per shift, per month-end. Then map to
5/3/1 so the arithmetic works, but keep the real figure visible — `06-business` and `12-metrics` need it
and cannot recover it from a score of 3.

**Record clustering.** A problem occurring thirty times on the last day of the month is not a daily
problem, and the difference changes both the product and the load figure `09-technology` sizes against.

**Note whether frequency is rising.** A problem worsening with volume, headcount or regulation has a
different urgency from a stable one, and `02-market`'s trends may already say which.

**Tag the source.** Observed, reported, or inferred. Reported frequency drifts toward the round and the
ideal, and a score built on it inherits that drift.

---

# Where It Misleads

**Frequency is the easiest dimension to inflate and the least likely to be challenged.** Rounding "a few
times a week" up to daily moves a score from 3 to 5 and multiplies the total, with no visible step where
the inflation happened.

**High frequency can indicate an accepted cost rather than an urgent one.** Something happening constantly
for years has usually been absorbed into how the work feels. That does not make it unreal, but it does
mean the workaround dimension carries the actual signal.

**Low frequency is dismissed too readily.** A problem occurring annually that costs a month of remediation
or carries a regulatory penalty outranks most daily irritations. Severity has to be read alongside, which
is why the score is a product rather than a sum.

**Averages hide the distribution that matters.** "Twice a week on average" can mean steadily, or eight
times in one bad week and none in the next three. The second is a much sharper problem.

---

# Related

| | |
| --- | --- |
| `Severity.md` | The cost per occurrence |
| `Current-Solutions.md` | The third dimension, and the most informative |
| `Cost.md` | Frequency × cost per occurrence |
| `03-user` | Where frequency is observed |

---

> **Concept Note**
>
> Count the problem, not the task.
>
> Frequency multiplies every other dimension, which is exactly why
> it is the one most quietly rounded up.
