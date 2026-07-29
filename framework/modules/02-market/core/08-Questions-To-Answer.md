---
Title: Questions To Answer
Module: 02-market
Section: core
Category: Interrogation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The question bank the agent works through to bound, size and characterize a market.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 02-market/core/06-Framework.md
Outputs:
  - Filled sections of the Market Analysis
  - state.open_questions
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - Questions
  - Research
---

# Questions To Answer

---

# Overview

Unlike `01-idea`, almost every question here is **the agent's to answer through research**,
not the operator's.

If a question in this module is being sent to the operator, check first whether it is
actually researchable. Asking a human for a market size is outsourcing the module's job.

The exceptions are marked **OPERATOR**.

---

# 1. Boundary

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | Who has this need? | The market has no population |
| 1.2 | What need, stated precisely? | The boundary is an adjective |
| 1.3 | In which jurisdiction? | Inherited from `idea_brief` — never re-decided here |
| 1.4 | What is explicitly outside this market? | The market will quietly widen in module 05 |
| 1.5 | What do practitioners call this category? | Later research will use wrong search terms |
| 1.6 | Take one borderline case — in or out? | The boundary has not actually been drawn |

> **1.6 is the test that proves the boundary exists.** If a borderline case cannot be
> ruled on, sections 2–5 are being built on nothing.

---

# 2. Regulation

<!-- This section runs before sizing. Regulation determines who may participate. -->

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | Which regimes apply in this jurisdiction? | Compliance surfaces at module 09, structurally |
| 2.2 | What triggers each regime — data type, entity type, activity? | Applicability is guesswork |
| 2.3 | What concrete obligations does each impose? | Module 09 receives regime names, not requirements |
| 2.4 | Is licensing or certification required to sell? | Barrier to entry unknown |
| 2.5 | What does clearing that barrier cost, in money and time? | Feasibility unknown |
| 2.6 | Does regulation exclude any segment named in the idea brief? | The run may be researching an unservable segment |
| 2.7 | Is regulation tightening, stable, or loosening? | Timing risk invisible |
| 2.8 | Are there data residency or cross-border constraints? | Architecture may be invalid |

**2.6 can end this module.** If the answer is yes, return to `01-idea`.

---

# 3. Size

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | How many potential buyers exist inside the boundary? | No TAM |
| 3.2 | What proportion can be legally and practically served? | No SAM |
| 3.3 | What could realistically be won in year one? | No SOM |
| 3.4 | What price point is being assumed, and on what basis? | The sizing rests on an invisible assumption |
| 3.5 | Was this built bottom-up or taken top-down? | The boundary may be borrowed |
| 3.6 | If both methods were used, do they agree? | A material disagreement is a finding |
| 3.7 | Which single input, if wrong, changes the figure most? | The load-bearing assumption is unidentified |

<!-- 3.7 identifies what to validate first. Usually it is price or adoption rate,
     not population count. -->

---

# 4. Trends

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | Is the underlying need growing or shrinking? | Direction unknown |
| 4.2 | Are new entrants arriving or leaving? | Supply-side blind |
| 4.3 | What recently became technically possible or affordable? | Timing rationale missing |
| 4.4 | What is changing in regulation? | Future barriers invisible |
| 4.5 | What are buyers doing differently than five years ago? | Behavioral shift missed |
| 4.6 | **Which trend argues against this idea?** | The research was selective |
| 4.7 | Is this early, on time, or late? | Timing risk unnamed |

> **4.6 is mandatory.** Every market has forces pushing both ways. An analysis where
> every trend is favorable is an analysis that stopped looking.

---

# 5. Gaps

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | Which segments are underserved? | No opening identified |
| 5.2 | What need goes unmet inside the boundary? | The gap is vague |
| 5.3 | **Why has this gap persisted?** | The gap is probably not real |
| 5.4 | Has anyone tried and failed to close it? | A paid-for lesson is being ignored |
| 5.5 | Is the gap structural or temporary? | Defensibility unknown |

For 5.3, the answer is one of: regulation, economics, distribution, data access,
incentives — or "no reason found", which is itself a finding and a reason for suspicion.

---

# 6. Structure

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | Is this market emerging, growing, mature, or declining? | Strategy has no context |
| 6.2 | Is it fragmented, consolidating, or dominated? | Entry difficulty unknown |
| 6.3 | Who holds the budget? | Module 06 has no payer |
| 6.4 | How do buyers in this market normally buy? | Go-to-market has no shape |
| 6.5 | How often do they switch provider? | Displacement difficulty unknown |

---

# 7. Questions for the Operator

Only these belong at a checkpoint. Everything above is researchable.

| # | Question | When to ask |
| --- | --- | --- |
| O1 | **OPERATOR** — Do you have existing access or distribution in this market? | Changes SOM materially |
| O2 | **OPERATOR** — Are you constrained to one jurisdiction, or is expansion in scope? | Changes TAM and the regulatory workload |
| O3 | **OPERATOR** — Is there a segment you would refuse to serve? | Bounds the market from the business side |

These are deferrable. Record an assumption and proceed; they do not halt the run.

---

# 8. Questions the Agent Asks Itself

- Did I draw the boundary to make the number look larger?
- Did I adopt a report's figure whose boundary I never checked?
- Would a domain practitioner recognize my category name?
- Did I check regulation before sizing, or after?
- Have I found a single fact that argues against this market?
- Am I doing module 05's work — naming competitors, comparing features?
- Could a reader challenge my TAM, or did I present it without a derivation?

---

# Anti-Patterns

| Anti-pattern | Example | Why it fails |
| --- | --- | --- |
| Asking the operator to research | "How big is this market?" | That is this module's job |
| Adjective boundary | "The healthcare market" | Cannot be measured or ruled on |
| Borrowed TAM | "$29.8B per «report»" with no boundary check | Sizes a different market |
| Trend without direction | "AI is important in healthcare" | An observation, not a trend |
| Gap without a reason | "Nobody serves solo practices" | Usually means the search stopped early |
| Competitor detail | A feature comparison table | Belongs to module 05 |

---

> **Interrogation Principle**
>
> In this module, a question sent to the operator is usually a question the
> agent did not want to research.
>
> Research first. Ask only what the operator alone can know.
