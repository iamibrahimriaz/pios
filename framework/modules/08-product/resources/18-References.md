---
Title: References
Module: 08-product
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Establish that requirements are derived, not researched, and what may legitimately enter.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Input routes for requirements
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Product
  - References
  - Reference
---

# References

---

# Overview

This module researches nothing. Every requirement is derived from an earlier module's output, which makes the relevant question not "what is
the source" but **"what is allowed to enter."**

---

# Where Requirements Come From

| Element | Source | Notes |
| --- | --- | --- |
| Parent problems | `04-problem`'s ranked list | The only admissible parent |
| Job steps — the spine | `03-user`'s workflow | Every step served or explicitly left alone |
| The cut line | `07-strategy` | Binding. MUST is reserved for above it |
| Non-goals | `07-strategy` | An excluded capability stays excluded |
| Conditions of use | `03-user`'s environment and immovables | Constrain behavior and edge cases |
| Obligations | `02-market` Frame 2, via `09-technology` | Above the line regardless of ranking |
| Accessibility requirements | `03-user`, and a binding standard if one applies | Specific obligations, not the standard's name |
| Performance figures | `03-user`'s available time — via `09-technology` | Never a convention |

---

# What May Not Enter

| Not admissible | Why |
| --- | --- |
| A capability with no ranked problem | An orphan. Deleted, not justified |
| Something traced to the vision or value proposition | Not a parent. `08-product/knowledge/Vision.md` |
| A customer or stakeholder request, as stated | Decode it into a problem first — `04-problem/knowledge/validation/Feedback.md` |
| A competitor's feature, because they have it | Table stakes belong in requirements only if a ranked problem needs them |
| A technology choice | `09-technology` decides, fifth of six |
| A screen or layout | Design's output, derived from behavior |
| A metric target | `12-metrics` |
| A date | `10-execution`, and the framework produces no durations |

The third row is the one that arrives with social weight. A request from a named customer is still an orphan if no ranked problem supports it —
and decoding it usually reveals a problem that is already in the inventory.

---

# The Standard, Not a Source

This module's quality bar is not a citation but a test:

> **The two-builder test.** Would two independent engineers, given only this text, build the same behavior?

It replaces "is this clear?", which cannot detect the problem because the writer already knows the answer they meant. The usable form is:
**name the point where two readings diverge**, then answer it.

The same logic applies to acceptance criteria. `Given / when / then` with a figure is checkable; the banned vocabulary is not:

| Banned | Replace with |
| --- | --- |
| fast, performant | a figure, sourced from `09-technology`'s budget |
| intuitive, easy, user-friendly | a completion rate or a step count |
| seamless | the absence of a named interruption |
| robust, reliable | behavior under a named failure |
| appropriate, sensible | the specific thing that happens |

---

# Sourcing the Edge Cases

The five categories are not invented here either:

| Category | Where the content comes from |
| --- | --- |
| Empty | First-use state — every screen has one |
| Invalid | Validation rules implied by `09-technology`'s constraints |
| Failure | `03-user`'s connectivity and interruption findings |
| Permission | `09-technology`'s disclosure policy — 404 or 403 |
| Limit or conflict | `03-user`'s environment; `09-technology`'s capacity figures |

Where a category genuinely does not apply, **"not applicable — «reason»"** is the correct entry. A blank is indistinguishable from not having
considered it.

---

# Source Tiers, Applied

| Tier | At the specification stage |
| --- | --- |
| **Primary** | Modules 03, 04 and 07's outputs. The operator, for decisions module 07 left open |
| **Industry** | Domain standards where a requirement must conform — via `02-market` |
| **Academic** | Not relevant |
| **Product and technical** | Records-system documentation, for what an integration permits |
| **Community** | Not relevant at this stage |
| **AI-assisted** | Drafting behavior text and generating edge cases to check against the five categories. **Never a parent problem, never a priority** |

The AI-assisted row has a genuinely useful application here: asking where two engineers would diverge from a given requirement. That is the
two-builder test performed adversarially, and it finds real ambiguity. What it must not do is supply the parent problem, because it will
generate a plausible one for any requirement.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A rationale in place of a parent | An orphan with a persuasive justification |
| A stakeholder request specified as stated | The roadmap set by whoever asks best |
| MUST applied below the cut line | Scope laundering; the approved cut is not the built one |
| A technology named in a requirement | `09-technology`'s decision removed before it runs |
| Blank edge categories | Half a specification, and the half products fail on |
| Aspirational criteria | Acceptance that cannot fail |

---

> **Resource Note**
>
> Nothing new is chosen here. Every requirement points back at a ranked
> problem, or it is deleted.
>
> And the quality bar is not clarity — it is naming the sentence where two
> engineers would build different things.
