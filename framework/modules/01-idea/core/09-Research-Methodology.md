---
Title: Research Methodology
Module: 01-idea
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what research is and is not appropriate at the idea stage, and how to conduct it honestly.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - engine/evidence-policy.md
  - 01-idea/core/06-Framework.md
Outputs:
  - Evidence-tagged claims in the idea brief
  - Entries in state.evidence_log
Related Modules:
  - 02-market
  - 05-competition
Tags:
  - Idea
  - Research
  - Methodology
---

# Research Methodology

---

# Overview

Module 01 is the lightest research module in Product Intelligence OS, and that is
deliberate.

The purpose here is not to establish facts. It is to establish **what needs
establishing**. Deep research happens in modules 02 through 05, once the idea is precise
enough to research without waste.

The most common failure at this stage is doing module 02's job badly, early, and calling
it done.

---

# Methodology Statement

> Research at the idea stage answers one question: is this idea specific enough
> that researching it would not be a waste of effort?

---

# What Belongs Here

| Activity | Why |
| --- | --- |
| **Existence check** | Does something like this already exist? A five-minute look prevents a five-module run researching a solved problem |
| **Terminology check** | What is this called by people who work in the domain? Wrong vocabulary produces wrong search results in every later module |
| **Obvious-blocker check** | Is there a regulatory, technical or structural reason this cannot exist? |
| **Framing check** | Has this problem been written about? By whom, and how do they frame it? |

Each is shallow by design. Timebox them.

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| Market sizing | `02-market` |
| Trend analysis | `02-market` |
| Regulatory deep-dive | `02-market` |
| Segment analysis | `03-user` |
| Persona construction | `03-user` |
| Problem quantification | `04-problem` |
| Competitor matrix | `05-competition` |
| Pricing research | `06-business` |

Doing this work now is not thoroughness. It is researching a target that has not stopped
moving — and it will need redoing after the human checkpoint changes the framing.

---

# The Existence Check

The single highest-value activity in this module.

1. Search using the operator's vocabulary.
2. Search again using the domain's vocabulary, if it differs.
3. Look for: direct products, adjacent products, open-source projects, and features
   inside larger platforms.
4. Record what is found — but do **not** build a competitor matrix. That is
   `05-competition`.

| Result | What it means | Action |
| --- | --- | --- |
| Nothing found | Either a genuine gap, or wrong vocabulary | Search again with domain terms before concluding |
| Many similar products | The problem is real and served | Note it; the differentiation question moves to `05-competition` |
| One dominant product | The market may be closed, or ripe for unbundling | Flag for `05-competition` |
| Exists but abandoned | Something killed it | **High-value finding.** Record it and find out what |

> An abandoned competitor is the cheapest lesson available in a product run.
> Somebody already paid for that experiment. Find out what it taught them.

---

# The Terminology Check

Domains have their own language. Researching a clinical product using consumer software
vocabulary returns nothing useful, and the agent concludes there is no market.

Record:

| | |
| --- | --- |
| Operator's terms | «their words» |
| Domain's terms | «what practitioners call it» |
| Standards or protocols named | «if any» |
| Regulatory vocabulary | «the terms the regime uses» |

This vocabulary carries forward and improves every later module's research quality.

---

# Evidence Discipline

Everything in this module follows `engine/evidence-policy.md`. Two rules matter most here:

**Most claims will be assumptions, and that is correct.** A module 01 brief with many
`[verified]` tags is suspicious — there has not been time to verify much, and the likely
explanation is invented sources.

**A shallow check produces a shallow tag.** "I searched and found three similar products"
is `[verified: search conducted <date>, products X, Y, Z]`. It is not
`[verified: the market is competitive]` — that is a conclusion, and it is module 05's to
draw.

---

# When Research Is Not Possible

If the agent has no retrieval capability, the existence check cannot be performed.

State that plainly:

```
[assumption: needs validation — no retrieval available;
 existence of competing products not checked]
```

Then add it to `state.open_questions` as a task for module 05, and continue. An honest
gap is workable. A fabricated finding is not.

---

# Recording Findings

Findings go to two places:

| Destination | What |
| --- | --- |
| `state.evidence_log` | Each claim, its tag, its source, and whether it is load-bearing |
| `idea_brief` | Only what changes the framing of the idea |

Do not put everything found into the brief. The brief is a framing document, not a
research dump. A finding that does not change how the idea is understood belongs in the
evidence log and nowhere else.

---

# Timeboxing

| Check | Depth |
| --- | --- |
| Existence | Enough to know whether this is a solved problem |
| Terminology | Enough to search competently in module 02 |
| Blockers | Enough to know if a hard stop exists |
| Framing | Enough to know how the domain thinks about this |

If the research at this stage is producing a document rather than a sharper question,
it has gone too far. Stop and hand off.

---

# Self Assessment

- Did I check whether this already exists?
- Did I search using the domain's vocabulary, not just the operator's?
- Did I find any abandoned attempt, and if so, do I know why it failed?
- Have I avoided doing module 02–05's work?
- Is every claim tagged at the depth it was actually established?
- Have I recorded what I could not check, rather than filling the gap?

---

> **Research Principle**
>
> The purpose of research at this stage is not to answer the question.
>
> It is to make sure the question is worth the cost of answering.
