---
Title: Template
Module: 07-strategy
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Strategy — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 07-strategy/core/06-Framework.md
Outputs:
  - projects/<slug>/research/07-strategy.md
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Strategy
  - Template
  - Output
---

# Template — Strategy

---

# Usage

Copy everything below the line into `projects/<slug>/research/07-strategy.md` and fill it.

This is a **working document**. It feeds the PRD, the Roadmap, Risks-and-Assumptions, and
the Executive Summary.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**This module ends at a human checkpoint.** The MVP cut is a commercial commitment, not a
research finding. Present it for approval; do not proceed past it alone.

---
---

# Strategy — «Project Name»

| | |
| --- | --- |
| Module | 07-strategy |
| Date | «ISO date» |
| Sharpest problem | «P«n» from 04-problem» |
| Problem evidence standing | **verified / assumed** |
| Status | draft / awaiting checkpoint / approved |

---

## 1. The Strategy, in One Paragraph

<!-- Write last. What we are building, for whom, why this approach, and what we are
     deliberately not doing. -->

«One paragraph.»

---

## 2. Inherited Position

<!-- What the research established. Restated so this document stands alone. -->

| | |
| --- | --- |
| Sharpest problem | «P«n»» — «statement» |
| Evidence standing | «verified / assumed» — from 04-problem |
| Primary persona | «name» — from 03-user |
| The gap | «summary» — from 05-competition |
| Defensibility | «defensible / temporary / not defensible» |
| Viability | «verdict» — from 06-business |
| Price | «figure» — from 06-business |

**If the problem is assumed rather than verified:** «state the consequence — Milestone
Zero is validation, and it appears in §10 Sequence before any build milestone»

---

## 3. Solution Options

<!-- Move 1. Minimum three, GENUINELY different. The test: would each produce a
     different first build? Three flavors of the same product is one option. -->

### Option A — «name»

| | |
| --- | --- |
| Approach | «one sentence» |
| Solves | P«n», P«n» |
| First build would be | «what you would make first» |
| Price it supports | «figure» |
| Defensibility | «assessment» |
| Biggest risk | «what» |
| **Provenance** | «`carried_from_research` — modules 02–06 researched this / `generated_here` — invented in this module» |
| **Chosen** | «true on exactly one option across the whole list, once §6 commits. The asymmetry rule fires on the winner and cannot fire without this» |
| **Never researched by** | «modules that did not examine this option, and what each would have tested. Only for `generated_here`; write "n/a" otherwise» |

### Option B — «name»

«same structure»

### Option C — «name»

«same structure»

**How these differ:** «one paragraph — if they differ only in feature scope, they are
one option and the module must generate more»

### Provenance and what it costs the comparison

<!-- Criterion 8. A generated option is frequently the RIGHT answer — it is what a run looks
     like when the evidence redirected it. What it is not is comparably evidenced. Say so
     HERE, where the scores are, not in a footnote. -->

**Options generated in this module:** «list, or "none — all three carried from research"»

**What they arrive without:** «per generated option — the market sizing, competitor set,
segment work and problem ranking that the researched options have and this one does not»

**If a generated option wins, the re-score test:** re-score it with every criterion it was
never researched on set to the lowest value any researched option scored on that criterion.

| | |
| --- | --- |
| Original score | «figure» |
| Re-scored at the floor | «figure» |
| **Still wins?** | «yes — the win is robust to the missing research / no — **the win rests on the gap**» |
| **`asymmetry_effect`** | «the sentence written to `state.outputs.solution_options[].asymmetry_effect`. The validator reads this field, not the table above — reasoning that lives only in prose here leaves it empty» |

**Path chosen:** «(a) a research pass through the skipped modules before the recommendation
stands / (b) a validation milestone closing its specific unresearched claims, placed first in
the roadmap and blocking the first build milestone»

**What still stands from the options it displaced:** «evidence does not stop being true
because the recommendation moved — name what survives and applies to the winner»

---

## 4. Pre-Registration

