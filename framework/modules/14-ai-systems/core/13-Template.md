---
Title: Template
Module: 14-ai-systems
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the AI Systems plan — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - projects/<slug>/research/14-ai-systems.md
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Template
  - Output
---

# Template — AI Systems

---

# Usage

Copy everything below the line into `projects/<slug>/research/14-ai-systems.md` and fill it.

This is a **working document**. It feeds:

| Deliverable | Fed by | Required |
| --- | --- | --- |
| `15-AI-Strategy.md` | all sections | optional — emitted when the run's scope calls for it |
| `03-PRD.md` | §4 capability detail, §8 acceptance | required |
| `12-Build-Handoff.md` | §4, §7, §9 — guardrails and fallbacks | required |

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**The discipline that governs this module:** every capability is justified against a genuine
non-AI alternative, and **dropping a capability is a successful outcome**. A module that proposes
five AI features and keeps one has done its job.

**If this product has no AI component**, that is a legitimate and complete answer. Fill §1 and
§2, state it, and skip the rest.

---
---

# AI Systems — «Project Name»

| | |
| --- | --- |
| Module | 14-ai-systems |
| Date | «ISO date» |
| Capabilities proposed | «n» |
| Capabilities kept | «n» |
| Regulated data in scope | «yes — regime / no» |
| Revenue per user per month | «figure, from 06-business» |
| Status | draft / reviewed / gated |

---

## 1. The Position, in One Paragraph

<!-- Write last. Which capabilities are served by a model, why each beat its alternative, and
     what happens when each is wrong. -->

«One paragraph.»

---

## 2. Candidate Capabilities and the Non-AI Alternative

<!-- Move 1 and 2. The alternative column is mandatory and must be a real attempt.
     A straw man here invalidates the whole module. -->

| # | Capability | Job served | Non-AI alternative | Which wins, and why | Verdict |
| --- | --- | --- | --- | --- | --- |
| AI1 | «capability» | J«n» | «the honest alternative» | «reasoning» | build |
| AI2 | «capability» | J«n» | «the honest alternative» | «the alternative wins» | drop |

**Dropped, and what was adopted instead:** «capability → the rule, form, lookup or default that
solved it»

**The advocate check:** «for each capability kept, could a competent person argue for the non-AI
alternative in one honest sentence? If not, the alternative was a straw man and the comparison
proved nothing.»

---

## 3. Where the Model Sits

<!-- Consistent with `09-technology` §8. This module does not invent architecture; it places
     the capability inside the one that exists. -->

| Capability | Component | Called when | Data it receives | Data it must never receive |
| --- | --- | --- | --- | --- |
| AI«n» | «from `09-technology` §8» | «trigger» | «fields» | «fields» |

---

## 4. Capability Detail

### AI«n» — «capability name»

| | |
| --- | --- |
| Job served | J«n» |
| Requirement served | R«n», from `08-product` |
| User-visible behavior | «what the user experiences» |
| **Autonomy level** | suggests / drafts / acts with confirmation / acts autonomously |
| Input | «what the model receives» |
| Output shape and constraints | «structure, length, allowed values» |
| Latency budget | «duration, from the flow requirements in `10-execution`» |
| Non-AI fallback | «what happens when it is unavailable — a requirement, not a contingency» |

### The Wrongness Cost

<!-- The question that determines the autonomy level. -->

| | |
| --- | --- |
| What one wrong output costs | «stated in the user's terms» |
| Who bears that cost | «the user / the operator / a third party» |
| **Can the user detect it is wrong?** | «yes — how / no» |
| Is it recoverable, and how | «answer» |
| **Autonomy justified because** | «reasoning against the above» |

> Where the user bears the cost and **cannot detect** the error, autonomy above "suggests" is not
> permitted without a mechanism that makes the error visible.

---

## 5. Model Strategy

