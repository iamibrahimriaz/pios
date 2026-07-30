---
Title: Workflow
Module: 09-technology
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Technology module.
Audience:
  - AI Agents
Prerequisites:
  - 09-technology/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/09-technology.md
  - state.outputs.data_model
Related Modules:
  - 10-execution
  - 13-operations
  - 14-ai-systems
Tags:
  - Technology
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Blueprint. This document is the procedure.

This module produces more of the final artifact set than any other: four of the sixteen
deliverables come directly from it.

---

# Position in the Run

```
08-product → [ 09-technology ] → 10-execution
                               → 13-operations
           → 14-ai-systems ────→
```

| | |
| --- | --- |
| Stage | `specify` |
| Depends on | `08-product` |
| Consumes | `feature_spec`, `acceptance_criteria`, `regulatory_landscape` |
| Produces | `data_model`, `api_contract`, `architecture`, `security_model`, `scalability_plan`, `tech_stack` |
| On fail | return to `08-product` |
| Human checkpoint | none |

`14-ai-systems` runs alongside this module and reads from it. Where a requirement is served
by a model rather than by deterministic logic, this module still owns the data it touches and
where it sits in the architecture.

---

# Step 1 — Verify Upstream and Inherit the Constraints

1. Confirm `08-product` is in `state.run.completed_modules` with a passing gate.
2. Read `feature_spec` — every MUST requirement, with its behavior.
3. Read `edge_cases` — all five categories per requirement. These become failure responses.
4. Read `acceptance_criteria` — these tell you what must be observable.
5. Read `regulatory_landscape` from `02-market`.
6. Read from `06-business`: the **cost-to-serve ceiling**, the price, and the launch and
   target user figures.
7. Read from `03-user`: the real operating environment — device, connectivity, interruption.

Record the constraints before designing anything:

| Inherited | Consequence |
| --- | --- |
| Regulatory regimes | Every obligation needs a mechanism, not an intention |
| Cost-to-serve ceiling | The design's cost per user must fit inside it |
| Launch and target scale | The capacity the design is sized to, and no more |
| User environment | Offline, interruption and device constraints are requirements |

> If a requirement cannot be met inside the cost ceiling or the regulatory constraint, that
> is a regress signal. Record it; do not absorb it silently by weakening the design.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `09-technology/core/03-Core-Principles.md`
3. `09-technology/core/06-Framework.md` — the Six Moves
4. `09-technology/core/08-Questions-To-Answer.md`
5. `09-technology/knowledge/database/` — Entities, Relationships, ERD, Indexes, Soft-Delete,
   Audit, History, Migration
6. `09-technology/knowledge/api/` — REST, Endpoints, Errors, Versioning, Authentication,
   Authorization, Pagination
7. `09-technology/knowledge/architecture/` — Architecture-Styles, Monolith, Modules,
   Microservices, Events, Queues, Caching, Scaling
8. `09-technology/knowledge/security/` — whichever regimes apply, plus OWASP, Encryption,
   Secrets, Backups, Recovery
9. The four deliverable templates this module feeds

---

# Step 3 — Derive

Move 1. Build the inventory before modeling anything.

1. Read the requirements for **nouns** — the things the system acts on. These are candidate
   entities.
2. Read for **verbs** — what is done to them. These are candidate operations.
3. Read for **states and conditions** — these become state machines and enumerations.
4. Run both checks:
   - **Orphan entity check** — any entity no requirement mentions. Remove it.
   - **Unmodeled requirement check** — any requirement whose data appears nowhere.

For an unmodeled requirement, ask which is true:

```
Is the requirement's data genuinely implicit?
  ├─ yes → module 08 left it implicit → name it and regress
  └─ no  → the inventory is incomplete → continue deriving
```

Do not resolve it by inventing the entity here. An invented entity is indistinguishable from
a derived one once written down, and nobody downstream will know which it was.

---

# Step 4 — Model

Move 2. Write the data model to the schema test.

For each entity: purpose sentence, source requirements, columns with type / nullability /
default / meaning, constraints with the business rule each encodes, indexes with the query
each serves, relationships with cardinality and on-delete behavior, and the classification
block.

Then, for every entity with a lifecycle, write the state machine — **including forbidden
transitions and what happens if one is attempted**.

**The schema test, run explicitly:** read §3 as though you had to generate DDL from it and no
one was available to ask. List every question you would have. The list must be empty.

---

# Step 5 — Expose

Move 3. Write the interface contract.

1. One operation per capability, with concrete request and response bodies.
2. Validation rules per writable field, traced to a requirement.
3. Failure responses mapped from `08-product` §8 — every edge case becomes a status and code.
4. The error taxonomy, once, consistently.
5. Idempotency stated per write operation.
6. The existence-disclosure position — 404 or 403 — stated and justified.
7. **The coverage table, both directions.** Uncovered requirements and orphaned operations
   both listed explicitly, even when the answer is "none".

---

# Step 6 — Protect

Move 4. Build the security model from the obligations.

1. Fill the control table: authentication, authorization, transit, rest, secrets, audit,
   backups, deletion.
2. Build the **regulatory obligation trace** — every obligation from `02-market` to a named
   mechanism at a named enforcement point, with the source cited.
3. List any obligation with no mechanism. These are **blockers**, and they go to
   `state.open_questions` and to the risk register, not into the prose as reassurance.
