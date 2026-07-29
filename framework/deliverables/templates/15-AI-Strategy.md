---
Artifact: ai-strategy
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [14-ai-systems]
Required: false
---

<!-- fill: Every AI capability must be justified AGAINST A NON-AI ALTERNATIVE. This is the
     discipline that keeps AI from being decoration. If a rule, a lookup table, or a
     better-designed form solves the problem, that is the correct answer — say so and
     drop the capability.
     Evaluation is defined BEFORE the capability is committed to. A feature nobody can
     measure is a feature nobody can fix.
     Remove every <!-- fill --> comment before delivery. -->

# AI Strategy — «Product Name»

## 1. Where AI Genuinely Helps

<!-- fill: One row per proposed capability. The "non-AI alternative" column is mandatory
     and must be a real attempt, not a straw man. Capabilities where the non-AI
     alternative wins are DROPPED — and that is a successful outcome of this analysis. -->

| # | Capability | Job served | Non-AI alternative | Why AI wins (or does not) | Verdict |
| --- | --- | --- | --- | --- | --- |
| AI1 | «capability» | J«n» | «the honest alternative» | «reasoning» | build |
| AI2 | «capability» | J«n» | «the honest alternative» | «alternative is better» | drop |

**Dropped capabilities:** «list, with the non-AI solution adopted instead»

---

## 2. Capability Detail

### AI«n» — «capability name»

| | |
| --- | --- |
| Job served | J«n» |
| User-visible behavior | «what the user experiences» |
| Autonomy level | «suggests / drafts / acts with confirmation / acts autonomously» |
| Non-AI fallback | «what happens when it is unavailable or wrong» |

**Why this level of autonomy:** «reasoning — in high-stakes domains, "suggests" is
usually correct and "acts autonomously" requires justification»

**Input:** «what the model receives»
**Output:** «shape and constraints»

---

## 3. Model Strategy

| | |
| --- | --- |
| Approach | «API model / fine-tune / retrieval-augmented / classical ML / hybrid» |
| Provider | «who» |
| Model | «which» |
| Why this approach | «reasoning» |
| Cost per operation | «figure» [tag] |
| Latency budget | «duration — from the UX flow requirements» |
| Fallback model | «if primary unavailable» |
| Vendor lock-in risk | «assessment and mitigation» |

---

## 4. Data Requirements

<!-- fill: Confirm availability. Do not assume data exists — this is the most common
     way AI features fail before they start. -->

| Need | Source | Available now? | Volume | Quality | Blocker |
| --- | --- | --- | --- | --- | --- |
| «training / grounding data» | «where from» | «yes/no» [tag] | «n» | «assessment» | «what stands in the way» |

**Cold start:** «how the capability behaves before any data has accumulated»

**Data rights:** «do we have the right to use this data this way? Under which regime?»
[tag]

<!-- fill: In regulated domains this is a legal question, not a technical one.
     Using patient or financial data for model input may require explicit consent. -->

---

## 5. Evaluation Plan

<!-- fill: Defined BEFORE building. State how quality is measured, what the passing bar
     is, and what happens when it is not met. "We will evaluate it" is not a plan. -->

| Capability | Metric | Method | Passing bar | Sample size | Cadence |
| --- | --- | --- | --- | --- | --- |
| AI«n» | «e.g. factual accuracy» | «human review / golden set / A-B» | «figure» | «n» | «cadence» |

**Golden set:** «how the evaluation set is constructed and kept honest»

**Who judges quality:** «and what qualifies them — in a domain product, this usually
must be a domain expert, not the build team»

**Ship gate:** «the result required before this reaches users»

---

## 6. Failure Modes

<!-- fill: Be specific to this product. "The model may hallucinate" is generic.
     "The model may invent a drug interaction that does not exist, which a rushed
     clinician could accept" is a failure mode you can design against. -->

| # | Failure mode | Likelihood | Consequence | Detection | Mitigation |
| --- | --- | --- | --- | --- | --- |
| F1 | «specific failure» | «h/m/l» | «what it costs the user» | «how it is caught» | «guardrail» |

**Worst realiztic outcome:** «state it plainly»

**Human fallback:** «what the user does when the AI is wrong, and how they notice»

---

## 7. Human Oversight

| Capability | Review required | Who reviews | Can the user override? | Is the override recorded? |
| --- | --- | --- | --- | --- |
| AI«n» | «always / sampled / never» | «role» | «yes/no» | «yes/no» |

**Audit trail:** «what is recorded about AI-generated content — in regulated domains
this is usually mandatory»

---

## 8. Transparency

| | |
| --- | --- |
| Is AI involvement disclosed to the user? | «yes/no — and how» |
| Is AI-generated content labelled? | «yes/no — and how» |
| Can the user see why a suggestion was made? | «yes/no» |
| Regulatory disclosure requirement | «regime and obligation» [tag] |

---

## 9. Cost Model

| Capability | Cost per operation | Operations per user/mo | Cost per user/mo |
| --- | --- | --- | --- |
| AI«n» | «figure» [tag] | «n» [tag] | «figure» |

**Total AI cost per user per month:** «figure»

**Against price point:** «compare to pricing in the dossier. If AI cost exceeds a
meaningful share of revenue per user, say so — this has killed products.»

---

## 10. AI Assumptions

| # | Assumption | Impact if wrong | Validation |
| --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «test» |

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Each capability justified against a genuine non-AI alternative
- [ ] Capabilities where the non-AI alternative wins are dropped and recorded
- [ ] Training / grounding data availability confirmed, not assumed
- [ ] Data rights checked against the regulatory regime
- [ ] Evaluation method, passing bar and ship gate defined before commitment
- [ ] Failure modes specific to this product, not generic
- [ ] Human fallback and oversight specified
- [ ] Cost per user compared against the price point
- [ ] Every fill comment removed
-->
