---
Title: Feature Comparison
Module: 05-competition
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Replace the feature checklist with a problem-coverage table that decides something.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Indirect-Competitors.md
Outputs:
  - feature_comparison
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Competition
  - Comparison
  - Method
---

# Feature Comparison

---

# What It Is

The central move of the module: every competitor scored against `04-problem`'s **ranked problems**, not against a
list of features.

| Problem | Rank | C1 | C2 | Status quo | Us |
| --- | --- | --- | --- | --- | --- |
| P1 | 1 | partly | not | partly | — |

| Score | Meaning |
| --- | --- |
| **well** | Solves it as the user would define solved |
| **partly** | Addresses it, with meaningful residual pain |
| **not** | Does not address it |

> A feature comparison tells you what exists. A problem-coverage table tells you where the market is failing the
> person you chose to serve.

Two questions come out of it: **who solves the top-ranked problem best today** — including the status quo, if that
is the honest answer — and **which ranked problems does nobody solve well.** The second is where the opening is, if
there is one.

---

# When It Applies

In Move 3 (Test). Everything before it is preparation; everything after it depends on the answers.

---

# How to Apply It Here

**Use module 04's ranking as the rows, unchanged.** Re-ranking here, or adding problems that were not in the
inventory, breaks the trace `08-product` depends on and usually smuggles in the problems this product happens to
address.

**Score to the user's definition of solved, not the vendor's.** "Has a transcription feature" is not "solves the
problem" if the output still needs fifteen minutes of correction. The residual pain is what "partly" records.

**Give the status quo a real column and a real score.** It is a competitor under the gate, and it commonly beats
funded products on the top-ranked problem.

**Separate table stakes from differentiation.** Capabilities every competitor has are the cost of entry — they
belong in `08-product`'s requirements without being a strategy. Only rows where coverage is uneven can produce
differentiation.

**Leave the "Us" column empty at this stage.** This module maps the field; `07-strategy` decides what to build.
Filling it in here turns the analysis into a plan before the gap has been tested for defensibility.

---

# Where It Misleads

**A large tick table with no conclusion is the module's characteristic failure.** It looks thorough, takes real
effort, and decides nothing — because features are not problems and parity on features is not a position.

**Feature counts favor incumbents and mislead in both directions.** More features is neither better nor worse; the
question is coverage of ranked problems. A product with a tenth of the features can score "well" where a mature
suite scores "partly".

**Marketing pages get scored instead of products.** A claimed capability and a working one differ, and the
difference is visible in support forums, reviews and changelogs rather than on the site.

**Charitable self-scoring inverts the table.** Scoring competitors as "not" where they are "partly", and this
product as "well" on capabilities that do not exist yet, produces an opening that closes on contact with reality.

**A "well" score for everyone is a real result.** If the top problems are all well solved, the honest finding is
that the opening is elsewhere — or absent — and `07-strategy` needs to hear it.

---

# Related

| | |
| --- | --- |
| `04-problem` | Where the rows come from, ranked |
| `Gap-Analysis.md` | What to do with an uneven row |
| `Indirect-Competitors.md` | Who else needs a column |
| `07-strategy` | Where the "Us" column is finally filled |

---

> **Concept Note**
>
> Score competitors against ranked problems, not against each other's
> feature lists.
>
> Parity on features is not a position — it is the entry fee, paid in
> full, for no advantage.
