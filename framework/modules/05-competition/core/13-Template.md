---
Title: Template
Module: 05-competition
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Competitive Analysis — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 05-competition/core/06-Framework.md
Outputs:
  - projects/<slug>/research/05-competition.md
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Template
  - Output
---

# Template — Competitive Analysis

---

# Usage

Copy everything below the line into `projects/<slug>/research/05-competition.md` and
fill it.

This is a **working document**. It feeds `01-Research-Dossier.md` §3, the Executive
Summary, and the positioning statement in the PRD.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**Competitors are compared on problems, not features.** Feature checklists are the most
common way this module produces a document that looks thorough and decides nothing.

---
---

# Competitive Analysis — «Project Name»

| | |
| --- | --- |
| Module | 05-competition |
| Date | «ISO date» |
| Market | «from market_definition» |
| Segment | «prioritized segment from 03-user» |
| Status | draft / complete |
| Confidence | «high / medium / low» |

---

## 1. The Competitive Position, in One Paragraph

<!-- Write this last. What a reader needs to know if they read nothing else. -->

«One paragraph: who owns this space today, where the opening is, and how defensible it is.»

---

## 2. Competitor Inventory

<!-- Move 1 and 2. Minimum five, spanning categories. The status quo is mandatory. -->

| # | Competitor | Type | Serves | Since | Scale | Source |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | «name» | direct | «segment» | «year» | «users/revenue if known» | [tag] |
| C2 | «name» | indirect | «segment» | «year» | «scale» | [tag] |
| C3 | «name» | substitute | «segment» | — | «scale» | [tag] |
| C4 | **Status quo** — «what they actually do today» | incumbent | all | — | universal | [tag] |
| C5 | **Non-consumption** — «who has this problem and does nothing» | — | «segment» | — | «share» | [tag] |

**Type definitions**

| Type | Meaning |
| --- | --- |
| Direct | Solves the same problem for the same segment |
| Indirect | Solves the same problem for a different segment, or an adjacent problem |
| Substitute | A different approach entirely — a service, a person, a spreadsheet |
| Status quo | What the user does today, from `03-user` `current_workflow` |
| Non-consumption | People with the problem who have chosen nothing |

<!-- C4 comes from 03-user's current_workflow. It is usually the strongest competitor:
     free, installed, trusted, zero switching cost. It must be taken seriously, not
     listed as a formality. -->

---

## 3. Problem Coverage

<!-- Move 3. THE CENTRAL TABLE OF THIS MODULE.
     Score each competitor against the ranked problems from 04-problem — not against
     a feature list. This is what makes the analysis decide something. -->

| Problem (from 04) | Rank | «C1» | «C2» | «C3» | Status quo | Us (proposed) |
| --- | --- | --- | --- | --- | --- | --- |
| P1 — «sharpest problem» | 1 | «well / partly / not» | | | | |
| P2 — «problem» | 2 | | | | | |
| P3 — «problem» | 3 | | | | | |

**Scoring:** *well* = solves it as the user would define solved. *partly* = addresses it
with meaningful residual pain. *not* = does not address it.

**Who solves P1 best today:** «name, including status quo if true» [tag]

**Problems nobody solves well:** «list — this is where the opening is, if there is one»

---

## 4. Feature Comparison

<!-- Secondary to §3. Useful for table stakes only: what must exist for the product to
     be considered at all. Do not use it to find differentiation — everyone ships
     everything eventually. -->

**Table stakes** — required to be taken seriously:

| Capability | «C1» | «C2» | Status quo | Required of us? |
| --- | --- | --- | --- | --- |
| «capability» | ✓ | ✓ | ✗ | yes |

**Differentiators claimed by competitors:**

| Competitor | Claims | Actually delivers? | Evidence |
| --- | --- | --- | --- |
| «name» | «claim» | «assessment» | [tag] |

---

## 5. Pricing

<!-- Move 4. Captured or explicitly marked unavailable. Never estimated silently. -->

| Competitor | Model | Entry price | Typical price | What is included | Source | Accessed |
| --- | --- | --- | --- | --- | --- | --- |
| «name» | subscription / usage / license / free | «figure» | «figure» | «scope» | [tag] | «date» |
| **Status quo** | — | free | free | — | — | — |

**Pricing not publicly available for:** «list — marked explicitly, not estimated»

