---
Title: Workflow
Module: 11-growth
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Growth module.
Audience:
  - AI Agents
Prerequisites:
  - 11-growth/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/11-growth.md
  - state.outputs.growth_loops
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Loop. This document is the procedure.

This module runs in the `operationalise` stage. Its output is consumed by `12-metrics`, which
turns the activation event, the retention mechanism and the loops into measurable definitions.

---

# Position in the Run

```
06-business ┐
08-product  ┴→ [ 11-growth ] → 12-metrics
```

| | |
| --- | --- |
| Stage | `operationalise` |
| Depends on | `06-business`, `08-product` |
| Consumes | `go_to_market`, `segments`, `feature_spec` |
| Produces | `acquisition_channels`, `growth_loops`, `retention_model`, `onboarding_strategy`, `expansion_paths` |
| On fail | return to `06-business` |
| Human checkpoint | none |

Run this before `12-metrics`. The dependency is declared in `12-metrics/module.yaml`, which
consumes `growth_loops` and `retention_model` — the activation event defined here becomes the
metric defined there.

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `06-business` and `08-product` are in `state.run.completed_modules`.
2. Read from `06-business`: the price, the **gross margin per user**, the route to market, the
   CAC and churn position — including how they were handled, which was a sensitivity table
   rather than a figure.
3. Read from `03-user`: the segments, and **where they were observed** — publications,
   gatherings, communities, referral norms.
4. Read from `05-competition`: the status quo, the switching cost, and where competitors reach
   this segment.
5. Read from `08-product`: the requirements — retention mechanisms must map to these.
6. Read from `10-execution`, if complete: the **activation moment**, time to first value, and
   the step count.
7. Check whether the sharpest problem is verified or assumed.

Record before planning:

| Inherited | Consequence |
| --- | --- |
| Price and gross margin | The CAC ceiling, and therefore which motions are possible |
| Where the segment was observed | The only defensible channel evidence |
| Switching cost | It belongs inside activation, not after it |
| CAC and churn unknown | They stay unknown here |
| Problem **assumed** | No acquisition spend before Milestone Zero |

> If `10-execution` has not yet run, the activation event may be defined here and must then be
> reconciled with time to first value once it does.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `11-growth/core/03-Core-Principles.md`
3. `11-growth/core/06-Framework.md` — the Six Moves
4. `11-growth/core/08-Questions-To-Answer.md`
5. `11-growth/knowledge/` — Acquisition-Channels, Activation, Onboarding, Retention, Churn,
   Growth-Loops, Referral, Expansion
6. `framework/deliverables/templates/13-Growth-Plan.md`

---

# Step 3 — Model, and Run the Payback Check

Move 1.

1. Choose one primary growth model, and state why not the alternative — from segment research,
   not preference.
2. State what the model requires the product to do, and whether the MVP supports it.
3. Run the payback check:

```
margin per user per month × acceptable payback months = CAC ceiling
cost of one unit of the motion ÷ conversions per unit = implied CAC
```

| Result | Action |
| --- | --- |
| Implied CAC under the ceiling | Continue |
| Over the ceiling | Record a **regress** — to `06-business` for the price, or `07-strategy` for the segment |

Do not resolve a failed payback check by raising the assumed conversion rate. That is the
single most common way an unaffordable motion survives a plan.

---

# Step 4 — Locate

Move 2.

1. List candidate channels, each with **where the segment was observed** and the citation.
2. Mark channels that cannot be evidenced — these are open questions, not plan rows.
3. Estimate the **learning cost** per channel: what one test costs and how long it takes to
   produce a usable answer.
4. Choose the first channel by learning cost.
5. Name the channels deliberately not used, with why they would waste money on this segment.

Any CAC figure here is `[assumption: needs validation]` with its basis stated. `06-business`
established that CAC is unknowable before launch; this module does not have new information.

---

# Step 5 — Activate

Move 3.

1. Name the activation event — a specific action, not a signup.
2. State why that action proves the user received value.
3. Carry time and step count from `10-execution`.
4. Name the biggest friction before activation.
5. Place the switching cost from `05-competition` **inside** the activation flow.
6. State a target activation rate, tagged as an assumption.
7. Name the one change that would most improve activation — from the flow analysis, not from
   general practice.

---

# Step 6 — Retain

Move 4.

1. Name each retention mechanism, and how it makes leaving costly.
2. **Map each to the requirement that delivers it.** List any mechanism with no requirement
   behind it.
