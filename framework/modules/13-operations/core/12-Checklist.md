---
Title: Checklist
Module: 13-operations
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Operational checklist for entering, running and exiting the Operations module.
Audience:
  - AI Agents
  - Operators
Prerequisites:
  - 13-operations/core/07-Workflow.md
  - 13-operations/core/11-Quality-Gate.md
Outputs:
  - Verified module completion
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Checklist
---

# Checklist

---

# Entry

- [ ] `10-execution` in `state.run.completed_modules`
- [ ] Security controls and **non-negotiables** read from `09-technology` §10
- [ ] **Obligation trace** read — every obligation and its mechanism
- [ ] Data classification and retention periods read from `09-technology` §3
- [ ] **Data-loss position, RPO and RTO** read from `09-technology` §11
- [ ] Infrastructure cost read from `09-technology` §12
- [ ] Regulatory landscape read from `02-market`, including notification deadlines
- [ ] Flow analysis read from `10-execution` §4
- [ ] Verification strategy read from `10-execution` §10
- [ ] Counter-metric thresholds read from `12-metrics` §7
- [ ] Measurement cost read from `12-metrics` §9
- [ ] **Cost-to-serve ceiling** and launch user count read from `06-business`
- [ ] Edge cases read from `08-product` §8 — these become runbook triggers
- [ ] **OPERATOR asked: who will run this after launch**
- [ ] **OPERATOR asked: what hours can genuinely be covered**
- [ ] `06-Framework.md` and `09-Research-Methodology.md` read

---

# Move 1 — Support

- [ ] Channels stated
- [ ] Hours stated, and **attributed to the operator**
- [ ] First response target stated, and **attributed**
- [ ] Resolution targets stated per severity
- [ ] Staffing named — a role, not "the team"
- [ ] Escalation path stated, with when it applies
- [ ] Volume estimate stated and **tagged as an assumption**
- [ ] Basis for the volume estimate stated, or "none — unknown"

**Support burden**

- [ ] Expected burdens listed, from the flow analysis
- [ ] Why each will happen, stated
- [ ] **Product change that would remove each, named**
- [ ] Those changes sent to the roadmap
- [ ] Permanent burden named, with why it is correct

---

# Move 2 — Grade

- [ ] Severity levels defined **by user impact**
- [ ] Ten-second test run — assignable without knowing the architecture
- [ ] **Data loss is S1**
- [ ] What counts as data loss, stated from `09-technology`
- [ ] First response time per level
- [ ] Resolution target per level
- [ ] **Who is woken, per level** — a named role

---

# Move 3 — Respond

- [ ] Six stages filled: Detect, Triage, Communicate, Mitigate, Resolve, Review
- [ ] **Named owner per stage**
- [ ] Timebox per stage
- [ ] **Status communication to users** — channel, author, timing
- [ ] Mitigate kept separate from Resolve
- [ ] Blameless review, with a window
- [ ] Who can declare an incident, stated
- [ ] If only one person can, recorded in §12
- [ ] **Regulatory notification deadlines stated, with who starts the clock**

---

# Move 4 — Runbooks

Per runbook:

- [ ] Precise trigger stated
- [ ] Access needed, and where to get it
- [ ] Steps as a table: do this / expected result / if different
- [ ] **Every step is an action, not a description**
- [ ] No step says "investigate", "look into", or "check things are working"
- [ ] **Every step has an expected result**
- [ ] **Recovery verification stated** — an observable condition
- [ ] **Escalation stated** — who, and how they are reached
- [ ] **"Do not do" stated** — the tempting action that makes it worse
- [ ] **3am test run**
- [ ] Whether it has been walked, recorded

Coverage:

- [ ] One runbook per foreseeable event from `09-technology` failure modes
- [ ] One per relevant edge case from `08-product` §8

---

# Alerting

- [ ] Counter-metric thresholds from `12-metrics` converted to alerts
- [ ] Operational alerts added from `09-technology` failure modes
- [ ] **Every alert has a condition**
- [ ] **Every alert has a severity**
- [ ] **Every alert routes to a named person**
- [ ] **Every alert names a runbook**
- [ ] What is deliberately not alerted on, stated with why
- [ ] Hygiene rule stated — unactioned alerts are deleted, not tolerated

---

# Move 5 — Comply

- [ ] Non-negotiables carried from `09-technology` §10
- [ ] **For each: how a breach becomes visible**
- [ ] Recurring obligation schedule built from the obligation trace
- [ ] **Cadence per obligation**
- [ ] **Named owner per obligation**
- [ ] **Evidence produced, per obligation**
- [ ] Where that evidence is kept
- [ ] Operational obligations added — restore tests, access reviews, dependency updates
- [ ] **Obligations with no owner listed explicitly**
- [ ] Audit readiness stated — what would be asked for, and how long to produce it

**Data lifecycle**

- [ ] Retention policy per data class, from `09-technology` §3
- [ ] Archival policy
- [ ] Deletion, including backups
- [ ] Subject access request process and deadline
- [ ] **Each marked automated or not**

**Backup and recovery**

- [ ] Frequency, retention, location and jurisdiction
- [ ] RPO and RTO consistent with `09-technology` §11
- [ ] **Restore test cadence stated — or "never", plainly**

