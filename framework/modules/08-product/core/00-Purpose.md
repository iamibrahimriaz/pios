---
Title: Purpose
Module: 08-product
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Product module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core
  - 07-strategy gate passed and checkpoint approved
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 09-technology
  - 10-execution
  - 12-metrics
Tags:
  - Product
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Module 07 decided what to build. This module makes that decision impossible to
misunderstand.

Nothing new is chosen here. The direction is settled, the cut is approved, and the operator
has committed. What remains is translation: turning a decision into a description precise
enough that someone who was never part of the run can build the right thing from it.

That sounds like the easy part. It is where most of the value of the preceding seven modules
is lost.

---

# Purpose Statement

> Specify the approved product precisely enough to be built — and no more broadly
> than it was approved.

---

# Why This Module Exists

Three failures dominate specification work.

**Vagueness that survives review.** A requirement everyone nods at, that two engineers would
build two different ways. It reads fine because every reader supplies their own meaning.

**Aspiration in place of criteria.** "Fast, intuitive, reliable." These cannot be observed,
so they cannot be failed, so they are not criteria. They are hopes with checkboxes.

**Scope laundering.** The spec grows past the approved cut, one individually reasonable
addition at a time. Nobody decided to move the line; it moved anyway, and the product being
built is no longer the product that was approved.

The module's structure — trace before specifying, priority anchored to module 07's line, the
two-builder test, banned aspirational words, a ledger that accounts for everything considered
— exists to make each of these visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `prd_body` | The problem, users, goals and explicit exclusions, stated for a builder |
| `feature_spec` | What the product does, precisely enough to build |
| `acceptance_criteria` | How anyone would know it works |
| `prioritization` | What gets built before what, and what ships first |
| `edge_cases` | What happens when it goes wrong — usually more than half the work |

---

# Core Objectives

- Trace every requirement to a ranked problem before writing it.
- Serve every problem above the line, or record its deferral.
- Reserve MUST for what module 07 put above the line.
- Describe behavior so that two builders would build the same thing.
- Specify the unhappy paths as carefully as the happy one.
- Write acceptance criteria that could actually fail.
- Account for everything considered — nothing dropped silently.

---

# What AI Should Learn Here

- Precision is not evidence. A precisely specified requirement serving an assumed problem is
  still assumed.
- An orphan requirement can always be justified. That is why it is deleted, not argued about.
- A criterion that cannot fail is not a criterion.
- Most of a product's real behavior is in its failure states.
- Specifying invites completeness, and completeness quietly breaks the cut.
- A requirement that names a technology has taken a decision from a later module.
- The reader of this document cannot ask questions.

---

# The Register Problem

Module 07's characteristic failure was confidence laundering — uncertainty upgraded by a
decisive writing style. This module has its structural twin:

> **Scope laundering.** An approved cut becomes a larger cut through additions nobody
> decided to make.

The mechanism is not carelessness. Working through a requirement in detail genuinely reveals
adjacent things the product appears to need, and each one is defensible on its own terms. A
day after a careful cut, the MUST list has grown by a third and no single addition looks
wrong.

The handling is fixed and it is not a judgment call:

| Situation | Action |
| --- | --- |
| Nice to have, discovered while specifying | Deferral ledger, with a revisit trigger |
| The core job cannot complete without it | Regress to `07-strategy`, recorded and surfaced |

There is no third option. In particular, "add it as a MUST because it is obviously needed"
is the failure, not the exception.

---

# Scope

**This module covers**

- Traceability from problems to requirements, in both directions
- Requirements with priority, behavior and dependencies
- Failure and edge states
- Acceptance criteria
- Prioritization, dependency order and the first shippable slice
- The deferral ledger
- Constraints inherited from earlier modules

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Whether to build this | `07-strategy` — settled |
| What the MVP contains | `07-strategy` — binding |
| Architecture and technology choices | `09-technology` |
| Entity shape and relationships | `09-technology`, derived from what is specified here |
| Screens and visual design | Design, from the behavior described here |
| Model behavior and prompt design | `14-ai-systems` |
| Milestone dates and resourcing | `10-execution` |
| Metric definitions and targets | `12-metrics` |

---

# Position in the Run

```
07-strategy → ⏸ CHECKPOINT PASSED → [ 08-product ] → 09-technology
                                                   → 14-ai-systems
```

This module opens the `specify` stage. There is no checkpoint of its own — the decision that
needed a human was made one stage earlier.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `feature_spec` | 09, 14 | Architecture, and the entities implied by the behavior |
| `edge_cases` | 09 | Failure handling, transactions, data integrity |
| `acceptance_criteria` | 10, QA | What "done" means |
| `prioritization` | 10 | Build order, critical path, first shippable slice |
| Goals | 12 | Metric definitions |
| `prd_body` | `03-PRD.md` | The shipped PRD |
| `feature_spec` | `04-Feature-Spec.md` | The shipped feature spec |

`09-technology` is the strictest consumer. It derives entities and relationships from the
behavior written here — so a requirement that leaves the data it touches implicit forces the
architecture module to invent it.

---

# The Reader

Every earlier module was read by an agent continuing a run, or by an operator making a
decision. This one is different.

> This document is read by someone who will build from it and cannot ask you anything.

That is the standard the whole module is calibrated to. It is why behavior is tested by
whether two builders would agree rather than by whether it reads clearly, why criteria must
be observable rather than persuasive, and why U6 — written for a reader with no access to
this conversation — carries more weight here than anywhere else in the framework.

---

# Success Criteria

- Every requirement traces to a ranked problem, and every problem above the line is served
  or explicitly deferred.
- No MUST below module 07's line.
- Behavior that survives the two-builder test.
- All five edge categories worked for every MUST requirement.
- Acceptance criteria that could fail.
- A ledger that accounts for everything considered.
- Confidence no higher than the problems the requirements serve.

---

# Self Assessment

- Did I trace before I specified?
- Is my MUST list the approved cut, or the approved cut plus what I noticed?
- Would two builders build the same product from this?
- Did I specify the failures, or only the successes?
- Can every criterion of mine be failed?
- Is anything I considered missing from the document entirely?

---

> **Purpose Principle**
>
> Seven modules established what should exist and why.
>
> This one exists so that none of that is lost in the handover to
> someone who will only ever read the document.
