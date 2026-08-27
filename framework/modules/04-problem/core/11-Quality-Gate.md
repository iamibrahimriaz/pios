---
Title: Quality Gate
Module: 04-problem
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Problem module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 04-problem/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Problem
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

**The gate checks whether the analysis was done honestly — not whether the news is good.**

A module reporting `UNVALIDATED` with a clear validation plan **passes**. A module
reporting `VALIDATED` on inference **fails**. Getting this the right way round is the
whole point.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Each problem scored on frequency, severity and current workaround

**Passes when:** every problem surviving classification carries all three scores, the
scales are stated, and the arithmetic is visible.

**Fails when:** any dimension is missing — most often the workaround.

The workaround dimension is not optional. A problem scored 5×5 with no workaround
assessment is indistinguishable from a problem somebody already solved adequately.

**Also required:** classification happened first. If preferences appear in the scoring
table, Stage 2 was skipped and this criterion fails.

| Fails | Passes |
| --- | --- |
| "P1: high priority" | "P1: frequency 5 (daily), severity 5 (unpaid hours), workaround 5 (none — they simply stay late). Score 125" |

---

# Criterion 2 — >= 3 problems carrying [verified] evidence, not inference

**Passes when:** three or more problems have `[verified]` tags resolving to retrievable
sources at evidence ladder ranks 1–3.

**Fails when:** the count is met by promoting inferred problems, or by tagging expert
assertion and reasoning as verified.

**The honest shortfall clause.** If fewer than three problems can be verified — which is
common, and normal when no primary research was possible — the criterion is **not**
satisfied by pretending otherwise. Instead:

1. State the actual count plainly.
2. Set the verdict to `PARTIALLY VALIDATED` or `UNVALIDATED`.
3. Set confidence to `low`.
4. Make the validation plan the document's centerpiece.
5. Record the shortfall in the gate verdict.

A run may proceed past this criterion **unsatisfied but declared**. It may not proceed
with the shortfall concealed. The gate verdict records `shortfall_declared: true`, and
module 09 must then produce a Milestone Zero.

This is the one criterion in the framework that can be consciously waived — because
demanding verification an agent cannot obtain would only produce fabricated verification.

---

# Criterion 3 — The single sharpest problem identified and defended

**Passes when:** exactly one problem is named as sharpest, the choice references the
scoring table, comparable scorers are addressed, and the evidence standing is stated
explicitly as verified or assumed.

**Fails when:** no single problem is chosen, or the choice is asserted without reference
to the scores.

**Test:** if the highest-scoring problem was not chosen, is there a stated reason? Passing
over the top scorer requires more defense than choosing it, not less.

**Also required:** the root cause check. If the product addresses a symptom rather than the
root, that must be a stated decision.

---

# Criterion 4 — Unvalidated problems explicitly listed as such

**Passes when:** validated and assumed problems appear in **visually separate sections**,
the assumed section carries an explicit warning, and no assumed problem appears in the
validated list.

**Fails when:** the two are blended in prose, or the distinction is made only through
tagging inside a shared narrative.

Structural separation matters more than tagging here. A reader skimming a blended section
absorbs assumed problems as established ones, however carefully each sentence was tagged.

---

# Criterion 5 — Substitute workflows enumerated by name, including what people do who use nothing in this category

**Passes when:** the module lists the specific things people do *instead* — by hand, with a
general-purpose tool, with something they built themselves, with an adjacent product, or by
tolerating the problem — each named, and each carrying a measure of scale where one exists.

**Fails when:** the substitutes section lists only competing products in the same category,
or lists "manual process" as a single undifferentiated row, or is absent because every
source consulted was a complaint about an existing tool.

**How to test it:** take the workaround score of the highest-ranked problem and ask which
named substitute justifies it. If the answer is "nothing in particular", the column was
scored from impression.

> **Why this is a gate and not a suggestion.** `09-Research-Methodology.md` ranks a widely
> shared workaround as **rank 1** — the strongest evidence class this module recognizes — and
> Stage 3 multiplies every score by the workaround dimension. The module was therefore scoring
> against, and reasoning from, something it never required anyone to collect.

**The most common failure is structural, not lazy.** Complaint sources — reviews, trackers,
forums — only contain people who adopted something and were disappointed. **The people using a
substitute successfully are silent by construction**, and a module that harvests only
complaints will conclude that every problem is unsolved.

---

# Criterion 6 — The evidence corpus states its selection rule and is justified independently of the product hypothesis

**Passes when:** the module names **where the problem evidence was read from**, states the
**rule** that selected those sources, and answers the independence test in writing.

