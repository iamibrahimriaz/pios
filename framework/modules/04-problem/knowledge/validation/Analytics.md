---
Title: Analytics
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use existing data to verify claims, and know what data cannot say.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Evidence.md
Outputs:
  - Data method within validation_plan
Related Modules:
  - 09-technology
  - 12-metrics
Tags:
  - Problem
  - Analytics
  - Method
---

# Analytics

---

# What It Is

Verification from data that already exists — the person's own records, an existing system's logs, published
statistics, or a dataset the operator can obtain.

It is the cheapest source of `[verified]` evidence in the framework and the most consistently overlooked, because
interviews are the habitual first move.

| Source | What it can verify |
| --- | --- |
| The user's own exports and records | Frequency, volume, duration, error rates — actual, not recalled |
| An incumbent system's logs or reports | When work happens, how long it takes, how often it fails |
| Published statistics for the sector | Population counts, incidence, direction of travel |
| Support tickets and public reviews | What goes wrong repeatedly, in the user's words |

A timestamp record showing notes completed after 7pm on four days of five settles a question that fifty
interviews would leave as reported.

---

# When It Applies

In Stage 6 for any claim about frequency, duration, volume or error rate — and it should be checked *before*
qualitative methods are planned for those claims, because it is both cheaper and stronger.

---

# How to Apply It Here

**Ask what the person can already export.** In most professional contexts the answer is more than expected, and
one export can convert several `[assumption]` tags at once.

**Record the source, the period and the population with the figure.** "Practice A, 12 weeks, 1 clinician" is a
finding with a scope. A percentage without those three is not tagged evidence.

**Use published statistics for the population, not the incidence.** A sector's total count is usually reliable;
how many of them have this specific problem almost never is. `02-market` inherits the same distinction.

**Check the data rights before the data.** Whether the operator may lawfully hold or process it is a `09-technology`
and Frame 2 question, and it applies to validation data as much as to production data.

**Do not build instrumentation here.** `12-metrics` defines events, and defining them early produces measures nobody
can compute. This method uses data that already exists.

---

# Where It Misleads

**Existing data records what the current system captures, which is a description of the system rather than the
work.** Time spent outside the software is invisible, and it is frequently exactly where the problem lives.

**Data shows what happened and never why.** A spike in a log has an explanation, and the explanation is not in the
log. Pairing data with a short interview is how the causal claim becomes legitimate.

**One organization's data reads as a general finding.** It is a strong sample of one. Say so — `Impact.md` needs
the distinction between a verified cost and a verified prevalence.

**Available data pulls the analysis toward the measurable.** The problems that leave traces get verified and the
ones that do not get demoted to assumptions, which distorts the ranking in favor of whatever the incumbent
software happened to log.

**Absence of a signal is read as absence of a problem.** Work done on paper, in someone's head, or after hours
produces no data at all.

---

# Related

| | |
| --- | --- |
| `Interviews.md` | For the why the data cannot supply |
| `Surveys.md` | For incidence where no data exists |
| `Evidence.md` | Where verified means retrievable |
| `12-metrics` | Where new instrumentation belongs |

---

> **Concept Note**
>
> Ask what they can already export before planning a single
> interview.
>
> One timestamp export outranks fifty recollections — and the problems
> that leave no trace are the ones this method will quietly demote.
