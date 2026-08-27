---
Artifact: research-dossier
Project: «project name»
Version: 1.0
Date: «ISO date»
Confidence: «high | medium | low»
Modules: [02-market, 03-user, 04-problem, 05-competition]
---

<!-- fill: This is the evidence base. Everything downstream cites it.
     EVERY factual claim carries exactly one tag:
       [verified: source]  [inferred: basis]  [assumption: needs validation]
     Untagged factual claims are defects. Hedging words are not tags.
     Remove every <!-- fill --> comment before delivery. -->

# Research Dossier — «Product Name»

## How to read this

Every claim below carries an evidence tag. Trust them accordingly:

- **`[verified: source]`** — checked against a named, retrievable source
- **`[inferred: basis]`** — reasoned from something verified
- **`[assumption: needs validation]`** — believed, not established

Overall confidence: **«high | medium | low»**

---

# 1. Market

## 1.1 Market Definition

<!-- fill: Define by boundary, not by adjective. "Software for doctors" is not a market.
     "Outpatient clinical documentation tools for solo and small-practice GPs in «country»"
     is a market. State what is inside and what is outside. -->

**In scope:** «definition»

**Out of scope:** «what this deliberately excludes, and why»

**Jurisdiction:** «country/region» — this determines the regulatory section below.

## 1.2 Sizing

| | Figure | Basis |
| --- | --- | --- |
| TAM | «figure» | «how derived» [tag] |
| SAM | «figure» | «how derived» [tag] |
| SOM (year 1) | «figure» | «how derived» [tag] |

<!-- fill: If you cannot source these, say so plainly and tag as assumption.
     A dossier that admits "market size unverified" is more useful than one
     that invents a number. -->

«One paragraph: what the sizing means and how much weight it can bear.»

## 1.3 Trends

| Trend | Direction | Evidence | Implication |
| --- | --- | --- | --- |
| «trend» | «growing/declining» | [tag] | «what it means for us» |
| «trend» | «growing/declining» | [tag] | «what it means for us» |
| «trend» | «growing/declining» | [tag] | «what it means for us» |

## 1.4 Regulatory Landscape

<!-- fill: Jurisdiction-specific. This shapes the data model and architecture — it is not
     a footnote. Identify the regimes that apply, what each requires, and the cost of
     compliance. If a vertical pack is loaded, draw from it. -->

| Regime | Applies because | Requires | Impact on build |
| --- | --- | --- | --- |
| «e.g. HIPAA» | «reason» | «obligations» | «design consequence» |

**Compliance cost estimate:** «figure or "not established"» [tag]

## 1.5 Market Gaps

«What the market is not currently served well on.» [tag]

---

# 2. Users

## 2.1 Segments

| Segment | Size | Pain intensity | Ability to pay | Reachable? | Priority |
| --- | --- | --- | --- | --- | --- |
| «segment» | «n» [tag] | «high/med/low» | «high/med/low» | «how» | 1 |
| «segment» | «n» [tag] | «high/med/low» | «high/med/low» | «how» | 2 |

**Segment targeted first: «segment»** — «why. Must reference the table, not preference.»

## 2.2 Personas

<!-- fill: One per prioritized segment. Grounded in the research, not invented.
     A persona that could describe anyone describes no one. -->

### «Persona name» — «role»

| | |
| --- | --- |
| Context | «where and how they work» |
| Goal | «what success looks like to them» |
| Frustration | «what makes the current situation bad» |
| Constraints | «time, budget, technical skill, regulation» |
| Buys or uses? | «buyer / user / both» |
| Decision trigger | «what would make them switch» |

## 2.3 Jobs To Be Done

<!-- fill: Jobs, not features. "When I «situation», I want to «motivation», so I can
     «outcome»." If it names a feature, it is not a job. -->

| # | Job | Frequency | Currently satisfied by |
| --- | --- | --- | --- |
| J1 | When «situation», I want to «motivation», so I can «outcome» | «daily/weekly» | «today's tool» |
| J2 | ... | | |

## 2.4 Current Workflow

<!-- fill: What actually happens today, step by step, including the tools being used.
     This is where the real opportunity is usually found — in the friction between steps. -->

```
«step 1» → «step 2» → «step 3» → «step 4»
```

**Where it breaks:** «the friction points» [tag]

**Tools being replaced:** «named products»

## 2.5 Switching Cost

<!-- fill: What it costs them to adopt this — in data migration, retraining, workflow
     disruption, contract lock-in, and risk. Underestimating this kills products. -->

| Cost type | Magnitude | Mitigation |
| --- | --- | --- |
| Data migration | «high/med/low» | «approach» |
| Retraining | «high/med/low» | «approach» |
| Workflow disruption | «high/med/low» | «approach» |
| Contractual lock-in | «high/med/low» | «approach» |

---

# 3. Competition

## 3.1 Competitor Matrix

<!-- fill: Minimum five, direct and indirect. "Doing nothing" and "spreadsheet + paper"
     are competitors and usually the strongest ones. Include them. -->

| Competitor | Type | Segment served | Pricing | Strength | Weakness |
| --- | --- | --- | --- | --- | --- |
| «name» | direct | «segment» | «price» [tag] | «strength» | «weakness» |
| «name» | indirect | «segment» | «price» [tag] | «strength» | «weakness» |
| **Status quo** | incumbent | all | free | «why it persists» | «where it hurts» |

## 3.2 Feature Comparison

| Capability | «Comp A» | «Comp B» | Status quo | Us (proposed) |
| --- | --- | --- | --- | --- |
| «capability» | ✓ | ✗ | ✗ | ✓ |

## 3.3 Pricing Comparison

| Competitor | Model | Entry price | Notes |
| --- | --- | --- | --- |
| «name» | «subscription/usage/license» | «figure» [tag] | «what is included» |

## 3.4 Gap Analysis

<!-- fill: Where is the actual opening? Be specific and defensible.
     "Better UX" is not a gap. "No incumbent supports «X» for «segment» because «reason»"
     is a gap. State WHY the gap exists — if there is no reason, it may not be real. -->

**The gap:** «one paragraph»

**Why it exists and persists:** «the reason incumbents have not closed it» [tag]

**Why it is defensible (or is not):** «honest assessment»

## 3.5 Positioning

«One sentence: for «segment» who «need», «product» is a «category» that «benefit», unlike «alternative».»

---

# 4. Sources

<!-- fill: Every [verified] tag above resolves to an entry here. If a reader cannot
     retrieve it from this list, it was not verified. -->

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation with URL or publication» | «report/vendor page/regulation» | «date» | «claims» |

---

# 5. Evidence Standing

| | Count |
| --- | --- |
| Verified claims | «n» |
| Inferred claims | «n» |
| Open assumptions | «n» |

**Largest evidence gap:** «what is least established, and what would close it»

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Market defined by boundary, not adjective
- [ ] TAM/SAM/SOM each sourced or explicitly marked assumption
- [ ] >= 3 trends with direction and evidence
- [ ] Regulatory constraints for the named jurisdiction identified, including its general data-protection regime
- [ ] >= 2 segments with a stated reason for prioritizing one
- [ ] Jobs stated as jobs, not features
- [ ] Current workflow documented including tools being replaced
- [ ] >= 5 competitors including status quo
- [ ] Every claim carries exactly one evidence tag
- [ ] Every [verified] resolves to an entry in Sources
- [ ] Every fill comment removed
-->
