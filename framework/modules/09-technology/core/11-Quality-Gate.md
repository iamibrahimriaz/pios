---
Title: Quality Gate
Module: 09-technology
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
  - 09-technology/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 10-execution
Tags:
  - Technology
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

Four deliverables come out of this module, and all four are read by someone about to write
code. Nothing between this gate and a running system will notice what it lets through.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Entities, relationships and constraints complete enough to generate a schema

**Passes when** every column has a type, a nullability and a default; every relationship has a
cardinality and an on-delete behavior; every entity with a lifecycle has a state machine
including forbidden transitions.

**Fails when** any of those is missing, anywhere.

**The schema test — how to run it.** Read §3 as though you had to write the DDL and nobody was
available to ask. Write down every question you would have. The criterion passes only when that
list is empty.

| Fails | Passes |
| --- | --- |
| `date` — "the appointment date" | `appointment_at` · timestamptz · not null · no default · "start time, stored UTC, displayed in the clinic's timezone" |
| "Patients have appointments" | `1:N` via `appointment.patient_id`, `ON DELETE RESTRICT` — "a patient with history cannot be deleted" |
| `status` — "the current status" | enum `patient_status` (`draft`,`active`,`discharged`); transitions in §5; `discharged → draft` forbidden |

**Also required, in both directions:**

| Direction | Failure |
| --- | --- |
| Entity → requirement | **Orphan entity** — modeled speculatively. Remove it |
| Requirement → data | **Unmodeled requirement** — a hole, or module 08 was vague |

**Also required:** every entity's classification block — PII columns, regulated data, retention
period with a cited basis, audit requirement. A retention period with no basis is an invented
legal position and fails both this criterion and Criterion 3.

---

# Criterion 2 — Every product capability has a supporting endpoint or interface

**Passes when** the coverage table in §7 is complete in both directions and both "uncovered"
lines are present, even when the answer is "none".

**Fails when** a MUST requirement is unreachable, or an operation serves no requirement.

| Direction | Failure | Consequence |
| --- | --- | --- |
| Requirement → operation | Uncovered capability | Discovered mid-build, when the design is fixed |
| Operation → requirement | Speculative surface | Code, tests, documentation and attack surface with no purpose |

**Also required:** every edge case in `08-product` §8 maps to a failure response. Module 08
specified five categories per requirement; if those do not appear here as statuses and codes,
they were specified and then dropped — which produces a product whose failure behavior is
whatever the framework does by default.

**Also required:** idempotency stated per write operation, and the existence-disclosure
position stated. Both are silent by default and both cause real defects — duplicate records,
and confirmation that a record exists to someone not permitted to see it.

**Concreteness test.** Request and response bodies must be actual shapes. "Returns the patient
record" is not a contract; two builders produce two different payloads from it.

---

# Criterion 3 — Regulatory requirements from 02-market reflected in the security model

**Passes when** every obligation in `02-market`'s regulatory landscape appears in §10's
obligation trace with a **named mechanism**, a **named enforcement point**, and a **citation**.

**Fails when** any obligation is met by a statement of intent, or is absent.

| Fails | Passes |
| --- | --- |
| "The system will be HIPAA compliant" | "Access restricted to the treating clinician — record-level authorization predicate, enforced in the query layer, `[verified: 45 CFR §164.312(a)(1)]`" |
| "Data is encrypted" | "Patient identifiers encrypted at field level, keys in «manager», rotated «period»" |
| "We retain records appropriately" | "`retained_until` column + nightly purge job, «n» years, `[verified: «source»]`" |

**The compliance-claim prohibition.** This document may not claim compliance. Compliance is
assessed by someone qualified to assess it. What this document can do — and must — is state the
mechanism by which each obligation is met, so that an assessment is possible.

**Obligations with no mechanism are blockers.** They belong in `state.open_questions` and in
the risk register, stated as blockers. An unmet legal obligation is not a risk to be weighed;
it means the product cannot lawfully operate.

**Also required:** authorization must be **located**, not only described. "Role-based access
control" with no enforcement point is the most common serious defect in designs of this kind,
because it reads as an answer.

---

# Criterion 4 — Stack choice justified with trade-offs stated, not asserted

**Passes when** every row in §9 names at least one rejected alternative, states what the choice
is worse at, and states what changing it would cost.