**Fails when:** the corpus is described as a list of sources with no rule behind it, or when
the justification for the sources is the product hypothesis itself.

## The rule, not the list

**A rule is reproducible.** *"Every product in the category above 2,000 installs with at least
20 reviews"* can be applied by a stranger who gets the same set. *"The main products"* is a
list assembled from memory, and it contains the ones the hypothesis already had in mind.

**State what the rule excludes and what that costs.** A rule that can only see one directory
cannot see the commercial products sold direct — often exactly where the paying customers are.

## The independence test, applied literally

> **If the product hypothesis were different, would this still be the right place to look for
> this problem?**

**If the honest answer is no, the corpus is a description of the hypothesis** and cannot be
evidence for it.

## Where this fails in practice

**A corpus drawn from the largest products in a category is not evidence that those products
are problem-heavy.** Raw complaint volume follows install base. On the run that produced this
criterion, the two products the entire problem inventory was read from turned out — once
complaints were normalized per active install per year — to be among the **least**
complained-about in their category, one of them the lowest of any established entrant. **The
corpus had been selected for size and then read as though it had been selected for severity.**

**The repair was not a correction. It was a re-rank**, which changed the sharpest problem,
which changed the strategy scoring, which changed the recommendation.

**Normalize, or refuse the comparison.** Any stated denominator beats none. Where none is
obtainable, say so and stop comparing across sources — an unnormalized cross-source comparison
is not a weak finding, it is a wrong one.

`knowledge/Corpus-Selection.md` carries the six biases this criterion tests for — selection,
denominator, survivorship, venue, product size and confirmation — and what each looks like.

| Fails | Passes |
| --- | --- |
| "Problems drawn from user reviews of «the two biggest products»" | "Rule: every product in the category above «n» installs with at least «n» reviews — 8 qualified, listed. Complaints normalized per 10,000 active installs per year. The two largest rank 5th and 7th of 8, so the corpus is not size-weighted" |
| "We looked at the forums" | "Two venue types with different incentives: support threads (collect failures) and reviews (collect sentiment). Issue trackers excluded — 63% of issues in the sample were authored by vendor accounts, so it is a backlog rather than a user corpus" |
| Justification: "these are the products our idea competes with" | Justification: "these are the products in which this problem class would appear if it exists, whatever we end up building" |

---

# Universal Gates

U1–U7 apply. Most often missed here:

| | |
| --- | --- |
| **U1** | Cost claims are the usual offenders — "costs about two hours a day" needs a source or a tag |
| **U3** | Problems must be attributable to the persona from `03-user`, not a different user |
| **U4** | The sharpest-problem choice is a decision; the alternatives rejected must be recorded |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Verify every `[verified]` problem sits at evidence ladder rank 1–3.
3. Verify validated and assumed sections are structurally separate.
4. Evaluate universal gates U1–U7.
5. Evaluate criteria 1–6. **All of them.**
6. Record the verdict.

```yaml
gate:
  module: 04-problem
  attempt: 1
  verdict_reported: PARTIALLY VALIDATED
  criteria:
    all_scored_three_dimensions: pass
    three_verified_problems: fail
    shortfall_declared: true          # verified count 1, stated plainly
    sharpest_identified_defended: pass
    unvalidated_listed_separately: pass
    substitutes_enumerated: pass
    corpus_selection_justified: pass
  universal: [U1 pass, U2 pass, U3 pass, U4 pass, U5 pass, U6 pass, U7 pass]
  verdict: pass_with_declared_shortfall
  note: "Only P1 reaches verified. Milestone Zero required before build."
  action: "Flag to 07-strategy and 09-Roadmap."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 03-user`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | Workaround dimension unscored | Revise here |
| **Upstream** | No friction in `current_workflow` to harvest from | Return to `03-user` |
| **Fundamental** | Every candidate is a preference | Return to `03-user`; the persona or workflow may be wrong |

A run that harvests nothing painful has learned something important. Returning upstream is
correct. Manufacturing a problem to justify continuing is the one failure this module
exists to prevent.

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate with the specific finding |

---

# What a Passing Module 04 Looks Like

- Preferences were identified and excluded, with reasons on the page.
- Symptoms were traced to the problems beneath them.
- Every problem carries three scores and visible arithmetic.
- A reader can tell at a glance which problems are proven and which are believed.
- One problem is named as sharpest, and the reasoning survives scrutiny.
- The validation plan contains tests that could actually fail.
- The verdict is stated first, and is not softer than the evidence supports.

---

> **Gate Principle**
>
> This gate is not asking whether the problem is real.
>
> It is asking whether the analysis is honest about how much we know.
