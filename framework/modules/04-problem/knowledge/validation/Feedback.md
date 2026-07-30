---
Title: Feedback
Module: 04-problem
Section: knowledge/validation
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Weigh unsolicited feedback correctly and extract the problem beneath the request.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Problem-Discovery.md
Outputs:
  - Feedback sources within evidence_log
Related Modules:
  - 05-competition
  - 13-operations
Tags:
  - Problem
  - Feedback
  - Concept
---

# Feedback

---

# What It Is

What people volunteer without being asked — reviews, forum posts, support tickets, complaints, feature requests.

It is abundant, free, and systematically skewed. Its value depends entirely on being weighed correctly:

| Source | Weight | Why |
| --- | --- | --- |
| **Support tickets about a competitor** | Strong | Someone paid, then hit a wall serious enough to ask for help |
| **Sustained complaint patterns in reviews** | Moderate | Repetition across independent authors is signal; a single review is not |
| **Forum discussion of workarounds** | Strong | People teaching each other to work around something proves the problem and the gap |
| **Feature requests** | Weak as stated, strong when decoded | The request is a proposed solution; the problem beneath it is the finding |
| **Isolated praise or criticism** | Weak | Self-selected, unrepresentative, unattributable |

---

# When It Applies

In Stage 1 (Harvest) as a source, and throughout as corroboration. It also supplies `05-competition` with what
incumbents' users actually complain about, and `13-operations` with the support load to expect.

---

# How to Apply It Here

**Decode every feature request into a problem.** "Add a bulk export" is a proposed solution. Why do they want
it? Because they reconcile against a spreadsheet monthly and re-type it. *That* is the problem, and it may have a
better answer than a bulk export.

**Count patterns, not instances.** Three independent authors describing the same friction is evidence. One
articulate complaint is a lead, and treating it as evidence is how a roadmap gets set by whoever writes best.

**Read competitor reviews for the persistent complaint.** The friction incumbents have not fixed after years is
usually structural — expensive, architectural, or against their commercial interest. That is the most defensible
gap available, and it connects straight to `02-market`'s question of why a gap persists.

**Note what people say they do while complaining.** Feedback often contains behavioral detail incidentally, and
incidental behavior is more reliable than the complaint wrapped around it.

**Tag it as reported and self-selected.** It is real evidence with a known bias, and both halves of that need to
be visible in the log.

---

# Where It Misleads

**Feedback over-represents the extremes.** People write when delighted or angry; the silent majority of adequate
experiences is invisible. Volume of complaints is therefore not proportional to severity, and absence of
complaints is not evidence of satisfaction.

**A well-argued feature request becomes a requirement.** The most articulate user shapes the product, and their
context may be atypical. `08-product` requires every requirement to trace to a ranked problem for exactly this
reason.

**Complaints about interfaces crowd out complaints about outcomes.** Surface irritations are the easiest to
articulate, so a review corpus over-weights polish and under-weights the structural failures that actually cost
money.

**Old feedback describes a product that has changed.** Reviews from three years ago may name friction the
incumbent has since fixed, and building against them targets a competitor that no longer exists. Date every
citation.

**It cannot establish incidence, ever.** No amount of feedback tells you what share of the segment is affected —
the sample is defined by the act of writing.

---

# Related

| | |
| --- | --- |
| `Problem-Discovery.md` | Where requests are classified |
| `Current-Solutions.md` | Workarounds shared in forums |
| `Surveys.md` | For the incidence feedback cannot give |
| `05-competition`, `13-operations` | Where the same corpus is reused |

---

> **Concept Note**
>
> Every feature request is a solution with a problem hidden behind
> it.
>
> Ask why they want it, and build against the answer — the request is
> their guess, not their need.
