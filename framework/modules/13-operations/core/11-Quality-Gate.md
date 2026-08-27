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

# Criterion 5 — A cost ceiling breach is resolved by a recorded change to 06-business price or 07-strategy scope, or the residual gap is stated as a figure and escalated to the viability decision — never by revising the forecast

**Passes when** one of three things is true:

1. **No breach occurred.**
2. **A breach is recorded together with the regress it triggered** — a price change in
   `06-business` or a scope change in `07-strategy` — the regress **closed the gap**, and the
   person who decided is named.
3. **A regress was made and the gap did not close.** The **residual gap is stated as a
   figure**, what each regress bought is recorded, and the run escalates to the viability
   decision rather than narrowing again.

**Fails when:** a breach is reported and the run continues on the original numbers, when the
forecast that produced the breach is revised downward to clear it, or when a regress is
recorded and the surviving gap is not.

## The third outcome, and why it needed its own words

**The original rule assumed a recorded change resolves the breach.** Sometimes it does not.

**A run narrowed its scope twice** — from a category product, to a reliability layer, to a
single narrow function — **and the venture still did not repay its build cost in any modelled
scenario.** The rule had no vocabulary for that, so the honest answer had to be invented in
prose. **And a run following the rule literally could record two scope changes, satisfy the
check, and never say that the thing still loses money.**

> **The danger is not a wrong answer. It is an indefinite loop.** Each narrowing feels like
> progress, each one is cheaper than the last, and nothing says when to stop narrowing and
> start deciding.

## What escalation requires

**State the residual gap as a number.** *"Remains challenging"* is not a statement of a gap.
Give the figure and say what it is a gap between.

**Record what each regress actually bought.** A narrowing that cut build cost by 40% and left
the venture unprofitable is a real finding about the shape of the opportunity, and it is lost
if only the final position is reported.

**Stop narrowing.** A third scope reduction is permitted **only when it targets a named cost
driver the first two did not touch**, and the module says which. Otherwise the remaining
question is not "what else can we cut".

**Escalate to the viability decision**, which is the operator's and is decision-dependent
(`engine/gates.yaml`): **standalone venture, one product in a portfolio, or not built?**
Recorded as an `open_question` with `blocking` and `premise_bearing` both true, each option's
consequence stated. **Scope reduction cannot answer it**, which is why it is not a gate the
run can pass by working harder.

**And it travels.** The residual gap changes what the whole run recommends, so it appears in
the Executive Summary's opening and in the decision report — not only here.

**The absorption to watch for.** "Support will take less time as the product matures." It is
probably true. It is also the only lever entirely within the author's control, which is why
it is reached for — and a margin produced this way exists only in the document.

| Fails | Passes |
| --- | --- |
| Two scope changes recorded, final scope presented as the answer | "Scope reduced twice. Build cost fell from «a» to «b». **Ceiling still exceeded by «figure»/yr.** Escalated: standalone, portfolio, or not built — Q«n», operator" |
| "The narrowed product is materially cheaper to build" | "«figure» cheaper, and still short by «figure». Narrowing addressed build cost; the gap is now maintenance labor, which no further narrowing touches" |
| A third narrowing round | "Not narrowed again. The first two targeted feature count; the residual driver is per-customer support, which scope reduction does not move" |

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
| U7 | Every control declared load-bearing names where it executes, and that place exists |

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
    cost_breach_resolved_or_escalated: pass | fail
  module_checks:
    rota_sustainable: pass | fail
    untested_assumptions_declared: pass | fail
    owners_real: pass | fail
    cost_within_ceiling: pass | fail
  universal: [U1, U2, U3, U4, U5, U6, U7]
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
