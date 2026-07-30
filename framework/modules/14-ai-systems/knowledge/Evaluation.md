---
Title: Evaluation
Module: 14-ai-systems
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Set the bar before committing, with both statistical and per-instance criteria.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/Automation.md
Outputs:
  - evaluation_plan
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Evaluation
  - Method
---

# Evaluation

---

# What It Is

The bar the capability must clear — defined **before** it is committed to, because a bar set afterwards is set to whatever was achieved.

"We will evaluate it" is not a plan. What is:

| Element | |
| --- | --- |
| Metric | What quality means for this capability |
| Method | Golden set, human review, A-B |
| Passing bar | A figure |
| Sample size | Enough to mean something |
| Cadence | How often it is re-checked |
| **Ship gate** | The result required before users see it |
| What happens if the bar is missed | The capability does not ship — stated |
| Regression check | How a model or prompt change is re-evaluated |

And the reconciliation with `08-product`, whose `Given / when / then` form assumes determinism:

| Type | Form | Example |
| --- | --- | --- |
| **Statistical** | A bar over a sample | "≥95% of 200 golden-set cases judged correct by a «domain expert»" |
| **Per-instance** | Always true, every time | "Output never exceeds «n» characters" · "Output always contains a citation" · "The user can always dismiss it" |

> The per-instance guarantees are ordinary requirements and belong in `08-product`'s criteria. **They are also where most real safety lives:**
> an output that must always be dismissible, always labeled, and always bounded is safe in ways no accuracy figure provides.

---

# When It Applies

In Move 5 (Evaluate), before commitment — evaluating after building sets the bar to whatever was achieved.

---

# How to Apply It Here

**Build the golden set from real cases and never tune against it.** A golden set that has been optimized against measures how well the
capability was fitted to it.

**Have a domain expert judge correctness.** `Automation.md`'s point applies: the build team cannot assess clinical, legal or financial
correctness, and their confidence is not evidence.

**Hand the per-instance criteria back to `08-product`.** They are conventional requirements, testable in the normal way, and they carry more
of the actual safety than the statistical bar does.

**Write the regression check.** A prompt change, a model version change or a provider default change can alter behavior silently.
`09-technology/knowledge/CI-CD.md` is where it runs.

**State the consequence of missing the bar, in advance.** The capability does not ship. Written afterwards, the bar becomes negotiable — the
same failure `04-problem/knowledge/validation/Success-Criteria.md` describes.

---

# Where It Misleads

**Demos are treated as evaluation.** They are curated cases. The distribution real work produces is messier, and the tail is where the
failures live.

**An average accepts catastrophic individual cases.** 92% accuracy is compatible with total failure on a recognizable subset — which is why
`08-product/knowledge/features/Acceptance-Criteria.md` requires both kinds of criterion.

**The bar is set after the first results arrive.** Every threshold becomes negotiable once a number exists, and the evaluation confirms rather
than tests.

**The golden set drifts into a tuning set.** It happens gradually and it invalidates every subsequent figure.

**Evaluation is scheduled once.** Models change, providers change defaults, and inputs drift. Without a cadence the bar was cleared once, in
conditions that no longer hold.

---

# Related

| | |
| --- | --- |
| `Automation.md` | The autonomy the bar supports |
| `AI-Risks.md` | The failures evaluation is looking for |
| `08-product` | Where per-instance criteria belong |
| `09-technology` | Where the regression check runs |

---

> **Concept Note**
>
> Set the bar before you have a number, or the number becomes the bar.
>
> Most real safety is in the per-instance guarantees — always
> dismissible, always labeled, always bounded — not in the accuracy
> figure.
