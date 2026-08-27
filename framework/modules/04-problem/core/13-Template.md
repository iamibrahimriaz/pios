---
Title: Template
Module: 04-problem
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Problem Analysis — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - projects/<slug>/research/04-problem.md
Related Modules:
  - 05-competition
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Template
  - Output
---

# Template — Problem Analysis

---

# Usage

Copy everything below the line into `projects/<slug>/research/04-problem.md` and fill it.

This is a **working document**. It feeds `deliverables/templates/02-Problem-Validation.md`
almost directly, plus the Research Dossier and the PRD.

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**Validated and assumed problems stay visually separate throughout this document.**
Never blend them in prose. The separation is the point of the module.

---
---

# Problem Analysis — «Project Name»

| | |
| --- | --- |
| Module | 04-problem |
| Date | «ISO date» |
| Persona | «primary persona from 03-user» |
| Status | draft / complete |
| Confidence | «high / medium / low» |

---

## 1. Verdict

<!-- State this first. It is the single most consequential line in the run. -->

**«VALIDATED | PARTIALLY VALIDATED | UNVALIDATED | INVALIDATED»**

«Two sentences on what that means for whether to proceed.»

| | |
| --- | --- |
| Problems identified | «n» |
| Carrying `[verified]` evidence | «n» |
| Assumed only | «n» |
| Is the sharpest problem verified? | «yes / no» |

<!-- If the sharpest problem is ASSUMED, say so here in bold. It changes the roadmap:
     module 09-Roadmap will require a Milestone Zero to validate before building. -->

---

## 1a. Evidence Corpus

<!-- Criterion 6. Written BEFORE the inventory, because the corpus determines the inventory
     more than the coding does. See knowledge/Corpus-Selection.md. -->

**Selection rule:** «a rule a stranger could apply and get the same set — not a list of
sources assembled from memory»

**What it excludes, and what that costs:** «the sources the rule cannot see, and what is
likely to live in them»

**Independence test — if the product hypothesis were different, would this still be the
right place to look for this problem?** «yes, because… / no — and the corpus is therefore a
description of the hypothesis, which is a finding»

| Bias | Present? | What was done about it |
| --- | --- | --- |
| Selection — chosen for availability or fit to the hypothesis | «y/n» | «» |
| Denominator — raw counts across populations of different sizes | «y/n» | «the denominator used, or why comparison was refused» |
| Survivorship — only surviving products, active venues, remaining customers | «y/n» | «who left, and whether they were reachable» |
| Venue — the venue shapes what gets said; check who is *authoring* | «y/n» | «venue types used, and their different incentives» |
| Product size — biggest products read as the problem-heavy part of the market | «y/n» | «normalization applied» |
| Confirmation — agreeing sources read closely, disagreeing ones read as noise | «y/n» | «what each source returned, including nothing» |

**Normalized rate, where one could be computed:** «figure, per what, per what period» — or
«none obtainable; no cross-source comparison is made below»

---

## 2. Problem Inventory

<!-- Stage 1. Every problem surfaced, before any filtering. Sources: workflow friction
     from 03-user, jobs poorly served, review complaints, forum threads. -->

| # | Problem, as stated | Where it came from |
| --- | --- | --- |
| P1 | «raw statement» | «workflow step 3 friction / review / forum» |
| P2 | «raw statement» | «source» |

---

## 2a. Substitute Workflows

<!-- Stage 1, and it is a research step rather than a recall step. What do people do INSTEAD?
     Not competing products in this category — the things people use who use nothing in this
     category at all. Section 4's workaround column is scored against this table, so an empty
     row here means that column was scored from impression. -->

| Substitute | Class | Who uses it | Scale, where measurable | Residual friction | Evidence |
| --- | --- | --- | --- | --- | --- |
| «named thing» | by hand | «segment» | «n, or NOT MEASURABLE» | «what it still costs them» | `[verified: source]` |
| «named thing» | general-purpose tool bent to the job | | | | |
| «named thing» | built it themselves | | | «does it travel? does it break?» | |
| «named thing» | adjacent product, different moment | | | | |
| Tolerating it | nothing | | | | |

