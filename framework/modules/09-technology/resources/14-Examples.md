---
Title: Examples
Module: 09-technology
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a design that passes the schema test, the cost check and the threat question.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - A reference technical design
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. Note the order — data, interfaces, controls, then technology fifth — and note that the design surfaces an **unresolved
blocker** rather than proceeding past it.

---

# The Worked Technical Design

```
TECHNICAL DESIGN — «Consultation notes», MVP (service-delivered)

MOVE 1 — DERIVE   (from 08-product's requirements, both directions)

  Nouns → entities   Practice · Clinician · Consultation · Recording ·
                     Note · AuditEntry
  Verbs → operations record · upload · transcribe · review · approve ·
                     discard · export
  States → machines  Consultation: recording → uploaded → transcribed →
                     documented | abandoned

  Orphan entities: none. Every entity names the requirement it serves.
  Unmodeled requirements: none. R-01..R-07 all have data.

MOVE 2 — MODEL   (schema test: no follow-up questions)

  ENTITY  Consultation                          Serves: R-01
    id              uuid        not null  pk
    practice_id     uuid        not null  fk → practice ON DELETE RESTRICT
    clinician_id    uuid        not null  fk → clinician ON DELETE RESTRICT
    patient_ref     text        not null  ← REGULATED
    occurred_at     timestamptz not null
    state           enum        not null  default 'recording'
    documented_at   timestamptz null
    created_at      timestamptz not null  default now()

    CHECK    documented_at is not null IFF state = 'documented'
    UNIQUE   (clinician_id, occurred_at)   ← enforces idempotency
    INDEX    (practice_id, occurred_at desc)
             serves: the consultation-list query, R-09 and the review screen
    INDEX    (state) WHERE state != 'documented'
             serves: the outstanding-drafts query

    FORBIDDEN TRANSITIONS
      documented → anything   (terminal)
      transcribed → recording (cannot re-record after transcription)

    CLASSIFICATION
      Regulated: YES (patient_ref) · Retention: 8 years [«citation»]
      Audit: YES, including READ · PII: patient_ref
      → the list 12-metrics checks every event property against

  ENTITY  Recording                              Serves: R-02
    id              uuid        not null  pk
    consultation_id uuid        not null  fk → consultation ON DELETE CASCADE
                                          (a recording has no meaning alone)
    storage_key     text        null      ← null once deleted
    duration_secs   integer     not null  CHECK duration_secs >= 5
                                          (R-02's invalid-input rule, in
                                           the schema rather than in code)
    uploaded_at     timestamptz null
    audio_deleted_at timestamptz null

    CHECK  storage_key is null IFF audio_deleted_at is not null
           (retention enforced structurally, not by a job's good behavior)

    CLASSIFICATION  Regulated: YES (audio content)
                    Retention: 30 days for audio [«citation»]

MOVE 3 — EXPOSE   (concrete, both directions checked)

  POST /consultations                              Serves: R-01
    Request   { clinician_id, patient_ref, occurred_at }
    Response  201 { id, state: "recording" }
    Idempotent  YES — the UNIQUE constraint makes a retry return 409 with
                the existing id, not a duplicate
    Failures  400 invalid_patient_ref · 409 duplicate_consultation ·
              403→404 (see disclosure) · 503 unavailable, retry safe

  POST /consultations/{id}/recording               Serves: R-02
    Request   multipart audio
    Response  202 { state: "uploaded" }
    Idempotent  YES — re-upload replaces while state = 'recording'
    Failures  413 recording_too_large · 422 recording_too_short (the
              5-second rule) · 404 not_found (for another practice's id —
              NEVER 403, per the disclosure policy)

  Coverage: every MUST requirement has an operation. No operation lacks a
  requirement. Checked both ways.

  DISCLOSURE POLICY: 404 for anything the caller may not see. Applied
  uniformly, including on the export and search paths. Recorded once here
  so inconsistency between endpoints is visible as a defect.

MOVE 4 — PROTECT   (obligations → mechanisms → enforcement points)

  Obligation              Mechanism                     Enforcement point
  Erasure on request      hard delete + cascade through   deletion service
   [«citation»]           consultation, recording, note,
                          draft; audit entry retained
  Retention 8 yr / 30 d   retention columns + nightly     job runner
   [«citation»]           job; structural CHECK backs it
  Treating-clinician      record-level check; practice_id  query layer —
   access only            from the session, never from     one point
   [«citation»]           the request
  Read auditable          audit entry on every regulated   query layer
   [«citation»]           read
  Residency «region»      provider region pinned; no CDN   infrastructure
   [«citation»]           for regulated content
  Breach notification     detection → assessment →         13-operations
   within «n» hours       communication runbook            runbook, owned

  ⚠ BLOCKER — not a risk
    Erasure must complete within «n» days. Backups are retained 90 days.
    These conflict, and the resolution is not designed.
    → OPEN QUESTION, surfaced. An obligation with no mechanism means the
      product cannot lawfully operate.
    Candidate resolutions: document that erasure completes within the
      backup cycle and re-apply outstanding erasures on any restore
      (09-technology/knowledge/security/Recovery.md), or shorten backup
      retention. Legal input required — operator decision.

  THREAT QUESTION, answered against this design
    What would it take for one GP to see another practice's consultation?
      They would need to reach a query that omits the practice link. Every
      read goes through «repository», which derives practice_id from the
      session. The paths that bypass it: the retention job (system role,
      reads all — by design) and export (same repository).
    TEST: automated cross-practice access attempts via the API, export and
      search endpoints, run in the pipeline. 09-technology/knowledge/CI-CD.md.

MOVE 5 — CHOOSE   (shape first, then technology)

  SHAPE  one deployable, enforced internal module boundaries
    Rejected  separate services
    Trade-off everything scales together — acceptable, see the load check
    Reversibility  the transcription path is the first extraction
      candidate; stateless, so extraction is a deployment change

  LOAD CHECK   target 24 practices [06-business]; peak Monday uploads.
    A single instance has substantial headroom. Designed capacity ~«n»×
    target. Stated.

  COST CHECK
    compute «x» + postgres «x» + object storage «x» + monitoring «x»
    inference £0 (service-delivered MVP — 07-strategy)
    idle floor £«x»/month  ← paid with no customers
    at 24 practices: £«x»/user/month vs 06-business's £20 ceiling ✓
    → forwarded to 13-operations, which adds support and compliance

  STACK   (alternative · trade-off · reversibility per row)
    Backend    «familiar runtime» · «alternative» · slower at high
               concurrency, irrelevant at our load; the operator knows it
               · reversibility high
    Database   PostgreSQL · MongoDB · less schema flexibility, which is
               the point — Move 2's constraints must be enforced by the
               store · reversibility LOW, a one-way door, chosen
               deliberately
    Hosting    «managed platform» · self-managed · higher unit cost, far
               lower operational load; correct for one operator ·
               provider lock-in noted

    THE BORING DEFAULT: considered per row, taken in three of four.
    NOT CHOSEN: search cluster (database full-text suffices, and a second
      store is another erasure path) · queue broker (one job, one
      scheduler) · orchestration (one deployable)

  OPERABILITY  one operator, weekday hours, one deployable, one datastore,
    four alerts. 13-operations can staff it.

MOVE 6 — SIZE
  FIRST BOTTLENECK  the consultation-list aggregate at «n» concurrent
    users. RESPONSE: cursor pagination + a covering index. Not a replica —
    that is the second response.
  SECOND  concurrent Monday uploads. RESPONSE: add worker capacity.
  DEGRADATION  uploads queue rather than fail; the GP sees the unsent
    count and continues. Already specified as R-02's limit case.
  MONITORED  list-query p95 · queue depth and age · scheduled job success
    (absence-alerted) · cost per user
  NOT BUILT FOR  multi-region (residency forbids it) · offline-first ·
    100k users · real-time multi-clinician editing (non-goal)

GATE
  ✓ Entities, relationships and constraints sufficient to generate a schema
  ✓ Every product capability has a supporting operation
  ✓ Regulatory requirements reflected in the security model
  ✓ Stack choices justified with trade-offs, not asserted
  ⚠ One blocker surfaced: erasure versus backup retention. Unresolved,
    stated, and it needs a decision before launch.
```