<!-- WRITE THIS BEFORE SECTION 5. It is the only section whose value depends entirely on
     when it was written, and the only one that cannot be repaired afterward. Once a single
     score is assigned, this section can no longer be written honestly at all.

     Copy the fields below into state.pre_registration verbatim. Do not invent field
     names — four runs each invented their own and none of them could be compared. -->

**Expected winner:** «Option X»

**Expected because:** «the reasoning as held right now, in one paragraph, referencing what
the research established rather than what feels right»

**Independence:** «independent / contaminated»

**If contaminated, what pre-committed the answer:** «name it — upstream modules that
already converged, an operator instruction that stated a direction, a previous run whose
conclusion was easy to defend. Leave blank only when marking independent»

> **Mark it `contaminated` when unsure.** A false `contaminated` discounts one honest
> prediction. A false `independent` reports a clean record the framework has not earned,
> and the error is invisible from inside this document.

<!-- Everything below is filled in AFTER section 5 completes. Nothing above is edited,
     including when the result is embarrassing. -->

**Actual winner:** «Option X — filled after scoring»

**Matched:** «yes / no»

**What this match or miss does and does not prove:** «one paragraph. A miss is the
strongest available evidence that the comparison did real work. A match on a contaminated
expectation proves nothing and must not be presented as confirmation»

---

## 5. Comparison

<!-- Move 2. Score against what the research established, not against preference. -->

| Criterion | Weight | A | B | C |
| --- | --- | --- | --- | --- |
| Solves the sharpest problem | high | «score» | | |
| Solves problems 2–3 | med | | | |
| Fits the gap from 05 | high | | | |
| Defensible | high | | | |
| Supports the price from 06 | high | | | |
| Buildable by the assumed team | med | | | |
| Time to first customer | med | | | |
| Survives if the assumed problem is wrong | med | | | |

**Scoring basis:** «how scores were assigned»

---

## 6. The Choice

<!-- Move 3. Commit. Record what was rejected and why — that is what makes this a
     decision rather than a preference. -->

## Chosen: Option «X» — «name»

**Why:** «one paragraph, referencing §5 and the ranked problems»

**Rejected**

| Option | Why not | What we would lose |
| --- | --- | --- |
| «A» | «reason» | «what it would have given us» |
| «C» | «reason» | «...» |

**What we are betting on:** «the belief this choice depends on»

**What would make us choose differently:** «the trigger that would reverse this»

### Differentiation

<!-- Criterion 9. Required when 01-idea recorded stance `category`. Where the stance was
     `committed`, write "not applicable — the thesis was set at 01-idea" and move on. -->

**Stance at 01-idea:** «`category` / `committed`»

**Resolved by:** «the option that supplies the differentiating position, and what it is —
or `not found`»

**If `not found`:** «the finding, with its evidence. A category with no available position
is a real conclusion and usually the one that saves the most money. It is stated here, not
left as an empty field»

---

## 7. MVP Definition

<!-- Move 4. The cut line, drawn and defended. -->

**The MVP is:** «one paragraph — the smallest thing that solves the sharpest problem
end to end for the primary persona»

### Above the line

| # | Capability | Serves | Why it cannot be cut |
| --- | --- | --- | --- |
| 1 | «capability» | P«n» | «reason» |

### Below the line

| # | Capability | Serves | Why deferred | Revisit when |
| --- | --- | --- | --- | --- |
| «n» | «capability» | P«n» | «reason» | «trigger» |

**The cut principle:** «one sentence — what makes something MVP in this product»

**The end-to-end test:** Can «primary persona» complete «the core job» using only what is
above the line? **«yes / no»**

<!-- If no, the cut is wrong. An MVP that cannot complete one job end to end
     teaches nothing when it ships. -->

**What the MVP proves:** «the specific belief it tests»

**What it deliberately does not prove:** «what still remains unknown after shipping it»

---

## 8. Non-Goals

<!-- Move 5. Explicit. This section prevents six months of argument. -->