**Largest substitute by scale:** «name it, with the figure»

**Is any substitute larger than this entire product category?** «yes / no — and if yes, that
is a finding for the operator before anything is scored, not a footnote»

**What the silent majority does:** «the people who never adopted anything here. If this row
cannot be filled, say so — every other source in section 2 is a complaint, and complaints only
come from people who adopted something and were disappointed»

---

## 3. Problem, Symptom, or Preference

<!-- Stage 2. The classification that prevents building for the wrong thing.
     A symptom points at a problem. A preference is not a problem at all. -->

| # | Statement | Type | If symptom, the problem beneath | If preference, why excluded |
| --- | --- | --- | --- | --- |
| P1 | «statement» | problem | — | — |
| P2 | «statement» | symptom | «the real problem» | — |
| P3 | «statement» | preference | — | «no cost when unmet» |

**Preferences excluded:** «list — recorded so nobody re-proposes them as problems»

---

## 4. Scoring

<!-- Stage 3. Score every surviving problem. Show the arithmetic. -->

| # | Problem | Frequency | Severity | Workaround | Score | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | «problem» | «daily = 5» | «high = 5» | «none = 5» | «125» | [tag] |
| P2 | «problem» | «weekly = 3» | «med = 3» | «adequate = 2» | «18» | [tag] |

**Scales used**

| | 5 | 3 | 1 |
| --- | --- | --- | --- |
| Frequency | Daily or more | Weekly | Monthly or less |
| Severity | Costs money, risk, or reputation | Costs significant time | Mildly annoying |
| Workaround | None — they simply suffer | Exists but poor | Exists and works |

`Score = Frequency × Severity × Workaround`

<!-- The workaround dimension is the one most often omitted and the most informative.
     A problem with a good workaround is a problem someone already solved. -->

**Cost per occurrence**

| # | What it costs them | Quantified | Evidence |
| --- | --- | --- | --- |
| P1 | «time / money / risk» | «figure» | [tag] |

---

## 5. Validated Problems

<!-- Stage 4a. ONLY problems with [verified] evidence. If this section is empty,
     say so explicitly. An empty validated section is a finding, not a failure. -->

> These problems are supported by retrievable evidence.

### P«n» — «problem statement»

| | | Evidence |
| --- | --- | --- |
| Who has it | «persona / segment» | [tag] |
| How often | «frequency» | [tag] |
| What it costs | «quantified» | [tag] |
| Current workaround | «what they do» | [tag] |
| Why the workaround fails | «reason» | [tag] |
| Score | «n» | — |

**Source of validation:** «what specifically evidences this»

---

## 6. Assumed Problems

<!-- Stage 4b. Plausible but not evidenced. These are NOT lesser problems — they may
     be the most important ones. They are simply unproven. -->

> ⚠️ **Believed but not established.** Do not build on these without validation.

| # | Assumed problem | Why we believe it | What would prove it | Cost to test |
| --- | --- | --- | --- | --- |
| P«n» | «problem» | «reasoning» | «evidence needed» | «effort» |

---

## 7. The Sharpest Problem

<!-- Stage 5. One problem. The product is built around this.
     Defend against the scoring table, not against interest. -->

## P«n» — «problem statement»

**Why this one**

«Reference the scoring. Explain why the other high scorers were not chosen. If the
highest-scoring problem was passed over, that needs a stronger defense than choosing it
would have.»

| | |
| --- | --- |
| Score | «n» |
| Evidence standing | **verified / assumed** |
| Who has it | «persona» |
| Frequency | «how often» |
| Cost when it occurs | «quantified» |
| Why nobody has solved it | «structural reason» [tag] |

**What the product must do about it:** «one sentence — this becomes the product's core job»