**Fails when** any row asserts a choice, or when the "trade-off" restates the benefit.

| Fails | Passes |
| --- | --- |
| "«Datastore» — reliable and widely used" | "«Datastore» — rejected «A» (no «feature» before v«n»), «B» (team has never operated it). Worse at «X». Changing it after launch means a data migration: one-way door" |

**The restated-benefit check.** A trade-off must be something the choice is *worse* at. "Slight
learning curve" is not a trade-off; it is a benefit with a hedge.

**Also required and evaluated here:**

| Check | Fails when |
| --- | --- |
| Operability | Nobody has established that the team can run this |
| Boring default | A more common technology would have served and no reason was written |
| One-way doors | The irreversible decisions are not identified |

---

# Criterion 5 — Regulated columns listed by name, not described

**Passes when:** an actual list of column names exists.

**Fails when:** the security model describes categories of personal data in prose.

**Why a list.** Three other modules check against it — `12-metrics` verifies no regulated
field reaches an analytics event property, `13-operations` schedules the review,
`14-ai-systems` verifies none enters a model input. A paragraph is not checkable, so those
three checks silently pass.

---

# Criterion 6 — Every obligation from 02-market mapped to a mechanism, or recorded as a blocker with a named owner

**Passes when:** each obligation has a named mechanism — a retention job, a deletion path,
an audit log, a residency decision — or a blocker with a named human owner.

**Fails when:** an obligation is acknowledged and nothing exists that would satisfy it.

**Blocker, not risk.** If no mechanism satisfies it, that is a blocker. Risks get managed
and blockers get resolved; softening one into the other buys time at a bad exchange rate.

**Why here.** This module is the middle link of the obligation chain. Break it and
`13-operations` has nothing to schedule — and nothing downstream notices a rule nobody
wrote down.

---

# Criterion 7 — Every external integration contract marked verified or inferred, and each inferred one names the verification step that blocks implementation

**Passes when:** every contract with a system this run does not control — a third-party API,
a plugin's data model, a partner's webhook, an export format — is marked **`[verified: named
documentation or source]`** or **`[assumption: needs validation]`**, and each inferred one
names the step that must confirm it **before** implementation.

**Fails when:** an inferred contract is written in the same voice as a verified one, or when
the verification step exists but is not stated to block.

## Why an inferred contract reads exactly like a verified one

**A method signature reconstructed from an error message on a support forum and a method
signature copied from vendor documentation are the same three lines of code on the page.**
Nothing about the artifact distinguishes them, and the builder has no reason to suspect one.

**This is where a specification's confidence is most easily overstated and least visible.**
Every other section carries prose that can hedge. An interface definition cannot hedge —
which is exactly why the tag has to be on it.

## What "blocks implementation" means here

**The framework does not build and does not verify.** What this criterion produces is a
**disclosure** carried into the handoff: which parts of the specification are assumptions,
and what would settle each one.

**Name it as a step with a position**, so it survives contact with a delivery plan:

> **Verify every `[assumption]` in the integration contracts against the vendor's source or
> documentation, and correct this document, before any implementation of the affected
> component.**

**Where verification turns out to be impossible** — no public API, no documentation, no
readable source — **that is a scope decision, not an implementation detail**, and it goes
back to `07-strategy` rather than being worked around by whoever hits it first.

## The failure this prevents

**Building an adapter on an unverified assumption is a defect the specification can catch and
the code cannot.** By the time the code exists, the assumption has been implemented, tested
against itself, and is indistinguishable from a requirement.

**Burying it is the same as omitting it.** An `[assumption]` tag on page nine of an interface
document is invisible to a builder who was told the package is complete. `engine/handoff.md`
requires it in the entry file's own text.

| Fails | Passes |
| --- | --- |
| `POST /v2/enroll {user_id, course_id}` with no tag, taken from a forum thread | `POST /v2/enroll {user_id, course_id}` [assumption: needs validation — reconstructed from error strings in «source», not vendor documentation]. **Verified in M0 against the vendor's published client, before any implementation** |
| "We will confirm the API during development" | "M0, three days, blocking: verify all six inferred signatures against source. If any has no public interface, it returns to 07-strategy as a scope decision" |
| A verified and an inferred endpoint in the same table, undifferentiated | A `Standing` column on every row: `verified` / `inferred`, with the source or the verification step |

