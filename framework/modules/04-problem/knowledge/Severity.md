---
Title: Severity
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the severity dimension by the kind of cost, not by how strongly it was expressed.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Frequency.md
Outputs:
  - Severity within ranked_problems
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Problem
  - Severity
  - Concept
---

# Severity

---

# What It Is

How much the problem costs when it occurs — the second scoring dimension, graded by the **kind** of cost.

| | 5 | 3 | 1 |
| --- | --- | --- | --- |
| **Severity** | Costs money, risk, or reputation | Costs significant time | Mildly annoying |

The grading is deliberate. Money, risk and reputation sit above time because they are the costs people act
on: a professional will absorb an hour of unpaid work indefinitely and will move immediately to avoid a
complaint, a penalty, or a mistake with a patient.

---

# When It Applies

In Stage 3 (Score), alongside frequency and workaround. It is the dimension `06-business` later converts
into a value case.

---

# How to Apply It Here

**Grade by the kind of cost, not by the intensity of the complaint.** Someone calm about a serious risk and
someone animated about a minor irritation are both common. The scale reads the cost, not the delivery.

**Name who bears it.** The person, their employer, their customer, or a third party. Where the cost falls on
someone other than the user, willingness to act drops sharply — and where it falls on the buyer,
`06-business` has its argument.

**Include risk that has not yet materialized.** A near-miss is severity 5. The cost of the event that has
not happened is real to the person carrying it, and it is frequently the strongest motivator in regulated
work.

**Separate the cost per occurrence from the total.** Severity is per occurrence; multiplying by frequency is
`Cost.md`'s job. Merging them double-counts frequency and distorts the ranking.

**Include wellbeing explicitly.** Unpaid evenings, interrupted rest, and the strain of always being behind
are costs. They resist quantification, which is why they get dropped — record them qualitatively rather than
scoring them at 1 by default.

---

# Where It Misleads

**Severity is judged by articulacy.** The most vividly described problem is rarely the most costly one, and
the most costly is often the one described flatly because it has been normalized for years.

**Time is over-scored and risk under-scored.** Time is easy to estimate and easy to talk about; risk is
uncomfortable and probabilistic. In regulated fields the risk column is usually where the real severity
sits, and `13-operations` will meet it again as an incident.

**A high severity with a good workaround is not urgent.** This is why the score is a product of three
dimensions. Severity alone identifies what hurts, not what is worth building — and `Current-Solutions.md`
carries the correction.

**Self-reported severity inflates when a solution is visible.** People describe a problem as worse when
someone appears able to fix it. Evidence gathered while pitching is compromised evidence, and
`validation/Interviews.md` says why.

---

# Related

| | |
| --- | --- |
| `Frequency.md` | How often the cost is paid |
| `Cost.md` | Severity × frequency, quantified |
| `Impact.md` | How widely it is borne |
| `06-business` | Where severity becomes willingness to pay |

---

> **Concept Note**
>
> Grade the cost, not the complaint.
>
> Money, risk and reputation move people. Time gets absorbed —
> indefinitely, and quietly.
