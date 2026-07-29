---
Artifact: operations-plan
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [13-operations]
Required: false
---

<!-- fill: How the product is RUN after it ships. Most blueprints stop at launch, which
     is why so many products become unmaintainable in month three. Ongoing compliance
     obligations need an owner and a cadence, not a mention.
     Remove every <!-- fill --> comment before delivery. -->

# Operations Plan — «Product Name»

## 1. Support Model

| | |
| --- | --- |
| Channels | «email / in-app / phone» |
| Hours | «coverage» |
| First response target | «duration» |
| Resolution target | «duration by severity» |
| Who staffs it | «role» |
| Escalation path | «to whom, when» |

**Expected volume:** «tickets per «n» users» [tag]

**Most likely support burden:** «what users will most often need help with, from the
UX flow analysis» — «and what product change would remove it»

---

## 2. Severity Levels

| Level | Definition | Response | Resolution | Who is woken |
| --- | --- | --- | --- | --- |
| S1 | «e.g. data loss or total outage» | «minutes» | «hours» | «role» |
| S2 | «major function unavailable» | «hours» | «day» | «role» |
| S3 | «degraded» | «day» | «week» | — |
| S4 | «cosmetic» | «week» | «backlog» | — |

---

## 3. Incident Process

```
Detect → Triage → Communicate → Mitigate → Resolve → Review
```

| Stage | Owner | Action | Timebox |
| --- | --- | --- | --- |
| Detect | «alerting» | «what fires» | — |
| Triage | «role» | «assign severity» | «duration» |
| Communicate | «role» | «who is told, how» | «duration» |
| Mitigate | «role» | «stop the bleeding» | «duration» |
| Resolve | «role» | «fix» | «duration» |
| Review | «role» | «blameless post-mortem» | «within n days» |

**Status communication:** «how users are informed during an incident»

---

## 4. Runbooks

<!-- fill: One per foreseeable operational event. A runbook that says "investigate the
     issue" is not a runbook — it should be followable by someone who did not build
     the system, at 3am. -->

| Runbook | Trigger | Steps | Owner |
| --- | --- | --- | --- |
| «name» | «when to run it» | «summary — full steps below» | «role» |

### «Runbook name»

**Trigger:** «the specific alert or symptom»

1. «step»
2. «step»
3. «step»

**Verify recovery by:** «observable condition»
**If this does not work:** «escalation»

---

## 5. Monitoring and Alerting

| Alert | Condition | Severity | Routes to | Runbook |
| --- | --- | --- | --- | --- |
| «name» | «threshold» | S«n» | «who» | «which» |

**Alert hygiene rule:** «e.g. every alert must be actionable — an alert nobody acts on
gets deleted, not ignored»

---

## 6. Backup and Recovery

| | |
| --- | --- |
| Backup frequency | «cadence» |
| Retention | «period, per regulation» |
| Storage location | «where, and in which jurisdiction» |
| RPO | «maximum acceptable data loss» |
| RTO | «maximum acceptable downtime» |
| Restore tested | «cadence — an untested backup is not a backup» |

---

## 7. Compliance Operations

<!-- fill: Ongoing obligations from the regulatory landscape. Each needs an owner and a
     cadence. "We are HIPAA compliant" is a claim; a schedule of recurring obligations
     with named owners is an operation. -->

| Obligation | Regime | Cadence | Owner | Evidence produced |
| --- | --- | --- | --- | --- |
| «e.g. access log review» | «regime» | «monthly» | «role» | «audit record» |
| «e.g. staff training» | «regime» | «annual» | «role» | «certificates» |
| «e.g. breach notification readiness» | «regime» | «reviewed quarterly» | «role» | «procedure doc» |

**Audit readiness:** «what would be required, and how long it would take to produce»

---

## 8. Data Lifecycle

| Stage | Policy | Automated? |
| --- | --- | --- |
| Retention | «period per data class» | «yes/no» |
| Archival | «when and where» | «yes/no» |
| Deletion | «trigger and method» | «yes/no» |
| Subject access request | «process and SLA» | «yes/no» |

---

## 9. Release Process

| | |
| --- | --- |
| Cadence | «how often» |
| Environments | «progression» |
| Gate before production | «tests, review, approval» |
| Rollback method | «how, and how long it takes» |
| Feature flags | «used? for what» |
| Migration policy | «forward-only? reversible?» |

---

## 10. Running Cost

| Item | Monthly at launch | At target scale | Driver |
| --- | --- | --- | --- |
| Infrastructure | «figure» [tag] | «figure» [tag] | «what grows it» |
| Third-party services | «figure» [tag] | «figure» [tag] | |
| Support staffing | «figure» [tag] | «figure» [tag] | |
| Compliance | «figure» [tag] | «figure» [tag] | |
| **Total** | «figure» | «figure» | |

**Cost per «user/account» at launch:** «figure» — compare against the price point in
`01-Research-Dossier.md` §3.3. «Is the unit economics viable? State it plainly.»

---

## 11. Operational Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| «e.g. single-person dependency» | «h/m/l» | «h/m/l» | «approach» |

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Support channel and response expectation defined
- [ ] Severity levels defined with response and resolution targets
- [ ] Incident and escalation path documented
- [ ] Runbooks followable by someone who did not build the system
- [ ] Backup policy states RPO, RTO and restore-test cadence
- [ ] Every ongoing compliance obligation has an owner and a cadence
- [ ] Running cost estimated and compared against the price point
- [ ] Every fill comment removed
-->
