---
Title: Common Mistakes
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in AI capability decisions and what each costs.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of AI-stage failure patterns
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Every mistake here shares one property: it makes an AI capability easier to adopt. That
is the direction the pressure runs, which is why this module's checks all run the other
way.

---

# 1. Capability Theater

**What it looks like.** An AI feature included because a product in this category is
expected to have one.

**Why it is tempting.** It is genuinely expected — by customers, by investors, by the
team. Not having it feels like falling behind.

**What it costs.** Build effort, inference cost, an evaluation burden, a new failure
surface, and a trust problem — all for a capability nobody's ranked problems required.

**Instead.** Trace it to a ranked problem. If there is none, it is an orphan by module
08's definition and should be recorded as rejected.

---

# 2. The Straw Man Alternative

**What it looks like.** "Alternative: manual entry. This is the problem we are solving."

**Why it is tempting.** The comparison is required, and a weak alternative satisfies the
requirement while confirming the conclusion.

**What it costs.** The gate's most important criterion becomes decorative. The comparison
proves nothing, and the capability proceeds having survived no test.

**Instead.** The advocate check. Write the alternative's case as its advocate would, in
one honest sentence. If you cannot, you do not understand it well enough to have rejected
it.

---

# 3. Autonomy Set by Accuracy

**What it looks like.** "At 95% accuracy, outputs are applied automatically."

**Why it is tempting.** Accuracy is the number you have, and a threshold on it feels
rigorous.

**What it costs.** It ignores the question that matters. If the user cannot detect the 5%,
their trust is calibrated to the 95% and the errors enter the record. The cost falls on
someone who had no way of knowing.

**Instead.** Ask whether the user can detect a wrong output. If not, the ceiling is drafts
regardless of the accuracy figure.

---

# 4. Data Availability Projected

**What it looks like.** "We will accumulate this data from usage."

**Why it is tempting.** It is probably true, eventually, and it keeps the capability on
the roadmap.

**What it costs.** The capability cannot be scheduled. It occupies a roadmap slot,
attracts design work, and blocks the sequencing conversation that would actually solve
it.

**Instead.** Confirm. Zero pairs today is a **blocker**, and treating it as one produces a
sequencing decision — in the worked example, delivering the service manually first, which
generated the data and solved the cold start at the same time.

---

# 5. Data Rights Assumed From an Existing Agreement

**What it looks like.** "We have a processing agreement, so we can use this for training."

**Why it is tempting.** An agreement exists and it covers the data.

**What it costs.** Consent for service delivery is not consent for model training. This is
a legal determination and getting it wrong is a regulatory event, not a product setback.

**Instead.** Treat it as a separate question with a named owner and a legal answer. And
check separately whether the provider's training on your data is **contracted** off, or
merely assumed.

---

# 6. Benchmarks as Accuracy Evidence

**What it looks like.** A published model score cited as evidence the capability will
work.

**Why it is tempting.** It is a real measurement, published, citable.

**What it costs.** Different task, different input distribution, different judge, and
often a different model version. It is evidence about something else, presented as
evidence about yours.

**Instead.** A golden set from real cases, judged by a domain expert, never used for
tuning. It is the only accuracy evidence about your task that exists.

---

# 7. The Golden Set of Clean Cases

**What it looks like.** Two hundred clear, well-formed, unambiguous examples.

**Why it is tempting.** They are the easiest to collect and they produce a good number.

**What it costs.** It measures performance on a population you do not serve. The real
inputs are noisy, accented, atypical and rushed, and the capability will meet them on day
one.

**Instead.** Stratify deliberately — include the hard cases, the unusual presentations,
the poor recordings. The purpose is to find where it fails, not to confirm where it
works.

---

# 8. Tuning Against the Golden Set

**What it looks like.** Iterating prompts until the golden set score improves.

**Why it is tempting.** It is the feedback loop that is available.

**What it costs.** The set then measures how well the capability was fitted to it, which
is not the same as how well it performs. The number stays high and stops meaning
anything.

**Instead.** Keep it sealed. Tune against a separate development set.

---

# 9. Generic Failure Modes

**What it looks like.** "The model may produce inaccurate output."

**Why it is tempting.** It is true, it covers everything, and it discharges the
requirement.

**What it costs.** It generates nothing. No guardrail can be built against a category,
so the output is a disclaimer where a mitigation belongs.

**Instead.** Specific enough to design against. "May invent a finding the patient did not
describe" produces three requirements; "may hallucinate" produces a paragraph in the terms
of service.

---

# 10. The Bar Set After the Result

**What it looks like.** "We will evaluate quality continuously and iterate."

**Why it is tempting.** It sounds like good practice and commits to nothing.

**What it costs.** The bar becomes whatever was achieved. Nobody ever concludes that a
capability they have built should not ship, unless they said so in advance.

**Instead.** Threshold, subset threshold, and what happens if missed — all before
building. "The capability does not ship; the service continues" is a sentence that has to
exist before there is a result to argue about.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Capability theater | Adopting under external pressure |
| Straw man | Satisfying a comparison requirement |
| Autonomy from accuracy | Using the number you have |
| Data projected | Keeping a capability alive |
| Rights assumed | Treating a legal question as technical |
| Benchmarks as evidence | Borrowing a measurement |
| Clean golden set | Measuring where it works |
| Tuning against the set | Using the only feedback available |
| Generic failure modes | Discharging a requirement |
| Bar set late | Avoiding a commitment that could fail |

All ten make adoption easier. Not one of them makes the capability better — which is what
distinguishes this module's failure profile from every other module in the framework.

---

> **Mistakes Principle**
>
> The pressure in this module runs one way, so every check in it runs the other.
>
> A capability that survives all ten has earned its place. Most do not, and that result
> is the module working rather than failing.
