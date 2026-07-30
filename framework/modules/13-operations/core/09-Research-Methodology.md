---
Title: Research Methodology
Module: 13-operations
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how operational claims are sourced, labeled and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 13-operations/core/06-Framework.md
Outputs:
  - Honestly bounded operations plan
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Methodology
  - Evidence
---

# Research Methodology

---

# Commitments Are Not Forecasts

This module contains two kinds of statement, and confusing them is its characteristic error.

| | Nature | Standing | Example |
| --- | --- | --- | --- |
| **Commitment** | A promise about what will be done | Requires the operator's agreement | "First response within four hours" |
| **Forecast** | A prediction about what will happen | An assumption before launch | "Roughly 3 tickets per 100 users per week" |

A commitment written without the operator's agreement is a promise made on their behalf, usually
to users, and they discover it when it is broken.

A forecast presented as a plan is a staffing decision resting on a guess.

| Statement | Correct form |
| --- | --- |
| Response target | `[verified: operator]`, or explicitly marked unapproved |
| Coverage hours | `[verified: operator]` |
| Ticket volume | `[assumption: needs validation]`, with the basis stated |
| Support hours per week | Derived from the volume and the target — assumption, not commitment |
| Cadences and owners | Commitments — the named owner must have been told |

**The owner rule.** An owner who has not been told is not an owner. Where the operator has not
supplied names, use roles and record it as an open question rather than inventing a person.

---

# The 3am Test Is the Only Runbook Standard

A runbook is not evidence-bearing in the usual sense; it is an instruction set, and instructions
are judged by whether they can be followed.

> Could someone who did not build this system follow this, alone, half awake, with nobody to ask?

| Fails | Passes |
| --- | --- |
| "Investigate the issue" | "Run «command». If the output contains «pattern», go to step 4" |
| "Check the logs" | "Open «location». Search «string», last 15 minutes" |
| "Restart the affected service" | "Run «command». Wait for «observable». If it does not appear in 60 seconds, escalate to «role»" |
| "Ensure the data is consistent" | "Run «query». The count should equal «n». If it does not, do not proceed — escalate" |

**Every step needs an expected result.** Without one, the reader cannot tell whether the step
worked, and they will proceed anyway.

**Every runbook needs a recovery verification and an escalation.** A runbook that ends after its
last step tells the reader nothing about whether they are finished, and nothing about what to do
when it did not work.

**Prefer walked runbooks.** A runbook that has been executed once, even in staging, is a different
artifact from one that has been written. Where none has been walked, say so — it is a real caveat
and it is cheap to close.

---

# Cost Figures

This module produces the framework's final cost figure, so its sourcing matters.

| Line | Source | Standing |
| --- | --- | --- |
| Infrastructure | `09-technology` §12 | As tagged there |
| Measurement | `12-metrics` §9 | As tagged there |
| Third-party services | Published prices, with dates | `[verified: source]` |
| Support staffing | Volume forecast × response target | `[assumption]` — inherits the forecast's weakness |
| Compliance operations | The §8 schedule, costed in hours | `[assumption]`, unless the operator supplied rates |

**Support staffing is a derived assumption, and it must stay one.** It comes from a volume
forecast nobody can verify before launch. What makes it useful is that it is derived transparently
— the volume, the target, the arithmetic — so that when real volume arrives, the line updates
instead of collapsing.

**Do not lower the support estimate to make the cost check pass.** The estimate was derived from
response targets the operator approved. Reducing it silently withdraws the commitment, and the
withdrawal surfaces as broken promises to users rather than as a revised plan.

---

# Compliance Claims, One Last Time

`09-technology` prohibited claiming compliance and required obligations to name mechanisms. This
module extends the same discipline to the operational half:

| Never | Instead |
| --- | --- |
| "We maintain HIPAA compliance" | "Access log review — monthly — «named role» — produces «audit record» — kept in «location»" |
| "Logs are reviewed regularly" | A cadence, an owner and an artifact |
| "Backups are in place" | Frequency, retention, location, RPO, RTO, and when restore was last tested |
| "Staff are trained" | Annual, owned, with certificates kept somewhere named |

> Compliance is a schedule, not a state. A mechanism that exists but is never exercised satisfies
> an auditor for exactly as long as nobody looks.

**The evidence column is not bureaucracy.** Being compliant and being able to demonstrate
compliance are different achievements, and only the second survives an audit. An obligation that
produces no artifact cannot be shown to have been met.

---

# The Untested Assumptions of Operations

Three claims in this module are routinely made and almost never verified. Each must state its real
status:

| Claim | Verified by | If never done |
| --- | --- | --- |
| Backups work | A restore test | Say "never tested" plainly |
| A release can be rolled back | A rollback rehearsal | Say so |
| A runbook works | Walking it | Mark it unwalked |

None of these is expensive to close. All of them are discovered, unclosed, during the incident
that needed them.

---

# Volume Estimates Without Data

There is no ticket history for a product with no users. The honest options, in order of quality:

| Basis | Standing |
| --- | --- |
| The operator's experience with a comparable product | `[inferred: operator experience]` |
| The flow analysis — steps most likely to confuse | `[inferred: 10-execution §4]` |
| A published figure for a comparable product and segment | `[inferred: source]`, noting the population differs |
| Nothing | Say "unknown", and state what the first month will establish |

**Do not import a support-volume benchmark as a plan.** Ticket rates vary by an order of magnitude
with onboarding quality, segment sophistication and product complexity — the three things a
benchmark cannot know about this product.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| State a response target without the operator's agreement | A promise made on their behalf, to users |
| Present a volume forecast as a plan | Staffing decided on a guess |
| Name an owner who has not been told | An unowned obligation wearing a name |
| Write "investigate" as a runbook step | The reader is stuck, at 3am |
| Write a step with no expected result | No way to know it worked |
| End a runbook with no verification or escalation | The reader cannot tell if they are finished |
| Claim compliance | It is not this document's to claim |
| List an obligation with no evidence artifact | Cannot be demonstrated |
| Say "backups are in place" | Not a statement about recovery |
| Report restore or rollback as working without a test | The most consequential untested assumption in operations |
| Lower the support estimate to pass the cost check | Silently withdraws an approved commitment |
| Claim coverage a rota cannot staff | It fails during the first incident |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Obligations | `09-technology` §10 obligation trace | An obligation has a mechanism but no schedule |
| Non-negotiables | `09-technology` §10 | A rule has no way of becoming visible |
| Severity | `09-technology` §11 | Data loss is not S1 |
| Recovery | `09-technology` §11 | RPO and RTO differ from what was designed |
| Retention | `09-technology` §3 | The lifecycle contradicts the modeled retention |
| Alerts | `12-metrics` §7 | A counter-metric threshold became no alert |
| Cost | `06-business` | True cost per user exceeds the ceiling with no regress |
| Coverage | Operator input | Claimed hours exceed what the operator said |
| Support burden | `10-execution` §4 | The likely confusions produce no roadmap item |

---

# Self Assessment

- Is every commitment attributed to the operator?
- Is every forecast tagged, with a basis?
- Has every named owner been told?
- Would a stranger get stuck in any runbook?
- Does every step have an expected result?
- Does every obligation produce an artifact?
- Have restore and rollback been tested, and does the document say so honestly?
- Did I reduce any cost line to make the arithmetic work?
- Does the claimed coverage match what the operator can staff?

---

> **Methodology Principle**
>
> Most of this module is a promise about someone's time.
>
> The framework cannot make that promise, which means its job is
> to write down exactly whose promise it is.
