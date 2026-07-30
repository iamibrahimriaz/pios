---
Title: CAC
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define cost of acquisition honestly, including the founder's time, and treat it as an assumption.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Pricing.md
Outputs:
  - CAC within unit_economics
Related Modules:
  - 11-growth
Tags:
  - Business
  - CAC
  - Concept
---

# CAC

---

# What It Is

The fully loaded cost of acquiring one paying customer.

```
total cost of acquisition effort ÷ customers acquired = CAC
```

"Fully loaded" is the part that gets dropped. It includes:

| Include | Commonly omitted |
| --- | --- |
| Advertising and channel spend | — |
| Sales and marketing salaries | Frequently |
| **The founder's own time, at a real rate** | Almost always |
| Conference and travel costs | Sometimes |
| Onboarding and implementation effort to convert | Usually |
| Free-trial and freemium serving costs for non-converters | Usually |

Before launch, CAC is an assumption. It is also — with churn — one of the two inputs most likely to decide the
verdict, which is why it needs a sensitivity range rather than a figure.

---

# When It Applies

In Entry 4 (Economics), derived from the channel assumption in Entry 5 (Route). It is re-examined in
`11-growth`'s payback check from the opposite direction.

---

# How to Apply It Here

**Derive it from the route, not from a benchmark.** Contacts reachable per month through a named channel, the
cost of reaching them, and a conversion assumption. An industry-average CAC describes other people's channels.

**Cost the founder's time.** Founder-led sales feels free and is the largest real cost in most early businesses.
Excluding it produces a CAC that collapses the moment anyone is hired to do the same work — which is exactly when
the model is being relied upon.

**Include the cost of everyone who did not convert.** Trials served, demos given, pilots run. `pricing/Trials.md`
and `pricing/Freemium.md` cover the serving cost of non-converters, and in AI products it is not small.

**Give a range, not a point.** Low, expected and high, with the assumption behind each. A single CAC on a
pre-launch model is the false precision the framework's principle names.

**Compare it to the payback ceiling.** `margin per customer per month × acceptable payback months` gives the
maximum CAC the model can bear. If the derived CAC exceeds it, the finding is here, not in `11-growth`.

---

# Where It Misleads

**Early CAC is unrepresentatively low and gets treated as the baseline.** The first ten customers come from
personal networks, warm introductions and goodwill. That channel does not scale and its cost cannot be
extrapolated — the eleventh customer is a different business.

**Blended CAC hides the channel that does not work.** Averaging a cheap referral channel with expensive paid
acquisition produces a number that describes neither. `11-growth` requires per-channel figures.

**Long sales cycles are ignored in the cost.** Nine months of contact with a buyer is nine months of someone's
time. In institutional markets the cycle length is a larger CAC driver than any media spend, and
`03-user`'s procurement findings predict it.

**CAC is assumed to fall with scale.** Sometimes it does; often it rises, as the easily reached segment is
exhausted and acquisition moves to colder audiences. Assuming improvement without a mechanism is
`11-growth`'s borrowed growth in cost form.

**It gets quietly reduced to make the LTV:CAC ratio pass.** That is the load-bearing assumption being adjusted to
produce the verdict, and `Financial-Risks.md` exists to catch it.

---

# Related

| | |
| --- | --- |
| `LTV.md` | The other half of the ratio |
| `Customer-Acquisition.md` | The route CAC is derived from |
| `Financial-Risks.md` | Sensitivity, where CAC usually decides |
| `11-growth` | Where the payback check runs from the other side |

---

> **Concept Note**
>
> Cost the founder's time, or the model breaks on the first hire.
>
> And never extrapolate from the first ten customers — they came from
> a channel that does not exist at scale.
