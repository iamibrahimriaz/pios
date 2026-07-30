---
Title: Mental Models
Module: 08-product
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a specification should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of the specification
Related Modules:
  - 09-technology
Tags:
  - Product
  - Mental Models
---

# Mental Models

---

# Model Statement

> A specification always looks complete to the person who wrote it.
>
> These lenses are ways of reading it as someone who was not there.

---

# 1. The Two-Builder Test

**Reveals:** underspecification.

Hand the requirement to two independent engineers. Would they build the same thing?

The value is in the form of the question. "Is this clear?" is unanswerable by the author, who
already knows what they meant. "Where would two readings diverge?" produces a specific
location, and the location produces the rewrite.

**Hides:** two builders can agree on a behavior that is wrong. Agreement is not correctness.

---

# 2. The Silent Reader

**Reveals:** everything the document assumes about its reader.

Read it as someone who joined today, has no access to the run, and cannot ask a question. At
each point where they would need to guess, mark it.

**Hides:** it can push toward over-explanation. The test is whether they could build it, not
whether they know everything you know.

---

# 3. The Job Walk

**Reveals:** holes in the product.

Take the numbered workflow from module 03. Walk it step by step against the requirements. For
each step: served by a requirement, left to a stated fallback, or unaccounted for.

An unaccounted step is where the user stops and the product ends.

**Hides:** it tests only the primary path for the primary persona. Secondary personas and
alternate paths need their own walks.

---

# 4. The Unhappy Path Inventory

**Reveals:** the half of the specification usually missing.

Five categories, per requirement: empty, invalid, failure, permission, limit or conflict.

Working a fixed list beats asking "what could go wrong?", because open questions return
whatever comes to mind first — which is the same two or three cases every time.

**Hides:** categories are not exhaustive. Anything about time — clock skew, timezones, stale
data, ordering — hides between them.

---

# 5. The Orphan Sweep

**Reveals:** requirements that came from somewhere other than the research.

Read the requirement list and cover the rationale column. For each, name the parent problem
from memory. Anything you cannot name is an orphan.

**Hides:** nothing. It is mechanical, and it works because reconstructing a parent is harder
than recognizing one when it is written next to the requirement.

---

# 6. The Cut Diff

**Reveals:** scope laundering.

Put module 07's above-the-line list beside this module's MUST list. Compare them as lists, not
as arguments.

Do not evaluate whether each addition is reasonable — every addition is reasonable, which is
why the check must be mechanical.

**Hides:** it will not detect a MUST that grew *within* an approved capability. A capability
approved as "record a consultation" can quietly become nine requirements.

---

# 7. The Falsification Read

**Reveals:** criteria that are hopes.

For each acceptance criterion, name the observation that would fail it. Not what would satisfy
it — what would break it.

Criteria that cannot be broken get marked complete during testing without anything being
verified, and nobody notices until the behavior is missing in production.

**Hides:** a falsifiable criterion can still test the wrong thing precisely.

---

# 8. Provenance Reading

**Reveals:** invented facts.

Read only the numbers, codes, field names and limits. For each, name its origin: a standard, a
finding, or a decision made here.

A document full of specifics reads as thoroughly researched. That impression is exactly what
makes an invented figure dangerous — it is authoritative and actionable at the same time.

**Hides:** it says nothing about whether a correctly sourced number is the right one for this
product.

---

# 9. Confidence Inheritance

**Reveals:** certainty manufactured by specification.

Read the requirements against module 04's evidence tags. Does any requirement present an
assumed problem as an established need?

| Module 04 said | The spec must not imply |
| --- | --- |
| `[assumption: needs validation]` | "Clinicians need…" as settled fact |
| `[inferred: from reviews]` | A verified frequency |

**Hides:** nothing. It is the same check module 07 ran, one translation later, and the
translation is where it is most likely to be lost.

---

# 10. The Absence Read

**Reveals:** what a reader will expect and not find.

Read the document as an experienced practitioner in the domain. What would they assume is
included because every product like this has it?

Each answer is either a requirement, a ledger row, or a non-goal. It cannot be nothing.

**Hides:** it imports convention. Some absences are the whole point of the strategy, and this
lens will flag them — which is why the answer may legitimately be "non-goal, deliberately".

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking a requirement is specified | The Two-Builder Test |
| Checking the document stands alone | The Silent Reader |
| Checking the product has no holes | The Job Walk |
| Checking failure coverage | The Unhappy Path Inventory |
| Checking nothing crept in | The Orphan Sweep |
| Checking the cut held | The Cut Diff |
| Checking criteria are real | The Falsification Read |
| Checking facts are facts | Provenance Reading |
| Checking honesty | Confidence Inheritance |
| Checking for surprises | The Absence Read |

Apply the Job Walk early — it shapes the requirement list. Apply the Cut Diff, Confidence
Inheritance and the Absence Read last, on the finished document.

---

# Self Assessment

- Can I name a divergence point in any of my requirements?
- Could a silent reader build this?
- Does every step of the job walk resolve?
- Did I work all five unhappy-path categories?
- Can I name every requirement's parent without looking?
- Does my MUST list still match the approved cut?
- Can every criterion be broken?
- Does every number have an origin?
- Have I made anything more certain than it arrived?
- What will a practitioner expect and not find?

---

> **Mental Model Principle**
>
> Every lens here is a way of not being the author for a moment.
>
> The author is the one person who cannot find what is missing.
