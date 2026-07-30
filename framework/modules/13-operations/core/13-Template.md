---
Title: Template
Module: 13-operations
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Operations Plan — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - projects/<slug>/research/13-operations.md
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Template
  - Output
---

# Template — Operations Plan

---

# Usage

Copy everything below the line into `projects/<slug>/research/13-operations.md` and fill it.

This is a **working document**. It feeds:

| Deliverable | Fed by | Required |
| --- | --- | --- |
| `14-Operations-Plan.md` | all sections | optional — emitted when the run's scope calls for it |
| `12-Build-Handoff.md` | §8 non-negotiables, §10 instrumentation for alerts | required |

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**The standard for this document** is that someone who did not build the system could follow it
at three in the morning, alone, with nobody to ask.

**Two kinds of statement live here and must not be confused.** Response targets and cadences are
**commitments** — the operator must approve them. Ticket volumes and staffing needs are
**forecasts**, and before launch they are assumptions.

---
---

# Operations Plan — «Project Name»

| | |
| --- | --- |
| Module | 13-operations |
| Date | «ISO date» |
| Regulated regimes | «from 02-market, or none» |
| Who operates this | «named role or person — or "not supplied", which is itself a finding» |
| Cost ceiling | «cost to serve, from 06-business» |
| Status | draft / reviewed / gated |

---

## 1. How This Is Run, in One Paragraph

<!-- Write last. Who answers when something breaks, what they do, and what it costs to keep
     the product alive. -->

«One paragraph.»

---

## 2. Inherited Inputs

| | |
| --- | --- |
| Launch milestone | «from 10-execution» |
| Security controls | «from 09-technology §10» |
| Non-negotiables | «from 09-technology §10» |
| Regulatory obligations and their mechanisms | «from 09-technology §10 obligation trace» |
| Counter-metrics and thresholds | «from 12-metrics §7» |
| Infrastructure cost at launch | «figure, from 09-technology §12» |
| Cost-to-serve ceiling | «figure, from 06-business» |
| Verification strategy | «from 10-execution §10» |
| **OPERATOR** — who will run this | «name / role / not supplied» |
| **OPERATOR** — what hours can be covered | «answer / not supplied» |

---

## 3. Support Model

<!-- Move 1. Channels and response targets are commitments and need the operator's
     approval. Volume is a forecast and must be tagged. -->

| | |
| --- | --- |
| Channels | «email / in-app / phone» |
| Hours covered | «coverage» — `[verified: operator]` |
| First response target | «duration» — `[verified: operator]` |
| Resolution target | «by severity — see §4» |
| Who staffs it | «named role» |
| Escalation path | «to whom, when» |
| Expected volume | «tickets per «n» users per week» `[assumption: needs validation]` |
| Basis for the volume estimate | «what it is derived from, or "none — unknown"» |

### The Support Burden Is a Product Signal

<!-- The most common support request is usually a design defect with a queue attached.
     Each row names the product change that would remove it — and that change goes to the
     roadmap, not into a permanent staffing line. -->

| Expected burden | Why it will happen | Product change that removes it | Where it goes |
| --- | --- | --- | --- |
| «what users will need help with» | «from 10-execution's flow analysis» | «the change» | roadmap / accepted |

**Accepted permanent burden:** «what will always need a human, and why that is correct»

---

## 4. Severity Levels

<!-- Move 2. Severity is defined by USER IMPACT, not by which component failed.
     "The database is down" is not a severity. "Users cannot save work" is. -->

| Level | User impact | First response | Resolution | Who is woken |
| --- | --- | --- | --- | --- |
| S1 | «work is lost, or nobody can use it» | «minutes» | «hours» | «named role» |
| S2 | «a core job cannot be completed» | «hours» | «same day» | «named role» |
| S3 | «degraded, workaround exists» | «next business day» | «week» | nobody |
| S4 | «cosmetic or minor» | «week» | backlog | nobody |

**Data loss is always S1.** «Confirm, and state what counts as data loss for this product —
from `09-technology`'s data-loss position»

---

## 5. Incident Process

<!-- Move 3. Every stage has an owner and a timebox. -->

```
Detect → Triage → Communicate → Mitigate → Resolve → Review
```

