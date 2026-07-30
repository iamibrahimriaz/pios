---
Title: Free
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat free as a funded strategy, and remember the status quo is already free.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Pricing.md
Outputs:
  - Free-tier decision within pricing_strategy
Related Modules:
  - 11-growth
  - 14-ai-systems
Tags:
  - Business
  - Pricing
  - Concept
---

# Free

---

# What It Is

Two distinct things share the word, and conflating them is expensive.

**Free as the competition.** The status quo costs nothing. `06-business/knowledge/Pricing.md` requires the price
to be justified against it, and that is the hardest objection in the market. This is a fact to answer, not a
strategy.

**Free as a strategy.** Deliberately giving the product away, funded by something else:

| Funded by | Requires |
| --- | --- |
| A paid tier | A conversion mechanism that actually works — `Freemium.md` |
| An adjacent business | That business to exist and to benefit |
| Data | A use of the data the buyer will accept — usually disqualifying in regulated markets |
| Investor patience | Funding, and a plan for when it ends |
| Nothing | It is not a strategy; it is deferral |

Free is never costless to the operator. Every free user consumes infrastructure, support, and — for AI features —
inference cost per use.

---

# When It Applies

In Entry 3 (Price). The free anchor is mandatory; a free tier is optional and must be funded explicitly.

---

# How to Apply It Here

**Answer the free-incumbent question in writing.** Why does someone pay when what they do today costs zero? The
answer references value from Entry 2 and switching cost from `03-user`, and if the price exceeds value net of
switching cost, the model fails at this point.

**Cost a free tier per user before offering one.** For AI products this is decisive: a free user running inference
has a real marginal cost, and `14-ai-systems` requires cost per user to be stated. Free users with a positive
marginal cost and no conversion path are a subscription to a loss.

**Name the funding source explicitly.** If it is a paid tier, `Freemium.md`'s conversion discipline applies. If it
is investor money, say so and say for how long.

**Check data-funded models against the regime.** In regulated and professional markets, monetizing usage data is
frequently unacceptable to the buyer and sometimes unlawful. `02-market` Frame 2 and `09-technology` decide, not
this module.

**Consider free-for-a-segment instead of free-for-all.** A free tier for a segment that will never pay is
marketing with a cost attached; free for a segment that grows into paying is a channel.

---

# Where It Misleads

**Free is treated as an acquisition strategy without a conversion mechanism.** Users arrive, cost money, and stay
free. `11-growth` requires a loop that closes; a free tier with no upgrade trigger does not close.

**"Free" is confused with "no barrier".** Professional buyers are frequently more suspicious of free tools than of
paid ones — free implies no support obligation, no continuity commitment, and an unclear funding model. In
regulated work that is a reason to decline.

**The support cost of free users is omitted.** They ask questions, report problems and consume attention at
roughly the rate paying customers do. `13-operations` staffs for all of them.

**Free is used to avoid the pricing conversation.** Launching free defers the hardest question — will anyone pay —
and it defers it past the point where the answer could still change the product.

**Competing with the free status quo on price is attempted.** It cannot be won; zero is the floor. The competition
is on value net of switching cost, which is a different argument entirely.

---

# Related

| | |
| --- | --- |
| `Freemium.md` | Free with a conversion mechanism |
| `Trials.md` | Time-boxed free, with a decision at the end |
| `06-business` `Pricing.md` | The mandatory free anchor |
| `14-ai-systems` | Cost per user, which free does not remove |

---

> **Concept Note**
>
> The status quo is free, and answering it is compulsory.
>
> Offering free yourself is optional, costs real money per user, and
> is only a strategy once you can name who pays for it.
