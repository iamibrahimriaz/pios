---
Title: Competitor Identification
Module: 05-competition
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Find everyone who competes for the problem, including what is not a product.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/core/06-Framework.md
Outputs:
  - competitor_matrix
Related Modules:
  - 03-user
  - 04-problem
Tags:
  - Competition
  - Identification
  - Method
---

# Competitor Identification

---

# What It Is

The enumeration of everything competing for the same problem — a minimum of five, drawn from across five
categories rather than one.

A competitor is anything the person could use **instead**. That definition includes things nobody markets, and
those are usually the ones that win.

| Where to look | What it yields |
| --- | --- |
| Category search using `02-market`'s domain vocabulary | Direct competitors |
| Adjacent categories | Indirect competitors |
| `current_workflow` from `03-user` | The status quo — the real incumbent |
| Review sites and "alternatives to" pages | What users actually compare |
| Forums where the problem is discussed | Substitutes and homemade solutions |
| Job postings naming tools | What organizations actually run |

---

# When It Applies

In Move 1 (Enumerate), before any classification or scoring. It consumes `03-user`'s workflow and
`04-problem`'s workaround list directly — those two contain most of the real competitive set.

---

# How to Apply It Here

**Start from the workarounds, not from the category.** `04-problem`'s `Current-Solutions.md` already lists what
people use today. That list is the competitive set that matters, and it is already evidenced.

**Include the two categories that are always forgotten.** The status quo — paper, a spreadsheet, an assistant, a
habit — is free, installed, trusted and requires no change. Non-consumption is the group who have the problem and
chose nothing at all.

**Search for who tried this and stopped.** A dead product, an abandoned open-source project, a feature an
incumbent shipped and withdrew. Each one is a finding about why the gap persists, and `02-market` needed exactly
that answer.

**Cite every entry.** A competitor with no source is a recollection. The gate requires sources, and pricing
requires dates.

**Search in the user's vocabulary, not the category's.** Practitioners and vendors use different words, and
searching in vendor language finds only vendors — which is how the status quo goes missing.

---

# Where It Misleads

**Searching for products finds products.** The instrument shapes the list: a category search cannot surface a
spreadsheet, an assistant, or inertia, and those three account for most of the addressable behavior in many
markets.

**Funded competitors are over-weighted because they are visible.** A well-marketed product with few users looks
more threatening than a decade-old habit with total penetration. Market presence is not the same as installed
base.

**Five is a floor treated as a target.** A list stopping at five direct competitors has usually skipped four of
the five categories.

**A long list substitutes for a decision.** Enumeration is Move 1 of six. Its output is only useful once Move 3
scores it against ranked problems — and a matrix that never reaches that move has decided nothing.

**Competitors get judged on their marketing.** A website describes intent and positioning, not capability.
Reviews, support forums and changelogs describe what the product actually does.

---

# Related

| | |
| --- | --- |
| `Direct-Competitors.md`, `Indirect-Competitors.md` | The classification that follows |
| `Feature-Comparison.md` | Where the list gets scored against problems |
| `04-problem` | Where the workaround list originates |
| `03-user` | Where the status quo is documented |

---

> **Concept Note**
>
> A competitor is anything they could use instead — including nothing.
>
> Search for products and you will find products. The thing that beats
> you is usually already installed and was never sold.