---

# Example 1 — A Rule Encoded as a Constraint

## ❌ Poor

```
The application validates that recordings are at least 5 seconds.
```

## ✅ Good

```
duration_secs integer not null CHECK duration_secs >= 5
```

**Why.** A business rule in prose is enforced by whoever remembers it. The same rule as a `CHECK` is enforced by the database, on every path,
including the ones nobody reviewed.

---

# Example 2 — The Blocker Stated Rather Than Absorbed

## ❌ Poor

```
Erasure requests will be handled within the required timeframe. Backup
retention is 90 days per our policy.
```

## ✅ Good

```
⚠ BLOCKER. These conflict. The resolution is not designed.
An obligation with no mechanism means the product cannot lawfully operate.
Candidates listed; legal input required; operator decision.
```

**Why.** The framework distinguishes a risk from a blocker precisely here: a risk might cost you something, and an unmet legal obligation means
you cannot operate. Absorbing it would leave a compliance failure discovered during a customer's security review.

---

# Example 3 — The Threat Question Answered Specifically

## ❌ Poor

```
We follow OWASP guidelines and use role-based access control.
```

## ✅ Good

```
What would it take for one GP to see another practice's consultation?
They would need a query that omits the practice link. Every read goes
through «repository», which derives practice_id from the session. The
bypass paths are the retention job (by design) and export (same
repository).
TEST: automated cross-practice attempts via API, export and search.
```

**Why.** A recital of vulnerability classes is not a threat model. One question answered against this design, with the test that verifies it, is.

---

# Example 4 — The Cost Check as Arithmetic

## ❌ Poor

```
Infrastructure costs are expected to be modest at launch scale.
```

## ✅ Good

```
idle floor £«x»/month — what we pay with no customers
at 24 practices: £«x»/user/month against a £20 ceiling ✓
forwarded to 13-operations, which adds support and compliance
```

**Why.** This is the framework's first of three arithmetic checks, and the idle floor is the figure that matters before revenue exists.

---

> **Resource Note**
>
> The passing design ends with a blocker on the page, unresolved.
>
> That is the module working. An obligation with no mechanism is not a risk
> to carry forward — it is a decision someone has to make before launch.