**Price range in this market:** «low – high»

**What the pricing tells us:** «who they are built for, and what they consider the value»

**Implication for us:** «where our price would have to sit, and why»

---

## 6. Strengths and Weaknesses

<!-- Only for the two or three competitors that actually matter. -->

### «Competitor name»

| | |
| --- | --- |
| Owns | «what they are genuinely best at» [tag] |
| Weak at | «where they fail, with evidence» [tag] |
| Why they are weak there | «structural reason, not "they haven't got round to it"» |
| Would they fix it if attacked? | «assessment — this is the defensibility question» |
| Their buyer | «who signs» |
| Their moat | «distribution / data / switching cost / brand / none» |

---

## 7. Gap Analysis

<!-- Move 5. A gap you can ENTER is not the same as a gap you can HOLD. -->

**The gap:** «one paragraph»

| | |
| --- | --- |
| Who is underserved | «segment» |
| Which ranked problem it corresponds to | P«n» |
| Why it exists | «structural reason» [tag] |
| Why incumbents have not closed it | «reason» [tag] |
| Could they close it in six months if we succeed? | **«yes / no»** — «reasoning» |
| If yes, what protects us | «distribution / data / focus / speed / nothing» |

**Defensibility verdict:** «defensible / temporary / not defensible»

<!-- "Not defensible" is a legitimate finding and must be stated. It does not
     necessarily stop the project — many good businesses have no moat at the start —
     but it must be a known condition, not a discovered one. -->

---

## 8. Positioning

<!-- Move 6. One sentence. It must be true, specific, and not claimable by a competitor. -->

> For «segment» who «need», «product» is a «category» that «key benefit», unlike
> «primary alternative», which «limitation».

**Test:** could «C1» make the same claim? «yes / no — if yes, rewrite»

**Category we are entering:** «existing category / new category»

<!-- Entering an existing category means competing on comparison. Creating a new one
     means paying for education. Both are valid; the cost differs and must be named. -->

---

## 9. Threats

| Threat | Likelihood | Impact | Early warning sign |
| --- | --- | --- | --- |
| «e.g. incumbent ships this as a feature» | «h/m/l» | «h/m/l» | «what you would see first» |
| «e.g. status quo remains good enough» | | | |

---

## 10. The Graveyard

<!-- Who tried this and stopped? The cheapest lesson available. -->

| Product | Active | Why it stopped | What it teaches | Source |
| --- | --- | --- | --- | --- |
| «name» | «years» | «reason, or "unknown"» | «lesson» | [tag] |

«Or: "No abandoned attempts found. Searched: «terms». This may mean the category is
young, or that the search was incomplete."»

---

## 11. Contradicting Evidence

<!-- From the adversarial pass. What suggests this market is well served already? -->

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against entry» | [tag] | «what it would mean» | «how addressed» |

---

## 12. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `competitor_matrix` | «summary» | 06-business, 07-strategy |
| `pricing_comparison` | «range and models» | 06-business |
| `gap_analysis` | «the gap and its defensibility» | 07-strategy |
| `positioning` | «the statement» | 07-strategy, 08-product |
| `feature_comparison` | «table stakes» | 08-product |

---

## 13. Sources

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation» | vendor page / review / filing / press | «date» | «claims» |

---

## 14. Evidence Standing

| | Count |
| --- | --- |
| Competitors with sourced pricing | «n» of «n» |
| Competitors assessed from direct evidence | «n» |
| Competitors assessed from third-party description only | «n» |
| Open assumptions | «n» |

**Confidence:** «high / medium / low»

**Largest gap:** «what is least established»

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] >= 5 competitors, spanning direct, indirect and substitute
- [ ] Status quo included and taken seriously, not listed as a formality
- [ ] Non-consumption considered
- [ ] Problem coverage table completed against ranked problems from 04
- [ ] Pricing captured or explicitly marked unavailable — never silently estimated
- [ ] Pricing sources dated
- [ ] Gap identified with the reason it exists
- [ ] Defensibility question answered honestly, including "not defensible"
- [ ] Positioning statement fails the competitor-claim test
- [ ] Graveyard searched
- [ ] Contradicting evidence non-empty
- [ ] Every claim carries exactly one evidence tag
- [ ] Every placeholder replaced, every guidance comment removed
-->
