---
Title: Automation
Module: 14-ai-systems
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Set the autonomy level from the wrongness cost, with detectability as the deciding question.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/AI-Use-Cases.md
Outputs:
  - Autonomy levels and oversight
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - AI
  - Autonomy
  - Method
---

# Automation

---

# What It Is

How much the model is allowed to do — decided by the cost of being wrong, not by how accurate it is.

| Level | The model | The user |
| --- | --- | --- |
| **Suggests** | Offers an option | Chooses |
| **Drafts** | Produces something | Edits and approves |
| **Acts with confirmation** | Proposes an action | Confirms |
| **Acts autonomously** | Does it | Finds out afterwards |

Three questions decide the level, and the third is the one usually skipped:

| Question | |
| --- | --- |
| What does one wrong output cost? | In the user's terms |
| Who bears that cost? | The user, the operator, or a third party |
| **Can the user detect it is wrong?** | This is the decisive one |

> Where the user bears the cost and cannot detect the error, autonomy above "suggests" is not permitted without a mechanism that makes the
> error visible.

> **Detectability governs autonomy more than accuracy does.** A capability that is right 99% of the time, whose 1% is undetectable and
> consequential, is more dangerous than one that is right 90% of the time and visibly wrong the rest.

---

# When It Applies

In Move 4 (Bound), after the capability has survived comparison and grounding.

---

# How to Apply It Here

**Answer the three questions in writing, per capability.** The answers are short and they determine the level without argument.

**Design the visibility mechanism where autonomy exceeds suggestion.** Showing the source, highlighting uncertain spans, requiring a specific
confirmation. `10-execution/knowledge/Interaction.md` builds it, and it is an interaction design rather than a model property.

**Name who reviews, and require domain expertise.** In a domain product, quality review requires a domain expert. The build team cannot assess
clinical, legal or financial correctness, and their confidence in an output is not evidence about it — the same reason `03-user` forbids
inventing user quotes.

**Record whether overrides are captured.** An override is the strongest signal the capability is wrong, and it is free to collect —
`12-metrics` can define it as a leading indicator.

**Check disclosure obligations.** Whether AI involvement must be disclosed is a regime question from `02-market` Frame 2, not a product
preference.

---

# Where It Misleads

**Accuracy is used to justify autonomy.** It is the wrong axis. An undetectable error at low frequency is worse than a visible one at high
frequency, because nobody catches it.

**Full autonomy is treated as the goal state.** For judgment work with undetectable errors it is not a later phase — it is the wrong
destination. `07-strategy/knowledge/solutions/Automation.md` makes the same point about automation generally.

**Accountability is removed along with the work.** In regulated work someone signs. Automation that removes the review without removing the
accountability creates exposure for the user, which means for the product.

**Acceptance is made frictionless.** One-click acceptance of an unverified output is exactly the case where detectability governs, and the
friction should be proportional to the cost of silent acceptance.

**Trust is assumed to arrive with accuracy.** Professional users grant autonomy gradually and withdraw it instantly after one bad outcome —
which `13-operations` then handles as an incident.

---

# Related

| | |
| --- | --- |
| `AI-Risks.md` | The plausibility problem behind detectability |
| `Evaluation.md` | The bar before users see it |
| `10-execution` `Interaction.md` | Where the visibility mechanism is designed |
| `07-strategy` `solutions/Automation.md` | Automation as a strategy decision |

---

> **Concept Note**
>
> Can the user tell it is wrong? That answer sets the ceiling.
>
> 99% accurate with an undetectable, consequential 1% is more dangerous
> than 90% accurate and visibly wrong.
