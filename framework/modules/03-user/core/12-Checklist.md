---
Title: Checklist
Module: 03-user
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the User module.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 03-user/core/07-Workflow.md
  - 03-user/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 04-problem
Tags:
  - User
  - Checklist
  - Verification
---

# Checklist

---

# Entry

- [ ] `01-idea` and `02-market` in `state.run.completed_modules`
- [ ] `idea_brief` read — especially the context block
- [ ] `market_definition` read — it bounds which segments are in scope
- [ ] Buyer-vs-user distinction from the brief carried forward
- [ ] `engine/evidence-policy.md` read
- [ ] `06-Framework.md` read
- [ ] `09-Research-Methodology.md` read
- [ ] **Research mode declared** — Primary, Proxy, or Inferred
- [ ] Mode written into the analysis header

---

# Move 1 — Divide

- [ ] At least two segments identified
- [ ] Each differs **behaviorally**, not just demographically
- [ ] The behavioral difference is stated explicitly
- [ ] Size estimated per segment
- [ ] Pain intensity assessed per segment
- [ ] Ability to pay assessed per segment
- [ ] Reachability assessed per segment
- [ ] Every column carries a tag
- [ ] All segments sit inside `market_definition`

---

# Move 2 — Choose

- [ ] One segment prioritized
- [ ] Choice defended against the criteria table
- [ ] If a larger segment was passed over, the reason is stated
- [ ] What is given up by the choice is named
- [ ] Trigger for revisiting the choice recorded

---

# Move 3 — Embody

- [ ] Primary persona built
- [ ] Every row carries a tag or an explicit inference marker
- [ ] Persona could not describe anyone else in the market
- [ ] **No invented quote, name, or statistic**
- [ ] Real quote attributed, or absence stated plainly
- [ ] Secondary persona built if the buyer differs from the user
- [ ] Decision trigger and decision blocker identified
- [ ] **Gaps section written** — what is not known

---

# Move 4 — Observe

- [ ] Workflow broken into steps
- [ ] Each step names the tool used
- [ ] Products being replaced are **named**, including paper or spreadsheets
- [ ] Time per step and total time estimated
- [ ] Friction points identified and ranked
- [ ] The step they would most want removed identified
- [ ] Tools the product must coexist with identified
- [ ] Per-step confidence stated where evidence varies

Switching cost, all five dimensions:

- [ ] Data migration
- [ ] Retraining
- [ ] Workflow disruption
- [ ] Contractual lock-in
- [ ] Perceived risk
- [ ] The bar the product must clear is stated
- [ ] Internal resistance identified, if applicable

---

# Move 5 — Job

- [ ] Jobs written as `When… I want… So I can…`
- [ ] **No job names a product, tool, or feature**
- [ ] Each job tested: would it survive the product being built differently?
- [ ] Frequency recorded per job
- [ ] Current satisfier recorded per job, with how well it works
- [ ] Primary job identified
- [ ] Jobs the product will not serve stated explicitly

---

# Immovables

- [ ] What this person would not change is documented
- [ ] Implication for the product stated for each

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/03-user.md`
- [ ] Research mode stated in the header
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed
- [ ] Every claim carries exactly one tag
- [ ] Every `[verified]` resolves to a row in Sources
- [ ] Contradicting Evidence section non-empty
- [ ] Confidence consistent with research mode

---

# State

- [ ] `outputs.segments` written, with priority and reasoning
- [ ] `outputs.personas` written
- [ ] `outputs.jobs_to_be_done` written
- [ ] `outputs.current_workflow` written
- [ ] `outputs.switching_cost` written
- [ ] `state.evidence_log` appended
- [ ] `state.assumptions` appended — every inferred persona attribute
- [ ] `state.open_questions` appended — **including every NEEDS USER question**
- [ ] User vocabulary recorded for downstream search

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — segment checked against `market_definition`
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — two segments, prioritization defended
- [ ] Criterion 2 — jobs not features
- [ ] Criterion 3 — workflow with named tools
- [ ] Criterion 4 — switching cost named
- [ ] Criterion 5 — every user finding marked observed, reported or reconstructed, with its basis
- [ ] Criterion 6 — switching cost broken into its five components, not carried as one figure
- [ ] Evidence honesty checks
- [ ] Universal gates U1–U7
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `03-user` appended to `state.run.completed_modules`
- [ ] Handoff satisfied for `04-problem`, `05-competition`, `06-business`, `08-product`, `10-execution`, `11-growth`
- [ ] `current_workflow` detailed enough for `04-problem` to rank problems against

---

# Red Flags

Re-run the module if any of these are true:

- [ ] The two personas are recognizably the same person
- [ ] The persona reads like a character sketch
- [ ] A user quote appears with no source
- [ ] Any job statement names a solution
- [ ] The workflow refers to "their existing system" instead of naming it
- [ ] Switching cost is asserted as low with no reasoning
- [ ] Confidence is `high` but no real user was consulted
- [ ] There is no "what we do not know" section
- [ ] The prioritized segment sits outside the market boundary

---

> **Checklist Principle**
>
> Every item about fabrication exists because a fabricated user is invisible
> after this module, and expensive forever after.
