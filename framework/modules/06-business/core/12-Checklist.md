---
Title: Checklist
Module: 06-business
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Business module.
Audience:
  - AI Agents
  - Founders
Prerequisites:
  - 06-business/core/07-Workflow.md
  - 06-business/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 07-strategy
Tags:
  - Business
  - Checklist
---

# Checklist

---

# Entry

- [ ] `02-market` and `05-competition` in `state.run.completed_modules`
- [ ] `pricing_comparison` read — anchors available, or their absence noted
- [ ] `tam_sam_som` read — SOM bounds the break-even count
- [ ] `segments` and buyer/blocker mapping read
- [ ] `switching_cost` from `03-user` read
- [ ] Cost per occurrence figures from `04-problem` read
- [ ] Regulatory cost estimate from `02-market` read
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Entry 1 — Payer

- [ ] Payer named
- [ ] Relationship to user stated explicitly, including "the same person"
- [ ] Budget source identified
- [ ] Approval path mapped — who else must sign
- [ ] Blocker from `03-user` carried forward
- [ ] **Willingness** assessed
- [ ] **Ability** assessed
- [ ] **Authority** assessed
- [ ] Purchase trigger identified

---

# Entry 2 — Value

- [ ] Cost per occurrence taken from `04-problem`
- [ ] Annual frequency applied
- [ ] Annual value at stake computed
- [ ] Share captured by the product estimated, with reasoning
- [ ] Visible vs absorbed cost flagged
- [ ] Whether the payer bears the cost stated
- [ ] Switching cost subtracted from net value
- [ ] **Value established before any price was written**

---

# Entry 3 — Price

- [ ] Competitor anchors listed from `05-competition`
- [ ] Market range stated
- [ ] Price chosen with model, unit and period
- [ ] Justified against value — as a stated share
- [ ] Justified against competitors — above, below or at market, with reason
- [ ] **Justified against free** — mandatory where the status quo costs nothing
- [ ] Price checked against the segment's plausible software budget
- [ ] Packaging and tiers defined
- [ ] Deliberate omissions stated — e.g. no free tier, and why

---

# Entry 4 — Economics

- [ ] Cost to serve **derived**, not assumed
  - [ ] Infrastructure per customer
  - [ ] Support per customer
  - [ ] Third-party and AI operations per customer
  - [ ] Compliance allocated
- [ ] Gross margin computed from cost to serve
- [ ] CAC stated with its basis
- [ ] Churn stated with its basis
- [ ] Lifetime and LTV derived
- [ ] LTV:CAC computed
- [ ] Payback period computed
- [ ] **Every input tagged**
- [ ] **Load-bearing assumption named**
- [ ] **Sensitivity table completed**
- [ ] Any backwards-solved figure declared as such

---

# Entry 5 — Route

- [ ] Ten customers named or specifically profiled
- [ ] Route to each stated
- [ ] Reason each would say yes stated
- [ ] Existing access recorded — or its absence
- [ ] Channels matched to where `03-user` said the segment is
- [ ] Sales motion stated
- [ ] Sales cycle length estimated
- [ ] Cycle length compared against runway, if runway is known

---

# Entry 6 — Test

- [ ] LTV:CAC threshold tested
- [ ] Payback threshold tested
- [ ] Gross margin threshold tested
- [ ] Price-to-value ratio tested
- [ ] Break-even customer count compared against SOM
- [ ] Thresholds used are stated, with why
- [ ] **Which threshold fails first** identified
- [ ] "What would have to be true" stated plainly

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/06-business.md`
- [ ] **Verdict stated first**
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Every number carries a tag
- [ ] Sourced / inferred / assumed counts recorded
- [ ] Contradicting evidence section non-empty
- [ ] Confidence consistent with the sourced-to-assumed ratio

---

# State

- [ ] `outputs.business_model` written
- [ ] `outputs.pricing_strategy` written
- [ ] `outputs.unit_economics` written, with sensitivity
- [ ] `outputs.go_to_market` written
- [ ] `outputs.revenue_model` written
- [ ] **Cost-to-serve constraint recorded for `09-technology`**
- [ ] `state.assumptions` appended — every assumed input, with a validation method
- [ ] `state.open_questions` appended — inputs most worth establishing, ranked
- [ ] `state.evidence_log` appended

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — price checked against segment budget
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — payer identified and distinguished
- [ ] Criterion 2 — price justified three ways
- [ ] Criterion 3 — economics with assumptions surfaced
- [ ] Criterion 4 — path to first 10 customers
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `06-business` appended to `state.run.completed_modules`
- [ ] Cost-to-serve constraint visible to module 09
- [ ] Handoff satisfied for `07-strategy`, `08-product`, `11-growth`, `12-metrics`

---

# Red Flags

Re-run the module if any of these are true:

- [ ] A price appears before a value calculation
- [ ] Gross margin is asserted rather than derived
- [ ] Any economics input is untagged
- [ ] A single LTV:CAC figure appears with no sensitivity, on mostly-assumed inputs
- [ ] There is no answer to "why pay when the status quo is free"
- [ ] The price exceeds the segment's plausible annual software budget
- [ ] The go-to-market section lists channels instead of customers
- [ ] A benchmark is cited that was never retrieved
- [ ] Confidence is `medium` or `high` while most inputs are assumed
- [ ] The verdict is more favorable than the sensitivity table supports

---

> **Checklist Principle**
>
> Every item about tagging exists because this module's output is arithmetic,
> and arithmetic is the most convincing way to be wrong.
