---
Title: Checklist
Module: 08-product
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Product module.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 08-product/core/07-Workflow.md
  - 08-product/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 09-technology
Tags:
  - Product
  - Checklist
---

# Checklist

---

# Entry

- [ ] `07-strategy` in `state.run.completed_modules`
- [ ] **Its human checkpoint was approved** — an unapproved cut is not a boundary
- [ ] `mvp_definition` read: above the line, below the line, cut principle
- [ ] What the MVP proves, and what it does not, both read
- [ ] `chosen_approach` and `non_goals` read
- [ ] `personas` and `jobs_to_be_done` read, including the numbered workflow
- [ ] `ranked_problems` read **with each problem's evidence tag**
- [ ] `state.run` checked for a declared shortfall from module 04
- [ ] The boundary recorded explicitly before any writing
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read
- [ ] `03-PRD.md` and `04-Feature-Spec.md` deliverable templates read

---

# Move 1 — Trace

- [ ] Ranked problems listed with evidence tags
- [ ] Core job written out as numbered steps
- [ ] Each step mapped to a parent problem
- [ ] Each step marked served, or left to a stated fallback
- [ ] **Orphan check run** — no capability above the line lacks a parent problem
- [ ] **Coverage check run** — no problem above the line lacks a capability
- [ ] Orphans deleted, not justified
- [ ] Spine written into §5 and §13 before requirements were written

---

# Move 2 — Specify

- [ ] A requirement exists for every served step
- [ ] Every requirement names a parent problem, job and step
- [ ] Every requirement has a priority: MUST / SHOULD / COULD
- [ ] **No MUST maps to a capability below module 07's line**
- [ ] The MUST list is meaningfully shorter than the requirement list
- [ ] Every requirement's basis marked `derived: «source»` or `design decision`
- [ ] Requirements serving an assumed problem marked accordingly
- [ ] Capabilities that surfaced while specifying handled by the rule, not by addition
- [ ] Any load-bearing surfaced capability escalated as a **regress**, and recorded

---

# Move 3 — Behave

For every MUST requirement:

- [ ] Trigger stated
- [ ] Input stated, including what is optional
- [ ] System response stated, including what the user cannot see
- [ ] Resulting state stated
- [ ] What the user sees stated
- [ ] **Two-builder test run** — no divergence point can be named
- [ ] No database, framework, library or screen layout named
- [ ] "Not included in this requirement" written

---

# Move 4 — Break

For every MUST requirement:

- [ ] Empty — first use, no data
- [ ] Invalid — wrong input, what the user is told, what is preserved
- [ ] Failure — cannot complete, whether work is lost, whether retry is safe
- [ ] Permission — refusal behavior, and what it does not reveal
- [ ] Limit / conflict — volume, size, concurrency, offline, interruption
- [ ] **Data-loss position stated explicitly**
- [ ] No category left blank — "not applicable — «reason»" where genuinely so

---

# Move 5 — Order

- [ ] One scoring method named
- [ ] Applied to every requirement, consistently
- [ ] Every score-versus-tier disagreement recorded with a reason
- [ ] Dependency graph built
- [ ] Critical path stated
- [ ] **First shippable slice named**
- [ ] Independently shippable requirements identified

---

# Move 6 — Prove

- [ ] Every requirement has acceptance criteria
- [ ] Criteria in `Given / when / then` form
- [ ] **Banned-word scan run** — no hits
- [ ] **Falsifiability check run** — every criterion has a failing observation
- [ ] Criteria exist for failure states, not only the happy path
- [ ] Criteria judgeable by someone with no context

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/08-product.md`
- [ ] §1 written last
- [ ] §5 end-to-end verdict answered — and the answer is yes
- [ ] §9 constraints traced to source modules
- [ ] §10 ledger accounts for everything considered
- [ ] Every ledger row has a reason and a revisit trigger
- [ ] Fast-follow and Deferred rows confirmed carried to the roadmap
- [ ] §12 design decisions recorded with alternatives
- [ ] §13 traceability complete in both directions
- [ ] §14 contradicting evidence non-empty
- [ ] §15 confidence does not exceed that of the underlying problems
- [ ] Every number checked: standard, derived, or registered decision
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.prd_body` written
- [ ] `outputs.feature_spec` written
- [ ] `outputs.acceptance_criteria` written
- [ ] `outputs.prioritization` written
- [ ] `outputs.edge_cases` written
- [ ] `state.decisions` appended with every design decision and its rejected alternative
- [ ] `state.assumptions` appended with every load-bearing design decision plus a validation method
- [ ] `state.open_questions` appended with every `NEEDS USER` and `OPERATOR` question

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — fits the price, cost ceiling and operating context
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — traceability, both directions
- [ ] Criterion 2 — acceptance criteria testable
- [ ] Criterion 3 — edge and failure states complete
- [ ] Criterion 4 — nothing dropped silently
- [ ] Boundary check — no scope laundering
- [ ] Two-builder check
- [ ] Confidence check
- [ ] Invented-number check
- [ ] Implementation-leak check
- [ ] Universal gates U1–U6
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `08-product` appended to `state.run.completed_modules`
- [ ] Any regress to `07-strategy` surfaced to the operator
- [ ] Handoff satisfied for `09-technology`, `14-ai-systems`, `10-execution`, `12-metrics`
- [ ] Deliverable inputs confirmed for `03-PRD.md` and `04-Feature-Spec.md`

---

# Red Flags

Re-run the module if any of these are true:

- [ ] A requirement's parent problem was chosen after the requirement was written
- [ ] A ranked problem above the line serves nothing, and no deferral is recorded
- [ ] Almost every requirement is a MUST
- [ ] A MUST corresponds to something module 07 put below the line
- [ ] A requirement's behavior could reasonably be built two ways
- [ ] A requirement has only happy-path criteria
- [ ] Any acceptance criterion cannot fail
- [ ] More than one edge category is blank
- [ ] The data-loss position is unstated
- [ ] The ledger is empty, or rows lack revisit triggers
- [ ] A regulated field, code, limit or retention period was written from memory
- [ ] A requirement names a technology
- [ ] The document reads more certainly than module 04's evidence tags allow

---

> **Checklist Principle**
>
> This is the last checklist before the framework stops asking
> *what should exist* and starts describing *how to build it*.
>
> Everything vague that survives here gets built as somebody's guess.
