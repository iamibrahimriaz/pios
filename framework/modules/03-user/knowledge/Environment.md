---
Title: Environment
Module: 03-user
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Record the physical, organizational and technical context, including what cannot change.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/Personas.md
Outputs:
  - Context and immovables within personas and current_workflow
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - User
  - Environment
  - Concept
---

# Environment

---

# What It Is

The conditions the product would have to work inside — and, most importantly, the parts of them that
will not move.

| Dimension | Examples of what it decides |
| --- | --- |
| **Physical** | Standing, moving, one hand free, a patient watching, noise, gloves |
| **Temporal** | Interruptions, a ten-minute slot, a queue outside the door |
| **Organizational** | Who authorizes, who else touches the work, whose sign-off is required |
| **Technical** | The device, the browser, the network, the system of record that cannot be bypassed |
| **Social** | Who can see the screen, and what must not be visible on it |

The module closes with the question this file exists to serve:

> **What would this person not change, no matter how good the product is?**

Habits, tools, rituals and constraints that are effectively fixed define the shape any successful
product must take. A product that requires an immovable to move does not get adopted — however good it
is. This question is under-asked and highly predictive.

---

# When It Applies

In Move 3 (Embody) as persona context, in Move 4 (Observe) as the setting of each step, and as **The
Immovables** before the module closes.

---

# How to Apply It Here

**List the immovables explicitly, as their own set of lines.** They become constraints in
`08-product`, non-negotiables in `09-technology`, and the shape of the flows in `10-execution`. Buried
in prose, they are read as context and ignored.

**Name the system of record.** In most institutional markets one system cannot be replaced or worked
around, and everything else must fit alongside it. That single fact frequently determines the
architecture.

**Record the device and the conditions of use.** A tool used one-handed while standing, on a shared
machine, with a patient present, is a different product from the same features on a desk. This is
where `10-execution` gets its real constraints.

**Capture who else is involved.** Work that passes through two people has a hand-off, and hand-offs
are where products are abandoned. `08-product` needs the permission and visibility requirements that
follow.

**Distinguish an immovable from a preference.** "They will not use a second system" may be a policy, a
budget, or a habit. Say which — policies need `09-technology`; habits are `11-growth`'s problem.

---

# Where It Misleads

**Environment is treated as color rather than constraint.** It reads like scene-setting, so it gets
written vividly and consulted never. If a line here does not turn into a requirement or a constraint,
it was decoration.

**Immovables get quietly reclassified as change management.** "They will adapt" is the assumption
behind a large share of failed institutional software. Adaptation is possible; assuming it without
evidence is not, and it belongs in the risk register when relied on.

**The ideal conditions get documented.** A quiet desk with a good connection is where the product gets
demonstrated, not where it gets used. `10-execution`'s demo test is passed by products that only work
in the demo.

**Technical constraints get deferred to `09-technology`.** By then the requirements are written. A
browser version, an offline period, or a locked-down device is cheap to learn here and expensive to
learn there.

---

# Related

| | |
| --- | --- |
| `Personas.md` | Where context is recorded |
| `Accessibility.md` | Constraints that are legal as well as practical |
| `User-Journey.md` | The setting of each step |
| `09-technology`, `10-execution` | Where immovables become constraints |

---

> **Concept Note**
>
> Ask what will not change, and believe the answer.
>
> A product that needs an immovable to move is not a product that
> loses slowly — it is one that never starts.