| | |
| --- | --- |
| Approach | API model / fine-tune / retrieval-augmented / classical ML / rules + model hybrid |
| Provider and model | «who, which» |
| Version pinned | «version» — `[verified: source, date]` |
| Why this approach | «reasoning, with the rejected alternative» |
| Cost per operation | «figure» `[verified: published price, date]` |
| Latency, measured or claimed | «figure» `[tag]` |
| Fallback model | «if the primary is unavailable» |
| Deprecation exposure | «what happens when this model version is retired» |
| Vendor lock-in | «assessment, and what switching would require» |

<!-- Model capabilities, limits and prices are version-scoped and change. Cite them with a
     version and a date, exactly as `09-technology` requires of every technology claim. -->

---

## 6. Data

<!-- Move 3. Availability is CONFIRMED, not assumed. This is the most common way an AI
     capability fails before it starts. -->

| Need | Source | Available now | Volume | Quality | Blocker |
| --- | --- | --- | --- | --- | --- |
| «training / grounding data» | «where» | «yes / no» `[tag]` | «n» | «assessment» | «what stands in the way» |

**Data we assumed exists and have not confirmed:** «none, or list — each is a blocker, not a
risk»

**Cold start:** «how the capability behaves before any data has accumulated. Most AI features are
at their worst exactly when the product is newest.»

### Data Rights

<!-- A legal question, not a technical one. -->

| | |
| --- | --- |
| Do we have the right to use this data this way | «yes / no / unknown» `[tag]` |
| Under which regime | «from `02-market`» |
| Is consent required, and do we have it | «answer» |
| Does the data leave our systems | «yes — to «provider», in «jurisdiction» / no» |
| Regulated or PII fields sent to a provider | «none — verified / list, which fails the gate» |
| Is provider training on our data disabled | «yes — how it is contracted / no» |

> Sending a regulated field to a model provider is the same class of exposure as putting one in an
> analytics event. Check the classification in `09-technology` §3 against every model input,
> mechanically.

---

## 7. Human Oversight and Transparency

<!-- Move 4. -->

| Capability | Review required | Who reviews | User can override | Override recorded |
| --- | --- | --- | --- | --- |
| AI«n» | always / sampled / never | «role» | yes / no | yes / no |

| | |
| --- | --- |
| Audit trail for AI-generated content | «what is recorded» |
| AI involvement disclosed to the user | «yes — how / no» |
| AI-generated content labeled | «yes — how / no» |
| User can see why a suggestion was made | «yes / no» |
| Regulatory disclosure obligation | «regime and obligation» `[tag]` |

**Who reviews, and what qualifies them:** «in a domain product this must usually be a domain
expert. The build team cannot assess clinical, legal or financial correctness, and their
confidence in the output is not evidence about it.»

---

## 8. Evaluation

<!-- Move 5. Defined BEFORE the capability is committed to. "We will evaluate it" is not a plan. -->

| Capability | Metric | Method | Passing bar | Sample size | Cadence |
| --- | --- | --- | --- | --- | --- |
| AI«n» | «e.g. factual accuracy» | golden set / human review / A-B | «figure» | «n» | «cadence» |

| | |
| --- | --- |
| Golden set — how constructed | «and how it is kept honest, i.e. never used for tuning» |
| Who judges | «role, and their qualification» |
| **Ship gate** | «the result required before users see this» |
| What happens if the bar is not met | «the capability does not ship — state it» |
| Regression check | «how a model or prompt change is re-evaluated before release» |

### Acceptance Criteria for a Nondeterministic Capability

<!-- `08-product` requires acceptance criteria that can fail. For a model-served capability,
     they are STATISTICAL rather than per-instance. Both forms are required. -->

| Type | Form | Example |
| --- | --- | --- |
| Statistical | «bar» over «sample» | "≥95% of 200 golden-set cases judged correct by «reviewer»" |
| Deterministic | Always true, per instance | "Output never exceeds «n» characters", "Output always contains a citation", "The user can always dismiss it" |

**Per-instance guarantees for this capability:** «the things that must be true every single time —
these are testable in the ordinary way and belong in `08-product`'s criteria»

---

## 9. Failure Modes

