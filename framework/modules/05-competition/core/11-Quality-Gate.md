---
Title: Quality Gate
Module: 05-competition
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Competition module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 05-competition/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 02-market
  - 07-strategy
Tags:
  - Competition
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This gate closes the research stage. After it, the run stops describing the world and
starts committing to a direction.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — >= 5 competitors, direct and indirect, with sources

**Passes when:** five or more entries exist, they span at least three of the five types
(direct, indirect, substitute, status quo, non-consumption), and each carries a source.

**Fails when:** all five are direct competitors, or any entry is named without a source.

Five funded products is not competitive coverage. It is a category search. The types that
actually displace new entrants — the status quo and doing nothing — are the ones a
category search never returns.

| Fails | Passes |
| --- | --- |
| Five SaaS products in the same category | Two direct products, one adjacent platform adding the feature, the status quo (paper plus after-hours transcription), and non-consumption (practices that accept the process) |

---

# Criterion 2 — Pricing captured or explicitly marked unavailable

**Passes when:** every competitor has either a sourced price with a date, or an explicit
"not published" marker with the implication noted.

**Fails when:** any price appears without a source, or a competitor's pricing row is simply
blank.

**The silent-estimate check.** Scan for figures phrased as approximations — "around",
"roughly", "about". Each must carry either a source or an `[inferred]` tag showing its
basis. An unsourced approximation becomes an input to module 06's revenue model, where it
stops looking like a guess.

**Dates are part of this criterion.** Pricing changes; an undated figure fails.

---

# Criterion 3 — "Do nothing / status quo" evaluated as a competitor

**Passes when:** the status quo has its own row, is scored in the problem coverage table
like any other competitor, and its strengths are stated honestly.

**Fails when:** it is mentioned in prose but not scored, or listed in the matrix and then
ignored for the rest of the document.

**Test:** does the analysis state what the status quo is *good at*? It is free, already
installed, fully trusted, requires no migration, and no one gets blamed for continuing it.
An analysis that treats it only as a weak baseline has not evaluated it.

**Also expected:** non-consumption considered. Not a separate gate criterion, but an
analysis that assumes everyone in the segment uses something has probably overstated the
addressable opportunity.

---

# Criterion 4 — >= 1 defensible gap articulated with reasoning

**Passes when:** a gap is identified, it maps to a ranked problem from module 04, the
reason it exists is stated, **and the six-month question is answered.**

> If this works, what stops the incumbent shipping it in six months?

**Fails when:** a gap is asserted with no structural reason, or the defensibility question
is not addressed at all.

**"Not defensible" passes this criterion.** The criterion requires the question to be
answered, not answered favorably. A stated finding of "nothing stops them; our advantage
would be focus and speed" is honest analysis and module 07 can plan around it. Silence
cannot be planned around.

| Fails | Passes |
| --- | --- |
| "Incumbents don't serve solo practices well" | "Incumbents don't serve solo practices because their sales motion requires a procurement committee and their pricing floor exceeds a solo practice's software budget. Could they close it in six months? They could build it; they could not sell it without a new motion. Defensibility: moderate." |

---

# Cross-Module Coherence

This module is the first place three research threads meet. Check them explicitly:

| Check | Fails when |
| --- | --- |
| The gap maps to a ranked problem from module 04 | The gap is a market observation, not an opportunity |
| Competitors serve the segment from module 03 | They compete in a different market |
| The analysis stays inside `market_definition` | The boundary was quietly widened to find competitors |

A gap that does not correspond to a real, ranked problem is not an opportunity. It is a
description of something nobody does.

---

# Universal Gates

U1–U7 apply. Most often missed here:

| | |
| --- | --- |
| **U1** | Vendor claims restated as capability is the classic untagged assertion in this module |
| **U3** | The competitor set must not contradict `market_definition` |
| **U4** | The positioning statement is a decision; alternatives considered should be recorded |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Verify every competitor and price resolves to a source.
3. Verify the gap maps to a ranked problem.
4. Evaluate universal gates U1–U7.
5. Evaluate criteria 1–4.
6. Record the verdict.

```yaml
gate:
  module: 05-competition
  attempt: 1
  criteria:
    five_competitors_typed: pass
    pricing_sourced_or_marked: fail
    status_quo_evaluated: pass
    defensible_gap_reasoned: pass
  coherence:
    gap_maps_to_ranked_problem: pass
    competitors_serve_target_segment: pass
  defensibility_verdict: moderate
  verdict: fail
  reason: "C3 priced at 'around $80/month' with no source or inferred tag."
  action: "Source it, or mark unavailable with the implication noted."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 02-market`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | Unsourced price, status quo unscored | Revise here |
| **Upstream (market)** | Competitors found serve a different market | Return to `02-market` |
| **Upstream (problem)** | The gap maps to no ranked problem | Return to `04-problem` via `02-market` |

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate |

---

# What a Passing Module 05 Looks Like

- The competitor list contains things that are not products.
- The status quo is described with genuine respect for why it persists.
- Competitors are scored against ranked problems, not a feature checklist.
- Every price is sourced and dated, or honestly marked unavailable.
- The gap maps to a specific ranked problem for a specific segment.
- The six-month question is answered plainly, including when the answer is unwelcome.
- The positioning statement could not appear on a competitor's homepage.

---

> **Gate Principle**
>
> This gate closes the research stage.
>
> Everything after it is commitment — so the last question research asks
> is whether the opening can actually be held.
