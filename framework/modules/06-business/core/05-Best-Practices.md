---
Title: Best Practices
Module: 06-business
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced operators do when modeling a business that inexperienced ones do not.
Audience:
  - AI Agents
  - Founders
  - Researchers
Prerequisites:
  - 06-business/core/06-Framework.md
Outputs:
  - Higher-quality business evidence
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Best Practices
---

# Best Practices

---

# 1. Find the Segment's Software Budget First

Before modeling anything, establish what this segment spends on software at all.

Professional body surveys, industry benchmark reports, and the low end of competitor
pricing all give it. A price that exceeds the segment's entire annual tool budget is a
contradiction, and it is cheaper to find here than in a sales meeting.

---

# 2. Write the Price Justification Before the Price

State the reasoning — value delivered, switching cost, competitor range, the free anchor —
and let the number fall out of it.

Writing the number first means the justification is assembled to reach it, and it always
can be.

---

# 3. Answer the Free Question Explicitly

Give it its own line: *why does someone pay «figure» when what they do today costs nothing?*

An answer that references value net of switching cost is a real answer. "Because our
product is better" is not.

---

# 4. Build Cost to Serve From Published Prices

Cloud pricing, API pricing and support-time estimates are all public or derivable.

A margin built from four published prices is `[inferred]` and defensible. A margin quoted
as a SaaS convention is `[assumption]` wearing a suit.

---

# 5. Model the AI Cost Per User Per Month

If the product uses per-operation AI, compute what it costs for one active customer over
one month.

Compare that against the monthly price. When it consumes a meaningful share of revenue,
that is a structural finding — and it has ended products whose engagement grew faster than
their pricing.

---

# 6. Solve Backwards, and Say So

When CAC cannot be estimated, compute what CAC the model tolerates.

Write it as a budget: "acquisition must stay below «figure» for this to work". Module 11
can act on that. A guessed CAC gives them nothing.

---

# 7. Vary the Two Unknowables

Build the sensitivity table around CAC and churn, because those are the two inputs no
research can settle.

If the verdict flips inside a plausible range, the verdict is `INSUFFICIENT EVIDENCE`,
however good the midpoint looks.

---

# 8. Name Ten Customers, Not Three Channels

Write ten rows. Real organizations where possible; otherwise profiles specific enough to
go and find — "practices that posted in «forum» about «problem» in the last year".

If ten cannot be produced, write that. An honest blank is a finding; a channel list
disguising the blank is not.

---

# 9. Check the Price Against the Sales Motion

A $30/month product that needs a demo call to close does not work. Neither does a
$50,000 product sold through a signup form.

Match them, or change one.

---

# 10. Compare the Sales Cycle to the Runway

A nine-month cycle and twelve months of money means one attempt.

That belongs in the risk register with a mitigation, not in a schedule.

---

# 11. Separate Benchmarks From Claims

```
Churn 20%/yr [assumption: needs validation — SMB SaaS benchmarks range
 15–30% [verified: «source»]; no product-specific basis exists]
```

The benchmark is verified and the application is assumed. Writing both makes the tag
honest and still uses the evidence.

---

# 12. Hand the Cost-to-Serve Budget Forward

Write it into state explicitly for module 09.

An architecture designed without a per-customer budget will be technically excellent and
commercially wrong, and nobody discovers it until the infrastructure bill arrives.

---

# 13. Count Your Tags Before Setting Confidence

Count sourced, inferred and assumed inputs. If assumed is the majority, confidence is
`low` — regardless of how complete the model looks.

Completeness and confidence are different properties, and this module makes them easy to
confuse.

---

# 14. Say Which Threshold Fails First

More useful than the verdict itself. It tells the operator what to watch after launch, and
what would change the answer.

---

# 15. Write the Unfavorable Verdict Plainly

If the model does not work at any price the segment would pay, say so in section 1, in
plain words, without cushioning.

That sentence is the most valuable output this module can produce, and burying it in
section 9 is how it gets missed.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Price chosen, then justified | The justification is always findable |
| Standard margin assumed | Ignores real cost to serve |
| CAC and churn given single values | The two unknowables presented as known |
| Point estimate on assumed inputs | False precision |
| Benchmarks cited as product facts | Evidence about somebody else |
| Channels instead of customers | No route to first revenue |
| Cost-to-serve constraint not handed forward | Margin lost in module 09 |
| Confidence set by completeness | A full model of guesses is still guesses |

---

# Self Assessment

- Do I know what this segment spends on software at all?
- Did the justification come before the number?
- Did I answer the free question in its own line?
- Is my margin built from published prices?
- Did I model AI cost per user per month?
- Did I declare anything I solved backwards?
- Does my sensitivity vary CAC and churn?
- Can I hand over ten names?
- Did I count my tags before setting confidence?

---

> **Practice Principle**
>
> The most useful business model is not the one that shows the business works.
>
> It is the one that shows exactly which belief the business is resting on.