| Stage | Owner | Action | Timebox |
| --- | --- | --- | --- |
| Detect | «alerting or report» | «what fires or arrives» | — |
| Triage | «named role» | Assign severity per §4 | «duration» |
| Communicate | «named role» | «who is told, through what channel» | «duration» |
| Mitigate | «named role» | Stop the harm — not necessarily fix it | «duration» |
| Resolve | «named role» | Fix | «duration» |
| Review | «named role» | Blameless review | within «n» days |

**Status communication to users:** «the channel, who writes it, and at what point»

**Who can declare an incident:** «anyone / a named role» — «if only one person can, that is a
single-person dependency and belongs in §12»

**Regulatory notification obligations:** «from `02-market` — the regime, the deadline, and who
starts the clock. A breach notification deadline that nobody knows is a deadline that gets
missed.»

---

## 6. Runbooks

<!-- Move 4. THE 3AM TEST: could someone who did not build this system follow it, alone,
     half awake, with nobody to ask?

     "Investigate the issue" is not a step. "Check the logs" is not a step unless it says
     which logs and what to look for. -->

| Runbook | Trigger | Owner |
| --- | --- | --- |
| «name» | «the specific alert or symptom» | «named role» |

### «Runbook name»

**Trigger:** «the precise alert or symptom that means run this»

**Before you start:** «what access you need, and where to get it»

| # | Do this | Expected result | If different |
| --- | --- | --- | --- |
| 1 | «specific action, with the command or the screen» | «what you should see» | «go to step «n» / escalate» |
| 2 | | | |

**Verify recovery by:** «the observable condition that means it worked»

**If this does not work:** «who to wake, and how»

**Do not do:** «the tempting action that makes it worse»

<!-- Repeat per runbook. One per foreseeable operational event — from 09-technology's
     failure modes and 08-product's edge cases. -->

---

## 7. Monitoring and Alerting

<!-- Every alert needs three things: a threshold, a person, and a runbook.
     An alert missing any of them trains people to ignore alerts. -->

| Alert | Condition | Severity | Routes to | Runbook |
| --- | --- | --- | --- | --- |
| «name» | «threshold» | S«n» | «named role» | «which runbook» |

**Alerts derived from `12-metrics` counter-metrics:** «which thresholds became alerts»

**Alert hygiene rule:** an alert nobody acts on is deleted, not ignored. A tolerated alert
teaches the team to tolerate all of them.

**What is deliberately not alerted on:** «and why — usually because there is no action to take»

---

## 8. Non-Negotiables and Compliance Operations

<!-- Move 5. `02-market` found the obligation. `09-technology` built the mechanism.
     This module RUNS it: an owner, a cadence, and the evidence produced.

     Compliance is a schedule, not a state. -->

**Non-negotiables carried from `09-technology` §10:**

| # | Rule | Consequence if broken | How a breach becomes visible |
| --- | --- | --- | --- |
| 1 | «rule» | «impact» | «alert, review, or audit» |

**Recurring obligations:**

| Obligation | Regime | Cadence | Owner | Evidence produced | Where kept |
| --- | --- | --- | --- | --- | --- |
| «access log review» | «regime» | monthly | «named role» | «audit record» | «location» |
| «restore test» | — | «cadence» | «named role» | «test record» | «location» |
| «staff training» | «regime» | annual | «named role» | «certificates» | «location» |
| «breach notification readiness» | «regime» | quarterly review | «named role» | «procedure doc» | «location» |

**Obligations with no owner:** «none, or list them — an unowned obligation is an unmet one»

**Audit readiness:** «what an auditor would ask for, and how long it would take to produce»

---

## 9. Data Lifecycle

<!-- An unautomated retention policy is a policy nobody executes. -->

| Stage | Policy | Automated | Owner |
| --- | --- | --- | --- |
| Retention | «period per data class, from `09-technology` §3» | yes / no | «role» |
| Archival | «when and where» | yes / no | «role» |
| Deletion | «trigger and method, including backups» | yes / no | «role» |
| Subject access request | «process and response deadline» | yes / no | «role» |

**Backup and recovery**

| | |
| --- | --- |
| Frequency | «cadence» |
| Retention | «period, per regulation» |
| Location and jurisdiction | «where» |
| RPO | «maximum acceptable data loss» |
| RTO | «maximum acceptable downtime» |
| **Restore tested** | «cadence — or "never", which must be stated plainly» |

> An untested restore is not a backup. It is a cost with an assumption attached.

---

