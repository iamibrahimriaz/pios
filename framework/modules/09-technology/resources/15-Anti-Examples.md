---
Title: Anti-Examples
Module: 09-technology
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show technical designs that fail the schema test or inflate the architecture.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - Recognition of architecture inflation and unmet obligations
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

Technical sections are reviewed by people who defer to them. Each example below would pass that review and fail the module's own tests.

---

# Anti-Example 1 — The Model That Cannot Generate a Schema

## ❌ Looks designed

```
Data model

Practice        — has many Clinicians, has many Consultations
Clinician       — belongs to Practice, has many Consultations
Consultation    — belongs to Clinician, has one Recording, has one Note
Recording       — audio file, belongs to Consultation
Note            — draft and final text, belongs to Consultation
AuditEntry      — tracks changes

Relationships are shown in the ERD below.
```

**Why it fails**

- **Apply the schema test:** could an engineer generate the schema from this without one follow-up question? No. No types, no nullability, no
  defaults, no on-delete behavior, no constraints, no classification.
- **"Consultation has one Note"** — is that enforced? What happens on a second attempt? Cardinality without a constraint is a hope.
- **No classification.** Which entities hold regulated data determines every obligation in Move 4, and `12-metrics` runs its privacy check
  against this list.
- **The diagram is offered as the model.** A picture cannot carry a retention period or a forbidden transition.

## ✅ Passes

```
ENTITY  Consultation                    Parent requirement: R-01
  id                uuid       not null  pk
  practice_id       uuid       not null  fk → practice(id) ON DELETE RESTRICT
  clinician_id      uuid       not null  fk → clinician(id) ON DELETE RESTRICT
  patient_ref       text       not null  ← REGULATED (identifier)
  occurred_at       timestamptz not null
  state             enum       not null  default 'recording'
  documented_at     timestamptz null     ← null until approved
  created_at        timestamptz not null  default now()

  CONSTRAINT  documented_at is not null IFF state = 'documented'
    (the business rule, encoded where it cannot be forgotten)
  UNIQUE      (clinician_id, occurred_at)
    (prevents duplicate consultations from a double submission —
     the idempotency rule from api/Endpoints.md, enforced in the schema)

  STATE MACHINE
    recording → uploaded → transcribed → documented
    recording → abandoned
    FORBIDDEN: documented → anything. Terminal.
    FORBIDDEN: transcribed → recording. Cannot re-record after transcription.
    (The forbidden transitions are where the bugs live.)

  CLASSIFICATION
    Contains regulated data: YES (patient_ref)
    Retention: 8 years [02-market Frame 2, «citation»]
    Audit required: YES, including READ (HIPAA-style obligation)
    PII columns: patient_ref
    → 12-metrics must check every event property against this list

ENTITY  Recording
  ...
  audio_deleted_at  timestamptz null
  CONSTRAINT  audio blob is null IFF audio_deleted_at is not null
    (retention enforced structurally, not by a job's good behavior alone)
```

---

# Anti-Example 2 — Compliance as Intention

## ❌ Looks designed

```
Security and compliance

The platform will be fully GDPR compliant. All data is encrypted in
transit and at rest. Access is role-based. Audit logging is enabled.
We follow OWASP best practices and will conduct a security review before
launch. Data is stored in «region».
```

**Why it fails**

- **"Will be fully GDPR compliant" is not a control.** It is a hope with a citation, and the framework forbids claiming compliance at all.
- **Not one obligation is named.** Erasure, retention, minimization, portability, breach notification — none appears, so none has a mechanism.
- **"Encrypted at rest" addresses stolen hardware and nothing else.** The likely breach path is a missing authorization check, which no
  encryption prevents.
- **"Role-based access" cannot express the actual rule**, which is relational: the clinician treating this patient.
- **"Follow OWASP" is a completed checklist with no mechanisms**, and the threat question was never asked.

## ✅ Passes

