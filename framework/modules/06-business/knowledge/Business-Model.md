---
Title: Business Model
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a business model must answer, starting with who signs.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/core/06-Framework.md
Outputs:
  - business_model
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Business
  - Model
  - Concept
---

# Business Model

---

# What It Is

The account of who pays, for what, how much, how often, and how they are reached — assembled in that order.

It begins with the payer, and the framework requires the payer to be established **separately from the user**.
Saying "the same person" is a required answer, not a reason to skip the question.

Where they differ, three separate conditions must all hold:

| | Question | Fails when |
| --- | --- | --- |
| **Willingness** | Do they want to pay? | The value is invisible to them |
| **Ability** | Can they afford it? | It exceeds the segment's software budget |
| **Authority** | Can they sign? | Approval sits with someone never consulted |

A product can fail on any one while the other two are fine. A user who wants it, in an organization that can
afford it, still needs someone with authority — and that person is usually the blocker `03-user` identified.

---

# When It Applies

In Entry 1 (Payer), and revisited in Entry 3 once the price exists — a price the payer cannot authorize is a
different model, not a pricing question.

---

# How to Apply It Here

**Name the payer, the user and the approver as three roles**, even when one person holds all three. That
structure is what makes the sale mappable, and it collapses cleanly when they coincide.

**Find the purchase trigger.** The event that makes them buy *now* rather than later: a renewal date, an audit,
a staff departure, a regulatory deadline, a budget cycle. Products without a trigger get agreed with and
deferred indefinitely — which is the most common way a good product dies quietly.

**Check ability against the segment's actual software budget**, not against the value. A practice with no
software line item is a harder sale than the arithmetic suggests, whatever the value at stake.

**Record who loses if this is bought.** In institutional settings a purchase can threaten a role, a
department's budget, or an existing supplier relationship. That opposition is real and rarely written down.

**Keep the model shape and the pricing model distinct.** Who pays and why is this file. Subscription versus
usage versus license is `Pricing.md` and the `pricing/` files.

---

# Where It Misleads

**Payer and user are assumed identical because in consumer software they usually are.** In professional and
institutional markets they usually are not, and the whole model turns on the difference. This is the module's
named failure.

**Willingness gets tested and authority does not.** Enthusiasm from the user is the easiest signal to gather
and does not survive contact with procurement. The sale stalls at a blocker nobody mapped.

**A model gets designed for the value rather than for the budget.** Value at stake sets the ceiling; the
budget sets what is actually available this year. Both constrain, and the smaller one wins.

**The trigger is assumed to be the problem.** The problem has existed for years without provoking a purchase.
Something else causes the decision, and finding it is worth more than another value argument.

---

# Related

| | |
| --- | --- |
| `ROI.md` | The case made to the payer |
| `Pricing.md` | What is charged, and against which anchors |
| `03-user` | Where the buyer and blocker are mapped |
| `07-strategy` | Where the model constrains scope |

---

> **Concept Note**
>
> Willingness, ability and authority are three conditions, and a
> product fails on any one of them alone.
>
> The user's enthusiasm is the cheapest of the three to collect and
> the least sufficient.
