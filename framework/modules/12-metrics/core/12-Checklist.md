---
Title: Checklist
Module: 12-metrics
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Metrics module.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 12-metrics/core/07-Workflow.md
  - 12-metrics/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Checklist
---

# Checklist

---

# Entry

- [ ] `08-product` and `11-growth` in `state.run.completed_modules`
- [ ] **Goals read from `08-product` §6** — each must become a metric
- [ ] Requirements read from `08-product` §7
- [ ] **Activation event read from `11-growth`**
- [ ] Retention mechanisms read from `11-growth` §6
- [ ] Growth loops and their closure verdicts read
- [ ] **Data classification read from `09-technology` §3** — PII and regulated columns
- [ ] Regulatory landscape read from `02-market`
- [ ] Decision points read from `10-execution` §9
- [ ] Time to first value read from `10-execution` §5
- [ ] Value unit and price read from `06-business`
- [ ] Cost model read from `09-technology` §12
- [ ] Baseline availability established
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read
- [ ] `11-Success-Metrics.md` and `12-Build-Handoff.md` §9 templates read

---

# Move 1 — Choose

- [ ] Unit of value identified from `06-business` and `04-problem`
- [ ] **Exactly one north star proposed**
- [ ] It represents user value, not company convenience
- [ ] At least two alternatives named, each with why it would mislead
- [ ] **Vanity check run** — the number could fall if the product got worse
- [ ] **Gaming question answered in writing**
- [ ] The answer retained for Move 4
- [ ] Alignment confirmed — it measures the unit the price is attached to
- [ ] Review cadence and owner stated

---

# Move 2 — Define

For the north star and every goal metric:

- [ ] Numerator stated
- [ ] Denominator stated, or "none — this is a count"
- [ ] Time window stated, rolling or calendar
- [ ] Population stated
- [ ] Exclusions stated
- [ ] Source events named
- [ ] **Computation test run** — no ambiguity remains

And:

- [ ] Every goal in `08-product` §6 mapped to a metric
- [ ] Unmeasurable goals listed with reasons, not dropped

---

# Move 3 — Split

- [ ] Metrics sorted into leading and lagging
- [ ] Each leading indicator names the lagging metric it predicts
- [ ] **Each states the basis for the link**, tagged as an inference
- [ ] Warning threshold per leading indicator
- [ ] Lead time stated, or explicitly unknown
- [ ] Each lagging indicator names what it confirms and who sees it

---

# Activation and Retention

- [ ] Activation event carried unchanged from `11-growth`
- [ ] Activation computation stated — numerator, denominator, window
- [ ] Target rate stated and tagged
- [ ] Target time consistent with `10-execution` §5
- [ ] Cohort definition stated
- [ ] Measurement point stated
- [ ] **"Returning" defined as an action, not a login**
- [ ] The retention mechanism being measured, named
- [ ] Early warning behavior carried from `11-growth`

---

# Move 4 — Guard

- [ ] Every gaming answer has a counter-metric
- [ ] Every counter-metric has a threshold
- [ ] Every counter-metric states what it protects against
- [ ] Operational floor included — errors, time per task
- [ ] **Non-negotiables carried from `09-technology` §10** where observable
- [ ] Who is alerted on a breach, stated

---

# Move 5 — Target

- [ ] Baseline availability stated plainly
- [ ] Basis stated per target
- [ ] Operator-supplied targets attributed to the operator
- [ ] **OPERATOR asked** what would count as success, and what would make them stop
- [ ] Every target is one a real result could miss
- [ ] Guessed targets listed, and in `state.assumptions`
- [ ] No industry benchmark imported as a target
- [ ] Milestone that produces the first real baseline, named

---

# Move 6 — Instrument

Per event:

- [ ] Precise trigger stated
- [ ] Every property named, with its type
- [ ] The metric it feeds, named
- [ ] **The milestone it ships in, named**

Coverage:

- [ ] **Metrics with no event — listed, or "none"**
- [ ] **Events with no metric — listed, or "none"**

Identity:

- [ ] How a user is identified
- [ ] Across sessions
- [ ] Across devices, or explicitly unresolved
- [ ] Before signup, and how it joins on signup

Privacy:

- [ ] What must never be captured, listed with its regime
- [ ] **Enforcement mechanism stated** — not an intention
- [ ] Regulated and PII columns from `09-technology` §3 listed
- [ ] **Every event property checked against that list**
- [ ] "None — verified" recorded, or the overlap removed
- [ ] Event data retention period stated

---

# Infrastructure

- [ ] Tool named
- [ ] Pipeline stated
- [ ] Dashboard location stated
- [ ] **Cost of measurement stated, and checked against `09-technology` §12**
- [ ] Reviewer and cadence named
- [ ] Reporting table written
- [ ] Metric for each decision point in `10-execution` §9
- [ ] Metric review triggers written

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/12-metrics.md`
- [ ] §1 written last
- [ ] **Confidence stated separately for definitions and targets**
- [ ] Open questions recorded
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.north_star_metric` written
- [ ] `outputs.success_metrics` written
- [ ] `outputs.leading_indicators` written
- [ ] `outputs.targets` written
- [ ] `outputs.instrumentation_plan` written
- [ ] `state.decisions` appended with the north star choice and rejected alternatives
- [ ] `state.assumptions` appended with every target lacking a baseline
- [ ] `state.open_questions` appended with unmeasurable goals and definition questions

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — north star matches the priced unit of value; activation matches `11-growth` and `10-execution`
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — one north star, with reasoning and both checks
- [ ] Criterion 2 — definitions, sources and targets
- [ ] Criterion 3 — leading and lagging distinguished, with bases
- [ ] Criterion 4 — event-level instrumentation
- [ ] Privacy check — no regulated property
- [ ] Confidence separation check
- [ ] Counter-metric check
- [ ] Decision point check
- [ ] Measurement cost check
- [ ] Universal gates U1–U6
- [ ] Event count and milestone assignment recorded
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `12-metrics` appended to `state.run.completed_modules`
- [ ] Every event handed to `10-execution` for its milestone's definition of done
- [ ] Counter-metrics, thresholds and cadence handed to `13-operations`
- [ ] **`12-Build-Handoff.md` confirmed to have its instrumentation section**
- [ ] Any privacy-check failure surfaced to the operator

---

# Red Flags

Re-run the module if any of these are true:

- [ ] There are two north stars
- [ ] The north star is revenue, or a cumulative count
- [ ] The vanity check was not run
- [ ] The gaming question was not answered
- [ ] The north star measures a different unit than the price
- [ ] Any metric is missing one of the five computation parts
- [ ] Any metric has no source events
- [ ] A goal from `08-product` §6 has no metric
- [ ] Any target cannot be missed
- [ ] An industry benchmark is presented as this product's target
- [ ] A leading indicator's link has no basis
- [ ] "Returning" is defined as a login
- [ ] A gaming answer has no counter-metric
- [ ] A counter-metric has no threshold
- [ ] A metric has no event behind it
- [ ] An event feeds no metric
- [ ] Identity resolution is unspecified
- [ ] A regulated or PII column appears as an event property
- [ ] Privacy exclusions have no enforcement mechanism
- [ ] Any event has no milestone
- [ ] One confidence figure covers definitions and targets

---

> **Checklist Principle**
>
> Two items here have consequences nothing later can undo:
> the events that never get built, and the regulated field that does.
>
> Both are checked mechanically, because neither is visible
> in a document that reads well.
