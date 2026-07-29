---
Title: Template
Module: 06-business
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Business Model — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 06-business/core/06-Framework.md
Outputs:
  - projects/<slug>/research/06-business.md
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Template
  - Output
---

# Template — Business Model

---

# Usage

Copy everything below the line into `projects/<slug>/research/06-business.md` and fill it.

This is a **working document**. It feeds the Executive Summary, the Research Dossier, and
the pricing sections of the PRD.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**Arithmetic does not create evidence.** Every number in this document that was not
sourced must carry an assumption tag, however precise the calculation around it looks.

---
---

# Business Model — «Project Name»

| | |
| --- | --- |
| Module | 06-business |
| Date | «ISO date» |
| Segment | «prioritized segment from 03-user» |
| Status | draft / complete |
| Confidence | «high / medium / low» |

---

## 1. Viability Verdict

<!-- Write this last. State it first. -->

**«VIABLE | VIABLE WITH CONDITIONS | NOT VIABLE AS MODELED | INSUFFICIENT EVIDENCE»**

«Two sentences. Does a business exist here, and what would have to be true?»

| | |
| --- | --- |
| Sourced inputs | «n» |
| Assumed inputs | «n» |
| The assumption that most changes the outcome | «which» |

---

## 2. The Payer

<!-- Entry 1. Who signs. Distinguished from who uses, even when they are the same. -->

| | | Evidence |
| --- | --- | --- |
| User | «who uses it» | from 03-user |
| **Payer** | «who pays» | [tag] |
| Same person? | «yes / no» | — |
| Budget it comes from | «which line» | [tag] |
| Approval needed from | «who else signs off» | [tag] |
| Who could block it | «role» | from 03-user |

**If payer ≠ user, what the payer needs to see:** «their criterion, which differs from
the user's» [tag]

**Purchase trigger:** «what event makes them buy now rather than later» [tag]

<!-- Willingness, ability and authority to pay are three different things.
     A user who wants it, in an organization that can afford it, still needs
     someone with authority to sign. -->

| | Assessment | Evidence |
| --- | --- | --- |
| Willingness to pay | «assessment» | [tag] |
| Ability to pay | «assessment» | [tag] |
| Authority to pay | «assessment» | [tag] |

---

## 3. Value Delivered

<!-- Entry 2. Establish value BEFORE price. Value comes from 04-problem's cost
     per occurrence. Price is then a fraction of value, anchored by competitors. -->

| Problem | Cost per occurrence | Frequency | Annual cost to them | Source |
| --- | --- | --- | --- | --- |
| P1 | «figure» | «n/year» | «figure» | from 04-problem [tag] |
| P2 | «figure» | «n/year» | «figure» | [tag] |

**Total annual value at stake:** «figure»

**Realistic share the product captures:** «%» — «reasoning» [tag]

**Value delivered per customer per year:** «figure»

**Is this value visible to the payer?** «yes / no»

<!-- An absorbed cost — unpaid overtime, a normalized workaround — is real but not
     felt. It is much harder to sell against. If module 04 flagged the cost as
     absorbed, say so here; it changes the sales difficulty, not the value. -->

---

## 4. Pricing

<!-- Entry 3. Anchored to two things: competitor pricing from 05, and value from §3.
     Never to instinct. -->

### Competitor anchors

| Competitor | Price | Model | Source |
| --- | --- | --- | --- |
| «name» | «figure» | «model» | from 05-competition [tag] |
| **Status quo** | free | — | — |

**Market range:** «low – high»

### Our price

| | |
| --- | --- |
| Model | «subscription / usage / license / freemium» |
| Price | «figure per unit per period» |
| Unit | «per user / per practice / per transaction» |
| Billing period | «monthly / annual» |

**Justification against value:** «price is «n»% of annual value delivered» — «reasoning»

**Justification against competitors:** «above / below / at market, and why»

**Justification against free:** «why someone pays when the status quo costs nothing»

<!-- The last one is mandatory whenever the status quo is free, which is usually. -->

### Packaging

| Tier | Price | For whom | Includes |
| --- | --- | --- | --- |
| «name» | «figure» | «segment» | «scope» |

**What we deliberately do not do:** «e.g. no free tier — and why»

---

## 5. Unit Economics

<!-- Entry 4. THE ARITHMETIC TRAP LIVES HERE.
     A model built from six guesses produces a precise-looking answer that is a guess.
     Tag every input. State which one the outcome depends on most. -->

| Input | Value | Basis | Tag |
| --- | --- | --- | --- |
| Price per customer per year | «figure» | §4 | [tag] |
| Gross margin | «%» | «cost to serve» | [tag] |
| Cost to acquire (CAC) | «figure» | «channel assumption» | [tag] |
| Annual churn | «%» | «basis» | [tag] |
| Customer lifetime | «years» | `1 / churn` | derived |
| Lifetime value (LTV) | «figure» | `price × margin × lifetime` | derived |
| LTV : CAC | «ratio» | derived | — |
| Payback period | «months» | `CAC / (monthly price × margin)` | derived |

**Cost to serve, per customer per year**