<!-- Move 6. Specific to THIS product. "The model may hallucinate" is not a failure mode. -->

| # | Failure mode | Likelihood | What it costs the user | Detection | Guardrail |
| --- | --- | --- | --- | --- | --- |
| F1 | «specific, concrete failure» | h/m/l | «consequence» | «how it is caught» | «mechanism» |

| | |
| --- | --- |
| **Worst realistic outcome** | «state it plainly» |
| Would we know it happened | «yes — how / no» |
| Human fallback | «what the user does when it is wrong, and how they notice» |
| Silent failure risk | «the failures that produce plausible wrong output with no signal» |

> **The plausibility problem.** A model's errors are fluent. They arrive in the same register as its
> correct answers, which means error rate matters less than **detectability**. A capability whose
> mistakes look exactly like its successes needs a guardrail, not a better prompt.

**Handed to `13-operations`:** «which failure modes need an alert, a runbook, or a support script»

---

## 10. Cost

| Capability | Cost per operation | Operations per user per month | Cost per user per month |
| --- | --- | --- | --- |
| AI«n» | «figure» `[tag]` | «n» `[tag]` | «figure» |

| | |
| --- | --- |
| **Total AI cost per user per month** | «figure» |
| Revenue per user per month | «figure, from `06-business`» |
| **AI cost as a share of revenue** | «percentage» |
| Acceptable | «yes / no» |

**If the share is large:** «say so plainly. A capability consuming a significant fraction of
revenue per user is a margin problem, and it has killed products. The options are a cheaper
approach, a lower operation count, a higher price, or dropping the capability.»

**Handed to the cost model:** «this figure goes to `09-technology` §12 and `13-operations` §11 as a
line in the cost to serve»

---

## 11. Assumptions

| # | Assumption | Impact if wrong | Cheapest validation |
| --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «test» |

<!-- Every quality expectation, operation count, latency figure and cost estimate is an
     assumption until measured on this product's real inputs. -->

---

## 12. Contradicting Evidence

<!-- Required and non-empty. What argues against using a model here at all? -->

- «finding that argues against a kept capability»

---

## 13. Confidence

| | |
| --- | --- |
| Confidence in the capability choices | «based on the non-AI comparisons» |
| Confidence in the quality expectations | «usually low until measured on real inputs» |
| Weakest element | «what, and why» |
| What would raise it | «a specific measurement» |

---

## 14. Handoff

| Consumer | What it takes from here |
| --- | --- |
| `08-product` | Per-instance guarantees, as ordinary acceptance criteria |
| `09-technology` | Model placement, data flow, cost line |
| `12-metrics` | Quality metrics and their instrumentation |
| `13-operations` | Failure modes needing alerts, runbooks or support scripts |
| `12-Build-Handoff.md` | Guardrails, fallbacks, output constraints |
| `15-AI-Strategy.md` | All sections |

---

<!-- ACCEPTANCE — remove before completing
- [ ] Every capability compared against a genuine non-AI alternative
- [ ] The advocate check passed — the alternatives were not straw men
- [ ] Dropped capabilities recorded, with what was adopted instead
- [ ] Autonomy level justified against the wrongness cost and detectability
- [ ] Model version pinned and cited with a date
- [ ] Data availability confirmed, not assumed — unconfirmed needs listed as blockers
- [ ] Cold-start behavior stated
- [ ] Data rights answered, including whether data leaves the system
- [ ] No regulated or PII field sent to a provider
- [ ] Evaluation method, passing bar and ship gate defined before commitment
- [ ] Who judges quality, and what qualifies them
- [ ] Statistical and per-instance criteria both present
- [ ] Failure modes specific to this product
- [ ] Detectability addressed, not just error rate
- [ ] Human fallback specified as a requirement
- [ ] AI cost per user compared against revenue per user
- [ ] Every «placeholder» replaced and every guidance comment removed
-->

---

> **Template Principle**
>
> The best outcome of this document is often a shorter product.
>
> A capability dropped here because a form field solved the problem
> is the module working exactly as intended.
