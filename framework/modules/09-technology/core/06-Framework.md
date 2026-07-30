---
Title: Framework
Module: 09-technology
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which a specification becomes a technical design.
Audience:
  - AI Agents
  - Engineers
Prerequisites:
  - 09-technology/core/03-Core-Principles.md
  - 08-product gate passed
Outputs:
  - data_model
  - api_contract
  - architecture
  - security_model
  - scalability_plan
  - tech_stack
Related Modules:
  - 10-execution
  - 13-operations
Tags:
  - Technology
  - Framework
  - Method
---

# Framework — The Blueprint

---

# The Method

> The specification says what the product does. This module says what exists.
>
> Nothing is invented. The data, the operations and the constraints are already
> implied by the requirements — this module finds them and makes them exact.

Six moves, in order. The order matters more here than in any other module: modeling before
interfaces, interfaces before architecture, and technology chosen **last**.

```
   Derive  →  Model  →  Expose  →  Protect  →  Choose  →  Size
     │         │         │          │           │         │
  entities   schema   contract   controls    stack     limits
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Derive | What things exist, and what happens to them? | The entity and operation inventory |
| 2. Model | Exactly what shape is the data? | `data_model` |
| 3. Expose | How is each capability reached? | `api_contract` |
| 4. Protect | What must be prevented, and by what mechanism? | `security_model` |
| 5. Choose | What are we building it with, and what shape? | `architecture`, `tech_stack` |
| 6. Size | How much load, and what breaks first? | `scalability_plan` |

---

# Move 1 — Derive

**Read the requirements and extract what the system must contain.**

Three passes over `08-product` §7 and §8:

| Pass | Looking for | Yields |
| --- | --- | --- |
| Nouns | Things the requirements act on | Candidate entities |
| Verbs | What is done to them | Candidate operations |
| Adjectives and states | Conditions, statuses, lifecycles | State machines and enumerations |

Then check both directions, the same discipline module 08 applied to problems:

| Failure | What it looks like | What it means |
| --- | --- | --- |
| **Orphan entity** | An entity no requirement mentions | Speculative modeling. Remove it |
| **Unmodeled requirement** | A requirement whose data is nowhere | The model is incomplete, or the requirement is vague |

An unmodeled requirement usually means the requirement left its data implicit. That is
module 08's defect, and the correct response is to name it and regress — not to invent the
missing entity here, where nobody will know it was invented.

**Why first.** A model built from a mental picture of the product, then reconciled with the
requirements afterwards, always reconciles. Deriving in the stated direction means the
requirements chose the entities.

---

# Move 2 — Model

**Make the data exact.**

The bar is objective and it is the module's defining standard:

> **The schema test.** Could an engineer or a coding agent generate the schema from this
> document without asking a single follow-up question?

Every column needs a type, a nullability, and a default. Every relationship needs a
cardinality and an on-delete behavior. Anything missing is not a detail deferred — it is a
decision handed to whoever builds it, made without any of this context.

**What must be modeled, not described**

| Element | Because |
| --- | --- |
| Types and nullability | "A date" is three different columns |
| Cardinality | 1:N and N:M are different products |
| On-delete behavior | Cascade versus restrict is a business rule |
| Constraints | A `UNIQUE` or `CHECK` is a requirement encoded where it cannot be forgotten |
| Indexes | Each names the query it serves — an index with no query is a guess |
| State machines | Including **forbidden** transitions, which is where the bugs live |
| Classification | PII, regulated data, retention period, audit requirement, per entity |

**Constraints are requirements in their strongest form.** A business rule written in prose
is enforced by whoever remembers it. The same rule written as a `CHECK` is enforced by the
database. Where a requirement can be expressed as a constraint, express it as one.

---

# Move 3 — Expose

**Define how each capability is reached.**

Concrete shapes — actual request and response bodies, actual field names, actual validation
rules. A description of an endpoint is not an endpoint.

**The coverage check, both directions:**

| Direction | Failure |
| --- | --- |
| Requirement → operation | A MUST requirement is unreachable. It will surface mid-build |
| Operation → requirement | Speculative surface area. Every endpoint is code, tests, docs and attack surface |

**Edge cases become failure responses.** Module 08 specified five categories per
requirement. Each maps to a status and an error code here. An edge case with no
corresponding failure response was specified and then dropped, which is worse than never
having specified it.

**Two decisions that are easy to leave implicit and expensive to leave implicit**

| Decision | Why it matters |
| --- | --- |
| Idempotency, per write operation | Retry is universal. Non-idempotent writes plus retries produce duplicates |
| Existence disclosure — 404 or 403 | Returning 403 for a record the caller may not see confirms it exists |

---

# Move 4 — Protect

**Turn obligations into mechanisms.**

This is the move most often written as intention rather than design, and it is the one with
legal consequences.

> "We will be compliant with «regime»" is not a control. It is a hope with a citation.

Every obligation from `02-market`'s regulatory landscape must trace to a **named mechanism
at a named enforcement point**:

| Obligation | Mechanism | Enforcement point |
| --- | --- | --- |
| Records retained for «n» years | Retention column + scheduled job | Datastore + job runner |
| Access restricted to treating clinician | Record-level authorization check | Query layer |
| Deletion on request | Hard delete + cascade + audit entry | Deletion service |

**An obligation with no mechanism is a blocker, not a risk.** It goes to the open questions
and it is surfaced. This distinction matters: a risk is something that might cost you; an
unmet legal obligation means the product cannot lawfully operate.

**Threats must be specific.** A recital of generic vulnerability classes is not a threat
model. The useful form is: *what would it take for one user of this product to see another
user's data?* — answered against this design, with the test that verifies it.

---

# Move 5 — Choose

**Shape first, then technology.**

Architecture shape — one deployable, a modular monolith, separate services — is chosen
against the load and the team, not against what the industry is discussing.

Then technology, one row per layer, and **every row states its trade-off**. An asserted
choice fails the gate:

| Required per choice | |
| --- | --- |
| What was rejected | At least one real alternative |
| The trade-off accepted | What this choice is worse at |
| Reversibility | What it would cost to change later |

**Architecture inflation** is this module's characteristic failure, and it is the structural
sibling of module 08's scope laundering:

> Designing for a scale that does not exist. Every component is individually justifiable;
> together they cost more than the business model can carry and take longer to build than
> the roadmap allows.

Two mechanical checks against it:

| Check | Fails when |
| --- | --- |
| **The load check** | The design's stated capacity far exceeds the launch and target figures from `06-business` |
| **The cost check** | Cost per user at launch exceeds the cost-to-serve ceiling from `06-business` |

The cost check is the sharper of the two, because it converts an aesthetic argument about
engineering taste into arithmetic. A design that breaks the ceiling breaks the business
model, and the resolution is a regress — to `06-business` for the price, or to `07-strategy`
for the scope — not a quiet acceptance here.

**Two further checks, both about honesty rather than elegance**

- **Operability.** Can the team that will run this actually run it? A design nobody can
  operate is not a design.
- **The boring default.** Where a more common technology would have served, name it and say
  why it was not chosen. If no reason survives being written down, take the boring one.

---

# Move 6 — Size

**Name the numbers, the first bottleneck, and what you are not building for.**

Scale figures derive from `06-business`'s own projections, with the arithmetic shown — the
same show-the-arithmetic rule module 02 applies to market sizing.

| Required | Not acceptable |
| --- | --- |
| "First bottleneck: the reporting query, at roughly 50 concurrent users" | "It should scale" |
| "Response: add a read replica" | "Scale horizontally" |
| "Not built for: multi-region. Correct because every user is in one country" | Silence |

The third row is the one usually missing. Stating what the system is deliberately **not**
built for is what makes the design defensible rather than merely modest — and it stops the
first person to hit a limit treating it as an oversight.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Choose the stack first | Requirements bent to fit the technology |
| Model before deriving | Entities from a mental picture, reconciled afterwards |
| Build interfaces before the model | Endpoints that cannot be implemented as specified |
| Add security last | Controls bolted on, and obligations discovered after the design is fixed |
| Size before choosing | Capacity planning for a shape you have not chosen |
| Skip the cost check | A technically excellent design the business cannot afford to run |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| What is in the MVP | `07-strategy` — binding |
| Model prompts, evaluation, fallback behavior | `14-ai-systems` |
| Build sequence and dates | `10-execution` |
| On-call, runbooks, support | `13-operations` |
| Product metric definitions | `12-metrics` |

---

# Self Assessment

- Did I derive the entities from the requirements, or from a picture of the product?
- Could someone generate the schema from §3 with no questions?
- Does every requirement have a reachable operation, and every operation a requirement?
- Does every edge case have a failure response?
- Does every regulatory obligation name a mechanism and an enforcement point?
- Does every technology choice state what it is worse at?
- Do my scale figures come from `06-business` or from ambition?
- Is the cost per user inside the ceiling?
- What am I deliberately not building for?

---

> **Framework Principle**
>
> This module's whole discipline is choosing technology last.
>
> Every failure in it comes from having chosen something before
> knowing what had to be built.
