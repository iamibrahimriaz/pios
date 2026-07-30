---
Title: References
Module: 10-execution
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Route flow and plan inputs to their sources, and state the estimate boundary as a sourcing rule.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Input routes for flows and delivery plans
Related Modules:
  - 03-user
  - 08-product
Tags:
  - Execution
  - References
  - Reference
---

# References

---

# Overview

This module produces the `critical` deliverable and researches almost nothing. Its two sourcing risks are **fabricated durations** and
**principles derived from nowhere**.

---

# Input → Source

| Input | Source | Notes |
| --- | --- | --- |
| Critical paths | `03-user`'s jobs and workflow | The core job is the first path |
| Failure and recovery experiences | `08-product`'s five edge categories | Already specified; translated here, not invented |
| Design principles | `03-user`'s findings and immovables | Each principle names its finding |
| Screen states | `08-product`'s behavior | The four unpopulated states per screen |
| Performance figures | `09-technology`'s budget, from `03-user`'s available time | Never a convention |
| Dependency order | `08-product`'s functional dependencies | Real dependencies only, not preferences |
| One-way doors | `09-technology`'s reversibility column | Placed deliberately in the sequence |
| Milestone Zero requirement | `04-problem`'s evidence standing, `07-strategy`'s binding | Not a judgment made here |
| Verification coverage | `08-product`'s criteria and edge cases | Each test traces to one |
| **Durations** | **The operator, with the assumed team stated** | Or `[assumption: needs validation]`. Never derived |
| Accessibility obligations | `03-user`, and a binding standard via `02-market` | Specific requirements, not the standard's name |

---

# The Estimate Boundary as a Sourcing Rule

> The framework does not know the team. It cannot produce durations.

| Can be established here | Cannot |
| --- | --- |
| Sequence | Calendar dates |
| Dependency | Durations in weeks |
| Relative size — S / M / L, with the basis | Team velocity |
| Critical path | Delivery commitments |
| What is parallelizable | — |

A duration has exactly two legitimate forms:

```
Operator input:  "M1: 3 weeks, assuming one full-time engineer with
                  «relevant» experience." [verified: operator]
Or an assumption: "M1: roughly 3 weeks [assumption: needs validation —
                  assumes one full-time engineer]"
```

**An estimate with no stated team is not an estimate.** It is a number that will be treated as one, by people who were not told where it came
from — which is the same laundering the framework guards against everywhere, with a deadline attached.

---

# Sourcing Design Principles

A principle without a finding is decoration, and the sourcing test is simple: **name the finding, or delete the principle.**

| Principle | Finding it must cite |
| --- | --- |
| "Every action survives being abandoned halfway" | `03-user`: constant interruption |
| "Nothing lengthens a consultation" | `03-user`: the 10-minute appointment, immovable |
| "Nothing sensitive displayed by default" | `03-user`: patients can see the screen |
| "Keep it simple" | — nothing. Delete it |

The citation does double work: it justifies the principle when someone wants to violate it, and it makes the principle removable if the finding
turns out to be wrong.

---

# What May Not Be Sourced Here

| Not admissible | Belongs to |
| --- | --- |
| A new requirement discovered while drawing flows | `08-product`, via the ledger — or a recorded regress |
| A technology choice | `09-technology` |
| A metric target | `12-metrics` |
| A support commitment | `13-operations` |
| A duration derived from anything | Nobody — see above |
| A consumer UX convention as a principle | Nothing. `03-user` decides, and this segment is not a consumer |

The last row matters because consumer heuristics are the most available design references and the least applicable to a professional tool used
dozens of times a day. `05-competition/knowledge/UX-Comparison.md` makes the same point: density that reads as poor in a five-minute review is a
feature to the trained daily user.

---

# Source Tiers, Applied

| Tier | At the execution stage |
| --- | --- |
| **Primary** | Modules 03, 08 and 09's outputs. The operator, for durations and team composition |
| **Industry** | Accessibility standards where one binds — via `02-market` |
| **Academic** | Not relevant |
| **Product and technical** | The target system's documentation, for what an integration permits |
| **Community** | Interface conventions the segment already knows — worth inheriting deliberately |
| **AI-assisted** | Drafting handoff text, and testing it against the cold-start standard. **Never a duration, never a principle** |

The AI-assisted row has a strong legitimate use here: hand the draft handoff to a fresh context and ask what it cannot start without. That is the
cold-start test performed rather than asserted, and it finds the "as discussed" references reliably.

---

# Documenting the Handoff

Four properties make it pass the cold-start test:

**No "as discussed", "as agreed" or "per the research".** The reader was not there.

**Essentials carried inline.** The schema, the operations, the disclosure policy, the data-loss position. They will not open five documents
before writing a line.

**No unresolved assumption in a build-blocking position.** Everything unresolved is in Blocked Work with a **named owner** — never "the team" —
and the handoff says what to build instead.

**A first task nameable in one sentence, and a definition of done including what is not done.** Otherwise day one is spent deciding, and "done"
is whoever's opinion prevails.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A duration with no team stated | A commitment nobody made, held against the builder |
| Principles from consumer heuristics | Design decisions that contradict `03-user`'s findings |
| Edge cases re-invented rather than translated | `08-product`'s work discarded, and coverage lost |
| An assumption left in the build instructions | Someone guesses, and never mentions it |
| Blocked work with no owner | Nothing moves, and nobody knows it is stalled |
| Milestone Zero treated as parallel | The build starts on an untested belief |

---

> **Resource Note**
>
> Hand the draft handoff to someone with no context and ask what they
> cannot start without.
>
> That is the cold-start test performed rather than claimed — and it finds
> every "as discussed" in the document.
