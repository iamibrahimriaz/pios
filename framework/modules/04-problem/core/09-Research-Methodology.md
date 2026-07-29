---
Title: Research Methodology
Module: 04-problem
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what counts as evidence that a problem is real, and how to establish it.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - engine/evidence-policy.md
  - 04-problem/core/06-Framework.md
Outputs:
  - Evidence-tagged problems
  - validation_plan
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Problem
  - Research
  - Validation
---

# Research Methodology

---

# Overview

This module's research question is unusually narrow and unusually consequential:

> What would make me believe this problem is real — and does that evidence exist?

Everything else in the module is scoring and organization. This is the part that decides
whether the blueprint rests on knowledge or on hope.

---

# Methodology Statement

> A problem is validated when someone other than the person proposing the product
> has demonstrated they experience it.
>
> Everything else is a hypothesis with good manners.

---

# The Evidence Ladder

Not all evidence that a problem exists is equal. From strongest to weakest:

| Rank | Evidence | Why it ranks there |
| --- | --- | --- |
| 1 | **Behavior costing them something** | They built a workaround, paid for a partial solution, or hired someone. Actions have a price; opinions do not |
| 2 | **Measured data** | Time studies, error rates, published research quantifying the cost |
| 3 | **Unprompted complaint** | They raised it without being asked — reviews, forums, support tickets |
| 4 | **Prompted complaint** | They agreed it was a problem when asked. Weak — people agree readily |
| 5 | **Expert assertion** | A practitioner or analyst says it is a problem |
| 6 | **Our own reasoning** | It seems like it would be painful |

**Ranks 1–3 can support a `[verified]` tag** when the source is retrievable.
**Ranks 4–6 cannot.** They are `[inferred]` or `[assumption]`.

The most common failure in this module is treating rank 4 as rank 1. People will agree
almost any problem is real when asked directly. Agreement is not evidence.

---

# Behavior Beats Opinion

The strongest available evidence is that someone spent something on this problem already.

Look for:

| Behavior | What it proves |
| --- | --- |
| A widely shared workaround | The problem is real and unsolved enough to warrant effort |
| A spreadsheet template circulating in a community | Same, with the shape of the need attached |
| A paid tool that partially solves it | Willingness to pay is established |
| Someone hired to do it manually | The cost exceeds a salary |
| A browser extension or script | Technical users cared enough to build |
| Recurring support tickets | The incumbent fails at it repeatedly |

Each of these is a person having voted with time or money. That is worth more than any
number of people saying "yes, that is annoying".

---

# Where Problem Evidence Lives

| Source | Evidence rank | What to extract |
| --- | --- | --- |
| Three-star product reviews | 3 | Specific, qualified complaints from daily users |
| Community forums | 1–3 | Workarounds, and how often they are shared |
| Support documentation | 3 | What users repeatedly fail at |
| Published studies | 2 | Quantified cost — hours, error rates, spend |
| Professional body surveys | 2 | Prevalence across the segment |
| Job postings | 1 | Roles hired specifically to absorb the problem |
| Competitor changelogs | 3 | What they keep fixing means what keeps breaking |
| Failed startups in the space | — | What they learned, at their expense |

**Competitor changelogs are underused.** A feature shipped repeatedly across releases
indicates a problem the vendor cannot solve structurally.

---

# Quantifying Cost

A problem without a cost is a preference. Establish the cost wherever possible.

| Cost type | How to establish |
| --- | --- |
| Time | Time studies, "I spend N hours" claims across multiple sources |
| Money | Salary of the person absorbing it, cost of the partial solution they buy |
| Risk | Regulatory penalties, error rates, published incident data |
| Wellbeing | Burnout surveys, attrition research, unpaid-hours reporting |

State the derivation, as in module 02. `"Costs about 90 minutes a day"` needs to show
where 90 came from.

Where cost cannot be established, say so — it becomes a validation task, and module 06
will need it for the value case.

---

# The Self-Selection Problem

Everyone who wrote something you can read chose to write it.

| Source | Who is over-represented | Who is missing |
| --- | --- | --- |
| Reviews | The annoyed and the delighted | Everyone content |
| Forums | The technically engaged | Everyone else |
| Studies | Whoever agreed to participate | Whoever declined |
| Support tickets | Those who report | Those who work around silently |

Tag accordingly, and name the absent group:

```
[inferred: from 22 forum threads describing manual re-entry —
 forum participants are technically engaged and may under-represent
 practitioners who accept the process as normal]
```

The silent majority in most markets finds the current workflow tolerable. They are the
hardest to convert and the easiest to forget.

---

# Distinguishing Real From Reported

Three checks that separate genuine problems from reported ones:

## The cost check

If it were never solved, what happens? If the honest answer is "nothing much", it is a
preference regardless of how often it is mentioned.

## The workaround check

If there is a good workaround, someone already solved this. The remaining problem is the
workaround's cost, not the original one — and that is a smaller problem than it first
appears.

## The top-three check

Would this person place this in their top three frustrations? People confirm almost any
problem is real. Only top-three problems get budget, attention, or a switch.

Proxy evidence rarely answers this directly. When it cannot, record it as a `NEEDS USER`
question rather than assuming the answer.

---

# Designing Validation That Can Fail

A validation plan is only real if some result would disprove the assumption.

| Weak | Strong |
| --- | --- |
| "Interview users about the problem" | "Interview 10 solo GPs. Ask how they handled their last three consultations' notes. If fewer than 6 describe after-hours work, the assumption is invalidated" |
| "Survey the market" | "Survey 100 practices: do you use any tool for X? If over 60% say yes and are satisfied, the gap is not real" |
| "Build an MVP and see" | "Landing page describing the outcome; if under 3% of 500 targeted visitors sign up, demand is unproven" |

Every test states: method, sample, effort, and **what result invalidates**.

Order by cheapest test of the most load-bearing belief. The cheapest test is often a
conversation; the most load-bearing belief is often willingness to pay, not existence of
the problem.

---

# When Retrieval Is Unavailable

Then nothing in this module can be validated, and the verdict is `UNVALIDATED`.

That is a legitimate, useful outcome. Handle it honestly:

1. Every problem goes in the assumed list.
2. The validated list is empty, and says so.
3. Verdict is `UNVALIDATED`.
4. Confidence is `low`.
5. The validation plan becomes the most important section in the document.
6. State plainly: **validate before building.**

Module 09 will convert this into a Milestone Zero. That is the framework working exactly
as intended — it has told the operator what to do first, and stopped them building on air.

---

# Recording

| Destination | What |
| --- | --- |
| `state.evidence_log` | Every problem claim, tag, source, evidence rank |
| `state.assumptions` | Every assumed problem, with its test |
| `state.open_questions` | Every `NEEDS USER` question |
| Analysis §11 | The validation plan |
| Analysis §14 | Honest evidence standing and confidence |

---

# Self Assessment

- Did I look for behavior, or only for opinion?
- Did I treat agreement as evidence?
- Does every `[verified]` problem rank 1–3 on the evidence ladder?
- Did I quantify cost, or assert it?
- Did I name who is missing from my sources?
- Does my validation plan contain a test that could fail?
- If the verdict is UNVALIDATED, did I say so plainly?

---

> **Research Principle**
>
> Look for what people already spent on this problem.
>
> Money and effort already committed are the only evidence that does not
> flatter the person asking.