---

# Release

- [ ] Cadence stated
- [ ] Environment progression stated
- [ ] Gate before production stated
- [ ] Who can deploy — named
- [ ] **Rollback method stated, with how long it takes**
- [ ] **Whether rollback has been tested**
- [ ] Migration policy — forward-only or reversible
- [ ] Feature flag policy, including who removes them

---

# Move 6 — Cost

- [ ] Infrastructure carried from `09-technology` §12
- [ ] Measurement carried from `12-metrics` §9
- [ ] Third-party services costed, with cited prices
- [ ] **Support staffing costed** — derived from volume and response targets
- [ ] **Compliance operations costed** — the §8 schedule in hours
- [ ] Total at launch and at target scale
- [ ] **True cost per user derived**
- [ ] **Compared against the ceiling from `06-business`**
- [ ] **No cost line was lowered to make the comparison pass**
- [ ] If over the ceiling, a regress is recorded

---

# The Rota

- [ ] Rota size stated
- [ ] Coverage claimed stated
- [ ] **Sustainability answered — a rota of one is not a rota**
- [ ] What happens when the on-call person is unavailable
- [ ] Single-person dependencies registered as risks
- [ ] Early warning per operational risk

---

# Assembly

- [ ] `13-Template.md` filled into `projects/<slug>/research/13-operations.md`
- [ ] §1 written last
- [ ] **Confidence stated separately for commitments and forecasts**
- [ ] Open questions recorded
- [ ] Every `«placeholder»` replaced
- [ ] Every guidance comment removed

---

# State

- [ ] `outputs.support_model` written
- [ ] `outputs.incident_process` written
- [ ] `outputs.runbooks` written
- [ ] `outputs.compliance_operations` written
- [ ] `outputs.cost_model` written
- [ ] `state.decisions` appended with operational decisions and rejected alternatives
- [ ] `state.assumptions` appended with every volume and staffing forecast
- [ ] `state.open_questions` appended with unowned obligations and coverage gaps
- [ ] Operational risks appended to the risk register

---

# Review

- [ ] Completeness pass run
- [ ] Evidence pass run
- [ ] Adversarial pass run — and produced something
- [ ] Coherence pass run — cost fits the price; coverage fits what the operator said
- [ ] Verdict recorded

---

# Gate

- [ ] Criterion 1 — support defined and attributed
- [ ] Criterion 2 — incident path documented, runbooks pass the 3am test
- [ ] Criterion 3 — obligations owned, scheduled, producing evidence
- [ ] Criterion 4 — running cost estimated, including support and compliance
- [ ] Criterion 5 — a breach is resolved by a recorded change, OR the residual gap is stated as a figure and escalated
- [ ] What each regress actually bought is recorded, not only the final position
- [ ] No third narrowing round unless it targets a named cost driver the first two did not touch
- [ ] The viability decision is raised as a blocking, premise-bearing operator question with each option's consequence
- [ ] An unresolved gap appears in the Executive Summary's opening and the decision report, not only here
- [ ] Rota check
- [ ] Untested-assumption check
- [ ] Owner reality check
- [ ] Cost check
- [ ] Universal gates U1–U7
- [ ] `restore_tested`, `rollback_tested` and `runbooks_walked` recorded
- [ ] Verdict recorded in `state.run`

---

# Exit

- [ ] `13-operations` appended to `state.run.completed_modules`
- [ ] Non-negotiables and alert instrumentation handed to the build handoff
- [ ] Support-burden product changes handed to the roadmap
- [ ] Operational risks handed to `10-Risks-and-Assumptions.md`
- [ ] Noted whether the operations plan deliverable is in scope — it is optional
- [ ] `operationalise` stage complete

---

# Red Flags

Re-run the module if any of these are true:

- [ ] A response target has no attribution
- [ ] A volume forecast reads as a plan
- [ ] A support burden was accepted with no product question asked
- [ ] A severity level requires knowing the architecture
- [ ] Data loss is not S1
- [ ] An incident stage has no named owner
- [ ] Users are never told anything during an incident
- [ ] Mitigate and Resolve are the same stage
- [ ] A notification deadline is unstated
- [ ] Any runbook step says "investigate"
- [ ] Any step has no expected result
- [ ] Any runbook lacks a verification or an escalation
- [ ] An alert has no person, or no runbook
- [ ] An obligation has no owner, cadence or evidence artifact
- [ ] A non-negotiable has no way of becoming visible
- [ ] Retention is unautomated and unacknowledged
- [ ] Restore has never been tested and the document does not say so
- [ ] Rollback is unspecified or untested
- [ ] Support staffing or compliance is missing from the cost model
- [ ] Any cost line fell while the cost check was being run
- [ ] True cost per user exceeds the ceiling with no regress
- [ ] Coverage is claimed that one person cannot staff
- [ ] "The team" appears as an owner

---

> **Checklist Principle**
>
> Three lines here are answered "never" more often than anyone admits:
> restore tested, rollback tested, runbook walked.
>
> Writing "never" is a passing answer. Leaving it blank is how it
> gets discovered during the incident that needed it.