```
OBLIGATIONS → MECHANISMS → ENFORCEMENT POINTS   (never "compliant")

Obligation                 Mechanism                    Enforcement point
Erasure on request         hard delete + cascade through  deletion service
  [«citation», «date»]     consultation, recording, note,
                           draft, and the search index;
                           audit entry retained
Retention 8 years          retention column + nightly     job runner
  [«citation»]             job; audio deleted at 30 days
Access limited to the      record-level check: the        query layer —
  treating clinician       clinician must be linked to    ONE point, and
  [«citation»]             the patient's practice         every path passes
                                                          through it
Read access auditable      audit entry on every read of   query layer
  [«citation»]             a regulated entity
Residency «region»         provider region pinned;        infrastructure
  [«citation»]             no CDN for regulated content   configuration
Breach notification        detection → assessment →       13-operations
  within «n» hours         communication runbook          runbook, owned

BLOCKER, not a risk
  The retention obligation conflicts with the backup policy: backups are
  held 90 days, and an erasure request must complete sooner.
  UNRESOLVED. This goes to open questions and it is surfaced.
  An obligation with no mechanism means the product cannot lawfully
  operate — it is not something to note and proceed past.

THREAT QUESTION, answered specifically
  What would it take for one GP to see another practice's consultation?
    They would have to reach a query that omits the practice link. Every
    read passes through «repository», which requires a practice_id derived
    from the session — not from the request. The paths that bypass it
    would be: the nightly retention job (runs as system, reads all — by
    design), and the export operation (uses the same repository).
  TEST: an automated test attempts cross-practice access via the API, the
    export operation and the search endpoint. Runs in the pipeline.
```

---

# Anti-Example 3 — Architecture Inflation

## ❌ Looks designed

```
Architecture

Microservices: auth-service, practice-service, consultation-service,
transcription-service, notification-service, audit-service.
Communication via a message broker with event sourcing for the audit
trail. Kubernetes across three availability zones. Redis for caching,
Elasticsearch for search, a data warehouse for analytics. CQRS separates
read and write paths. Designed to handle 100,000 concurrent users.
```

**Why it fails**

- **The load check fails immediately.** `06-business` projects 24 practices in year one. The design's stated capacity exceeds the target by
  four orders of magnitude.
- **The cost check fails.** Six services, a broker, Kubernetes, Redis, Elasticsearch and a warehouse each carry a monthly floor. Summed, that
  is the idle cost before any customer exists — against a £20/user/month ceiling.
- **Every component is individually justifiable**, which is exactly what makes inflation hard to see.
- **The operability check fails.** One operator cannot run this, and `13-operations` inherits it as a rota of one across six services.
- **Event sourcing was chosen for its audit benefits**, which `database/Audit.md` satisfies far more cheaply.

## ✅ Passes

```
SHAPE: one deployable, with enforced internal module boundaries.
  Rejected: separate services.
  Trade-off accepted: everything scales together. Acceptable — see the
    load check.
  Reversibility: the transcription path is the identified first
    extraction candidate. Stateless by design, so extracting it later is
    a deployment change, not a rewrite.

LOAD CHECK
  06-business target: 24 practices year one, ~«n» consultations/week.
  Peak: Monday mornings, ~«n» concurrent uploads.
  A single instance handles this with substantial headroom.
  Designed capacity: ~«n»× target. Stated.

COST CHECK   (the sharper of the two)
  compute            £«x»/month
  managed postgres   £«x»/month
  object storage     £«x»/month
  monitoring         £«x»/month
  inference          £0 — the MVP is service-delivered, 07-strategy
  TOTAL idle floor   £«x»/month  ← what we pay with no customers
  At 24 practices: £«x»/user/month against 06-business's £20 ceiling. ✓

  No queue, no cache, no search cluster, no warehouse. Each was considered
  and each has no requirement behind it yet.

OPERABILITY
  One operator, weekday hours. One deployable, one datastore, one
  dashboard, four alerts. 13-operations can staff this.

NOT BUILT FOR — stated, so nobody treats a limit as an oversight
  Multi-region. Correct: every practice is in one jurisdiction, and
    residency forbids it anyway.
  Real-time collaboration. No requirement.
  100k concurrent users. See the load check.
```

---

# Anti-Example 4 — Technology Chosen First

## ❌ Looks designed

```
Technology stack

Frontend    React with Next.js
Backend     Rust with Axum, for performance and safety
Database    MongoDB, for schema flexibility
Search      Elasticsearch
Deployment  Kubernetes on «provider»
Queue       Kafka

These choices give us a modern, scalable foundation.
```

**Why it fails**

- **No alternatives, no trade-offs, no reversibility.** The gate requires all three per row, and an asserted choice fails it.
- **MongoDB "for schema flexibility"** contradicts Move 2, which encoded business rules as `UNIQUE` and `CHECK` constraints. Choosing a store
  that cannot enforce them moves the rules into application code, where they are optional.
