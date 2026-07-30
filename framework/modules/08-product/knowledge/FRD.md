---
Title: FRD
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain what a functional requirements document adds, and when it should not exist separately.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/PRD.md
Outputs:
  - feature_spec
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - FRD
  - Concept
---

# FRD

---

# What It Is

The functional detail — behavior, edge states and acceptance criteria at the level a builder implements from.

Where a PRD and an FRD are separated, the division is by **audience and volatility**:

| | PRD | FRD |
| --- | --- | --- |
| Answers | Why, for whom, what and in what order | Exactly what happens |
| Read by | Operator, stakeholders, all later modules | Whoever builds and tests it |
| Changes | Rarely — a change is a scope decision | Frequently, as detail is resolved |
| Contains | The spine, priorities, non-goals | Given/when/then, the five edge categories, dependencies |

**For most products, one document is correct.** Splitting is worth it when the functional detail is large enough to
make the PRD unreadable, or when different people own the two. Splitting by default produces two documents that
disagree, and the disagreement is discovered during implementation.

---

# When It Applies

Across Moves 3, 4 and 6 — behavior, break and prove. Its content is the `feature_spec` output regardless of whether it
lives in a separate file.

---

# How to Apply It Here

**Decide the split deliberately and record it.** One document or two, and who owns each. An unrecorded split is how
two sources of truth appear.

**Keep the trace in whichever document holds the requirement.** The parent problem travels with the requirement, not
with the PRD. Otherwise the functional document becomes a list of behaviors with no justification, and orphans become
undetectable.

**Put the five edge categories here, worked per MUST requirement.** Empty, invalid, failure, permission, limit or
conflict. This is the bulk of the functional content and the half of the specification most often missing.

**Write behavior, not implementation.** Trigger, input, system response, resulting state, what the user sees. No
framework, no schema, no component names — those are `09-technology`'s and design's.

**Make it the thing `10-execution` slices from.** The first shippable slice is derived from behavior and dependencies,
so both need to be at a granularity that can be cut.

---

# Where It Misleads

**Two documents diverge and nobody notices until build time.** The PRD says one thing about a limit, the FRD another.
This is the standard cost of splitting, and it is why single-document is the default.

**An FRD becomes a technical design document.** Once it names tables, endpoints and services, it has taken
`09-technology`'s decisions while lacking module 09's method — which derives the data model before choosing technology.

**Functional detail is written for requirements that will not ship.** Detailing SHOULD and COULD items before the MUST
list is complete is effort spent on things below the line. The order of the moves prevents it if followed.

**The document is written once and treated as final.** Functional detail is the volatile layer; that is its nature. What
must be stable is the cut, and changes to it belong in the deferral ledger.

**Behavior is described only for the happy path.** A requirement with no unhappy paths is roughly half specified, and
the missing half is where products fail in front of real users.

---

# Related

| | |
| --- | --- |
| `PRD.md` | The document this may or may not be part of |
| `features/Edge-Cases.md` | The five categories in detail |
| `features/Acceptance-Criteria.md` | The provable form |
| `10-execution` | Where behavior becomes slices |

---

> **Concept Note**
>
> One document unless there is a reason for two — and the reason is
> ownership, not tidiness.
>
> Two sources of truth disagree eventually, and they disagree during
> implementation.
