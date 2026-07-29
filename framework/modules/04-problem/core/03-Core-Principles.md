---
Title: Core Principles
Module: 04-problem
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when validating problems.
Audience:
  - AI Agents
  - Researchers
  - Product Managers
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent problem judgment
Related Modules:
  - 07-strategy
Tags:
  - Problem
  - Principles
---

# Core Principles

---

# Principle Statement

> A problem is not real because it is plausible.
>
> It is real because someone is already paying for it — in time, money, risk,
> or effort spent working around it.

---

# Principle 1 — No Cost, No Problem

If nothing bad happens when a thing is never fixed, it is a preference.

Preferences are not worthless — they influence choice between comparable products. But
they do not justify building one, and ranking them alongside real costs dilutes the MVP.

Ask of every candidate: *what does it cost when this goes unsolved?*

---

# Principle 2 — Symptoms Point, They Do Not Locate

"The export takes four clicks" is a symptom. Ask why it matters and you find the missed
deadline underneath.

Building for the symptom produces an efficient solution to the wrong thing. Building for
the problem often produces a different product entirely — and usually a better one.

Ask "why does that matter?" until the answer stops changing.

---

# Principle 3 — Score the Workaround

Frequency and severity are the obvious dimensions. The workaround is the informative one.

A problem with a good workaround was already solved by the person who has it. Displacing
a working workaround is harder than solving something with no answer at all — and the
product must beat the workaround, not the raw problem.

---

# Principle 4 — Agreement Is Not Evidence

People will confirm almost any problem is real when asked directly. It is polite, it is
easy, and it costs nothing.

What costs something: building a workaround, buying a partial solution, hiring someone to
absorb the work, staying late. Look for those.

---

# Principle 5 — Only Top-Three Problems Get Budget

A problem can be genuinely real, widely acknowledged, and still never funded — because it
sits fourth on everyone's list.

The question is not "is this a problem?" It is "is this among the three things they most
want fixed?" Most research never asks the second question, which is why so much of it
produces polite interest and no sales.

---

# Principle 6 — Keep the Two Lists Apart

Validated and assumed problems must sit in structurally separate sections.

Careful tagging inside a shared narrative is not enough. A reader skimming a blended
section absorbs assumptions as findings — not because anyone lied, but because prose
flattens distinctions that structure preserves.

---

# Principle 7 — An Empty Validated List Is a Finding

If nothing can be verified, the correct response is to say so.

Promoting inferred problems to populate the section does not make the analysis stronger.
It makes it wrong in a way nobody downstream can detect.

An empty validated list changes the roadmap — validation becomes Milestone Zero. That is
the framework working, not failing.

---

# Principle 8 — Choose One

A ranked list with no choice made leaves module 07 with nothing to build strategy around,
and the MVP becomes everything scoring above average.

One problem. Defended against the scores. If the top scorer was passed over, that requires
more justification than choosing it would have.

---

# Principle 9 — A Test That Cannot Fail Proves Nothing

"Interview users about the problem" is not validation. No result could disprove anything.

Every test states what result would invalidate the assumption. If no such result exists,
the test is theater and should be replaced.

---

# Principle 10 — Define Failure Before You Need To

What result would mean this should not be built?

Teams almost never answer this in advance, and it is why doomed projects run for years —
by the time the evidence arrives, too much has been invested to read it honestly.

Write the stop condition while the thinking is still cheap.

---

# Principle 11 — Bad News Early Is the Product

The most valuable output this module can produce is often a clear statement that the
problem is not proven.

That finding costs a week. Discovering it after a build costs a year. A framework that
cannot deliver it is not doing its job.

---

# Principle Hierarchy

```
Cost exists
   ↓
Problem, not symptom
   ↓
Frequency and severity
   ↓
Workaround inadequate
   ↓
Evidenced, not assumed
   ↓
Top three for this person
```

A problem must clear every level. Most candidates fail at the first or the last.

---

# Common Violations

- Ranking preferences alongside costs.
- Optimizing a symptom because it is more concrete than the problem.
- Omitting the workaround dimension.
- Treating "yes, that's annoying" as validation.
- Blending validated and assumed problems in one narrative.
- Padding the validated list to reach a threshold.
- Producing a ranked list with no choice made.
- Writing a validation plan with no failure condition.
- Softening an `UNVALIDATED` verdict because it is unwelcome.

---

# Self Assessment

- Does every problem on my list cost someone something?
- Did I trace symptoms to their causes?
- Did I score workarounds honestly, or generously?
- Is my evidence behavior, or agreement?
- Are my two lists structurally separate?
- Did I choose one problem and defend it?
- Could any of my proposed tests fail?
- Did I write the verdict the evidence supports, or the one that was wanted?

---

> **Core Principle**
>
> Look for what someone already spent on this problem.
>
> Money and effort already committed are the only evidence that does not
> flatter the person asking.
