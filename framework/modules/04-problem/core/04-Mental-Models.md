---
Title: Mental Models
Module: 04-problem
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which candidate problems should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 04-problem/core/03-Core-Principles.md
Outputs:
  - Multi-perspective problem analysis
Related Modules:
  - 07-strategy
Tags:
  - Problem
  - Mental Models
---

# Mental Models

---

# Model Statement

> A problem looks real from the inside of an idea.
>
> These models are ways of standing outside it.

---

# 1. The Cost Test

**Reveals:** whether a candidate is a problem at all.

If it is never solved, what happens? Name the cost in time, money, risk, or wellbeing.

"Nothing much" is a complete answer, and it means the candidate is a preference.

**Hides:** costs that are absorbed without being noticed. Someone who has done notes at
home every evening for ten years may not describe it as a cost — it is simply the job.
Look for costs the person has normalized.

---

# 2. The Five Whys

**Reveals:** whether you are looking at a problem or its shadow.

```
"Export takes four clicks"
  why does that matter? → "I do it forty times a week"
  why does that matter? → "It eats my Friday afternoon"
  why does that matter? → "I miss my accountant's deadline"
  why does that matter? → "I pay late-filing penalties"
```

The problem is the penalty, not the clicks. A product built for the fourth answer looks
different from one built for the first.

**Hides:** the chain can be followed too far, arriving at "because the industry works this
way" — true, unactionable, and not a product. Stop where the answer stops being something
anyone could change.

---

# 3. The Workaround Lens

**Reveals:** whether the problem is already solved.

Every unsolved problem that hurts enough produces a workaround. Find it, then evaluate it.

| Workaround state | What it means |
| --- | --- |
| Good, widely used | Somebody solved this. The remaining problem is the workaround's cost |
| Poor, widely used | Strong signal — real pain, no adequate answer |
| None, and it hurts | Very valuable, or structurally impossible |
| None, and nobody minds | Not painful enough to be a product |

**Hides:** a workaround's true cost is often invisible to the person using it. Habituation
makes an eleven-step process feel like one step.

---

# 4. Frequency × Severity

**Reveals:** that two very different problems can score the same.

| | High frequency | Low frequency |
| --- | --- | --- |
| **High severity** | Urgent — build for this | Insurance — hard to sell, real when it hits |
| **Low severity** | Erosion — felt constantly, rarely prioritized | Ignore |

Rare-and-catastrophic and constant-and-minor are both real problems, but they need
completely different products, pricing, and messaging.

**Hides:** the multiplication flattens the distinction. Always look at the two numbers as
well as the product of them.

---

# 5. Top Three

**Reveals:** whether the problem will ever get budget.

People confirm almost any problem is real. Far fewer will place it among the three things
they most want fixed.

Everything below third place gets acknowledged, agreed with, and never funded.

**Hides:** the top three is contextual and changes with the season, the quarter, and the
last thing that went wrong. A problem outside the top three today may enter it after a
regulatory change or an incident.

---

# 6. Behavior Over Opinion

**Reveals:** which evidence to trust.

| Opinion | Behavior |
| --- | --- |
| "That would be useful" | Built a spreadsheet to do it |
| "Price is the issue" | Switched for convenience |
| "We'd definitely use that" | Never opened the trial |

Behavior has a price attached. Opinion does not, which is why it is freely given.

**Hides:** behavior only reveals choices within available options. It cannot show demand
for something that has never existed — which is why genuinely new categories look
unwanted in behavioral data.

---

# 7. The Absorbed Cost

**Reveals:** problems nobody complains about.

Some costs are invisible because they have been normalized: unpaid overtime, a role that
exists only to absorb a process failure, a step everyone assumes is inherent.

These are frequently the largest problems and the least reported, because complaining
requires first noticing.

Look for: roles that exist to work around a system, "that's just how it is" statements,
and time spent outside working hours.

**Hides:** an absorbed cost is hard to sell against precisely because it is not felt. The
problem may be real and the sale still difficult — module 06 needs to know that.

---

# 8. Who Bears It

**Reveals:** whether the sufferer is the payer.

| Bearer | Implication |
| --- | --- |
| The user | Simplest case — they feel it and may buy |
| Their employer | The user feels it; someone else must be convinced |
| Their customer | Neither party may prioritize fixing it |
| Nobody, yet | A future or regulatory problem |

A problem borne by one party and paid for by another is a harder sale than its severity
suggests.

**Hides:** it says nothing about who has authority to buy — that comes from `03-user`'s
buyer/blocker mapping.

---

# 9. The Graveyard

**Reveals:** what has already been learned at someone else's expense.

If a problem is obvious and valuable, someone has probably tried. Find them: shutdown
notices, dormant projects, acquisitions that quietly disappeared, forum threads about
tools that no longer exist.

What killed them is usually not "bad execution". It is a structural fact about the
problem — the buyers would not pay, the workaround was good enough, the sale required
a committee.

**Hides:** survivorship works both ways. A failed attempt may have been genuinely badly
executed, or too early. Find the reason before concluding.

---

# 10. The Falsification Frame

**Reveals:** whether the analysis can be wrong.

Ask: **what would I expect to see if this problem were not real?**

Then check whether you are seeing it. Common signals: everyone agrees but nobody has built
a workaround; complaints exist but nobody has switched tools; the problem is mentioned
only when prompted.

**Hides:** nothing. It is the correction for every other model here, and the one most often
skipped because the answer is unwelcome.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Deciding whether it is a problem at all | The Cost Test |
| Finding the real problem under a complaint | The Five Whys |
| Judging urgency | The Workaround Lens |
| Understanding what kind of problem it is | Frequency × Severity |
| Predicting whether it gets funded | Top Three |
| Weighing evidence | Behavior Over Opinion |
| Finding unreported problems | The Absorbed Cost |
| Anticipating the sale | Who Bears It |
| Learning cheaply | The Graveyard |
| Checking yourself | The Falsification Frame |

Apply The Cost Test first — it removes most candidates. Apply The Falsification Frame
last, to whatever survived.

---

# Self Assessment

- Did I name the cost of every problem I kept?
- Did I follow the why-chain past the first concrete answer?
- Did I find and evaluate the workaround?
- Did I look at frequency and severity separately, not just the product?
- Would this problem be in their top three?
- Is my evidence behavior, or opinion?
- Did I look for problems nobody complains about?
- Did I check the graveyard?
- What would I see if this problem were not real — and am I seeing it?

---

> **Mental Model Principle**
>
> An idea makes its own problem look real.
>
> These models exist to give you somewhere to stand that is outside the idea.
