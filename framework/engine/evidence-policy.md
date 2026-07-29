---
Title: Evidence Policy
Layer: Engine
Version: 1.0.0
Status: Approved
Purpose: Define how claims are sourced, tagged and trusted across every module.
Binding: Mandatory. No module output is valid without compliant tagging.
---

# Evidence Policy

This is the most important rule in Product Intelligence OS.

A blueprint nobody can trust is worth less than no blueprint at all. A language model will
state a market size, a competitor's price, or a regulatory requirement with the same
confidence whether it looked it up or invented it. The framework's job is to make that
difference visible on the page.

---

# The Three Tags

Every factual claim in every module output carries exactly one tag.

## `[verified: <source>]`

The claim was checked against a named, retrievable source.

```
The global EMR market was valued at USD 29.8B in 2023 [verified: Grand View Research, 2024].
```

A source is only a source if a reader can go and find it. "Industry reports" is not a source.

## `[inferred: <basis>]`

The claim follows by reasoning from something verified. State what it follows from.

```
Solo practitioners likely represent under 15% of licensed spend
[inferred: from clinic-size distribution in the AMA 2023 census].
```

## `[assumption: needs validation]`

The claim is a belief. It may be a reasonable belief. It is not knowledge.

```
Doctors will accept a 20-second review step for AI-generated notes
[assumption: needs validation — see validation_plan].
```

---

# The Prohibition

**An assumption must never be smoothed into a fact.**

This is the single failure mode that destroys the framework's value. It usually happens
through language, not through intent:

| Prohibited | Required |
| --- | --- |
| "The market is growing at 12% annually." | "...growing at 12% annually [verified: &lt;source&gt;]." |
| "Doctors want faster charting." | "Doctors want faster charting [assumption: needs validation]." |
| "Competitors charge around $99/month." | "Practice Fusion lists $99/user/month [verified: vendor pricing page, accessed &lt;date&gt;]." |

Hedging words are not tags. "Likely", "generally", "typically" and "studies show" do not
satisfy this policy. Tag it or delete it.

---

# When Research Is Not Possible

An agent without retrieval cannot verify. That is an acceptable state — concealing it is not.

If a claim cannot be verified:

1. Tag it `[assumption: needs validation]`.
2. Add it to the project's `open_questions`.
3. State what evidence *would* settle it.

A deliverable that says *"we assumed $40/month; untested; validate before build"* is honest
and useful. One that silently asserts $40/month is a liability.

---

# Confidence

Each module output carries an overall confidence level, derived mechanically:

| Level | Condition |
| --- | --- |
| `high` | >= 70% of load-bearing claims tagged `[verified]` |
| `medium` | >= 40% verified, and no unflagged assumption in a decision-critical claim |
| `low` | below 40% verified, or any decision rests on an untagged claim |

A load-bearing claim is one that, if false, changes a decision.

**A run may complete at `low` confidence.** It may not complete while pretending to be
higher. The Executive Summary states the confidence level and lists what would raise it.

---

# Reviewer Checklist

Before any module passes its gate:

- [ ] Every factual claim carries exactly one tag
- [ ] Every `[verified]` names a source a reader could retrieve
- [ ] Every `[inferred]` names what it was inferred from
- [ ] Every `[assumption]` appears in the validation plan
- [ ] No hedging language substituting for a tag
- [ ] Confidence level computed and recorded

---

> **Engine Principle**
>
> The framework is not judged on how confident it sounds.
> It is judged on whether a reader can tell which parts to trust.