4. Write threats specific to this product, each with the test that would verify the
   mitigation.

The authorization model deserves particular care: state whether it is role-level or
record-level, and **where it is enforced**. Authorization described but not located is the
most common serious defect in specifications of this kind.

---

# Step 7 — Choose

Move 5. Architecture shape, then technology.

1. Choose the shape against the load and the team. State what is deliberately not added.
2. Fill the technology table — one row per layer, each with version, rejected alternatives,
   the trade-off accepted, and reversibility.
3. Run the **operability check**: can the team that will run this actually run it?
4. Run the **boring-default check**: where a more common technology would have served, name
   it and say why it was not chosen.

---

# Step 8 — Size, and Check the Cost

Move 6.

1. Derive launch and target figures from `06-business`, showing the arithmetic.
2. Name the first expected bottleneck and the load at which it appears.
3. Name the specific response — not "scale horizontally".
4. State what the system is deliberately not built for.
5. Fill the cost model, then run the two checks:

| Check | Action on failure |
| --- | --- |
| **Load check** — capacity far exceeds the projections | Simplify the design |
| **Cost check** — cost per user exceeds the ceiling from `06-business` | Regress: the design, the price, or the scope |

The cost check is not advisory. A design whose cost per user exceeds what the business model
can carry has invalidated the business model, and this module is where that becomes visible
for the first time.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/09-technology.md`. Write §1 last.

```yaml
outputs:
  data_model:        # §3, §4, §5 — schema-generatable
  api_contract:      # §6, §7 — concrete shapes and coverage
  architecture:      # §8 — shape, components, boundaries
  security_model:    # §10 — controls and the obligation trace
  scalability_plan:  # §11 — figures, bottleneck, what is not built for
  tech_stack:        # §9 — choices with trade-offs
```

Append every technical judgment made without evidence to `state.assumptions` with a
validation method — U5. Append every architecture decision to `state.decisions` with the
alternatives rejected — U4. Append every unresolved technical fact to
`state.open_questions`.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which entity did I model because products like this usually have one?
- Which column's type or nullability would a builder have to guess?
- Which requirement cannot actually be implemented against this model?
- Which endpoint exists because it seemed like it should?
- Which edge case from module 08 has no failure response?
- Which regulatory obligation is met by a sentence rather than a mechanism?
- Where is authorization described but not located?
- Which technology did I choose because it is interesting rather than because it fits?
- What in this design is sized for a scale the business model does not project?
- Which version-specific claim did I write from memory?

The coherence pass: does this design fit the cost ceiling from `06-business`, the operating
environment from `03-user`, and the first shippable slice from `08-product`? A design whose
first buildable piece is three months of infrastructure contradicts the roadmap it feeds.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

A **regress** is the correct outcome — not a failure of this module — when a requirement is
unimplementable as written, when an obligation cannot be met, or when the cost check fails.
Record which, and where it went.

---

# Step 12 — Hand Off

1. Append `09-technology` to `state.run.completed_modules`.
2. Confirm the four deliverables it feeds have everything they need.
3. Hand to `10-execution` and `13-operations`.
4. Confirm `14-ai-systems` has the architecture position and data scope for any model-served
   requirement.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `10-execution` | `architecture`, one-way doors, environments | Sequencing, and what must be right first |
| `13-operations` | `security_model`, backups, observability, degraded operation | Runbooks and support |
| `14-ai-systems` | `architecture`, `data_model` | Where the model sits and what data it may touch |
| `12-metrics` | Observability points | Where instrumentation goes |
| `05-Data-Model.md` | `data_model` | The shipped data model |
| `06-API-Contract.md` | `api_contract` | The shipped API contract |
| `07-Architecture.md` | `architecture`, `security_model`, `scalability_plan`, `tech_stack` | The shipped architecture |
| `12-Build-Handoff.md` | Stack, first slice, data and API starting points | The shipped build handoff |

`10-execution` needs the **one-way doors** specifically. Decisions that cannot be cheaply
reversed determine what must be sequenced early and what can wait — that is the main thing
this module tells the execution plan.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Entities that match no requirement | Modeled from a mental picture | Re-derive from the requirement text |
| A requirement with nowhere to store its data | Move 1 check skipped | Name it and regress to `08-product` |
| Columns without types or nullability | Schema test not run | Run it: list every question a builder would have |
| Relationships without on-delete behavior | Treated as an implementation detail | It is a business rule; state it |
| State machines with no forbidden transitions | Only the happy lifecycle modeled | Add them; that is where bugs live |
| A MUST requirement with no operation | Coverage check skipped | Add it, or record it as uncovered |
| Endpoints serving nothing | Speculative surface area | Remove them |
| "Compliant with «regime»" | Obligation stated as intention | Trace it to a mechanism and an enforcement point |
| Generic threat list | Threat model copied, not written | Ask how one user could see another's data |
| Stack asserted without alternatives | Move 5 shortcut | State rejected options and the trade-off |
| Distributed design at pre-launch scale | Architecture inflation | Run the load and cost checks |
| Cost above the ceiling | Design outgrew the business model | Regress to `06-business` or `07-strategy` |

---

> **Workflow Principle**
>
> Four deliverables come out of this module, and all four are read
> by someone about to write code.
>
> It is the last place a missing answer is cheap.
