---
Title: Quality Gate
Module: 14-ai-systems
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
  - 14-ai-systems/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This is the framework's last module gate. What passes here becomes a part of the product whose
mistakes are fluent, which is why three of the four criteria are about what happens when it is wrong.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# The Empty Case

**A run with no AI capability passes this gate** when §1 and §2 record that no capability was
justified, with the comparison that established it.

An empty module is a legitimate result. What fails is silence — a section left blank leaves the reader
unable to tell whether the question was considered or skipped.

---

# Criterion 1 — Each AI capability justified against a non-AI alternative

**Passes when** every candidate has a stated non-AI alternative, the alternative survives the
advocate check, the verdict is recorded, and dropped capabilities are listed with what replaced them.

**Fails when** any alternative is missing, any alternative is a straw man, or nothing was dropped and
no explanation is given.

> **The advocate check.** Could a competent person argue for the alternative in one honest sentence?

| Straw man — fails | Honest — passes |
| --- | --- |
| "The user could memorize all 70,000 codes" | "A search box ordered by this clinician's own 40 most-used codes" |
| "Someone could read every document manually" | "Require the sender to submit structured data, which most already have" |
| "We could hard-code every rule" | "The eight rules covering 90% of cases, plus a manual path" |

A straw man does not weaken the analysis — it **invalidates** it, because this criterion is the only
thing standing between the product and the module's characteristic failure:

> **Capability theater.** A model added because it is expected rather than because it wins. It costs
> money per operation, needs evaluation nobody scheduled, fails in ways nobody predicted, and
> replaces a form field that would have worked.

**The ratio is a signal.** Proposed versus kept. A module keeping everything it proposed did not run
this criterion honestly, and the gate should say so.

**Also required:** every kept capability serves a requirement from `08-product`. A capability with no
requirement arrived from what is technically possible, which is the orphan problem in its
AI-specific form.

---

# Criterion 2 — Training / grounding data availability confirmed, not assumed

**Passes when** every data need states its source, its volume, its quality, and **confirmed present
availability with evidence**; and cold-start behavior is stated.

**Fails when** any need is projected rather than confirmed, or when cold start is unaddressed.

| Fails | Passes |
| --- | --- |
| "We have historical consultations to ground on" | "`[verified: 4,100 records in «source», sampled «date»]`" |
| "The operator has this data" | `[verified: operator]`, having actually asked |
| "Data will accumulate after launch" | Not availability — this is the cold-start answer |

> An unconfirmed data need is a **blocker, not a risk**. It cannot be estimated, scheduled or built,
> and it surfaces in implementation week one — the most expensive place to find it.

**Cold start is not optional.** Most model-served features are at their worst exactly when the
product is newest and users are least tolerant. The answer is usually a non-AI path for the first
period, which is a design decision rather than a disappointment.

## The Data Rights Check

**Fails when** the right to use the data this way is unresolved, or when any regulated or PII field
from `09-technology` §3 appears as a model input.

The check is mechanical, and it is the fourth place the framework runs it:

```
List regulated and PII fields from 09-technology §3
Check each against every model input
  ├─ overlap → FAIL. Remove, redact, or the gate fails
  └─ none    → record "none — verified"
```

Sending a regulated field to a provider is the same class of exposure as putting one in an analytics
event property. **Also required:** whether data leaves the system, to whom, in which jurisdiction,
and whether provider training on it is contractually disabled rather than assumed.

---

# Criterion 3 — Evaluation method defined before the capability is committed to

**Passes when** every kept capability states a metric, a method, a passing bar, a sample size, a
cadence, a **ship gate**, and what happens if the bar is missed; the golden set's construction is
described; the judge is named and qualified; and both statistical and per-instance criteria exist.

**Fails when** any of those is absent, or when the bar was set after seeing outputs.

| Fails | Passes |
| --- | --- |
| "We will evaluate accuracy" | "≥95% of 200 golden-set cases judged correct by a «domain expert», re-run monthly and on every prompt change" |
| "Quality reviewed by the team" | A named reviewer with a stated qualification |
| "It seemed good in testing" | A bar, a sample, and a ship gate |

**On who judges.** In a domain product the reviewer must be a domain expert. This is the same
principle `03-user` applies when it forbids inventing user quotes:

> A developer who finds a generated clinical summary convincing has established that it is
> convincing — which is precisely the property that makes a wrong one dangerous.

**The golden set must be honest**: built from real cases, and never used for tuning. A set that has
been optimized against measures how well the capability was fitted to it.

