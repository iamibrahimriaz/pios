---
Title: Checklist
Module: 09-technology
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Technology module.
Audience:
  - AI Agents
  - Engineers
Prerequisites:
  - 09-technology/core/07-Workflow.md
  - 09-technology/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 10-execution
Tags:
  - Technology
  - Checklist
---

# Checklist

---

# Entry

- [ ] `08-product` in `state.run.completed_modules` with a passing gate
- [ ] `feature_spec` read — every MUST requirement with its behavior
- [ ] `edge_cases` read — all five categories per requirement
- [ ] `acceptance_criteria` read
- [ ] `regulatory_landscape` read from `02-market`
- [ ] **Cost-to-serve ceiling** read from `06-business`
- [ ] Launch and target user figures read from `06-business`
- [ ] Operating environment read from `03-user`
- [ ] First shippable slice read from `08-product` §11
- [ ] Constraints recorded before any design work
- [ ] Any requirement unmeetable inside the constraints flagged as a regress signal
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read
- [ ] The four deliverable templates this module feeds read

---

# Move 1 — Derive

- [ ] Requirements read for nouns — candidate entities listed
- [ ] Read for verbs — candidate operations listed
- [ ] Read for states — lifecycles and enumerations listed
- [ ] **Orphan entity check run** — no entity without a requirement
- [ ] **Unmodeled requirement check run** — no requirement without data
- [ ] Each unmodeled requirement resolved by deriving further, or by a recorded regress
- [ ] Nothing invented to fill a gap
- [ ] Central entity identified

---

# Move 2 — Model

For every entity:

- [ ] Purpose sentence written
- [ ] Source requirements named
- [ ] Every column has a type
- [ ] Every column has a nullability
- [ ] Every column has a default, or explicitly none
- [ ] Constraints stated, each with the business rule it encodes
- [ ] Every index names the query it serves
- [ ] Every relationship states cardinality
- [ ] Every foreign key states on-delete behavior, with a reason
- [ ] PII columns identified
- [ ] Regulated data and regime identified
- [ ] Retention period stated **with a cited basis**
- [ ] Audit requirement stated
- [ ] Encryption-at-rest position stated

Global:

- [ ] Conventions stated — keys, naming, timestamps, soft delete, timezones
- [ ] History-preservation decisions made where past state matters
- [ ] **Schema test run** — the list of questions a builder would have is empty

---

# State Machines

For every entity with a lifecycle:

- [ ] Legal states listed
- [ ] Legal transitions listed with triggers
- [ ] **Forbidden transitions listed explicitly**
- [ ] Behavior on an attempted forbidden transition stated
- [ ] Who may cause each transition stated
- [ ] Side effects per transition stated
- [ ] What is editable in each state stated

---

# Move 3 — Expose

- [ ] Interface style chosen, with a reason
- [ ] Versioning policy stated
- [ ] Every operation has a concrete request shape
- [ ] Every operation has a concrete success response shape
- [ ] Every writable field has a validation rule traced to a requirement
- [ ] Every operation names the requirement it serves
- [ ] **Every edge case from `08-product` §8 maps to a failure response**
- [ ] Error taxonomy defined once, consistently
- [ ] Idempotency stated per write operation
- [ ] Existence-disclosure position stated — 404 or 403 — with a reason
- [ ] Pagination, filtering and sorting conventions stated
- [ ] Rate limits stated with the response when exceeded
- [ ] **Coverage table complete in both directions**
- [ ] "Uncovered requirements" line present, even if none
- [ ] "Operations serving no requirement" line present, even if none

---

# Move 4 — Protect

- [ ] Authentication mechanism stated
- [ ] Authorization model stated — role-level, record-level, or both
- [ ] **Authorization enforcement point named**
- [ ] Transit encryption stated with version and boundary
- [ ] At-rest encryption stated with scope and key custody
- [ ] Secret storage and rotation stated
- [ ] Audit log contents, retention and immutability stated
- [ ] Backup frequency and retention stated
- [ ] **Restore addressed — tested or explicitly untested**
- [ ] Deletion behavior stated, including backups
- [ ] What must not be logged stated
- [ ] **Obligation trace complete** — every obligation to a mechanism, enforcement point and citation
- [ ] Obligations with no mechanism listed as **blockers**
- [ ] No compliance claim made anywhere in the document
- [ ] Threats specific to this product, each with the verifying test

