---
Title: Checklist
Module: 11-growth
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Growth module.
Audience:
  - AI Agents
  - Founders
Prerequisites:
  - 11-growth/core/07-Workflow.md
  - 11-growth/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Checklist
---

# Checklist

---

# Entry

- [ ] `06-business` and `08-product` in `state.run.completed_modules`
- [ ] Price and **gross margin per user** read from `06-business`
- [ ] CAC and churn position read — including that both were unknown
- [ ] Route to market read from `06-business`
- [ ] Segments read from `03-user`, **with where they were observed**
- [ ] Referral norms read from `03-user`
- [ ] Status quo and **switching cost** read from `05-competition`
- [ ] Competitor channels read from `05-competition`
- [ ] Requirements read from `08-product` — retention must map to these
- [ ] Activation moment and time to first value read from `10-execution`, if complete
- [ ] Problem evidence standing checked — verified or assumed
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Move 1 — Model

- [ ] One primary growth model chosen
- [ ] Alternative rejected, with reasoning from segment research
- [ ] What the model requires the product to do, stated
- [ ] Whether the MVP supports it, stated
- [ ] **OPERATOR asked** for an acceptable payback period

**Payback check**

- [ ] Gross margin per user per month recorded
- [ ] CAC ceiling computed
- [ ] Cost of one unit of the motion recorded, with a citation
- [ ] Conversions per unit stated as an assumption
- [ ] Implied CAC computed
- [ ] Comparison made
- [ ] **No conversion assumption was raised to make it pass**
- [ ] If over the ceiling, a regress is recorded

---

# Move 2 — Locate

- [ ] Candidate channels listed
- [ ] **Every channel cites where the segment was observed**
- [ ] Unevidenced channels moved to open questions, not left in the plan
- [ ] Competitor channels noted as their behavior, not as proof
- [ ] Learning cost per channel stated — what one test costs
- [ ] Time to a usable answer per channel stated
- [ ] **First channel chosen by learning cost**
- [ ] Channels deliberately not used, listed with reasons
- [ ] Every CAC figure tagged as an assumption with its basis

---

# Move 3 — Activate

- [ ] Activation event is a specific action, not a signup
- [ ] Why that action proves value, stated
- [ ] Time in minutes carried from `10-execution`
- [ ] Step count carried from `10-execution`
- [ ] Consistency with `10-execution` §5 confirmed
- [ ] Biggest friction named
- [ ] **Switching cost placed inside the activation flow**
- [ ] Target activation rate stated and tagged
- [ ] The one change that would most improve activation, named

---

# Move 4 — Retain

- [ ] Each mechanism named mechanically — not "a great product"
- [ ] **Each mechanism maps to a requirement from `08-product`**
- [ ] Mechanisms with no requirement listed explicitly
- [ ] Location check run — each requirement genuinely creates a cost to leaving
- [ ] Whether retention depends on the MVP or deferred scope, stated
- [ ] If deferred, "retention is unproven at launch" stated plainly
- [ ] Churn carried from `06-business` at the same confidence
- [ ] **Observable behavior that precedes leaving, named**
- [ ] First retention risk point in the lifecycle, named

---

# Move 5 — Loop

Per candidate loop:

- [ ] Cycle written — input, action, output
- [ ] **Closure test run: does the output become the next input?**
- [ ] Closure verdict recorded — loop or funnel
- [ ] Cycle time stated
- [ ] Amplification stated, or "nothing — it is linear"
- [ ] Leak point named
- [ ] Evidence stated, or "none, this is a hypothesis"
- [ ] **No arrow drawn back on a funnel**
- [ ] If nothing closes, the honest statement is written

---

# Move 6 — Name and Sequence

- [ ] First ten written — named, or specifically profiled
- [ ] Route per person is specific, not a channel category
- [ ] Why each would say yes, from their perspective
- [ ] **What would make them say no**, from `05-competition`
- [ ] Pitch written in one sentence
- [ ] Where the problem is assumed, the ten identified as the **validation sample**
- [ ] Onboarding stages with goals and observable success signals
- [ ] Skippable stages marked
- [ ] Highest drop-off risk named
- [ ] Expansion paths written, or "none" stated with revenue per customer
- [ ] Referral position taken from `03-user`, not designed
- [ ] **Sequencing table written** — what must be true before each stage
- [ ] Where the problem is assumed, **no spend before Milestone Zero**, stated

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/11-growth.md`
- [ ] §1 written last
- [ ] Every rate and cost figure either cites a source or appears in §12
- [ ] §13 contradicting evidence non-empty
- [ ] §14 confidence stated — low is an acceptable and often correct answer
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.acquisition_channels` written
- [ ] `outputs.onboarding_strategy` written
- [ ] `outputs.retention_model` written
- [ ] `outputs.growth_loops` written, with closure verdicts
- [ ] `outputs.expansion_paths` written, or explicitly none
- [ ] `state.decisions` appended with the model choice and its rejected alternative
- [ ] `state.assumptions` appended with every unsourced rate, cost and conversion figure
- [ ] `state.open_questions` appended with unevidenced channels and `NEEDS USER` items

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — the model fits the price and the segment
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — channels evidenced
- [ ] Criterion 2 — at least one loop, with a closure verdict
- [ ] Criterion 3 — retention mechanism located in the product
- [ ] Criterion 4 — time to first value in minutes
- [ ] Payback check
- [ ] Growth laundering check
- [ ] Sequence check — spend gated on validation
- [ ] Referral coherence check
- [ ] Universal gates U1–U7
- [ ] `compounding` recorded as loop, funnel or none
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `11-growth` appended to `state.run.completed_modules`
- [ ] Activation event, retention model and loops available to `12-metrics`
- [ ] Sequencing table available to the roadmap output
- [ ] Noted whether the growth plan deliverable is in scope — it is optional

---

# Red Flags

Re-run the module if any of these are true:

- [ ] A channel has no evidence the segment is there
- [ ] A competitor's channel spend is used as proof it works
- [ ] The payback check passes because a conversion rate was raised
- [ ] The motion cannot be funded at this price and nothing was recorded
- [ ] Activation is defined as a signup
- [ ] The activation event would count a user who never returned
- [ ] The switching cost sits after activation
- [ ] Retention rests on product quality
- [ ] A retention mechanism has no requirement behind it
- [ ] Retention depends on deferred scope and nothing says so
- [ ] CAC or churn is stated more confidently than in `06-business`
- [ ] A funnel is drawn with an arrow back to the top
- [ ] A loop's evidence is a plausible story
- [ ] The first ten are a market description
- [ ] A referral program assumes a norm the research contradicts
- [ ] Spend is planned before Milestone Zero on an assumed problem
- [ ] §14 claims high confidence for a pre-launch growth plan

---

> **Checklist Principle**
>
> One line in this module decides more than the rest of it:
> whether the compounding verdict is loop or funnel.
>
> Get it wrong in the flattering direction and every financial
> model built afterwards is wrong too.