**If this problem is assumed rather than verified:** «state the consequence — Milestone
Zero in the roadmap, validate before building»

---

## 8. Problems We Are Not Solving

<!-- Real problems, deliberately out of scope. Prevents scope creep and shows the
     choice was made rather than overlooked. -->

| # | Problem | Real? | Why not now |
| --- | --- | --- | --- |
| P«n» | «problem» | yes | «adjacency / cost / segment mismatch / timing» |

---

## 9. Root Cause Check

<!-- For the sharpest problem: is it the problem, or a consequence of one?
     Ask "why does this happen?" until the answer stops being actionable. -->

```
«P«n»» → why? → «cause» → why? → «deeper cause» → why? → «root»
```

**Where the chain stopped being actionable:** «which level»

**Are we solving the root or the symptom?** «honest answer»

<!-- Solving a symptom is sometimes correct — the root may be outside anyone's control.
     But it must be a decision, not an oversight. -->

---

## 10. Contradicting Evidence

<!-- From the adversarial review pass. What argues that this problem is not worth
     solving? Must not be empty. -->

| Finding | Source | Implication | Resolved? |
| --- | --- | --- | --- |
| «what argues against» | [tag] | «what it would mean» | «how addressed» |

**Has anyone tried to solve this and failed?** «what happened, and what it teaches» [tag]

---

## 11. Validation Plan

<!-- Stage 6. Ordered by CHEAPEST TEST OF THE MOST LOAD-BEARING BELIEF.
     Concrete: "interview 10 solo GPs about consultation-time data entry",
     not "conduct user research". -->

| Order | What to test | Method | Sample | Effort | Would invalidate |
| --- | --- | --- | --- | --- | --- |
| 1 | «assumption» | «interviews / survey / prototype / data pull» | «n and who» | «days» | «what stops if false» |
| 2 | ... | | | | |

**Test this first:** «the single cheapest test of the most load-bearing belief»

**Stop-and-rethink trigger:** «the result that would mean this should not be built»

**Questions inherited from 03-user (NEEDS USER):** «carried forward»

---

## 12. Handoff

| Field | Value | Consumed by |
| --- | --- | --- |
| `ranked_problems` | «ordered list with scores» | 05, 07, 08 |
| `problem_inventory` | «full list including excluded» | 07 |
| `substitute_workflows` | «named substitutes with scale and residual friction» | 05, 07 — **05-competition treats these as competitors, not adjacencies** |
| `validation_plan` | «ordered tests» | 07, 09-Roadmap |
| Sharpest problem | «P«n»» | 07-strategy — the product is built around this |

---

## 13. Sources

| # | Source | Type | Accessed | Used for |
| --- | --- | --- | --- | --- |
| S1 | «citation» | review / forum / study / interview | «date» | «claims» |

---

## 14. Evidence Standing

| | Count |
| --- | --- |
| Verified problems | «n» |
| Assumed problems | «n» |
| Contradicting findings | «n» |
| Open assumptions | «n» |

**How much weight can the problem foundation bear?** «one honest sentence»

**Confidence:** «high / medium / low»

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] Verdict stated first
- [ ] Every statement classified as problem, symptom, or preference
- [ ] Every problem scored on frequency, severity AND workaround
- [ ] Scoring arithmetic visible
- [ ] Validated and assumed sections visually separate — never blended
- [ ] >= 3 problems with [verified] evidence, or the shortfall stated plainly
- [ ] Sharpest problem identified and defended against the scoring table
- [ ] Evidence standing of the sharpest problem stated explicitly
- [ ] Root cause check performed
- [ ] Contradicting evidence non-empty
- [ ] Validation plan concrete and ordered by cheapest-test-of-biggest-belief
- [ ] Stop-and-rethink trigger defined
- [ ] Every claim carries exactly one evidence tag
- [ ] Every placeholder replaced, every guidance comment removed
-->
