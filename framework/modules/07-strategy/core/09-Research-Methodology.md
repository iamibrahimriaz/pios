---
Title: Research Methodology
Module: 07-strategy
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how strategic reasoning is evidenced when the subject is a decision, not a fact.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - engine/evidence-policy.md
  - 07-strategy/core/06-Framework.md
Outputs:
  - Evidenced strategic reasoning
  - state.decisions
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - Strategy
  - Research
  - Decisions
---

# Research Methodology

---

# Overview

This module researches almost nothing new.

Its subject is a **decision**, and a decision cannot be verified against a source. There is
no citation for "we should build the narrow tool rather than replace the workflow".

That does not exempt it from the evidence policy. It changes what evidence means here:
instead of sourcing claims about the world, this module must show that its reasoning
**traces to** claims other modules already sourced.

---

# Methodology Statement

> A strategy cannot be verified. It can be traced.
>
> Every strategic claim must resolve to a finding from an earlier module,
> or be declared as a bet.

---

# The Two Kinds of Statement

Everything in a strategy document is one of two things:

| Type | Definition | How it is evidenced |
| --- | --- | --- |
| **Derived** | Follows from research findings | Cite the module and the finding |
| **Bet** | A belief the strategy depends on that no research established | Declare it, and register it as a risk |

Both are legitimate. Confusing them is not.

```
Derived:
  The MVP targets solo practices [derived: 03-user §2 prioritization —
  highest pain intensity, lowest approval friction].

Bet:
  Practitioners will accept a 20-second review step for generated notes
  [bet: no evidence; registered as R2; invalidated if fewer than 6 of 10
  interviewees accept it in Milestone Zero].
```

The second is not weaker research. It is a correctly labeled commitment.

---

# Tracing the Choice

The gate requires the choice to be justified against the ranked problems rather than
preference. In practice that means each scoring row cites its source:

| Criterion | Cites |
| --- | --- |
| Solves the sharpest problem | `04-problem` — the ranked list and its scores |
| Fits the gap | `05-competition` — the gap and which problem it maps to |
| Defensible | `05-competition` — the six-month answer |
| Supports the price | `06-business` — price and value calculation |
| Buildable by the team | `06-business` — cost structure and assumed team |
| Time to first customer | `06-business` — sales cycle and first-ten route |

A score with no citation is a preference with a number attached.

---

# Evidencing Option Quality

The straw-man failure is invisible in the finished document — three options appear, one is
chosen, the reasoning looks sound.

Two checks make it visible:

**The different-first-build test.** State, for each option, what would be built first. If
the answers match, the options are one option.

**The advocate test.** For each rejected option, write the strongest case *for* it — one
sentence, made honestly. If that sentence cannot be written, the option was never viable
and should be replaced rather than counted.

Recording what each rejected option would have given us is the durable form of this test,
and it is what the gate checks.

---

# Evidencing the MVP Cut

The cut is a judgment, but it has one objective test:

> Can the primary persona complete the core job using only what is above the line?

That is answerable yes or no by walking the workflow from `03-user` step by step against
the included capabilities. Do that walk explicitly rather than asserting the answer.

The cut principle should also trace: "everything required to complete job J1 for persona P,
nothing else" is a principle derived from module 03. "The most valuable features" is not a
principle at all.

---

# Rating Risk Honestly

Risk ratings are judgments, and judgments drift toward comfortable values. Two disciplines
help.

**Rate the likelihood before the impact.** Rating impact first anchors the likelihood — a
catastrophic risk gets quietly downgraded in probability because the combination is
unbearable.

**Require an early warning sign.** A risk with no observable precursor is usually one that
has not been thought about. Producing the warning sign forces the mechanism to be
articulated, and the mechanism reveals the true likelihood.

Then check the distribution. If every risk is medium, the register was filled in rather
than assessed.

---

# Inherited Uncertainty

This module sits downstream of three verdicts, and it must not launder them.

| Inherited | Must appear as |
| --- | --- |
| Sharpest problem is assumed | Milestone Zero, plus a registered risk that the product rests on an untested belief |
| Gap is not defensible | A registered risk with a timescale, plus a speed or focus answer |
| Business viable only under conditions | Those conditions restated as risks or stop conditions |

The characteristic failure is **confidence laundering**: three modules report honest
uncertainty, and the strategy document — written in the decisive register that strategy
documents use — presents a clean plan that reads as though the uncertainty resolved.

It did not. Carry it forward in the same words the source module used.

---

# Stop Conditions Must Be Falsifiable

"If traction is poor, we will reconsider" is not a stop condition. Nothing can trigger it.

A usable one names an observable, a threshold, a time, and an owner:

```
If fewer than 3 of the first 10 pilot practices complete a second week of
use by «date», stop and re-examine the problem framing. Reviewed by «role».
```

Derive the numbers from module 06 where possible — the break-even customer count and the
activation assumptions both suggest thresholds.

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| New market or user research | Modules 02–05; return there if needed |
| Requirement specification | `08-product` |
| Architecture decisions | `09-technology` |
| Detailed milestone planning | `10-execution` and the Roadmap deliverable |
| Channel strategy | `11-growth` |

If this module finds itself needing new research to choose between options, that is a
signal to return upstream rather than to research inline. Options that cannot be
distinguished without new evidence indicate the earlier modules stopped too early.

---

# Recording

| Destination | What |
| --- | --- |
| `state.decisions` | Every decision with alternatives rejected and rationale — U4 requires it |
| `state.assumptions` | Every bet, with what would invalidate it |
| `state.open_questions` | Anything the checkpoint must resolve |
| Strategy §9 | The risk register |
| Strategy §11 | Stop conditions with thresholds |

---

# Self Assessment

- Is every strategic claim either derived with a citation, or declared as a bet?
- Did I write what each rejected option would have given us?
- Did I walk the workflow to test the MVP cut, or assert the answer?
- Did I rate likelihood before impact?
- Does every risk have an observable early warning?
- Did I carry inherited uncertainty forward in its original strength?
- Are my stop conditions falsifiable?

---

> **Research Principle**
>
> Strategy documents are written in a confident register.
>
> That register is borrowed, not earned — and it must not quietly upgrade
> the uncertainty it inherited.