| Not doing | Why | Reconsider when |
| --- | --- | --- |
| «capability or market» | «reason» | «trigger, or "not planned"» |

**Segments we are not serving:** «who, and why»

**Problems we are not solving:** «from 04-problem's excluded list»

---

## 9. Risk Register

<!-- Move 6. Likelihood, impact, mitigation, and the early warning sign. -->

| # | Risk | Category | Likelihood | Impact | Mitigation | Early warning sign |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | «risk» | market | h/m/l | h/m/l | «action» | «what you would see first» |
| R2 | «risk» | technical | | | | |
| R3 | «risk» | commercial | | | | |
| R4 | «risk» | regulatory | | | | |

<!-- Be honest with the ratings. A register where everything is "medium" is useless. -->

### Top risks in detail

#### R«n» — «name»

| | |
| --- | --- |
| What happens | «description» |
| Why it is plausible | «reasoning» [tag] |
| Leading indicator | «what you would observe first» |
| Mitigation | «what reduces likelihood» |
| Contingency | «what you do if it happens anyway» |
| Accepted? | «yes — we proceed knowing this / no — mitigation required first» |

### Risks inherited

| Source | Risk |
| --- | --- |
| 04-problem | «if the problem is assumed — the whole product rests on it» |
| 05-competition | «if not defensible — the six-month clock» |
| 06-business | «the load-bearing economic assumption» |

---

## 10. Sequence

<!-- Move 6 continued. High-level only — 09-Roadmap.md is the full artifact. -->

| Milestone | Delivers | Proves | Depends on |
| --- | --- | --- | --- |
| **M0 — Validate** | «the test» | «the belief» | — |
| M1 | «capability» | «what we learn» | M0 |
| M2 | «capability» | | M1 |

**Is M0 required?** «yes / no» — «required whenever the sharpest problem is assumed, or
module 04 declared a shortfall»

**What we learn at each milestone:** «one line each — a milestone that teaches nothing is
a schedule entry, not a milestone»

---

## 11. Stop Conditions

<!-- Define failure before it arrives, while the thinking is still cheap. -->

| Signal | Threshold | What it means | Action |
| --- | --- | --- | --- |
| «observable» | «specific number» | «interpretation» | stop / pivot / rethink |

---

## 12. Contradicting Evidence

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against this strategy» | [tag] | «what it would mean» | «how addressed» |

---

## 13. For the Checkpoint

<!-- This section is what the operator reads. Make it decidable. -->

**We are proposing to:** «one sentence»

**We are deliberately not:** «one sentence»

**This rests on:** «the load-bearing assumption»

**Decisions we need from you**

| # | Decision | Options | Our recommendation |
| --- | --- | --- | --- |
| 1 | «e.g. approve the MVP cut» | «approve / expand / narrow» | «which, and why» |

**If you approve, next is:** «module 08 — the PRD»

---

## 14. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `chosen_approach` | «summary» | 08, 09 |
| `mvp_definition` | «the cut» | 08 |
| `non_goals` | «list» | 08 |
| `risk_register` | «table» | 10-Risks deliverable |
| `roadmap` | «milestones» | 09-Roadmap deliverable |

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] >= 3 genuinely different options — each implies a different first build
- [ ] Options compared against research-established criteria, weighted
- [ ] One chosen, with rejected options and what they would have given us
- [ ] The bet stated, and the trigger that would reverse it
- [ ] MVP cut line drawn with the principle recorded
- [ ] End-to-end test passes — the persona can complete the core job
- [ ] What the MVP proves, and does not prove, both stated
- [ ] Explicit non-goals listed
- [ ] Risks rated honestly with mitigations and early warning signs
- [ ] Inherited risks from 04, 05 and 06 carried forward
- [ ] Milestone Zero present if the sharpest problem is assumed
- [ ] Stop conditions defined with thresholds
- [ ] Checkpoint section is decidable
- [ ] Every placeholder replaced, every guidance comment removed
-->
