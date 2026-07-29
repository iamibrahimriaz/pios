---
Title: Template
Module: 02-market
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Market Analysis — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 02-market/core/06-Framework.md
Outputs:
  - projects/<slug>/research/02-market.md
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - Template
  - Output
---

# Template — Market Analysis

---

# Usage

Copy everything below the line into `projects/<slug>/research/02-market.md` and fill it.

This is a **working document**, not a customer deliverable. It feeds
`deliverables/templates/01-Research-Dossier.md` §1 and the Executive Summary.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

A section that cannot be filled is a finding. Write what is missing and why. Never delete
a section to hide a gap, and never write filler to occupy one.

---
---

# Market Analysis — «Project Name»

| | |
| --- | --- |
| Module | 02-market |
| Date | «ISO date» |
| Jurisdiction | «from idea_brief» |
| Status | draft / complete |
| Confidence | «high / medium / low» |

---

## 1. Market Definition

<!-- Frame 1. Define by BOUNDARY, not by adjective. The test: could a reader use this
     definition to decide whether a given company is in the market or outside it? -->

**The market:** «one sentence naming who, what need, and where»

**Inside this market**

| Included | Why |
| --- | --- |
| «type of participant or offering» | «reason» |

**Outside this market**

| Excluded | Why |
| --- | --- |
| «type of participant or offering» | «reason» |

**The boundary test:** «name one borderline case and rule it in or out, with the reason»

**Category name:** «what this market is called by people who work in it» [tag]

<!-- If the domain has no established name for this category, that is a finding.
     A market with no name may be a market with no buyers. Say so. -->

---

## 2. Regulatory Landscape

<!-- Frame 2. Runs BEFORE sizing, because regulation determines who may participate at
     all. Jurisdiction comes from idea_brief and is never assumed. -->

**Jurisdiction:** «country / region»

| Regime | Applies because | Requires | Consequence for the product |
| --- | --- | --- | --- |
| «name» | «trigger» | «obligations» | «design consequence» [tag] |

**Barriers to entry created by regulation**

| Barrier | Type | Cost to clear | Time to clear |
| --- | --- | --- | --- |
| «e.g. certification» | «licensing / certification / audit» | «figure» [tag] | «duration» [tag] |

**Does regulation exclude any segment named in the idea brief?** «yes/no — if yes, this
returns to 01-idea»

**Regulatory direction of travel:** «tightening / stable / loosening» [tag]

---

## 3. Market Size

<!-- Frame 3. Every figure sourced or explicitly marked as an assumption.
     Show the derivation, not just the number. A number without a derivation cannot be
     challenged, and an unchallengeable number is not evidence. -->

| | Figure | Derivation | Tag |
| --- | --- | --- | --- |
| **TAM** | «figure» | «how derived» | [tag] |
| **SAM** | «figure» | «how derived» | [tag] |
| **SOM** (year 1) | «figure» | «how derived» | [tag] |

**Method used:** «top-down / bottom-up / both»

<!-- Prefer bottom-up. A top-down figure taken from a market report is usually a
     different market than the one defined in section 1. If both methods were used and
     they disagree, that disagreement is a finding — record it rather than picking the
     more attractive number. -->

**Bottom-up derivation**

```
«unit count» × «price» × «adoption assumption» = «figure»
```

| Input | Value | Tag |
| --- | --- | --- |
| «e.g. number of solo practices in jurisdiction» | «n» | [tag] |
| «e.g. realistic annual price» | «figure» | [tag] |
| «e.g. reachable share in year 1» | «%» | [tag] |

**If top-down and bottom-up disagree:** «by how much, and which is more trustworthy here»

**How much weight can this sizing bear?** «honest assessment in one sentence»

---

## 4. Trends

<!-- Frame 4. Minimum three. Each needs a DIRECTION and EVIDENCE — a trend without a
     direction is an observation. Include at least one that works against the idea. -->

| # | Trend | Direction | Evidence | Implication for this product |
| --- | --- | --- | --- | --- |
| T1 | «trend» | growing / declining | [tag] | «what it means» |
| T2 | «trend» | growing / declining | [tag] | «what it means» |
| T3 | «trend» | growing / declining | [tag] | «what it means» |

**Trend working against this idea:** «which one, and how much it matters»

<!-- If no trend works against the idea, the research was selective. Look again. -->

**Timing assessment:** «is this early, on time, or late? Why?» [tag]

---

## 5. Market Gaps

<!-- Frame 5. Where is the market underserved — and WHY has it stayed that way?
     A gap with no explanation is usually not a gap. -->

| # | Gap | Who is underserved | Why it persists | Evidence |
| --- | --- | --- | --- | --- |
| G1 | «what is missing» | «segment» | «structural reason» | [tag] |

**Most promising gap:** «which one, and why»

**Why incumbents have not closed it:** «the structural reason — regulation, economics,
distribution, data access, or incentive» [tag]

<!-- If there is no reason a gap persists, be suspicious of the gap rather than excited
     by it. Detailed competitor analysis belongs to 05-competition, not here. -->

---

## 6. Market Structure

| | |
| --- | --- |
| Maturity | «emerging / growing / mature / declining» [tag] |
| Concentration | «fragmented / consolidating / dominated» [tag] |
| Typical buyer | «who holds the budget» |
| Typical sales motion | «self-serve / sales-led / procurement» [tag] |
| Switching frequency | «how often buyers change provider» [tag] |

---

## 7. Contradicting Evidence

<!-- From the adversarial review pass. What did you find that argues this market is
     unattractive? This section must not be empty. -->

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against» | [tag] | «what it would mean» | «how addressed» |

---

## 8. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `market_definition` | «summary» | 05-competition, 06-business |
| `tam_sam_som` | «figures» | 06-business |
| `trends` | «summary» | 05-competition |
| `regulatory_landscape` | «summary» | 09-technology |
| `market_gaps` | «summary» | 05-competition, 07-strategy |

**Domain vocabulary for later modules:** «terms that improve search quality downstream»

---

## 9. Sources

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation with URL or publication» | «report / regulation / vendor» | «date» | «claims» |

---

## 10. Evidence Standing

| | Count |
| --- | --- |
| Verified claims | «n» |
| Inferred claims | «n» |
| Open assumptions | «n» |

**Largest gap:** «what is least established, and what would close it»

**Confidence:** «high / medium / low»

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] Market defined by boundary, with a borderline case ruled on
- [ ] Regulatory landscape researched for the named jurisdiction
- [ ] Checked whether regulation excludes a segment from the idea brief
- [ ] TAM / SAM / SOM each sourced or explicitly marked assumption
- [ ] Sizing derivation shown, not just the figure
- [ ] >= 3 trends with direction and evidence
- [ ] At least one trend working against the idea
- [ ] Each gap explains why it persists
- [ ] Contradicting evidence section non-empty
- [ ] Every claim carries exactly one evidence tag
- [ ] Every [verified] resolves to an entry in Sources
- [ ] Every placeholder replaced, every guidance comment removed
-->
