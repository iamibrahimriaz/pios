---
Title: Roadmap
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Maintain the deferral ledger so nothing leaves scope silently.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - Deferral ledger within prd_body
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Product
  - Roadmap
  - Concept
---

# Roadmap

---

# What It Is

The **deferral ledger** — this module's contribution to the roadmap, and the mechanism that makes the cut honest.

The gate criterion is explicit: anything out of MVP scope is moved to the roadmap, **not dropped silently.**

Each entry carries three things:

| | |
| --- | --- |
| **What** | The capability, specified enough to be recognizable later |
| **Why deferred** | Below the line, no parent problem, or serving a segment not yet addressed |
| **What would bring it back** | The trigger — evidence, a segment, a customer count, a regulatory date |

`07-strategy` owns the roadmap artifact and the release horizons. This module owns the ledger of what specification
revealed and set aside — which is where most of the roadmap's real content comes from.

---

# When It Applies

Throughout Move 2 (Specify) and Move 5 (Order). Every capability discovered while specifying goes here rather than to
the MUST list.

---

# How to Apply It Here

**Write the entry at the moment of deferral.** Recorded later, the reasoning is reconstructed; recorded then, it is
accurate. The reasoning is the part that saves the argument.

**Record the trigger, not a version number.** "When a second clinician shares the record" is a trigger. "V2" is a
label that will be interpreted differently by everyone who reads it.

**Include the high-scoring below-line items explicitly.** Where `features/Feature-Prioritization.md`'s score disagrees
with the tier, the disagreement is recorded here — module 07's cut outranks the arithmetic, and the tension is
information rather than an error to hide.

**Log orphans separately from deferrals.** A capability with no parent problem is deleted, not deferred. Recording that
it was proposed and why it was rejected prevents it returning as a new idea.

**Keep it in the PRD, not in a side document.** A ledger nobody reads alongside the requirements is a ledger that stops
being maintained by the second week.

---

# Where It Misleads

**Deferral becomes deletion when the reason is omitted.** The item leaves the document, the reasoning is lost, and six
weeks later the same capability is proposed with a fresh argument.

**The ledger becomes the next release's scope by default.** Everything cut is promoted wholesale to V1, which recreates
the product the cut was made to avoid. `07-strategy`'s `V1.md` requires each item re-justified against what was learned.

**Triggers are written as intentions.** "When we have time" and "later" are not triggers. A trigger is an observable
event.

**It gets used to end arguments rather than record them.** Deferring a contested capability resolves the meeting and
records nothing if the reason and trigger are left blank. That is the ledger being used as a release valve.

**Roadmap presentation replaces the ledger.** A tidy three-horizon diagram is a communication artifact. The ledger is
the working record, and it is the one that prevents silent scope change.

---

# Related

| | |
| --- | --- |
| `features/Future-Scope.md` | What belongs beyond this release |
| `features/Feature-Prioritization.md` | Where score and tier may disagree |
| `Requirements.md` | Where discovered capabilities are diverted from |
| `07-strategy` | The roadmap artifact and the release horizons |

---

> **Concept Note**
>
> Write the reason and the trigger at the moment of deferral.
>
> An item removed without them will be proposed again as a new idea,
> and nobody will remember it was already decided.
