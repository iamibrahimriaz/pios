---
Title: Churn
Module: 11-growth
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Identify the observable behavior that precedes leaving, since the percentage is not actionable.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 11-growth/knowledge/Retention.md
Outputs:
  - Leading indicators within retention_model
Related Modules:
  - 06-business
  - 12-metrics
Tags:
  - Growth
  - Churn
  - Concept
---

# Churn

---

# What It Is

Users leaving — and the framework's position on it is a division of labor:

| | Owner |
| --- | --- |
| Churn as a **number** for the arithmetic | `06-business`, with a sensitivity table because it cannot be known |
| Churn as a **mechanism** to be prevented | `Retention.md` |
| Churn as an **observable precursor** | This file |

> Churn stays an assumption. What can be established is the **observable behavior that precedes leaving** — that is actionable, and a
> churn percentage is not.

The precursors worth watching, in rough order of how early they appear:

| Signal | What it indicates |
| --- | --- |
| Never activated | Not churn at all — an onboarding failure, and a different fix |
| Frequency falling below the job's natural rate | The product is being worked around |
| The workaround reappearing | `03-user`'s spreadsheet is back — the strongest signal available |
| One user of several stops | A workflow dependency breaking from one end |
| Support contact about a core path | Friction that has become intolerable rather than annoying |
| Export or data request | Frequently the last event before leaving |

---

# When It Applies

In Move 4 (Retain), as the actionable half of the retention model.

---

# How to Apply It Here

**Separate failure-to-activate from churn.** They look identical in a cancellation number and have opposite fixes.
`Activation.md` draws the line and `12-metrics` must define the two populations separately.

**Compare observed frequency against the job's natural frequency.** `03-user` recorded how often the job arises. Usage below that rate
means something else is doing the job.

**Watch for the workaround returning.** It is the clearest evidence available that the product stopped being worth the switch, and it
is observable if the events exist.

**Define the precursors as metrics.** `12-metrics` needs the numerator, denominator, window and population. A precursor nobody
instrumented is a precursor nobody sees.

**State what the response would be.** A signal with no intended action is monitoring for its own sake, and
`07-strategy/knowledge/risks/Mitigation.md` makes the same point about early warnings.

---

# Where It Misleads

**A churn percentage is treated as a diagnosis.** It says how many left, not why or which ones. Every action available comes from the
precursors instead.

**Churn is measured on renewal for an annually contracted product.** The decision was made months earlier and the signal arrived
months earlier. Waiting for the renewal is waiting for the outcome.

**A benchmark churn rate is imported.** `06-business` covers this: averages across markets, price points and contract shapes are not a
benchmark for anything specific.

**Silence is read as satisfaction.** A retained customer who has stopped using the product is churn with a delay, and
`12-metrics`' point applies — a login is not a return.

**Exit interviews are the primary evidence.** They are `04-problem`'s weakest evidence class: reported, retrospective and polite. The
behavior before leaving is stronger and available earlier.

---

# Related

| | |
| --- | --- |
| `Retention.md` | The mechanisms that prevent it |
| `Activation.md` | The failure that is not churn |
| `06-business` | Churn as an arithmetic assumption |
| `12-metrics` | Defining the precursors computably |

---

> **Concept Note**
>
> A churn percentage tells you how many left. The behavior before
> leaving tells you what to do.
>
> The strongest signal available is the old spreadsheet coming back.
