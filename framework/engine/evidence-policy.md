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

## Three different reasons a claim is unverified — do not conflate them

The tag is the same in all three cases. **What happens next is not**, and recording the wrong
reason sends the run down the wrong path.

| Reason | Where it is handled |
| --- | --- |
| **No retrieval capability.** The agent cannot search at all | `gates.yaml` → `degraded_mode` |
| **Retrieval works; the evidence needs a person, and no person is reachable yet** | `remote-validation.md` — work the public ladder to its edge, then state the edge |
| **Retrieval works; the evidence does not exist in retrievable form at all** | `remote-validation.md` establishes it, and if a gate depends on it, `gates.yaml` → `conditional_continuation` |

**The second and third are the common cases and neither is a research failure.** Reaching the edge
of public evidence and naming it precisely is completed work — it produces the fieldwork plan, and
the absence of a public corpus is frequently evidence about the market in its own right.

**None of the three lowers the evidence bar.** A claim reached remotely is tagged by its source
exactly as any other, and no amount of searching converts an `[assumption]` into a `[verified]`.

---

# Six Claims That Are Routinely Collapsed

**A tag says how well a claim is evidenced. It does not say what the claim is about** — and the most
expensive errors this framework can produce come from evidence for one claim being read as evidence
for another.

**These are six different claims. Each needs its own evidence, and passing a gate on one never
passes another.**

| # | Claim | Established by | Says nothing about |
| --- | --- | --- | --- |
| 1 | **Existence** — the problem happens | Any firsthand report of it happening | How often, or to whom |
| 2 | **Frequency** — how often, per what | A count over a stated denominator | Whether it matters when it happens |
| 3 | **Severity** — how bad it is when it happens | The consequence the sufferer states | Whether it cost them anything |
| 4 | **Business impact** — what it costs | Money, customers, data or hours **named by the person who lost them** | Whether they would pay to prevent it |
| 5 | **Solution demand** — they want it fixed | Built workarounds, paid substitutes, active searching | Whether they would pay *you* |
| 6 | **Willingness to pay** — they will pay, at a price | Money moved, or the strongest available proxy | Retention, or that the price is right |

> **The gap between 4 and 6 is where products die.**
>
> A problem can be real, recurring, cross-vendor and expensively documented, and people will still
> not pay to prevent it. That is the ordinary fate of insurance products, and no volume of evidence
> for claims 1 through 5 constitutes evidence for claim 6.

**The collapse is a sentence, not a decision.** *"44 people reported losing money to this, so there
is clearly demand"* moves from claim 4 to claim 5 in one clause, and nothing in the paragraph looks
wrong. **The tag on that sentence is `[verified]` for the first half and `[assumption]` for the
second, and only splitting the sentence makes that visible.**

## What each module owes

| Module | Establishes | Must not claim |
| --- | --- | --- |
| `04-problem` | 1, 2, 3, 4 | 5 or 6. A ranked problem list is not a demand signal |
| `05-competition` | Partial 5 — people pay *someone* for something adjacent | That they will pay you, or at your price |
| `06-business` | 6, or records it as unestablished | That problem evidence carried it |

**Where claim 6 cannot be established** — and from a public corpus it never can — **the honest output
is that it is unestablished, and a validation test that measures it becomes the first milestone.**
See `engine/instrument-substitution.md` for the willingness-to-pay ladder, and `gates.yaml`
`validation_outcomes`: a test that could not run has produced no evidence about the product.

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
