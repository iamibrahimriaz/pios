---
Title: Purpose
Module: 07-strategy
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Strategy module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - core/00-Purpose.md
  - 06-business gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Strategy
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Every module before this one gathered information. This one spends it.

The research established what is true: a market exists, a person has problems, some are
proven, nobody serves them well, and a business could plausibly work. None of that says
what to build.

This module decides. It is the hinge of the run — everything before is reversible,
everything after executes the choice made here.

---

# Purpose Statement

> Choose what to build, in what order, and what deliberately not to build —
> then hand that decision to the human who has to fund it.

---

# Why This Module Exists

Two failures dominate strategy work, and both are avoidable.

**Choosing without generating.** Arriving with an answer already in mind and producing
alternatives to justify it. The document looks like a decision was made; it was not.

**Deciding without cutting.** Producing a strategy where everything is important. A plan
with no exclusions is a summary of research wearing a strategy's clothes, and it delays
first contact with a real user by months.

This module's structure — generate three genuinely different options, score them against
research findings, cut hard, and write down what is excluded — exists to make both failures
visible.

---

# The Judgment This Module Makes

| Output | The commitment it represents |
| --- | --- |
| `chosen_approach` | Which of several viable directions we take |
| `mvp_definition` | What ships first, and what does not |
| `non_goals` | What we refuse to do |
| `risk_register` | What we know could go wrong, and what we would see first |
| `roadmap` | The sequence, including validation before building if the problem is unproven |

---

# Core Objectives

- Generate at least three genuinely different approaches.
- Score them against what the research established, not against preference.
- Commit to one, and record what the rejected options would have given us.
- Draw an MVP line small enough to solve one problem end to end.
- State explicitly what this product will not do.
- Register risks with observable early warnings.
- Present the commercial decision to the operator, cleanly.

---

# What AI Should Learn Here

- A strategy is defined by what it refuses to do.
- Three options that would produce the same first build are one option.
- An MVP that cannot complete a single job teaches nothing when it ships.
- Writing down what an MVP does **not** prove prevents the wrong conclusion later.
- A risk without an early warning sign has not been thought through.
- Inherited uncertainty must not be upgraded by a confident writing style.
- The cut is a commercial decision and belongs to the operator.

---

# The Register Problem

Strategy documents are written decisively. That register is a convention of the genre, not
a claim about certainty — and it creates this module's characteristic failure:

> **Confidence laundering.** Three upstream modules report honest uncertainty. The strategy
> document restates their conclusions in decisive language, and the uncertainty quietly
> disappears.

An assumed problem becomes "the problem". A gap that any incumbent could close becomes "our
advantage". Conditional viability becomes "viable".

The gate checks for it explicitly. Inherited uncertainty is carried forward in the strength
the source module used.

---

# Scope

**This module covers**

- Option generation and comparison
- The strategic choice and what it rejects
- The MVP cut
- Non-goals
- Risk registration
- High-level sequencing and stop conditions

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| New research to distinguish options | Return to modules 02–06 |
| Requirement specification | `08-product` |
| Architecture | `09-technology` |
| Detailed milestone planning | `10-execution` |
| Channel strategy | `11-growth` |

---

# Position in the Run

```
04-problem ┐
05-competition ├→ [ 07-strategy ] → ⏸ HUMAN CHECKPOINT → 08-product
06-business ┘
```

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `mvp_definition` | 08 | The binding scope — nothing below the line is a MUST |
| `chosen_approach` | 08, 09 | What the product and architecture serve |
| `non_goals` | 08 | Explicit exclusions in the PRD |
| `risk_register` | Risks deliverable | The shipped risk artifact |
| `roadmap` | 10, Roadmap deliverable | Sequencing, including Milestone Zero |

---

# Milestone Zero

When module 04 could not verify the sharpest problem — or recorded a declared shortfall —
this module must open the sequence with validation rather than building.

That is the mechanism by which the framework's honesty about evidence changes what
actually happens first. Without it, module 04's carefully labeled uncertainty becomes a
paragraph nobody acts on.

---

# Success Criteria

- Three options a competent person could genuinely choose between.
- A choice whose every scoring row traces to a research finding.
- Rejected options recorded with what they offered.
- An MVP small enough to pass the end-to-end test.
- Non-goals covering capabilities, segments and problems.
- Differentiated risk ratings with observable early warnings.
- Milestone Zero present when the problem is unproven.
- A checkpoint that presents a decision, not an announcement.

---

# Self Assessment

- Did I generate before I chose?
- Would my three options produce different first builds?
- Is my MVP a cut, or a ranking?
- Have I written what we are not doing?
- Does my language claim more certainty than I inherited?
- Am I asking the operator, or telling them?

---

> **Purpose Principle**
>
> Research can be redone. This decision cannot be un-made cheaply.
>
> That is why the module ends by handing it to a person.
