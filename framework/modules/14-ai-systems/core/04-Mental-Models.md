---
Title: Mental Models
Module: 14-ai-systems
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a proposed AI capability should be examined.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - 14-ai-systems/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of AI capabilities
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - ../constitution/core/04-Mental-Models.md
---

# Mental Models

---

# Model Statement

> A proposed AI capability always sounds impressive, which is a property
> of the proposal rather than the product.
>
> These lenses are ways of finding out which ones are worth building.

---

# 1. The Simpler Thing

**Reveals:** capability theater.

For each capability, describe the least clever thing that would mostly work. A sorted list. Eight
rules. A better form. Asking the sender for structured data.

Then compare honestly. The lens works because the simpler thing is usually cheaper, faster, more
reliable and easier to explain — and it is rarely written down beside the model version, which is the
only reason the model version wins.

**Hides:** "mostly works" is doing real work in that sentence. Sometimes the last 20% is the product.

---

# 2. The Advocate

**Reveals:** straw men.

Write one honest sentence in favor of the simpler alternative. If it cannot be written, the comparison
proved nothing.

This is `07-strategy`'s advocate test, and it fails the same way: not by producing a bad argument, but
by producing an argument nobody could make.

**Hides:** a good sentence can be written for almost anything. It filters decoration, not weak
reasoning.

---

# 3. The Data That Isn't There

**Reveals:** the most common pre-start failure.

Do not ask whether the data exists. Ask: where is it, how many records, sampled when, and by whom?

The difference between "we have consultation history" and "4,100 records in «source», sampled last
Tuesday" is the difference between a plan and a hope.

**Hides:** volume is not quality. Plenty of data can be plenty of the wrong data.

---

# 4. Day One

**Reveals:** cold-start failure.

Imagine the first user, on the first day, with no accumulated data. What does the capability do?

Most model-served features are at their worst exactly when the product is newest and users are least
forgiving — which is a design problem with a known answer, not an unavoidable dip.

**Hides:** it focuses on the product's first day. Each new *user's* first day has the same problem, and
that one never goes away.

---

# 5. The Wrongness Cost

**Reveals:** how much autonomy is justified.

What does one wrong output cost, who pays it, and can they tell?

The third question is the one that decides. It is also the one that gets skipped, because the answer is
often uncomfortable.

**Hides:** it treats errors as independent. Correlated errors — the same mistake across every record in
a batch — cost far more than the per-instance answer suggests.

---

# 6. The Fluent Error

**Reveals:** why accuracy is the wrong headline number.

Imagine the capability's output when it is wrong. Does it look different from when it is right?

If not, the error rate is not the risk. The risk is that every output arrives with the same confident
tone, and the user has no signal to sort them by.

**Hides:** nothing. It is the central fact about this class of component.

---

# 7. The Rushed User

**Reveals:** what happens to guardrails under real conditions.

Take the persona's real context from `03-user` — interrupted, behind schedule, doing this for the
fortieth time today. Now hand them a plausible wrong output with a confirmation dialog.

Do they catch it? A guardrail that depends on careful reading is a guardrail that works in the demo.

**Hides:** it can argue against all automation. The useful conclusion is usually a different guardrail,
not no capability.

---

# 8. The Bar Before the Build

**Reveals:** evaluation that will be shaped by its results.

Write the passing bar now, then ask what you would do if the capability came in just below it.

If the honest answer is "ship it and iterate", the bar was never a bar — and finding that out costs
nothing today and quite a lot later.

**Hides:** a bar set in ignorance can be wrong in either direction. It can be revised — the record just
has to show it was.

---

# 9. Who Is Qualified to Say

**Reveals:** evaluation by the wrong people.

Ask who will judge whether an output is correct, and what makes them able to.

In a domain product the answer must be a domain expert. A developer's confidence in a generated
clinical summary is evidence that it reads well, which is the exact property that makes a wrong one
dangerous.

**Hides:** experts disagree. Two reviewers and a documented disagreement rate is stronger than one
confident reviewer.

---

# 10. The Outage

**Reveals:** whether the fallback is real.

The provider is down for four hours. What does the user see, and what can they still do?

If the answer is "the feature is unavailable" and the feature was the core job, there is no fallback —
there is a dependency nobody registered.

**Hides:** it tests availability, not correctness. The more common failure is that the capability is up
and wrong.

---

# 11. The Deprecation Notice

**Reveals:** version exposure.

An email arrives: this model version retires in ninety days. What has to be re-evaluated, re-tuned,
re-tested?

Everything the answer names is work that was invisible when the capability was approved.

**Hides:** it looks like a reason to self-host. Usually the right conclusion is a pinned version, an
evaluation suite, and a fallback — not owning infrastructure.

---

# 12. The Share of the Bill

**Reveals:** whether the capability is affordable.

Cost per operation, times operations per user per month, against revenue per user.

The lens is decisive for the same reason the other arithmetic lenses in this framework are: the
numerator is a published price and the denominator is somebody else's decision, so there is nothing to
be persuasive about.

**Hides:** cost per operation falls over time. Check whether the plan depends on that, and say so if it
does.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking a capability is warranted | The Simpler Thing |
| Checking the comparison was honest | The Advocate |
| Checking feasibility | The Data That Isn't There |
| Checking early experience | Day One |
| Setting autonomy | The Wrongness Cost |
| Understanding the real risk | The Fluent Error |
| Testing guardrails | The Rushed User |
| Checking evaluation integrity | The Bar Before the Build |
| Checking the reviewer | Who Is Qualified to Say |
| Checking the fallback | The Outage |
| Checking version exposure | The Deprecation Notice |
| Checking affordability | The Share of the Bill |

Apply The Simpler Thing and The Advocate first — they decide what survives. Apply The Rushed User and
The Share of the Bill last, on what remains.

---

# Self Assessment

- What is the least clever thing that would mostly work?
- Can I argue for it in one sentence?
- Where exactly is the data, and who counted it?
- What happens on day one?
- What does one wrong output cost, and can the user tell?
- Does a wrong output look different from a right one?
- Would a rushed user catch it?
- What would I do if quality came in just below the bar?
- Who is qualified to judge, and is it them?
- What happens during a four-hour provider outage?
- What breaks when this model version retires?
- What share of revenue does this consume?

---

> **Mental Model Principle**
>
> The Fluent Error is the lens to keep if you keep one.
>
> Everything difficult about building on models follows from the fact
> that their mistakes and their successes are written in the same voice.
