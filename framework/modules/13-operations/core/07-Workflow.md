---
Title: Workflow
Module: 13-operations
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Operations module.
Audience:
  - AI Agents
Prerequisites:
  - 13-operations/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/13-operations.md
  - state.outputs.runbooks
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Watch. This document is the procedure.

This module closes the `operationalise` stage. It is also where the framework's third and final
arithmetic check against the business model happens, because it is the first point at which the
complete cost to serve is known.

---

# Position in the Run

```
10-execution → [ 13-operations ] → deliver stage
```

| | |
| --- | --- |
| Stage | `operationalise` |
| Depends on | `10-execution` |
| Consumes | `delivery_plan`, `security_model`, `regulatory_landscape` |
| Produces | `support_model`, `runbooks`, `incident_process`, `compliance_operations`, `cost_model` |
| On fail | return to `10-execution` |
| Human checkpoint | none — but two operator inputs are required |

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `10-execution` is in `state.run.completed_modules`.
2. Read `09-technology` §10 — the **security controls**, the **non-negotiables**, and the
   **obligation trace**: every regulatory obligation and the mechanism that meets it.
3. Read `09-technology` §3 — retention periods and data classification per entity.
4. Read `09-technology` §11 — the data-loss position, RPO and RTO.
5. Read `09-technology` §12 — the infrastructure cost at launch.
6. Read `02-market` — the regulatory landscape, including any **notification deadlines**.
7. Read `10-execution` §4 and §10 — the flow analysis, and the verification strategy.
8. Read `12-metrics` §7 and §9 — counter-metrics with thresholds, and measurement cost.
9. Read `06-business` — the **cost-to-serve ceiling** and the launch user count.
10. Read `08-product` §8 — the edge cases, which become runbook triggers.

Then ask the operator two questions. Neither can be inferred:

| Question | Without it |
| --- | --- |
| Who will run this after launch? | Every owner in the document is fictional |
| What hours can actually be covered? | The response targets are promises made on their behalf |

Record before planning:

| Inherited | Consequence |
| --- | --- |
| Obligation trace | Each obligation becomes a scheduled operation with an owner |
| Non-negotiables | Each needs a way to become visible when breached |
| Data-loss position | Defines S1 |
| Counter-metric thresholds | Become alerts |
| Infrastructure cost | One line of a larger total |
| Cost ceiling | The true cost to serve must fit under it |
| Operator answers, or their absence | Determines whether coverage claims are real |

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `13-operations/core/03-Core-Principles.md`
3. `13-operations/core/06-Framework.md` — the Six Moves
4. `13-operations/core/08-Questions-To-Answer.md`
5. `13-operations/knowledge/` — Support-Model, SLAs, Incident-Process, Runbooks, Monitoring,
   Backups, Compliance-Operations, Cost-Model
6. `framework/deliverables/templates/14-Operations-Plan.md`

---

# Step 3 — Support

Move 1.

1. State channels, hours and response targets — attributed to the operator, or flagged as
   unapproved.
2. Estimate volume, **tagged as an assumption with its basis**. Where there is no basis, say so.
3. Name who staffs it and the escalation path.
4. Work the **support burden** table from `10-execution`'s flow analysis: what users will need
   help with, why, and **the product change that would remove it**.
5. Send those product changes to the roadmap.
6. Name the burden that is permanent, and why that is correct.

A burden accepted without asking for the product change becomes a permanent staffing line paid
for a fixable defect.

---

# Step 4 — Grade

Move 2.

1. Define severity levels **by user impact**, never by component.
2. Make data loss S1, using `09-technology`'s data-loss position.
3. Per level: first response, resolution target, and **who is woken**.

Check each definition by asking whether the person who noticed the problem could assign a
severity in ten seconds without knowing the architecture. If not, it is component-based.

---

# Step 5 — Respond

Move 3.

1. Fill the six stages, each with a **named owner** and a timebox.
2. Write **status communication to users**: channel, author, and the point at which it happens.
3. Keep **Mitigate separate from Resolve**.
4. State who can declare an incident. If only one person can, record it in operational risks.
5. Write the **regulatory notification obligations**: the regime, the deadline, and who starts
   the clock.

---

# Step 6 — Write the Runbooks

Move 4. One per foreseeable operational event, drawn from `09-technology`'s failure modes and
`08-product`'s edge cases.

Per runbook:

- The precise trigger
- What access is needed and where to get it
- Numbered steps as a table: **do this / expected result / if different**
- A recovery verification — an observable condition
- An escalation
- **"Do not do"** — the tempting action that makes it worse

Then run the **3am test** on each:

```
Read the runbook as someone who did not build the system.
For each step, ask: do I know exactly what to type or click?
  ├─ no  → the step is a description. Rewrite it
  └─ yes → does it tell me what I should see?
             ├─ no  → add the expected result
             └─ yes → continue
```

Any step containing "investigate", "look into", "check that things are working" fails.

---

# Step 7 — Alert

Still Move 4's territory, and the bridge to Move 5.

1. Convert `12-metrics`'s counter-metric thresholds into alerts.
2. Add operational alerts from `09-technology`'s failure modes.
3. Per alert: condition, severity, **named person**, and **which runbook**.
4. State what is deliberately not alerted on, and why.
5. Apply the hygiene rule: an alert with no action is deleted, not tolerated.

An alert missing a runbook or a person is worse than no alert, because it trains everyone to
ignore the ones that matter.

---

# Step 8 — Comply

Move 5.

1. Carry the **non-negotiables** from `09-technology` §10, and state for each **how a breach
   becomes visible**. A rule with no visibility is a preference.
2. Build the recurring obligation schedule from the obligation trace. Per row: regime, cadence,
   **named owner**, **evidence produced**, and where it is kept.