---

# Move 5 — Choose

- [ ] Architecture shape chosen, with a reason at this scale
- [ ] Components and responsibilities listed
- [ ] System boundaries stated
- [ ] **Architectural capability deliberately not added, stated**
- [ ] Every technology row states a version
- [ ] Every row names at least one rejected alternative
- [ ] Every row states what the choice is **worse** at
- [ ] Every row states the cost of changing it
- [ ] **Operability check run** — the team can run this
- [ ] **Boring-default check run**
- [ ] One-way doors identified
- [ ] Vendor risk stated for critical third parties

---

# Move 6 — Size

- [ ] Launch and target figures derived from `06-business`
- [ ] **Arithmetic shown, including the peak-to-average assumption**
- [ ] First expected bottleneck named, with the load
- [ ] Specific response named — not "scale horizontally"
- [ ] **What the system is deliberately not built for, stated**
- [ ] Availability target stated with a justification
- [ ] Data durability stated — replication, backup, RPO and RTO
- [ ] Degraded-operation behavior stated
- [ ] Failure isolation stated

---

# Cost

- [ ] Every component costed with a cited price and date
- [ ] Tier and region stated
- [ ] Commonly forgotten items included — egress, backups, log retention, staging
- [ ] Total at launch stated
- [ ] Cost per user derived
- [ ] **Compared against the ceiling from `06-business`**
- [ ] If over the ceiling, a regress is recorded — not absorbed

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/09-technology.md`
- [ ] §1 written last
- [ ] Every version claim, limit and price cited
- [ ] Every judgment labeled as a judgment
- [ ] One-way doors given the strongest justifications in the document
- [ ] §15 open questions recorded
- [ ] §16 confidence stated with its basis
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.data_model` written
- [ ] `outputs.api_contract` written
- [ ] `outputs.architecture` written
- [ ] `outputs.security_model` written
- [ ] `outputs.scalability_plan` written
- [ ] `outputs.tech_stack` written
- [ ] `state.decisions` appended with every architecture decision and its rejected alternatives
- [ ] `state.assumptions` appended with every one-way door and unevidenced judgment
- [ ] `state.open_questions` appended with every lookup and operator question, and every blocker

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — fits the cost ceiling, the environment and the first shippable slice
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — schema-generatable, both traceability directions
- [ ] Criterion 2 — capability coverage, both directions
- [ ] Criterion 3 — obligations traced to mechanisms
- [ ] Criterion 4 — stack trade-offs stated
- [ ] Cost check
- [ ] Load check
- [ ] Provenance check
- [ ] Deliberate-absence check
- [ ] Restore check
- [ ] Universal gates U1–U6
- [ ] Blockers listed and surfaced to the operator
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `09-technology` appended to `state.run.completed_modules`
- [ ] Any regress recorded with its target
- [ ] Handoff satisfied for `10-execution`, `13-operations`, `14-ai-systems`, `12-metrics`
- [ ] Deliverable inputs confirmed for the data model, API contract, architecture and build handoff

---

# Red Flags

Re-run the module if any of these are true:

- [ ] An entity exists because products like this usually have one
- [ ] A requirement's data is not modeled anywhere
- [ ] Any column lacks a type or a nullability
- [ ] Any relationship lacks an on-delete behavior
- [ ] A state machine lists only legal transitions
- [ ] A MUST requirement has no operation
- [ ] An operation serves no requirement
- [ ] An edge case from module 08 has no failure response
- [ ] Authorization is described but not located
- [ ] An obligation is met by an intention
- [ ] The document claims compliance
- [ ] A retention period has no cited basis
- [ ] A technology row has no rejected alternative
- [ ] A "trade-off" is a benefit with a hedge
- [ ] A version claim, limit or price was written from memory
- [ ] The design is sized far beyond the business model's projections
- [ ] Cost per user exceeds the ceiling and nothing was recorded
- [ ] Backups are specified and restore is not
- [ ] Nothing is stated as deliberately not built

---

> **Checklist Principle**
>
> This is the last checklist in the framework whose items become
> code rather than plans.
>
> Everything unanswered here is answered by a builder, alone.
