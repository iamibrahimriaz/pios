---
Title: Future Scope
Module: 08-product
Section: knowledge/features
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Record what is out of scope with a trigger, and keep it out of the build.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Roadmap.md
Outputs:
  - Future-scope entries within the deferral ledger
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - Product
  - Scope
  - Concept
---

# Future Scope

---

# What It Is

Everything the specification revealed and set aside — recorded so that it is out of the build without being out of the
record.

Three kinds arrive here, and they are handled differently:

| Kind | Handling |
| --- | --- |
| **Below the line** | Deferred, with a reason and a trigger |
| **A non-goal from `07-strategy`** | Stays excluded; note the reconsider trigger if module 07 gave one |
| **An orphan** | Deleted, and the deletion recorded so it is not re-proposed as new |

The distinction that matters most: **knowing about a future capability is free; building for it is not.**
`09-technology` may be told a direction as context, and must not treat it as a requirement — that is architecture
inflation, and it is paid for immediately in complexity nobody asked for.

---

# When It Applies

Throughout Moves 2 and 5, written at the moment something is set aside.

---

# How to Apply It Here

**Write the trigger as an observable event.** "When a second person needs access to the same record." Not "V2", not
"when we have time".

**Separate deleted orphans from deferred capabilities.** They look identical in a list and mean opposite things. One is
awaiting evidence; the other was rejected for lacking any.

**Pass architectural implications to `09-technology` as context, labeled.** "A likely later direction is multi-user
access" is useful. It is not a requirement, and module 09's job is to note it without designing for it.

**Keep future scope out of the acceptance criteria.** A criterion referencing something not being built cannot pass or
fail, and it will be interpreted as a commitment.

**Re-check the ledger at the next cut.** `07-strategy`'s `V1.md` requires each item re-justified against what was
learned rather than promoted automatically. The ledger is the input to that review, not its conclusion.

---

# Where It Misleads

**Future scope becomes present architecture.** "We will need this eventually" justifies building the abstraction now.
That is the single most expensive way a specification leaks into a codebase, and `09-technology` guards against it
because this module handed it over.

**The ledger becomes the next release's plan.** Everything set aside gets promoted, and the product the cut was designed
to avoid gets built one release later.

**Deleted orphans reappear as new ideas.** Without the record of rejection, the same capability arrives again with a
fresh justification — which will sound reasonable, because orphan justifications always do.

**Out-of-scope items get specified in detail.** Effort spent describing what will not be built is effort not spent on
the two-builder test for what will. A one-line entry is the right fidelity.

**"Future" is used to avoid saying no.** Deferring a contested capability with no trigger is a refusal to decide, and it
leaves the argument to be repeated.

---

# Related

| | |
| --- | --- |
| `08-product` `Roadmap.md` | The ledger itself |
| `Feature-Lifecycle.md` | Why deferral is cheaper than removal |
| `Feature-Discovery.md` | The orphan rule |
| `07-strategy`, `09-technology` | Non-goals, and the inflation guard |

---

> **Concept Note**
>
> Knowing a direction is free. Building for it is not.
>
> Record the trigger, keep the fidelity to one line, and note deleted
> orphans separately — they are not waiting, they were refused.
