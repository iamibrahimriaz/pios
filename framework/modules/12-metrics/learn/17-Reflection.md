---
Title: Reflection
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Prompt a learner to examine what their metrics will cause people to do.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/learn/16-Evaluation.md
Outputs:
  - Examined assumptions about your own measurement habits
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Reflection
  - Learn
---

# Reflection

---

# Overview

You have written an instruction that will outlast its reasons. These questions are about
what it instructs.

---

# On the North Star

**Why this one?** Write the reason down now, because in two quarters nobody will
remember and the metric will still be there.

**What does it not capture?** Every metric has a blind spot. Naming yours tells you which
guardrail you need.

**Who benefits when it goes up?** Sometimes the answer is the user, sometimes the
business, sometimes only the dashboard. All three are worth knowing.

---

# On the Definitions

**Where did you leave something implicit?** There is usually one — the window, or who is
excluded.

**Would you compute this the same way in six months?** If not, the definition is not
finished; it is a convention you currently remember.

**What happens to late-arriving data?** A small question that produces persistent
disagreement about historical numbers.

---

# On Gaming

**How would you move your north star dishonestly?** Then ask how you would move it
*honestly but thoughtlessly*, which is the version that actually happens.

**Is the gamed behavior something you would tolerate?** If yes, the metric is well chosen.
If no, you have a guardrail to write.

**Who will be measured on this?** A metric applied to a person behaves differently from
one applied to a product. The same number becomes an incentive.

---

# On What You Are Not Measuring

**What would you notice only by accident?** Usually quality, and usually because quality
is expensive to instrument and easy to assume.

**What would tell you the product is being used badly?** Most metric sets can distinguish
usage from non-usage and nothing else.

**Which of module 09's failure modes has no signal?** Module 13 will need those signals
for its alerts, and a failure mode with no signal is one nobody will detect.

---

# On the Instrumentation

**Which property carries something it should not?** Check. Free text is the usual
offender, and it usually arrived to make debugging easier.

**Where does this data go, and who else can read it?** An analytics vendor is a data
processor, and the question is contractual rather than technical.

---

# On Your Own Pattern

| Look for | What it suggests |
| --- | --- |
| Your dashboards are all lagging | You report rather than steer |
| Your metrics rise steadily | Some of them are cumulative |
| You have never rejected a metric for being gameable | The gaming question is not yet live |
| Your definitions are one line | You have not met the two-analysts problem |
| Quality is unmeasured | It is being assumed, which is how it degrades unnoticed |

---

# The Question Worth Returning To

> If a team optimized only this number for a year, what would the product look like?

Picture it in detail. This question predicts more about the next year than any amount of
reasoning about what the metric means, because it describes what will actually happen
rather than what was intended.

If the picture is unappealing, the metric is wrong — however well it captures the concept
you had in mind.

---

> **Reflection Principle**
>
> Nobody games a metric maliciously. They are told a number matters and they move it.
>
> Which means the responsibility for the resulting behavior sits with whoever chose the
> number, not with whoever moved it.
