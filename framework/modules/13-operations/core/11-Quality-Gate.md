---
Title: Quality Gate
Module: 13-operations
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how each gate criterion for this module is evaluated.
Audience:
  - AI Agents
Prerequisites:
  - 13-operations/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This is the last gate in the `operationalise` stage, and the last place the framework checks its
own arithmetic against the business model.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Support channel and response expectation defined

**Passes when** channels, hours and response targets are stated **and attributed** — either
`[verified: operator]` or explicitly marked as unapproved — and the volume forecast is tagged as
an assumption with its basis.

**Fails when** a response target appears with no attribution, or when a volume estimate is
presented as a plan.

| Fails | Passes |
| --- | --- |
| "Support responds within 4 hours" | "First response within 4 hours, weekdays 9–5 — `[verified: operator]`" |
| "Expect around 20 tickets a week" | "≈3 tickets per 100 users per week `[assumption: needs validation]` — basis: the confusion points in `10-execution` §4" |

**Why attribution matters.** A response target is a promise to users. Written without the
operator's agreement, it is a promise made on their behalf — and they find out when it breaks.

**Also required — the support burden analysis.** Each expected burden names why it will happen and
**the product change that would remove it**, with that change carried to the roadmap.

> The most common support request is usually a design defect with a queue attached.

A burden accepted with no product question asked becomes a permanent staffing line paid for a
fixable problem. Where a burden genuinely is permanent, that must be stated with the reason.

---

# Criterion 2 — Incident and escalation path documented

**Passes when** severity levels are defined by user impact, every incident stage has a **named
owner** and a timebox, status communication to users is specified, and regulatory notification
deadlines are stated where they apply.

**Fails when** severity is component-based, any stage is unowned, or user communication is absent.

**The ten-second test for severity.** Could the person who noticed the problem assign a level
without knowing the architecture?

| Fails | Passes |
| --- | --- |
| "S1: database unavailable" | "S1: users cannot save work, or work has been lost" |
| "S2: queue backlog exceeds «n»" | "S2: a core job cannot be completed" |

Component-based severity produces an argument during the incident, which is the worst available
time to have it.

**Data loss is always S1**, using `09-technology`'s data-loss position. That position was required
there; this criterion makes it operational.

**Two stages fail most often, and both are the ones users notice:**

| Stage | Failure |
| --- | --- |
| Communicate | Users experience the outage *and* silence, which is a worse incident |
| Mitigate | Conflated with Resolve, so incidents stay open while somebody diagnoses |

**Also required:** the **runbook standard**. Every runbook must pass the 3am test — could someone
who did not build the system follow it, alone, with nobody to ask? Any step containing
"investigate", "look into", or "check that things are working" fails. Every step needs an expected
result; every runbook needs a recovery verification and an escalation.

**Also required — alert integrity.** Every alert has a threshold, a **named person**, and a
**runbook**. An alert missing any of the three is worse than no alert:

> A tolerated alert teaches the team to tolerate all of them.

---

# Criterion 3 — Ongoing compliance obligations mapped to an owner and a cadence

**Passes when** every obligation from `09-technology`'s obligation trace appears with a cadence, a
named owner, the **evidence it produces**, and where that evidence is kept.

**Fails when** any obligation has no owner, no cadence, or no artifact.

| Fails | Passes |
| --- | --- |
| "We maintain HIPAA compliance" | "Access log review — monthly — «named role» — produces «audit record» — kept in «location»" |
| "Logs are reviewed regularly" | A cadence, an owner, an artifact |
| "Staff are trained" | Annual, owned, certificates kept somewhere named |

This is the third stage of a chain the framework runs end to end:

| Module | With an obligation |
| --- | --- |
| `02-market` | Finds it |
| `09-technology` | Builds the mechanism |
| **`13-operations`** | **Runs it** |

> Compliance is a schedule, not a state. A mechanism that exists but is never exercised satisfies
> an auditor for exactly as long as nobody looks.

**The evidence column is not bureaucracy.** Being compliant and being able to demonstrate
compliance are different achievements, and an obligation producing no artifact cannot be shown to
have been met.

**Also required:**

| Check | Fails when |
| --- | --- |
| Non-negotiables | A rule from `09-technology` §10 has no way of becoming visible when breached |
| Data lifecycle | Retention is stated but unautomated, and that is not acknowledged |
| **Restore** | Backups are specified and the restore-test cadence is absent — "never" is an acceptable answer, silence is not |
| Rollback | The release process states no rollback method, or no test status |
| Unowned obligations | Any exist and are not listed as such |

An unautomated retention policy is a policy nobody executes. An untested restore is a cost with an
assumption attached.

---

