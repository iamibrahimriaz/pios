---
Artifact: risks-and-assumptions
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [07-strategy, all]
---

<!-- fill: The honest register. Every open assumption from state.assumptions appears here.
     Order by what BREAKS THE PRODUCT if wrong — not by category, not by how comfortable
     it is to discuss. The first item should be the thing most likely to sink this.
     Remove every <!-- fill --> comment before delivery. -->

# Risks and Assumptions — «Product Name»

## 1. The Assumptions That Would Invalidate This Product

<!-- fill: Lead with these. Three to five, ranked. If any one of them is wrong, the
     product as specified does not work. These are what to test before spending money. -->

| # | Assumption | Why we believe it | If wrong | Cheapest test |
| --- | --- | --- | --- | --- |
| A1 | «statement» | «basis» | «the product does not work because...» | «test» |
| A2 | «statement» | «basis» | «...» | «test» |
| A3 | «statement» | «basis» | «...» | «test» |

**Test A«n» first.** «One sentence on why that one, and what it costs to run.»

---

## 2. Full Assumption Register

<!-- fill: Everything from state.assumptions. Grouped by domain for scanning, but the
     ranking above is what matters for action. -->

### Market and Business

| # | Assumption | Impact if wrong | Validation | Status |
| --- | --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «method» | open |

### Users and Problem

| # | Assumption | Impact if wrong | Validation | Status |
| --- | --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «method» | open |

### Product and Behavior

| # | Assumption | Impact if wrong | Validation | Status |
| --- | --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «method» | open |

### Technical

| # | Assumption | Impact if wrong | Validation | Status |
| --- | --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «method» | open |

### Regulatory and Operational

| # | Assumption | Impact if wrong | Validation | Status |
| --- | --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «method» | open |

---

## 3. Risk Register

<!-- fill: Risks are things that might happen. Assumptions are things we believe.
     Keep them separate — they are managed differently.
     Likelihood and impact: high / medium / low. Be honest; a register where everything
     is "medium" is useless. -->

| # | Risk | Category | Likelihood | Impact | Mitigation | Owner | Early warning sign |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | «risk» | market | high | high | «action» | «who» | «what you would see first» |
| R2 | «risk» | technical | med | high | «action» | «who» | «what you would see first» |
| R3 | «risk» | regulatory | low | high | «action» | «who» | «what you would see first» |

### Top Risks Detail

<!-- fill: The two or three that warrant more than a table row. -->

#### R«n» — «risk name»

**What happens:** «description»

**Why it is plausible:** «reasoning» [tag]

**Leading indicator:** «what you would observe before it fully materialises»

**Mitigation:** «what reduces likelihood»

**Contingency:** «what you do if it happens anyway»

**Accepted?** «yes — we proceed knowing this / no — mitigation required before build»

---

## 4. What Would Make Us Stop

<!-- fill: Define failure conditions in advance, while the thinking is clear.
     Teams almost never do this, and it is why doomed products run for years.
     Be specific enough that the condition is unambiguous when it occurs. -->

| Signal | Threshold | What it means | Action |
| --- | --- | --- | --- |
| «observable» | «specific number» | «interpretation» | stop / pivot / rethink |

---

## 5. Open Questions

<!-- fill: From state.open_questions. Blocking questions must be answered before
     the work they block begins. -->

| # | Question | Blocks | Blocking? | Owner |
| --- | --- | --- | --- | --- |
| Q1 | «question» | «what it blocks» | yes | «who» |

---

## 6. Evidence Gaps

<!-- fill: Where the research is thin, stated plainly. This is a service to the reader,
     not an admission of failure. Concealing it would be the failure. -->

| Area | What is missing | Why it could not be established | Impact on confidence |
| --- | --- | --- | --- |
| «e.g. willingness to pay» | «no pricing research» | «no access to buyers» | «pricing model is assumption-based» |

---

## 7. Register Summary

| | Count |
| --- | --- |
| Open assumptions | «n» |
| Validated assumptions | «n» |
| Invalidated assumptions | «n» |
| High-likelihood / high-impact risks | «n» |
| Blocking open questions | «n» |

**Overall confidence in the blueprint: «high | medium | low»**

«One paragraph: what a reader should understand about how much weight this blueprint
can bear, and what would raise it.»

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Product-invalidating assumptions listed FIRST and ranked
- [ ] Every open assumption from state.assumptions appears in the register
- [ ] Risks separated from assumptions
- [ ] Likelihood and impact assigned honestly, not uniformly
- [ ] Every risk has an early warning sign
- [ ] Stop conditions defined with specific thresholds
- [ ] Evidence gaps stated plainly
- [ ] Overall confidence recorded and matches the Executive Summary
- [ ] Every fill comment removed
-->
