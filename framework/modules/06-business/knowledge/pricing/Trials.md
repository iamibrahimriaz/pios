---
Title: Trials
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Size a trial to the job's frequency so it produces a decision rather than a lapse.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/pricing/Free.md
Outputs:
  - Trial terms within pricing_strategy
Related Modules:
  - 03-user
  - 11-growth
Tags:
  - Business
  - Pricing
  - Concept
---

# Trials

---

# What It Is

Time-boxed free access, ending in a decision.

The distinguishing property against freemium is exactly that ending: a trial forces a choice, a free tier
postpones one indefinitely. For most professional products that makes trials the better instrument.

The length is not a convention — it is derived:

```
trial length ≥ time for the job to occur enough times to form a judgment
```

| Job frequency | Trial that works |
| --- | --- |
| Several times daily | Days — a week is generous |
| Weekly | A month, so the judgment covers four occurrences |
| Monthly or per-episode | A single cycle is not enough; consider a guided pilot instead |

A fourteen-day trial of a monthly job tests nothing, and the user's non-conversion carries no information.

---

# When It Applies

In Entry 3 (Price), and it interacts with `GTM.md` — a trial is a self-serve instrument, and an institutional
buyer usually needs a pilot with an owner instead.

---

# How to Apply It Here

**Derive the length from `03-user`'s observed frequency.** This is the single most consequential trial decision
and it is usually made by convention instead.

**Require the trial to reach real value, not just real access.** If setup takes a week and the trial is two, the
user gets one week of product. Onboarding effort is part of the trial length.

**Decide the credit-card question against the buyer.** Requiring payment details up front reduces volume and
raises conversion quality; for institutional buyers it may block the trial entirely, since it implies a purchase
decision has already been made.

**Say what happens to their data at the end.** A trial that deletes real work is a trust failure; one that holds
it hostage is a different one. `09-technology` needs the retention rule either way.

**Cost the trial population.** Non-converting trial users consume infrastructure, inference and support.
`CAC.md` requires that cost included — it is part of acquisition, not overhead.

---

# Where It Misleads

**Trial length is copied from other products with different job frequencies.** The fourteen-day convention comes
from daily-use consumer software. Applied to a monthly professional job it guarantees an uninformative result.

**Non-conversion is read as rejection.** A user who never reached the value — because setup was incomplete, or
the job did not arise — has not evaluated anything. Conversion analysis has to separate the two, and most does
not.

**Trials substitute for validation.** A trial measures whether this build converts; it cannot establish whether
the problem was real. `04-problem`'s methods do that, and a trial run in place of them answers a narrower question
at higher cost.

**Extensions are granted routinely, which removes the deadline.** The deadline is the mechanism. An indefinitely
extended trial is freemium without the funding decision.

**Institutional trials are run without an owner.** A pilot with no named person responsible produces no decision
at the end, only a lapse — and `13-operations`' "the team is not an owner" rule applies here too.

---

# Related

| | |
| --- | --- |
| `Freemium.md` | The alternative that never forces a decision |
| `Free.md` | Free as strategy, and its funding |
| `03-user` | Where job frequency is observed |
| `CAC.md` | Where non-converters are costed |

---

> **Concept Note**
>
> Set the trial by how often the job happens, not by what other
> products do.
>
> Fourteen days for a monthly job tests nothing, and the
> non-conversion tells you nothing either.
