---
Title: Research Methodology
Module: 05-competition
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how competitive evidence is gathered, judged and recorded.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - engine/evidence-policy.md
  - 05-competition/core/06-Framework.md
Outputs:
  - Evidence-tagged competitive findings
  - pricing_comparison
Related Modules:
  - 06-business
Tags:
  - Competition
  - Research
  - Methodology
---

# Research Methodology

---

# Overview

Competition is the most researchable subject in Product Intelligence OS. Vendors publish
their pricing, describe their capabilities, and are reviewed publicly by their users.

The difficulty is not access. It is **credulity** — most of what a competitor publishes
about itself is written to persuade, and it is easy to build an analysis entirely out of
marketing copy.

---

# Methodology Statement

> A vendor tells you what they want to be true.
>
> Their users tell you what is true.
>
> Their changelog tells you what keeps breaking.

---

# Source Hierarchy

| Tier | Source | Trust | Use it for |
| --- | --- | --- | --- |
| 1 | Public pricing page | High for price | Price, packaging, buyer segment — **date it** |
| 2 | Three-star reviews | High for capability | What the product actually does and fails at |
| 3 | Changelogs and release notes | High | What keeps breaking; what they prioritize |
| 4 | Support documentation | High | Where users get stuck; real limitations |
| 5 | Public filings, funding announcements | High for scale | Size, runway, strategic direction |
| 6 | Community and forum discussion | Medium | Substitutes, workarounds, real comparisons |
| 7 | Analyst and comparison sites | Medium | Discovery of competitors; often vendor-influenced |
| 8 | Vendor marketing and homepage | Low | Their positioning claim — **not** their capability |
| 9 | Vendor-authored comparison pages | Lowest | Their opponent list, nothing more |

**Tier 8 and 9 are for discovering what a vendor *claims*, never for establishing what it
*does*.** Record a marketing claim as a claim:

```
Claims real-time sync [verified: vendor homepage, accessed 2026-04-02]
— reviews describe 15-minute delays [verified: 6 reviews, «platform», Q1 2026]
```

Both are verified. They say different things, and the difference is the finding.

---

# The Changelog Method

Underused and unusually reliable.

Read a competitor's release notes across a year and look for the same area being fixed
repeatedly. Repeated fixes mark a **structural** weakness — something their architecture
or business model makes hard — not a passing bug.

That is a validated competitor weakness, evidenced by their own engineering spend.

Also note what they ship **first** after funding or a leadership change. Priorities reveal
strategy more reliably than any published roadmap.

---

# Pricing Research

Pricing is the most consequential output of this module, because module 06 uses it
directly.

| Situation | Record |
| --- | --- |
| Published | Figure, unit, what is included, **date accessed** |
| Tiered | Every tier — the shape reveals the intended buyer |
| "Contact us" | **Mark unavailable.** Note the implication: sales-led motion, price floor, negotiated deals |
| Free | How it is funded — ads, open core, loss leader, upsell. This predicts their next move |
| Usage-based | The unit and the typical monthly total, not just the rate |

**Never estimate silently.** A figure with no source becomes an input to a revenue model
two modules later, where it acquires the appearance of a fact.

If an estimate is genuinely necessary, tag it:

```
[inferred: ~$1,200/yr — from a review mentioning "about a hundred a month";
 no published pricing found]
```

**Always date pricing.** It changes, and an undated figure is unusable within a year.

---

# Finding the Competitors You Would Otherwise Miss

Direct competitors are easy. The ones that beat products are not.

| To find | Search |
| --- | --- |
| Substitutes | "how do you handle «problem»" in community forums |
| Status quo | Already in `current_workflow` from module 03 — use it |
| Non-consumption | Threads where the answer is "we just live with it" |
| Adjacent entrants | Larger platforms adding this as a feature |
| Regional players | The domain vocabulary in the target jurisdiction's language |
| Internal tools | Job postings mentioning custom-built systems |

The "alternatives to «leading product»" page on review sites is the fastest route to the
comparison set buyers actually use — which is often different from the set a category
search returns.

---

# Assessing Defensibility

The one question in this module that cannot be looked up. It has to be reasoned, from
evidence.

Build the answer from:

| Evidence | Tells you |
| --- | --- |
| Their business model | Whether serving this gap would cannibalize their revenue |
| Their pricing structure | Whether this segment is economically viable for them |
| Their changelog priorities | What they consider worth engineering effort |
| Their sales motion | Whether they could sell to this buyer even if they built it |
| Their existing customer base | Whether current customers would object to the change |
| Their acquisition history | Whether they buy rather than build |

Then answer plainly: **if this works, could they ship it in six months?**

"Yes, and nothing would stop them" is a legitimate and important finding. Record it.
Module 07 needs to know whether it is planning a company or a feature.

---

# The Graveyard

Search for failure, not success.

| Search | Yields |
| --- | --- |
| "shutting down" + category | Public shutdown notices |
| "sunset" / "no longer maintained" + category | Abandoned products |
| "acquired" + category | Products absorbed and discontinued |
| Dormant repositories in the category | Open-source attempts that stopped |
| Forum threads about tools that no longer exist | Why users left |

For each, establish **why**. The reason is usually structural: buyers would not pay, the
workaround was good enough, the sale required a committee, the regulation made it
uneconomic.

If nothing is found, record the search terms. "No abandoned attempts found, searched X, Y,
Z" is a finding. Silence is not.

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| Market sizing | `02-market` |
| Segment definition | `03-user` |
| Problem ranking | `04-problem` |
| Our own pricing decision | `06-business` |
| Our feature set | `08-product` |

This module establishes what exists and where the opening is. Module 07 decides what to
do about it.

---

# When Retrieval Is Unavailable

This module degrades worse than any other, because competitors are almost entirely
external knowledge.

1. Record what is known about the category from general reasoning, tagged
   `[assumption: needs validation]`.
2. State plainly that no competitor research was possible.
3. Set confidence to `low`.
4. Add "competitive landscape unresearched" to `state.open_questions` as a high-priority
   task.
5. Do **not** produce a competitor matrix from memory. Naming specific products, their
   prices and their weaknesses without checking is the most likely place in this framework
   for confident fabrication to occur.

An empty, honest competitive analysis is workable. An invented one misprices the product,
mislocates the gap, and misinforms the strategy.

---

# Recording

| Destination | What |
| --- | --- |
| `state.evidence_log` | Every competitor claim, tag, source, date |
| `state.assumptions` | Every inferred price or capability |
| `state.open_questions` | Competitors that could not be assessed |
| Analysis §13 | Sources — every `[verified]` resolves here |

---

# Self Assessment

- Did I distinguish what vendors claim from what users report?
- Did I read changelogs, not just homepages?
- Is every price sourced and dated, or explicitly marked unavailable?
- Did I search for substitutes and non-consumption, not just products?
- Did I reason about defensibility from actual evidence?
- Did I search the graveyard, and record my search terms?
- Did I name any product I did not actually verify exists?

---

> **Research Principle**
>
> Almost everything about a competitor is public.
>
> The failure is not lack of access — it is quoting their marketing back
> as though it were a finding.
