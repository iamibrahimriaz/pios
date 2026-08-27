---
Title: Corpus Selection
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Justify where problem evidence was drawn from, independently of the product hypothesis, and name the six biases that make a corpus argue for whatever selected it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
  - 04-problem/knowledge/Evidence.md
Outputs:
  - evidence_log
  - problem_inventory
Related Modules:
  - 03-user
  - 05-competition
  - 07-strategy
Tags:
  - Problem
  - Evidence
  - Method
  - Concept
---

# Corpus Selection

---

# What It Is

**The set of sources the problem evidence was read from, and the argument for why that set represents
the problem rather than something else.**

Every problem inventory rests on a corpus: support threads, reviews, tickets, interview transcripts,
community posts, issue trackers. The corpus is chosen before anything is read, usually in a few
seconds, usually on grounds of availability — and **it determines the answer more than the coding
does.**

> **A corpus selected by the hypothesis will confirm the hypothesis.**
>
> Not through bad coding. Through the sampling frame, which nobody re-examines because it was never
> written down as a decision.

**The corpus decision is an output, not a preliminary.** It goes in the module document with its
justification, so a reader can disagree with the frame rather than only with the findings.

---

# When It Applies

**Before the first source is read, and again before the ranking is trusted.**

The second pass is the one that matters. By then you know what the corpus returned, and the question
is whether a different defensible corpus would have returned something else. **If you cannot say,
the ranking is provisional and must say so.**

---

# How to Apply It Here

## Write the selection rule before collecting

**A rule, not a list.** *"Every product in the category above 2,000 installs with at least 20
reviews"* is a rule — someone else can apply it and get the same set. *"The main products"* is a
list assembled from memory, and it will contain the ones the hypothesis already had in mind.

**State what the rule excludes and what that costs.** A rule that can only see products in one
directory cannot see the commercial ones sold direct — often exactly where the paying customers are.
**Record the exclusion as a known gap, not as a footnote.**

## Justify the corpus independently of the product

**The test, applied literally:**

> If the product hypothesis were different, would this still be the right place to look for this
> problem?

If the honest answer is no, the corpus is a description of the hypothesis and cannot be evidence for
it.

## Normalize before comparing anything

**Raw counts measure the size of the population that produced them.** The largest product in a
category generates the most complaints because it has the most users, and reading that as a quality
signal is the most common quantitative error in this module.

**Divide by something.** Complaints per active user per year, incidents per thousand transactions,
tickets per customer. Any denominator, stated, beats none. **Where no denominator is obtainable, say
so and stop making comparisons across sources** — an unnormalized comparison is not a weak finding,
it is a wrong one.

## The six biases, and how each one shows up

| Bias | What it does | The check |
| --- | --- | --- |
| **Selection** | The corpus was chosen for availability or because it fit the hypothesis | Write the rule first. Could a stranger reproduce the set from it? |
| **Denominator** | Raw counts compared across populations of different sizes | Normalize, or refuse the comparison. State the denominator every time |
| **Survivorship** | Only the surviving products, active communities and remaining customers are visible | **Who left, and where did they go?** Dead products, abandoned forums and churned customers hold the problem's most expensive evidence and are the hardest to see |
| **Venue** | The venue shapes what gets said. A support forum collects failures; a review site collects sentiment; an issue tracker collects whatever the vendor's own staff filed | Use at least two venue types with different incentives. Check who is *authoring* — a tracker dominated by vendor accounts is a backlog, not a user corpus |
| **Product size** | A corpus drawn from the biggest products is treated as representing the problem-heavy part of the market | Normalize by install base or user count. **Popularity and problem density are frequently inverse** |
| **Confirmation** | Sources that agree are read closely; sources that disagree are read as noise | Record what each source returned *including nothing*. A search that produced no support for the hypothesis is a result, and it is recorded before it can be forgotten |

## What to do when a bias is found after the fact

**Re-rank without the compromised evidence and compare the two rankings.** Do not quietly re-weight
until the original answer returns.

**If the ranking changes, the ranking changed.** Everything derived from it — the sharpest problem,
the strategy scoring, the roadmap — is re-derived from the new one, and the old one is superseded
rather than deleted. `engine/gates.yaml` `late_answer_rederivation` is the closest analogue and the
same discipline applies: a conclusion that survives for a *different* reason has changed.

**If the ranking does not change, that is a genuinely strong result** — say so, because a ranking
that survives losing a chunk of its evidence base is more robust than one that never had it
questioned.

---

# Where It Misleads

**A justified corpus is not a representative one.** The justification establishes that the frame was
chosen deliberately and can be argued with. It does not establish that the frame is unbiased, and
those get conflated the moment the justification is written down.

**Two venues are not independent if they share a population.** A forum and a review page for the
same product are largely the same people in two moods. Independence is about who, not about where.

**Normalization can be overdone.** Dividing by a denominator that has nothing to do with the failure
mechanism produces a confident, meaningless rate. If the problem is per-transaction, users are the
wrong denominator.

**A corpus that returns nothing is evidence.** A category with no public discussion, no review body
and no community is telling you how its buyers behave — and it means review-mining and search-driven
acquisition are *unavailable*, not merely underused. `engine/remote-validation.md` covers what
follows from that.

---

# Related

| | |
| --- | --- |
| `Evidence.md` | What verification means here, and the two-list separation |
| `Frequency.md` | Where the denominator problem bites hardest |
| `engine/instrument-substitution.md` | Coding public user-generated evidence: firsthand, dedup, reporters, impact |
| `engine/remote-validation.md` | When the corpus does not exist at all |
| `07-strategy` | Where a re-ranked problem set changes the option scores |

---

> **Concept Note**
>
> The corpus is chosen in seconds and determines the answer.
>
> Write the selection rule before you read anything, normalize before you compare anything, and ask
> once whether a different defensible corpus would have said something else.