**Both criterion types are required**, because `08-product`'s `Given / when / then` form assumes
determinism:

| Type | Example |
| --- | --- |
| Statistical | "≥95% of 200 cases judged correct" |
| Per-instance — always true | "Output never exceeds «n» characters" · "Always contains a citation" · "The user can always dismiss it" |

The per-instance guarantees go back to `08-product` as ordinary requirements, and they are where most
real safety lives: they hold on every single output, where an accuracy figure holds only on average
and users experience instances.

---

# Criterion 4 — Failure modes and human fallback specified

**Passes when** failure modes are specific to this product, each with detection and a guardrail; the
worst realistic outcome is stated; silent failures are identified; and the non-AI fallback is
specified **as a requirement**.

**Fails when** any failure mode is generic, when detection is absent, or when the fallback is
described as a contingency.

| Generic — fails | Specific — passes |
| --- | --- |
| "The model may hallucinate" | "The model may invent a drug interaction that does not exist, which a rushed clinician could accept" |
| "Output quality may vary" | "For handwritten notes, extraction drops silently to partial, and missing fields look like fields the user left blank" |

## The Detectability Check

**Fails when** a capability's autonomy exceeds "suggests" while the user bears the cost of an error
they cannot detect, and no mechanism makes the error visible.

> **The plausibility problem.** A model's errors are fluent. They arrive in the same register as its
> correct answers.

So error rate matters less than detectability, and the wrongness cost is what governs autonomy:

| Question | |
| --- | --- |
| What does one wrong output cost, in the user's terms? | |
| Who bears it? | |
| **Can the user detect it?** | The decisive one |

A capability right 99% of the time whose 1% is undetectable and consequential is more dangerous than
one right 90% of the time and visibly wrong the rest.

**A better prompt is not a guardrail.** A guardrail is a constraint on the output, a required
citation, a confidence threshold below which nothing is shown, a validation against a real source, or
a human confirmation step.

**Also required:** would we know it happened? "No" is a common answer and an important finding.

---

# Module-Specific Checks

## The Cost Ratio Check

**Fails when** AI cost per user per month is not compared against revenue per user from
`06-business`, or when a large share is noted without an option being chosen.

```
cost per operation × operations per user per month ÷ revenue per user = the share
```

A capability consuming a significant fraction of revenue per user is a margin problem, and it has
killed products. The options are a cheaper approach, fewer operations, a higher price, or dropping
the capability — and one must be chosen rather than noted.

The figure also goes to `09-technology` §12 and `13-operations` §11, where the framework's three cost
checks will find it.

## The Version Pin Check

**Fails when** a model claim carries no version and date, or when the capability is designed against
an unpinned model.

Model capabilities, limits and prices are version-scoped with a fast clock. An unpinned model changes
behavior with no deployment, and evaluation results expire silently.

**Also required:** deprecation exposure, a fallback model, and what switching provider would take.

## The Fallback-Is-Scope Check

**Fails when** the non-AI fallback appears only in this document.

It is a requirement, and it belongs in `08-product` where every other requirement lives — not in an AI
annex nobody opens at build time. The provider will have an outage; that path gets built or it does
not exist.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `ai_opportunities`, `model_strategy`, `data_requirements`, `evaluation_plan`, `failure_modes` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | Every kept-or-dropped verdict records the alternative it rejected |
| U5 | Every quality expectation, operation count and cost estimate is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |

---

# Verdict

```yaml
gate:
  module: 14-ai-systems
  applies: yes | no   # "no" with a recorded comparison is a pass
  criteria:
    justified_against_non_ai_alternative: pass | fail
    data_availability_confirmed: pass | fail
    evaluation_defined_before_commitment: pass | fail
    failure_modes_and_fallback_specified: pass | fail
  module_checks:
    data_rights_and_no_regulated_inputs: pass | fail
    detectability_governs_autonomy: pass | fail
    cost_ratio_computed: pass | fail
    version_pinned: pass | fail
    fallback_is_a_requirement: pass | fail
  universal: [U1, U2, U3, U4, U5, U6]
  proposed: «n»
  kept: «n»
  verdict: pass | fail
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `12-metrics` and `13-operations` |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

`proposed` and `kept` are recorded because their ratio is the most honest single signal about whether
Criterion 1 was run properly. A module that kept everything it proposed did not ask the question.

---

> **Gate Principle**
>
> This is the framework's last module gate, and it guards against
> the one failure the framework itself is built to prevent:
> something uncertain, stated fluently, and believed.