## 10. Release Process

| | |
| --- | --- |
| Cadence | «how often» |
| Environments | «progression, from `09-technology` §14» |
| Gate before production | «tests, review, approval — from `10-execution` §10» |
| Rollback method | «how, and how long it takes» |
| Who can deploy | «named role» |
| Migration policy | «forward-only / reversible» |
| Feature flags | «used for what, and who removes them» |

**Rollback tested:** «yes / no — an untested rollback is the same problem as an untested restore»

---

## 11. Running Cost

<!-- Move 6. This is where the TRUE cost to serve finally exists. `09-technology` costed
     the infrastructure; support and compliance are the lines that get forgotten. -->

| Item | Monthly at launch | At target scale | Driver | Source |
| --- | --- | --- | --- | --- |
| Infrastructure | «figure» | «figure» | «what grows it» | `09-technology` §12 |
| Third-party services | «figure» `[tag]` | «figure» | | |
| Measurement and analytics | «figure» | «figure» | «event volume» | `12-metrics` §9 |
| Support staffing | «figure» `[tag]` | «figure» | «ticket volume» | this module §3 |
| Compliance operations | «figure» `[tag]` | «figure» | «audit, training, review time» | §8 |
| **Total** | «figure» | «figure» | | |

| | |
| --- | --- |
| Users at launch | «n», from `06-business` |
| **True cost per user at launch** | «figure» |
| Ceiling from `06-business` | «figure» |
| **Within ceiling** | «yes / no» |

**If no:** «this is the complete cost to serve, and it breaks the business model. Regress to
`06-business` for the price or `07-strategy` for the scope. Do not absorb it by assuming
support takes less time than stated.»

---

## 12. Operational Risks

| Risk | Likelihood | Impact | Mitigation | Early warning |
| --- | --- | --- | --- | --- |
| «single-person dependency» | «h/m/l» | «h/m/l» | «approach» | «observable» |

**Who is on call, and can they sustain it?**

| | |
| --- | --- |
| Rota size | «n» |
| Coverage claimed | «hours» |
| Sustainable | «yes / no — a rota of one is not a rota» |
| What happens when that person is unavailable | «answer, or "unresolved" — which is a risk, not a detail» |

<!-- For a solo operator this section is the most important in the document. Stating the
     limit honestly is more useful than a coverage table nobody can staff. -->

---

## 13. Open Questions

| # | Question | Blocks | Who answers |
| --- | --- | --- | --- |
| Q1 | «question» | «obligation, alert or target» | operator / legal / vendor |

---

## 14. Confidence

| | |
| --- | --- |
| Confidence in the commitments | «high — these are decisions» |
| Confidence in the forecasts | «volume and staffing — usually low pre-launch» |
| Weakest element | «what, and why» |
| What would raise it | «specific evidence» |

---

## 15. Handoff

| Consumer | What it takes from here |
| --- | --- |
| `12-Build-Handoff.md` | Non-negotiables, and any instrumentation an alert requires |
| `14-Operations-Plan.md` | All sections |
| `09-Roadmap.md` | Product changes that remove support burden |
| `10-Risks-and-Assumptions.md` | Operational risks from §12 |

---

<!-- ACCEPTANCE — remove before completing
- [ ] Channels, hours and response targets stated, and attributed to the operator
- [ ] Support volume tagged as an assumption with its basis
- [ ] Each expected support burden names the product change that would remove it
- [ ] Severity levels defined by user impact, not by component
- [ ] Data loss is S1
- [ ] Every incident stage has a named owner and a timebox
- [ ] Regulatory notification deadlines stated, with who starts the clock
- [ ] Every runbook passes the 3am test — no step says "investigate"
- [ ] Every runbook states a recovery verification and an escalation
- [ ] Every alert has a threshold, a named person and a runbook
- [ ] Every recurring obligation has an owner, a cadence and evidence produced
- [ ] Restore test cadence stated — or "never", plainly
- [ ] Rollback method stated, and whether it has been tested
- [ ] Running cost includes support staffing and compliance
- [ ] True cost per user compared against the ceiling
- [ ] On-call sustainability answered honestly
- [ ] Every «placeholder» replaced and every guidance comment removed
-->

---

> **Template Principle**
>
> Every other document in the framework is read while thinking.
>
> This one is read while something is broken, by somebody who was
> asleep ten minutes ago.
