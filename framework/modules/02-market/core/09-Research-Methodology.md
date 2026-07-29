---
Title: Research Methodology
Module: 02-market
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how market evidence is sourced, judged and recorded in this module.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - engine/evidence-policy.md
  - 02-market/core/06-Framework.md
Outputs:
  - Evidence-tagged claims
  - state.evidence_log entries
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - Research
  - Methodology
---

# Research Methodology

---

# Overview

This is the first module that does real research, and the first place a language model
can do serious damage — by producing a confident, specific, entirely invented market
figure.

The rules below exist to make that impossible to do accidentally.

---

# Methodology Statement

> A market figure with no visible derivation cannot be challenged.
>
> A number that cannot be challenged is not evidence. It is decoration.

---

# What Belongs Here

| Activity | Depth |
| --- | --- |
| Bounding the market | Until a borderline case can be ruled on |
| Regulatory research | Until concrete obligations are named, not just regimes |
| Sizing | Until every input is sourced or explicitly assumed |
| Trend research | At least three, including one unfavorable |
| Gap identification | Until each gap has a reason it persists |

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| Naming and comparing competitors | `05-competition` |
| Feature or pricing comparison tables | `05-competition` |
| Segment prioritization | `03-user` |
| Persona construction | `03-user` |
| Problem quantification | `04-problem` |
| Willingness-to-pay research | `06-business` |
| Compliance implementation detail | `09-technology` |

This module establishes the *container*. Later modules populate it.

Doing module 05's work here is the most common overreach — and it produces a worse
competitor analysis, because module 05 will have the segment and problem context that
this module does not.

---

# Source Hierarchy

Not all sources are equal. Judge them in this order:

| Tier | Source | Trust | Caution |
| --- | --- | --- | --- |
| 1 | Government or regulator statistics | Highest | May lag reality by years |
| 2 | Industry body / professional association data | High | May serve members' interests |
| 3 | Regulatory text itself | High for obligations | Interpretation is not the same as text |
| 4 | Audited public company filings | High | Only covers public players |
| 5 | Reputable analyst reports | Medium | **Check the boundary they measured** |
| 6 | Vendor pricing pages | High for price, low for market | Snapshot only — date it |
| 7 | Trade press | Medium | Often recycles a single analyst figure |
| 8 | Vendor marketing claims | Low | Treat as an assertion, not a fact |

**Tier 5 carries the trap.** An analyst TAM is measuring a boundary somebody else drew.
Before using one, check whether that boundary matches the one drawn in Frame 1. Usually
it does not.

---

# Sizing Discipline

## Show the derivation

Never write a figure alone.

```
❌  SAM: $180M

✅  SAM: $180M
    = 12,400 solo practices in «jurisdiction» [verified: «registry», 2025]
    × $1,450 realistic annual price [inferred: from competitor pricing, §3.3]
    ×  ~100% legally serviceable [verified: no licensing barrier identified]
```

The second version can be challenged. Someone can say "1,450 is too high" and the
conversation is productive. The first version can only be believed or disbelieved.

## Prefer bottom-up

Bottom-up sizing uses your own boundary. Top-down imports someone else's.

Where both are available, run both and compare. A material disagreement is a **finding**
to record, not a choice between numbers.

## Tag every input

A single unsourced input makes the whole figure an assumption — no matter how precise
the arithmetic looks. Tag at the input level, not just the result.

## Identify the load-bearing input

Which single input, if wrong, moves the figure most? Usually price or adoption rate, not
population. Name it — it becomes a validation priority in module 04.

---

# Regulatory Research

The output of this frame is consumed by `09-technology`, seven modules later, by someone
who will not re-read this analysis.

Write for that reader:

```
❌  "HIPAA applies."

✅  "HIPAA applies because the product stores identifiable patient health
     information [verified: 45 CFR §160.103].
     Requires: encryption at rest and in transit, access audit logging retained
     6 years, breach notification within 60 days, and a signed BAA with every
     subprocessor [verified: 45 CFR §164]."
```

The first is a label. The second is a specification.

---

# Trend Research

A trend needs three things: a **direction**, **evidence**, and an **implication**.

Two or more independent sources for any trend that a decision rests on. A single trade
article restating one analyst's projection is one source, not two.

**Search deliberately for the unfavorable trend.** It will not appear on its own —
searches phrased around an idea return material that supports it. Invert the query.

---

# When Retrieval Is Unavailable

An agent without retrieval cannot size a market from sources. State it, do not conceal it.

1. Build the sizing bottom-up from **stated** assumptions, showing the arithmetic.
2. Tag every input `[assumption: needs validation]`.
3. Set `state.run.confidence` to `low`.
4. Add the sizing to `state.open_questions` with what would settle it.
5. Say so in the Evidence Standing section.

```
[assumption: needs validation — no retrieval available; practice count
 estimated from population ratio, not from a registry]
```

A market analysis that shows its assumptions is workable. One that invents a citation
poisons every module downstream and destroys trust in the whole blueprint.

---

# Recording

| Destination | What |
| --- | --- |
| `state.evidence_log` | Every claim, its tag, its source, whether load-bearing |
| `state.assumptions` | Every unsourced input, with a validation method |
| `state.open_questions` | Anything that could not be established |
| Market Analysis §9 | Sources table — every `[verified]` must resolve here |

If a `[verified]` tag has no matching row in the Sources table, it is not verified.
Run that check before the gate.

---

# Self Assessment

- Does every figure show its derivation?
- Did I check the boundary of any external figure I adopted?
- Are my regulatory findings concrete obligations, or just regime names?
- Do I have a trend that argues against this idea?
- Does every `[verified]` resolve to a retrievable source?
- Did I identify which input the sizing most depends on?
- Have I stayed out of module 05's territory?

---

> **Research Principle**
>
> The most dangerous output of this module is a plausible number.
>
> Show the arithmetic, name the sources, and let the reader disagree with you.
