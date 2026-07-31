---
Title: References
Module: 07-strategy
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Establish that this module's inputs are internal, and what that obliges.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - ../constitution/resources/18-References.md
Outputs:
  - Input routes for strategic decisions
Related Modules:
  - 04-problem
  - 06-business
Tags:
  - Strategy
  - References
  - Reference
---

# References

---

# Overview

This module researches almost nothing. Its inputs are the previous six modules' outputs, plus the operator. That makes its sourcing discipline
unusual: the risk is not fabricating external evidence but **silently upgrading inherited evidence.**

---

# Where Each Input Comes From

| Input | Source | Must be carried with |
| --- | --- | --- |
| Ranked problems | `04-problem` | Their tags, unchanged |
| Evidence standing of the sharpest problem | `04-problem` | Whether it is verified or assumed — this drives Milestone Zero |
| Any declared shortfall | `04-problem` | It propagates; it is not resolved here |
| Gap and defensibility verdict | `05-competition` | Including "not defensible" where that was the finding |
| Price, margin, CAC ranges | `06-business` | The ranges, not their midpoints |
| The load-bearing economic assumption | `06-business` | Its name and its threshold |
| Switching cost | `03-user` | The binding dimension, not the average |
| Immovables | `03-user` | They constrain every option |
| **The operator's goal, runway and risk appetite** | **The operator** | `[verified: operator]` |
| Weights for the comparison | Derived from the above, published first | The derivation |

The last operator row matters as much here as in `01-idea`. Runway determines whether a nine-month sales cycle is survivable; appetite determines
whether a moatless position is acceptable. Neither is inferable.

---

# The Characteristic Sourcing Failure

Not invention — **promotion**.

| What happens | How it looks |
| --- | --- |
| An `[assumption]` is restated confidently in a new document | "The problem is that GPs finish notes after hours" |
| A range becomes its midpoint | "CAC of £575" from a £250–£900 range |
| "Moderate, partly inferred" becomes "defensible" | A one-word summary in an executive section |
| A declared shortfall is not mentioned | The strategy reads as evidenced |

Each is a small editorial act. The sum is a strategy document that appears to rest on research, presented to an operator who was not present for
the research.

The defense is mechanical: **carry the tag on the claim, wherever the claim appears.** The tag lives on the sentence, not on the module.

---

# What the Comparison Criteria May Draw On

The eight criteria are specified by the framework, each with a named source module. Adding one requires justifying it from the research, because
**any additional criterion favors something.**

Criteria that fail that test, and are the usual smuggled additions:

| Criterion | Why it is not admissible |
| --- | --- |
| Novel or interesting | Not a property the research established |
| Aligned with our vision | The vision is a tiebreaker after scoring, not a criterion |
| Technically ambitious | An internal preference |
| What the team wants to build | Legitimate as an operator input; not a research criterion |
| Investor appeal | An operator consideration, stated as such if it applies |

---

# Source Tiers, Applied

| Tier | At the strategy stage |
| --- | --- |
| **Primary** | The operator. The six prior modules' outputs |
| **Industry** | Only where a timing or regulatory date is needed — `02-market` holds it |
| **Academic** | Not relevant |
| **Product and technical** | `05-competition`'s changelogs, for the reversal trigger |
| **Community** | Not relevant at this stage |
| **AI-assisted** | Generating option shapes and stress-testing the comparison. **Never a criterion, never a weight, never an option's score** |

The AI-assisted row has a specific legitimate use here: asking for the strongest case *against* the preferred option, which is a genuine aid to
the advocate check. What it must not do is score the options, because it will score the one it just helped articulate most favorably.

---

# Documenting the Decision

Three records make the strategy auditable a year later:

**Publish the weights before the scores.** Weights chosen afterwards are the scores rewritten.

**Record what each rejected option offered.** Not why it lost — what is lost by not taking it.

**Timestamp the stop conditions.** Written before anything is built, they are conditions. Written afterwards, they are interpretations.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| An assumption restated as a fact | The operator approves a cut believing it is evidenced |
| A range reduced to a point | False precision enters the plan |
| The declared shortfall omitted | Milestone Zero is not required, and the build starts on a belief |
| A criterion added without derivation | The comparison confirms the preference |
| Weights set after scoring | The arithmetic is decorative |
| The operator's goal inferred | The most consequential input in the framework, guessed |

---

> **Resource Note**
>
> This module invents no evidence. Its failure mode is quieter: it
> promotes what it inherited.
>
> Carry the tag on the claim, every time it appears — including in the
> sentence the operator will actually read.