# Criterion 4 — Running cost estimated at launch scale

**Passes when** the cost model includes infrastructure, third-party services, measurement,
**support staffing** and **compliance operations**; a true cost per user is derived; and it is
compared against `06-business`'s ceiling.

**Fails when** support staffing or compliance is omitted, or when the comparison is absent.

**Why those two lines specifically.** They are the ones no earlier module could supply, and the
ones every cost model forgets:

| Line | Why it was missing before |
| --- | --- |
| Support staffing | The volume forecast and response targets did not exist |
| Compliance operations | The recurring obligations were not yet a schedule |

With them, the **true cost to serve** exists for the first time in the run.

## The Cost Check

**Fails when** true cost per user exceeds the ceiling and no regress is recorded.

This is the third and last of the framework's arithmetic checks against the business model:

| Module | Check |
| --- | --- |
| `09-technology` | Infrastructure cost per user against the ceiling |
| `11-growth` | Implied CAC against the payback ceiling |
| **`13-operations`** | **Complete cost to serve against the ceiling** |

**The bent-estimate watch.** If the support estimate fell while this check was being run, the gate
fails. That estimate was derived from response targets the operator approved; lowering it silently
withdraws the commitment, and the withdrawal surfaces later as broken promises rather than as a
revised plan.

A failed cost check is a regress — `06-business` for the price, `07-strategy` for the scope.

---

# Criterion 5 — A cost ceiling breach is resolved by a recorded change to 06-business price or 07-strategy scope, never by revising the forecast

**Passes when:** no breach occurred, or a breach is recorded together with the regress it
triggered — a price change in `06-business` or a scope change in `07-strategy` — and the
person who decided.

**Fails when:** a breach is reported and the run continues on the original numbers, or when
the forecast that produced the breach is revised downward to clear it.

**The absorption to watch for.** "Support will take less time as the product matures." It is
probably true. It is also the only lever entirely within the author's control, which is why
it is reached for — and a margin produced this way exists only in the document.

---

# Module-Specific Checks

## The Rota Check

**Fails when** claimed coverage exceeds what the operator said can be staffed, or when the rota's
sustainability is not addressed.

| | |
| --- | --- |
| A rota of one | Not a rota |
| Coverage claimed with nobody behind it | A promise broken during the first incident |
| No answer for the on-call person's absence | An operational risk, unregistered |

For a solo operator this is the most consequential check in the module. "Weekday hours, best
effort, and here is what happens when I am away" passes. A four-hour target staffed by one person
does not.

## The Untested-Assumption Check

**Fails when** backups, rollback or runbooks are presented as working without a test, walk or
rehearsal.

| Claim | Verified by | If never done |
| --- | --- | --- |
| Backups work | A restore test | State "never tested" |
| A release can be rolled back | A rehearsal | State it |
| A runbook works | Walking it | Mark it unwalked |

None is expensive to close. All three are discovered unclosed during the incident that needed
them.

## The Owner Reality Check

**Fails when** an owner has been named who has not been told, or when "the team" appears as an
owner anywhere.

This is the same rule `10-execution` applies to blocked work, and for the same reason: unowned work
is unstarted work, and a name nobody has agreed to is decoration.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `support_model`, `runbooks`, `incident_process`, `compliance_operations`, `cost_model` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | Every operational decision records the alternative it rejected |
| U5 | Every volume and staffing forecast is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |

U6 has its strictest interpretation here. The reader has no access to the conversation **and** is
under pressure — which is why the runbook standard is what it is.

---

# Verdict

```yaml
gate:
  module: 13-operations
  criteria:
    support_defined_and_attributed: pass | fail
    incident_path_documented: pass | fail
    obligations_owned_and_scheduled: pass | fail
    running_cost_estimated: pass | fail
  module_checks:
    rota_sustainable: pass | fail
    untested_assumptions_declared: pass | fail
    owners_real: pass | fail
    cost_within_ceiling: pass | fail
  universal: [U1, U2, U3, U4, U5, U6]
  restore_tested: yes | no | never
  rollback_tested: yes | no | never
  runbooks_walked: «count of «n»»
  verdict: pass | fail
  regressed_to: «06-business / 07-strategy / 10-execution / none»
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to the `deliver` stage |
| Fail | Revise, or `return to 10-execution`. Three attempts, then halt |

`restore_tested: never` is a passing value when stated. It is recorded at the gate because it is
the single assumption in this module most likely to be discovered at the worst possible moment, and
an operator deserves to see it before launch rather than during recovery.

---

> **Gate Principle**
>
> Three criteria here concern documents. The fourth concerns money.
>
> The checks that matter most concern neither — they concern whether
> a real person can actually do what this plan says.
