---
Title: Business Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register the load-bearing economic assumption and the risks around who signs.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Mitigation.md
Outputs:
  - Business risks within risk_register
Related Modules:
  - 06-business
  - 11-growth
Tags:
  - Strategy
  - Risk
  - Concept
---

# Business Risks

---

# What It Is

The risks to the model — inherited from `06-business` and centered on the one input the verdict depends on.

| Risk | Early warning sign |
| --- | --- |
| **The load-bearing assumption is wrong** — usually CAC or churn | The first ten customers' actual acquisition cost |
| **The payer cannot authorize the purchase** | Deals stall after user enthusiasm, at a named approval step |
| **There is no purchase trigger** | Buyers agree, praise it, and do not proceed |
| **The price cannot be justified against free** | Discount requests in the first conversations |
| **The channel does not repeat** | Customers eleven onward cost far more than the first ten |
| **The sales cycle exceeds the runway** | Cycle length observed on the first two deals |
| **Cost to serve consumes the margin** | Per-user infrastructure or inference cost at real usage |

`06-business` names the load-bearing assumption during Entry 4. That name belongs at the top of this section, with the
figure at which the verdict changes.

---

# When It Applies

In Move 6 (Register). These are the risks the human checkpoint is really about, since they determine whether the
money works.

---

# How to Apply It Here

**State the load-bearing assumption with its breaking value.** "If CAC exceeds £900, payback passes 18 months and the
model requires funding." That is a monitored threshold rather than a worry.

**Register the authority risk separately from the willingness risk.** `06-business` separated willingness, ability and
authority for exactly this reason, and authority is the one that produces stalled deals with happy users.

**Watch customers eleven to twenty.** The first ten come through existing access and prove the problem, not the
channel. `11-growth`'s repeatable channel requirement is what this risk tests.

**Include the cost-to-serve risk with a figure.** For AI products, per-user operating cost against margin per user.
`09-technology` and `14-ai-systems` both check it, and this is where a failure becomes a business risk rather than a
technical one.

**Set the runway against the observed sales cycle, not the assumed one.** Two real deals give a better estimate than
any benchmark, and the comparison is arithmetic.

---

# Where It Misleads

**The load-bearing assumption is registered without its threshold.** "Churn may be higher than modeled" is not
monitorable. The threshold is what makes it a signal.

**Early acquisition cost is used as the baseline.** Founder-led sales through a warm network is the cheapest CAC the
business will ever see, and extrapolating it hides the risk entirely.

**Pricing risk is registered as a competitor comparison.** The harder risk is the free status quo, and `06-business`
requires the price justified against zero. That is where the objection actually comes from.

**The absent purchase trigger goes unregistered because nothing has failed yet.** Indefinite deferral is the quietest
way a product dies, and it produces no negative signal at all — only silence and polite interest.

**Financial and business risks are merged.** Runway, funding and cash timing are `Financial.md`. This file is about
whether the model's assumptions hold.

---

# Related

| | |
| --- | --- |
| `Financial.md` | Runway, cash and funding |
| `Market.md` | Risks from outside the model |
| `06-business` | Where the load-bearing assumption is named |
| `11-growth` | Where the channel must prove repeatable |

---

> **Concept Note**
>
> Register the assumption with the number at which the verdict
> changes.
>
> And watch customer eleven — the first ten proved the problem, not
> the business.
