---
Title: Frontend
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose the client layer against the real conditions of use, not against screen designs.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Tech-Stack.md
Outputs:
  - Frontend choice within tech_stack
Related Modules:
  - 03-user
  - 10-execution
Tags:
  - Technology
  - Frontend
  - Concept
---

# Frontend

---

# What It Is

The client layer — chosen against `03-user`'s recorded conditions of use rather than against visual ambition.

The deciding inputs are already on the page:

| From `03-user` | What it constrains |
| --- | --- |
| The device, and whether it is shared | Session handling, sign-in frequency, what may be cached locally |
| Connectivity, including any offline period | Whether local state and sync are required — a large decision |
| Physical conditions — one hand, gloves, sunlight | Target sizes, input methods, contrast |
| Who can see the screen | What may be displayed by default |
| Accessibility needs and any binding standard | Input methods that must work, from `03-user/knowledge/Accessibility.md` |

Offline capability is the one that changes everything. Retrofitting it means adding a second source of truth and a
conflict-resolution policy, which is a data-model decision rather than a frontend one.

---

# When It Applies

In Move 5 (Choose). Screens are design's output, derived from `08-product`'s behavior — not decided here.

---

# How to Apply It Here

**Settle offline first, or rule it out explicitly.** If any part of the job happens without connectivity, that is a Move 2
consequence: local state, sync, and a documented conflict policy.

**Match the delivery model to the buyer's environment.** Institutional devices may be locked down, may run old browsers,
and may forbid installation. Web, installed app and mobile are not interchangeable under those constraints.

**Carry the accessibility requirements through as constraints.** Keyboard-only operation, screen-reader compatibility and
imprecise touch are requirements from `08-product`, not styling.

**Keep authorization server-side.** A client may hide what a user cannot do; it cannot enforce it. The enforcement point
named in Move 4 is on the server, always.

**State what the client stores.** Cached regulated data on a shared device is a security decision, and `security/Encryption.md`
and Move 4's classification both apply to it.

---

# Where It Misleads

**The frontend is chosen from designs that do not exist yet.** Behavior from `08-product` is the input; layout comes later,
and choosing a framework to suit an imagined interface is backwards.

**Offline is deferred as an enhancement.** It is architectural. Deferring it means rebuilding the data flow when it
arrives, and it usually arrives because a user's connection was always unreliable.

**Client-side validation is mistaken for enforcement.** It is a usability affordance. Every rule it expresses must also be
enforced server-side, and `api/Errors.md` covers what the client is told.

**The demo environment substitutes for the real one.** `10-execution`'s demo test applies: a client that performs on a
desk and fails on a ward has been tested against the wrong conditions.

**Rendering strategy is chosen on convention.** For an internal professional tool the trade-offs differ sharply from a
public site, and the reason should be stated rather than assumed.

---

# Related

| | |
| --- | --- |
| `Tech-Stack.md` | The justification format |
| `03-user` | Devices, conditions, accessibility |
| `security/Authentication.md` | Session lifetime on shared devices |
| `10-execution` | Where flows are designed from behavior |

---

> **Concept Note**
>
> Choose it against the ward, the van or the shared desk — not against
> the design.
>
> Offline is not a frontend feature. It is a second source of truth, and
> it is decided in the data model.