3. State whether retention depends on the MVP or on deferred scope. If deferred, say plainly
   that retention is unproven at launch.
4. Carry the churn position from `06-business` as an assumption.
5. Name the **observable behavior that precedes leaving** — this is the actionable output;
   a churn percentage is not.

---

# Step 7 — Loop

Move 5.

For each candidate loop, write the cycle and then run the **closure test**:

```
Does the output become the next input?
  ├─ yes → it is a loop. State cycle time, amplification, leak, evidence
  └─ no  → it is a funnel. Say so, in those words
```

Then write the honest statement: if nothing closes, the product grows linearly with spend, and
the plan says that. A funnel drawn with an arrow back to the top misrepresents the business to
the person funding it.

---

# Step 8 — Name, and Sequence

Move 6.

1. Write the first ten customers — named where possible, specifically profiled otherwise, with
   the route, their reason, and what would make them say no.
2. Write the pitch in one sentence.
3. Where the problem is assumed, state that these ten are **Milestone Zero's validation
   sample**, not a sales pipeline.
4. Write onboarding stages with success signals.
5. Write expansion paths, or state plainly that there are none.
6. Write the **sequencing table**: what must be true before the first ten, before the first
   channel test, and before channel scale.
7. Where the problem is assumed, state that no acquisition spend happens before Milestone Zero
   completes.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/11-growth.md`. Write §1 last.

```yaml
outputs:
  acquisition_channels:  # §3 — with evidence and learning costs
  onboarding_strategy:   # §4, §8 — activation and stages
  retention_model:       # §6 — mechanisms mapped to requirements
  growth_loops:          # §7 — with closure verdicts
  expansion_paths:       # §9 — or an explicit none
```

Append every rate, cost and conversion figure without a source to `state.assumptions` with a
validation method — U5. Append the model choice to `state.decisions` with the alternative
rejected — U4. Append unevidenced channels to `state.open_questions`.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which channel did I include because products like this use it?
- Did I raise a conversion assumption to make the payback check pass?
- Is my activation event chosen because it proves value, or because it is easy to log?
- Which retention mechanism has no requirement behind it?
- Have I drawn an arrow back on a funnel?
- Which loop's "evidence it works" is actually a plausible story?
- Are the first ten real people, or a profile with a number next to it?
- Am I planning to spend money before knowing whether the problem is real?

The coherence pass: does the growth model fit the price from `06-business` and the segment from
`03-user`? A self-serve motion for a product sold to a procurement committee is a contradiction,
not an ambition.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 06-business`. Three attempts, then halt |

---

# Step 12 — Hand Off

1. Append `11-growth` to `state.run.completed_modules`.
2. Hand the activation event, retention mechanisms and loops to `12-metrics`.
3. Hand the sequencing table to the roadmap output.
4. Note whether the growth plan deliverable is in scope — it is optional in the manifest.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `12-metrics` | Activation event, `retention_model`, `growth_loops` | These become the north star, the activation metric and the leading indicators |
| `09-Roadmap.md` | Sequencing table | When growth work starts, and what gates it |
| `13-Growth-Plan.md` | All outputs | The shipped growth artifact, when in scope |

`12-metrics` is the strict consumer. The activation event defined here becomes an instrumented
event with properties; if it is vague, the metric is uncomputable and the product ships unable
to tell whether anyone activated.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Channels with no evidence | Borrowed growth | Cite where the segment was observed, or move it to open questions |
| Payback check passes on a raised conversion rate | Arithmetic bent to fit | Restore the assumption and record the regress |
| Motion the price cannot fund | Payback check skipped | Run it; change the model, price or segment |
| Activation defined as signup | Convenience over meaning | Name the action that proves value |
| Switching cost placed after activation | Migration treated as onboarding's problem | Move it inside the activation flow |
| "A great product" as retention | Mechanism not identified | Name the mechanism and its requirement |
| Retention mechanism in deferred scope | Not checked against the MVP | State that retention is unproven at launch |
| Funnel presented as a loop | Closure test not run | Call it a funnel |
| Loop with invented evidence | Hypothesis written as finding | Tag it as a hypothesis |
| First ten as a market description | Move 6 skipped | Name people, or profile them specifically |
| Spend planned before validation | Sequence rule ignored | Gate spend on Milestone Zero |

---

> **Workflow Principle**
>
> Every number in this module is about behavior that has not happened yet.
>
> The honest output is not a forecast. It is an order of experiments,
> and a statement of what must be true before each one.