- **Rust "for performance"** — the load check shows performance is not the constraint. The real constraint is one operator's time, and the
  choice ignores it.
- **The boring default was never named.** The rule is that if the reason for rejecting it does not survive being written down, take the boring
  one.
- **"Modern and scalable" is not a justification**, and no buyer has ever chosen a product for its framework.

## ✅ Passes

```
Layer      Choice        Rejected        Trade-off accepted        Reversibility
Backend    «familiar     «alternative»   Slower at high            High — the
           runtime»                      concurrency than          data model is
                                         alternatives. Irrelevant  independent
                                         at our load, and the
                                         operator knows it, which
                                         is the deciding factor
Database   PostgreSQL    MongoDB         Less schema flexibility.  LOW — this is
                                         That is the POINT:        a one-way
                                         Move 2's constraints      door. Chosen
                                         must be enforced by the   deliberately
                                         store, not remembered
Frontend   «server-      «SPA            Less interactive than a   Moderate
           rendered»     framework»      full client app. The job
                                         is a form and a review
                                         screen
Hosting    «managed      «self-managed»  Higher unit cost, far     Moderate —
           platform»                     lower operational load.   provider
                                         Correct for one operator  lock-in noted

THE BORING DEFAULT
  Considered for each row. Taken in three of four. The one departure
  («server-rendered» over a plain server-rendered template) is justified
  by the review screen's interactivity, and that reason survives writing
  down.

NOT CHOSEN, and why
  Search cluster    — database full-text is sufficient at this volume,
                      and a second store is another erasure path
  Queue             — one background job, one scheduler. No broker needed
  Container orchestration — one deployable
```

---

# Anti-Example 5 — "It Should Scale"

## ❌ Looks designed

```
Scalability

The architecture is designed to scale horizontally. Stateless services
behind a load balancer allow us to add capacity as demand grows. Database
read replicas and caching will handle increased read load. We will monitor
performance and scale as needed.
```

**Why it fails**

- **"It should scale" is what Move 6 explicitly rejects.** No figure, no named bottleneck, no response.
- **No first bottleneck**, so there is nothing to monitor and nothing to verify.
- **"Scale horizontally" is a category, not a response.**
- **Nothing is stated as deliberately not built for**, which is the row usually missing and the one that stops a limit being read as an
  oversight.

## ✅ Passes

```
FIRST BOTTLENECK
  The consultation-list query for a practice with «n» historical
  consultations, at roughly «n» concurrent users.
  Basis: the query aggregates across consultations and notes; the index
  on (practice_id, occurred_at) serves it, and beyond «n» rows the
  aggregate becomes the cost. [inferred: query plan]
  RESPONSE: paginate by cursor — api/Pagination.md — and add a covering
  index. Not a read replica; that is the second response, not the first.

SECOND BOTTLENECK
  Concurrent uploads on Monday mornings, at roughly «n».
  RESPONSE: the upload path is already asynchronous. Add worker capacity.

DEGRADATION
  Approaching capacity, uploads queue rather than fail. The GP sees
  "Waiting to upload — «n» recordings" and can continue working.
  That state is R-02's limit edge case, already specified in 08-product.

MONITORED
  The consultation-list query's p95 latency · queue depth and oldest item
  age · scheduled job success (absence-alerted) · cost per user.

NOT BUILT FOR — stated
  Multi-region     correct: one jurisdiction, and residency forbids it
  Offline-first    the GP has connectivity in the practice; the upload
                   path tolerates loss, which is a different requirement
  100k users       four orders of magnitude beyond target
  Real-time multi-clinician editing   non-goal from 07-strategy
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Unschematizable model | Entities and relationships with no types, constraints or classification |
| Compliance as intention | "Will be compliant", no obligation named, no mechanism |
| Architecture inflation | Six services for 24 practices; every component defensible |
| Technology first | A stack with no alternatives, trade-offs or reversibility |
| "It should scale" | No bottleneck, no figure, no non-goals |

---

> **Resource Note**
>
> The cost check is the sharpest tool in this module because it converts an
> argument about engineering taste into arithmetic.
>
> Six managed services for twenty-four practices is not a debate. It is a
> number against a ceiling.