3. Add the operational obligations that are not regulatory but behave the same way — restore
   tests, access reviews, dependency updates.
4. List any obligation with **no owner**. An unowned obligation is an unmet one.
5. Write **audit readiness**: what an auditor would ask for, and how long producing it would
   take.
6. Fill the data lifecycle table, and mark each stage automated or not.

> An unautomated retention policy is a policy nobody executes.

7. Fill backup and recovery, including **whether restore has ever been tested**. "Never" is an
   acceptable answer and must be written plainly.

---

# Step 9 — Release

1. Cadence, environments, the gate before production, and who can deploy.
2. The rollback method, how long it takes, and **whether it has been tested**.
3. Migration policy — forward-only or reversible.
4. Feature flags: what they are for, and who removes them.

An untested rollback is the same class of assumption as an untested restore.

---

# Step 10 — Cost, and Check It

Move 6. The framework's last arithmetic check against the business model.

1. Carry infrastructure cost from `09-technology` §12.
2. Carry measurement cost from `12-metrics` §9.
3. Add third-party services.
4. Add **support staffing** — derived from the volume estimate and the response targets.
5. Add **compliance operations** — the time the §8 schedule actually consumes.
6. Total, then divide by launch users.

| Result | Action |
| --- | --- |
| True cost per user under the ceiling | Continue |
| Over the ceiling | Record a **regress** — `06-business` for the price, `07-strategy` for the scope |

Do not resolve it by reducing the support estimate. The estimate was just derived from the
response targets the operator approved; lowering it silently withdraws the commitment.

---

# Step 11 — The Rota Question

1. State the rota size, the coverage claimed, and whether it is sustainable.
2. Answer what happens when the on-call person is unavailable.
3. Register single-person dependencies as operational risks with early warnings.

For a solo operator, an honest limit is worth more than an unstaffable coverage table.

---

# Step 12 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/13-operations.md`. Write §1 last.

```yaml
outputs:
  support_model:           # §3 — channels, targets, burden analysis
  incident_process:        # §4, §5 — severity and the six stages
  runbooks:                # §6, §7 — steps, verification, escalation, alerts
  compliance_operations:   # §8, §9 — schedule, owners, evidence, data lifecycle
  cost_model:              # §11 — the true cost to serve
```

Append every volume and staffing estimate to `state.assumptions` with a validation method — U5.
Append operator-approved targets as `[verified: operator]`. Append unowned obligations and
unresolved coverage questions to `state.open_questions`. Append operational risks to the risk
register.

---

# Step 13 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which response target did I set without the operator's agreement?
- Which support burden did I accept instead of asking what would remove it?
- Which severity level requires knowing the architecture to assign?
- Which runbook step would leave a stranger stuck at 3am?
- Which runbook have I never actually walked through?
- Which alert has no runbook, or no person?
- Which obligation has an owner who has not been told?
- Has restore been tested, or is it merely configured?
- Which cost line did I omit because it was awkward — support time, or compliance time?
- Is this rota one person with a coverage table drawn around them?

The coherence pass: does the true cost to serve fit the price from `06-business`, and do the
coverage claims fit whatever the operator actually said? A support model promising four-hour
responses with one part-time person is a contradiction, not an aspiration.

---

# Step 14 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U7.

| Verdict | Action |
| --- | --- |
| Pass | Hand to the `deliver` stage |
| Fail | Revise, or `return to 10-execution`. Three attempts, then halt |

---

# Step 15 — Hand Off

1. Append `13-operations` to `state.run.completed_modules`.
2. Hand non-negotiables and any alert-required instrumentation to the build handoff.
3. Hand support-burden product changes to the roadmap.
4. Hand operational risks to `10-Risks-and-Assumptions.md`.
5. Note whether the operations plan deliverable is in scope — it is optional in the manifest.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `12-Build-Handoff.md` | Non-negotiables, alert instrumentation | Rules that must hold, and what must be emitted for alerts to fire |
| `09-Roadmap.md` | Support-burden product changes | Fixes that remove permanent staffing cost |
| `10-Risks-and-Assumptions.md` | Operational risks | Single-person dependencies and coverage gaps |
| `14-Operations-Plan.md` | All outputs | The shipped operations artifact, when in scope |

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Response targets nobody agreed to | Operator not asked | Attribute them, or mark them unapproved |
| Volume presented as a plan | Forecast treated as a commitment | Tag it, and state the basis |
| Support burden accepted permanently | The product question not asked | Name the change that removes it |
| Severity by component | Grading from the architecture | Regrade by user impact |
| Incident stages with no owner | Move 3 half done | Name a person per stage |
| Users never told anything | Communicate stage missing | Add channel, author, timing |
| Incidents that stay open for days | Mitigate conflated with Resolve | Separate them |
| Notification deadline unknown | Regulatory obligation not carried | State the regime, deadline and who starts the clock |
| "Investigate the issue" as a step | 3am test not run | Rewrite as an action with an expected result |
| Runbook with no verification | Steps without an endpoint | Add the observable recovery condition |
| Alerts nobody acts on | Hygiene rule ignored | Delete them, or give each a runbook and a person |
| Obligations with no owner | Schedule not built | Assign a named person, or record it as unmet |
| Compliance claimed, never exercised | Mechanism treated as sufficient | Give it a cadence and evidence |
| Backups configured, never restored | Restore test not scheduled | Schedule it, or state "never" plainly |
| Cost model missing support and compliance | The two hardest lines omitted | Add them; they are why this module costs anything |
| A rota of one with a coverage table | The rota question not asked | State the honest limit |

---

> **Workflow Principle**
>
> This module is written before anyone is tired.
>
> Every step of it will be read by someone who is, which is the
> only test that matters.