| Component | Cost | Basis |
| --- | --- | --- |
| Infrastructure | «figure» | «from 07-Architecture estimate, if available» [tag] |
| Support | «figure» | «tickets × time × rate» [tag] |
| Third-party / AI costs | «figure» | «per-operation × volume» [tag] |
| **Total** | «figure» | |

**The load-bearing assumption:** «which input, if wrong by 50%, changes the verdict»

**Sensitivity**

| If this changes | Verdict becomes |
| --- | --- |
| CAC doubles | «viable / not» |
| Churn doubles | «viable / not» |
| Price halves | «viable / not» |

<!-- Sensitivity is more honest than a point estimate when most inputs are assumed. -->

---

## 6. Revenue Model

| | |
| --- | --- |
| Revenue type | «recurring / transactional / one-off / hybrid» |
| Predictability | «high / medium / low» |
| Expansion path | «how revenue per customer grows» |
| Year 1 revenue at «n» customers | «figure» |
| Customers needed to cover fixed costs | «n» |

**Break-even assumption:** «what fixed cost base is assumed» [tag]

---

## 7. Go To Market

<!-- Entry 5. The reality test of this module. -->

### The first 10 customers

<!-- Name them, or describe them specifically enough to go and find them.
     "Marketing" is not a plan for the first ten. If this section cannot be
     filled concretely, the go-to-market does not exist yet. -->

| # | Who | How reached | Why they would say yes | Status |
| --- | --- | --- | --- | --- |
| 1 | «named org or specific profile» | «specific route» | «their reason» | «prospect / warm / cold» |

**The pitch, in one sentence:** «what you say to them»

**Existing access:** «any relationship, channel or audience already available» [tag]

### Channels

| Channel | Reaches | Cost per acquisition | Effort | Priority |
| --- | --- | --- | --- | --- |
| «channel» | «segment» | «figure» [tag] | «S/M/L» | 1 |

**Sales motion:** «self-serve / founder-led / inside sales / partner»

**Sales cycle length:** «duration» [tag]

<!-- Sales cycle interacts with runway. A 9-month enterprise cycle and 12 months of
     funding is a finding, not a detail. -->

---

## 8. Cost Structure

| Cost | Type | Year 1 | At scale | Basis |
| --- | --- | --- | --- | --- |
| Build | one-off | «figure» | — | «team × duration» [tag] |
| Infrastructure | variable | «figure» | «figure» | [tag] |
| Support | variable | «figure» | «figure» | [tag] |
| Compliance | fixed | «figure» | «figure» | from 02-market [tag] |
| Sales and marketing | variable | «figure» | «figure» | [tag] |

**Regulatory cost carried from module 02:** «figure» — «what it covers»

---

## 9. Viability Test

<!-- Entry 6. Does the arithmetic survive contact with reality? -->

| Test | Threshold | Actual | Pass? |
| --- | --- | --- | --- |
| LTV : CAC | > 3 | «ratio» | «yes/no» |
| Payback period | < 12 months | «months» | «yes/no» |
| Gross margin | > 60% for software | «%» | «yes/no» |
| Price vs value delivered | < 30% of value | «%» | «yes/no» |
| Customers to break even reachable in year 1? | — | «n vs SOM» | «yes/no» |

**Where the model breaks:** «the first threshold to fail as assumptions worsen»

**What would have to be true for this to work:** «stated plainly»

---

## 10. Contradicting Evidence

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against viability» | [tag] | «what it would mean» | «how addressed» |

<!-- E.g. competitors priced far below the modeled price; the segment's software
     budget is smaller than the price; a free incumbent is well funded. -->

---

## 11. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `business_model` | «summary» | 07-strategy |
| `pricing_strategy` | «price and model» | 07, 08, 11 |
| `unit_economics` | «LTV:CAC, payback, margin» | 07, 12 |
| `go_to_market` | «channels, first 10» | 11-growth |
| `revenue_model` | «type and projection» | 12-metrics |

**Cost-to-serve constraint for module 09:** «the per-customer infrastructure budget the
architecture must stay inside»

---

## 12. Sources

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation» | pricing page / report / benchmark | «date» | «claims» |

---

## 13. Evidence Standing

| | Count |
| --- | --- |
| Sourced inputs | «n» |
| Inferred inputs | «n» |
| Assumed inputs | «n» |

**Confidence:** «high / medium / low»

<!-- If most inputs are assumed — which is normal without primary research —
     confidence cannot exceed low, regardless of how complete the model looks. -->

**What would raise it:** «the two or three inputs most worth establishing»

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] Verdict stated first
- [ ] Payer identified and distinguished from user, even when identical
- [ ] Willingness, ability and authority to pay assessed separately
- [ ] Value established BEFORE price, from 04-problem's cost figures
- [ ] Price justified against value, against competitors, and against free
- [ ] Every unit-economics input carries a tag
- [ ] The load-bearing assumption named
- [ ] Sensitivity table completed
- [ ] First 10 customers named or specifically profiled
- [ ] Sales cycle length stated
- [ ] Regulatory cost from module 02 carried forward
- [ ] Viability thresholds tested and failures stated
- [ ] Contradicting evidence non-empty
- [ ] Confidence consistent with the sourced/assumed ratio
- [ ] Every placeholder replaced, every guidance comment removed
-->
