---
Title: Tech Stack
Module: 09-technology
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Justify every technology choice with a rejected alternative, a trade-off and a reversibility cost.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - tech_stack
Related Modules:
  - 06-business
  - 10-execution
Tags:
  - Technology
  - Stack
  - Method
---

# Tech Stack

---

# What It Is

The technology chosen per layer — **fifth of six moves**, after the data, the interfaces and the controls exist.

Every row states three things, and an asserted choice fails the gate:

| Required per choice | |
| --- | --- |
| **What was rejected** | At least one real alternative |
| **The trade-off accepted** | What this choice is worse at |
| **Reversibility** | What it would cost to change later |

And the discipline that catches most bad choices:

> **The boring default.** Where a more common technology would have served, name it and say why it was not chosen. If no
> reason survives being written down, take the boring one.

---

# When It Applies

In Move 5 (Choose), after the architecture shape is settled. Shape first, then technology.

---

# How to Apply It Here

**Choose against the requirements, not against interest.** The data model and the operations are already on the page.
The question is what serves them, for this team, at this scale.

**Run the operability check.** Can the team that will run this actually run it? A design nobody can operate is not a
design, and `13-operations` inherits the answer as a rota.

**State reversibility honestly.** A database is expensive to change; a queue library is not. Knowing which decisions are
one-way lets the reversible ones be made quickly.

**Include what the choice costs to run.** Managed services trade money for operational load. That trade belongs in the
cost check against `06-business`'s ceiling, not in a footnote.

**Prefer what the team already knows.** Familiarity is a legitimate technical criterion and frequently the strongest one
available. It should be written down as the reason rather than left as an unstated bias.

---

# Where It Misleads

**The stack gets chosen first and the requirements bend to fit it.** That is why this is Move 5. A stack chosen before the
data model produces a model shaped by the tool.

**Trade-offs are stated as advantages.** "Chosen for scalability" is not a trade-off. The trade-off is what this choice is
*worse* at, and every choice is worse at something.

**Novelty is justified by future needs.** `07-strategy`'s far horizon is not a requirement. Choosing an unfamiliar
technology for a scale that does not exist is architecture inflation in the stack table.

**Reversibility is assumed to be high.** Data stores, authentication providers and public interfaces are the hard ones,
and they are usually chosen fastest.

**The boring option is rejected on grounds nobody writes down.** The rule is specifically that the reason must survive
being written. Most do not.

---

# Related

| | |
| --- | --- |
| `architecture/Architecture-Styles.md` | The shape chosen before the stack |
| `Backend.md`, `Frontend.md`, `Storage.md` | The layers |
| `Infrastructure.md`, `Hosting.md` | What running it costs |
| `06-business` | The cost ceiling every choice must respect |

---

> **Concept Note**
>
> Name the alternative, name what this is worse at, name what changing
> it would cost.
>
> If the reason for rejecting the boring option does not survive being
> written down, take the boring option.