---

# Module-Specific Checks

Not in `module.yaml`. Each fails the gate independently, because each is a way a design can
satisfy all four criteria and still be wrong.

## The Cost Check

Compare cost per user at launch in §12 against the cost-to-serve ceiling from `06-business`.

**Fails when** the design exceeds the ceiling and no regress is recorded.

This is the check that converts an argument about engineering taste into arithmetic. A design
that costs more per user than the business model can carry has invalidated the business model,
and this module is where that becomes visible for the first time. The resolution is a regress —
to `06-business` for the price, or to `07-strategy` for the scope — not an absorbed
inconsistency.

## The Load Check — architecture inflation

Compare the design's implied capacity against the launch and target figures from
`06-business`.

**Fails when** the design is sized for a scale the business model does not project.

> Every component is individually justifiable. Together they cost more than the business can
> carry and take longer to build than the roadmap allows.

The evaluation is arithmetic, not taste: if the sizing in §11 shows fractions of a request per
second at launch, a queue-based distributed design needs a reason that is not "eventually".

## The Provenance Check

Every version claim, limit, quota, price and regulated fact must cite a source with a version
or a date.

**Fails when** any is written from memory. Version-specific claims are the most reliably wrong
class of statement in technical writing, and they are stated with complete confidence.

## The Deliberate-Absence Check

**Fails when** §8 and §11 do not state what is deliberately not built and not built for.

Without those lines, every limit in the design reads as an oversight to the first person who
hits one — and gets "fixed" by someone who does not know it was a decision.

## The Restore Check

**Fails when** backups are specified and restore is not addressed.

An untested restore is not a backup. It is a cost with an assumption attached.

## The Identifier Check

Every name used in a schema statement, a query, an index, a grant, a trigger or an interface
path must resolve to something this module defines under that exact spelling.

**Fails when** any identifier is referenced and never defined — including when a definition
exists under a near-miss spelling: singular against plural, `snake_case` against `camelCase`,
or a table named one way in the schema and another way in the migration that constrains it.

**How to evaluate.** Collect every identifier the design *creates*. Collect every identifier
it *references*. Subtract. Anything left is a fail. This is mechanical, it takes a minute, and
`engine/validate-run.py` repeats it over the finished artifacts — but the gate is where it
should be caught, because by then the same name has usually been copied into four documents.

> **Criterion 1 asks whether the schema could be generated. It does not ask whether the rest
> of the design refers to the schema that was generated.** The two are different questions and
> a design can pass the first while failing the second in the statement that matters most —
> typically the constraint protecting the product's central guarantee, because that statement
> is written last, in a separate block, after the naming convention has drifted.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `data_model`, `api_contract`, `architecture`, `security_model`, `scalability_plan`, `tech_stack` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | Every architecture decision records the alternatives it rejected |
| U5 | Every one-way door and unevidenced judgment is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |
| U7 | Every control declared load-bearing names where it executes, and that place exists |

---

# Verdict

```yaml
gate:
  module: 09-technology
  criteria:
    schema_generatable: pass | fail
    capability_coverage: pass | fail
    obligations_traced_to_mechanisms: pass | fail
    stack_tradeoffs_stated: pass | fail
    regulatory_in_security_model: pass | fail
    regulated_columns_named: pass | fail
    integration_contracts_marked: pass | fail
  module_checks:
    cost_within_ceiling: pass | fail
    load_matches_projections: pass | fail
    provenance_cited: pass | fail
    deliberate_absences_stated: pass | fail
    restore_addressed: pass | fail
  universal: [U1, U2, U3, U4, U5, U6, U7]
  blockers: «unmet regulatory obligations, or none»
  verdict: pass | fail
  regressed_to: «08-product / 06-business / 07-strategy / none»
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `10-execution` and `13-operations` |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

Any entry in `blockers` must be surfaced to the operator regardless of the verdict. A design
that passes every criterion while containing an unmet legal obligation is a design that cannot
be built into a lawful product, and the gate verdict is not the right place for that to be
mentioned quietly.

---

> **Gate Principle**
>
> The next reader of this document is writing code from it.
>
> Everything this gate accepts becomes a fact about a running
> system, filled with real data, before anyone reads it again.
