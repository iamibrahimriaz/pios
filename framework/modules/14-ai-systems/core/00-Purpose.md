---
Title: Purpose
Module: 14-ai-systems
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the AI Systems module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - core/00-Purpose.md
  - 08-product and 09-technology gates passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Some products have a part that cannot be specified as a rule — a judgment, a generation, an
extraction, a prediction. This module decides which parts those genuinely are, and what happens when
they are wrong.

It is the framework's last module, and the one most likely to be run for the wrong reason. So its
discipline is a single question, asked without flinching:

> Would something simpler have worked?

**A product with no AI component is a complete product.** Recording that no capability was justified
is a legitimate output of this module, not a failure of it.

---

# Purpose Statement

> Decide where a model genuinely beats the simpler alternative — and define, before
> committing, how it will be evaluated and what happens when it is wrong.

---

# Why This Module Exists

Three failures dominate AI planning.

**Capability theater.** A model added because it is expected rather than because it wins. It costs
money per operation, needs evaluation nobody scheduled, fails in ways nobody predicted, and replaces
a form field that would have worked.

**The data that was never there.** The most common way an AI capability fails is that it fails before
it starts, because the data it needed did not exist in the form it needed. Nobody checked, because
checking felt like a formality.

**Evaluation after the fact.** The capability is built, then assessed — and the bar becomes whatever
was achieved. A feature nobody can measure is a feature nobody can fix.

The module's structure — a mandatory non-AI comparison, confirmed data availability, and an
evaluation plan written before commitment — exists to make each of these visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `ai_opportunities` | Which capabilities earned their place, and which were dropped |
| `model_strategy` | The approach, the pinned version, and what happens when it is retired |
| `data_requirements` | What data is needed, whether it exists, and whether we may use it |
| `evaluation_plan` | The bar that must be cleared before users see it |
| `failure_modes` | How it goes wrong here, how that is detected, and what the user does then |

---

# Core Objectives

- Compare every capability against a genuine non-AI alternative, and drop the ones that lose.
- Confirm data availability rather than assuming it.
- Establish the right to use the data, under a named regime.
- Set autonomy from the cost of being wrong and whether the user can detect it.
- Define the metric, the bar and the ship gate before committing.
- Write failure modes specific to this product, with detection and guardrails.
- Make the non-AI fallback a requirement.
- Compute the share of revenue per user this consumes.

---

# What AI Should Learn Here

- Dropping a capability is a successful outcome of this analysis.
- A straw-man alternative invalidates the comparison rather than weakening it.
- Unconfirmed data is a blocker, not a risk.
- Consent for one purpose is not consent for model input.
- Detectability governs autonomy more than accuracy does.
- A bar set after seeing outputs is a description, not a bar.
- A better prompt is not a guardrail.
- The non-AI fallback is scope, not a contingency.

---

# The Plausibility Problem

Every module in this framework guards against something. This one guards against the failure the
framework itself was built to prevent — occurring inside the product rather than inside the document.

| The framework's own rule | What a model does |
| --- | --- |
| An assumption must never be smoothed into a fact | Exactly that, by default, in every sentence |

> A model's errors are fluent. They arrive in the same register as its correct answers.

Which is why this module weights **detectability** above accuracy. A capability right 99% of the time
whose 1% is undetectable and consequential is more dangerous than one right 90% of the time and
visibly wrong the rest. And it is why **per-instance guarantees** — always labeled, always
dismissible, always bounded, always cited — carry more real safety than any accuracy figure: they hold
on every output, where an accuracy figure holds on average and users experience instances.

---

# The Wrongness Cost

The autonomy ladder is not a design preference. It is set by three questions:

| Question | |
| --- | --- |
| What does one wrong output cost, in the user's terms? | |
| Who bears that cost? | |
| **Can the user detect that it is wrong?** | The decisive one |

> Where the user bears the cost and cannot detect the error, autonomy above "suggests" is not
> permitted without a mechanism that makes the error visible.

This is `07-strategy`'s reversibility thinking applied per output rather than per decision — and in
domains where the user's work is regulated and audited, it usually resolves to "suggests".

---

# Scope

**This module covers**

- Candidate capabilities and their comparison against non-AI alternatives
- Where the model sits in the existing architecture
- Autonomy, oversight, transparency and disclosure
- Data availability, quality, cold start and rights
- The evaluation plan, the golden set, and the ship gate
- Failure modes, detection, guardrails and the human fallback
- Model version, deprecation exposure and vendor lock-in
- Cost per operation and the share of revenue it consumes

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| The architecture | `09-technology` — the model is placed inside it |
| Prompt text and implementation | Build time, within these constraints |
| Metric instrumentation | `12-metrics` |
| Alerts, runbooks and support scripts | `13-operations` |

---

# Position in the Run

```
08-product ┐
09-technology ┴→ [ 14-ai-systems ] → 12-metrics
                                   → 13-operations
```

This module runs in the `specify` stage, alongside `09-technology`.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| Per-instance guarantees, non-AI fallbacks | **8** | Ordinary requirements and acceptance criteria |
| Model placement, data flow, cost line | 9 | Architecture and the cost model |
| Quality metrics and bars | 12 | Instrumentation and monitoring |
| Failure modes, fallbacks | 13 | Alerts, runbooks, support scripts |
| Guardrails and output constraints | `12-Build-Handoff.md` | What must hold at build time |
| All outputs | `15-AI-Strategy.md` | The shipped AI artifact — optional in the manifest |

`08-product` is an unusual consumer: this module hands **back** to a module that has already
completed. That is deliberate. The per-instance guarantees and the non-AI fallback are ordinary
requirements, and they belong where every other requirement lives rather than in an AI annex nobody
opens while building.

---

# One Discipline, Four Times

The regulated-field check appears in four modules, against the same list from `09-technology` §3:

| Module | Checks it against |
| --- | --- |
| `09-technology` | Obligations, mechanisms, enforcement points |
| `12-metrics` | Event properties |
| `13-operations` | The review schedule |
| **`14-ai-systems`** | **Model inputs** |

Sending a regulated field to a model provider is the same class of exposure as putting one in an
analytics event: the data now lives in a third-party system with different retention, different access
control, and possibly a different jurisdiction.

---

# Success Criteria

- Every capability compared against an alternative that survives the advocate check.
- Something dropped, with the simpler thing that replaced it recorded.
- Every data need confirmed, with cold-start behavior stated.
- Data rights established, and no regulated field as a model input.
- Autonomy justified by the wrongness cost and detectability.
- A bar, a qualified judge and a ship gate, all set before commitment.
- Failure modes specific to this product, with detection and guardrails.
- A non-AI fallback that exists as a requirement.
- The share of revenue computed, and a lever chosen if it is large.

---

# Self Assessment

- Would something simpler have worked?
- What did I drop?
- Is any data need unconfirmed?
- May we legally use this data this way?
- Can the user tell when it is wrong?
- Did I set the bar before or after seeing what it could do?
- Is my worst realistic outcome written down plainly?
- What share of revenue does this consume?

---

> **Purpose Principle**
>
> This is the last module in the framework, and its best outcome
> is often a shorter product.
>
> A capability dropped here because a sorted list solved the problem
> is the whole framework working as intended.
