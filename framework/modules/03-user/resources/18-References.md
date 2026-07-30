---
Title: References
Module: 03-user
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Rank the evidence available about users, and set the rule against invented voices.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for user research
Related Modules:
  - 04-problem
Tags:
  - User
  - References
  - Reference
---

# References

---

# Overview

This module's sources are people, and people are unreliable in specific, predictable ways. What follows is the ranking, the routes, and one
prohibition.

---

# The Evidence Ranking

Every claim about a user carries a standing determined by how it was obtained:

| Strength | Source | Example |
| --- | --- | --- |
| **Strongest** | Observed behavior with a cost attached | A paper pad maintained through every consultation |
| Strong | A workaround they built | A private spreadsheet kept in parallel |
| Strong | Their own data | Timestamps on records; a system export |
| Moderate | Reported behavior | "I usually finish around seven" |
| Weak | Stated preference | "I'd like it to be faster" |
| **Weakest** | Predicted behavior | "I would definitely use that" |

The bottom two rows are the easiest to collect and the most likely to be wrong. `04-problem` will not accept them as verification, so
gathering only those produces a module whose output cannot pass the next gate.

---

# Where to Find Each

| Need | Route | Standing |
| --- | --- | --- |
| Observed behavior | Sitting with one practitioner for a session | `[verified]`, sample of one — say so |
| Their own data | Ask what they can export. Frequently more than expected | `[verified]` with a population and period |
| Reported workflow | Structured interviews about the **last** occurrence | `[reported]` |
| Vocabulary | Their own writing — professional forums, bodies' publications | `[verified]` for the terms |
| Role structure and who signs | Professional body guidance, contract frameworks, job postings | `[verified]` for the structure |
| Accessibility needs and standards | Regulator or standards publications, via `02-market` Frame 2 | `[verified]` for obligations |
| Segment size | Registers and membership lists — `02-market` | `[verified]` for counts |

The second row is the underused one. `04-problem/knowledge/validation/Analytics.md` makes the same point: one timestamp export converts
several `[assumption]` tags at once and costs a single question.

---

# The Prohibition

> **Never invent a quote.**

A fabricated user voice reads as primary evidence, propagates verbatim into the PRD, and **nobody downstream can tell it was invented.** It
is the only error in the framework with that property.

The correct handling when no voice exists:

```
Primary voice: none located.
No practitioner outside the operator's network has been interviewed.
Three reported statements appear in the workflow section, labeled as
reports and paraphrased.
```

That sentence is a finding. It tells `04-problem` exactly what its validation plan must produce.

The same rule applies to a model's synthesis. A generated account of what clinicians say is the model's inference, and presenting it in
quotation marks is fabrication regardless of intent.

---

# Interview Sourcing Discipline

**Ask about the last time, never the next time.** Interviews are excellent about history and worthless about prediction.

**Record the number and who they were.** "Five single-handed GPs in «region»" is a finding with a scope. "Users we spoke to" cannot be
tagged.

**Say nothing about the product until the questions are done.** Once a solution is visible, severity inflates and the session becomes a demo
with polite feedback.

**Note the recruitment bias.** People who agree to discuss a problem are people for whom it is salient, which biases incidence upward — one
more reason interviews cannot answer "how common".

---

# Source Tiers, Applied

| Tier | At the user stage |
| --- | --- |
| **Primary** | The practitioners themselves; their exports; direct observation |
| **Industry** | Professional bodies on role structure, obligations and working patterns |
| **Academic** | Occasionally establishes population-level working patterns nothing else does |
| **Product and technical** | Incumbent system documentation — what the current tool makes them do |
| **Community** | Forums. Strong for vocabulary and workarounds, weak for prevalence |
| **AI-assisted** | Generating interview questions and orienting. **Never a persona row, never a quote** |

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| An invented quote | Undetectable fabrication in the most-read artifact |
| A persona generated rather than compressed | Fiction with a photograph, built on by four modules |
| Stated preference recorded as evidence | `04-problem`'s gate fails, or passes on nothing |
| One person's behavior as a segment claim | A distribution asserted from a sample of one |
| No gaps section | Nothing tells the next module what to validate |
| Vocabulary paraphrased | The model, interface and copy all drift from the domain |

---

> **Resource Note**
>
> Ask what they can export before planning an interview.
>
> And if no real voice exists, write that sentence down — it is the one
> finding that cannot be faked and the one that directs the next module.
