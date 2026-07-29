---
Title: Template
Module: 01-idea
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Idea Brief — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - projects/<slug>/research/01-idea.md
Related Modules:
  - 02-market
Tags:
  - Idea
  - Template
  - Output
---

# Template — Idea Brief

---

# Usage

Copy everything below the line into `projects/<slug>/research/01-idea.md` and fill it.

This is a **working document**, not a customer deliverable. It feeds the deliverable
templates in `framework/deliverables/templates/` — principally the Executive Summary and
the PRD — but it is not itself shipped.

Conventions:

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

A section that cannot be filled is a finding. Write what is missing and why. Never delete
a section to hide a gap, and never write filler to occupy one.

---
---

# Idea Brief — «Project Name»

| | |
| --- | --- |
| Slug | `«kebab-case»` |
| Date | «ISO date» |
| Module | 01-idea |
| Status | draft / checkpoint / complete |
| Confidence | «high / medium / low» |

---

## 1. Raw Idea

<!-- Verbatim. Exactly as the operator gave it. Never edited, at any later point. -->

> «the operator's original words»

---

## 2. The Idea, Sharpened

<!-- One sentence. Names who it is for, what it does, and what changes for them.
     Must pass the cold-read test: two readers should picture the same product. -->

«One sentence.»

**What changed from the raw idea:** «what the six passes revealed, or "nothing — the
original framing held"»

---

## 3. Solution vs Problem

<!-- Pass 2. Both, separately. Do not blend them. -->

| | |
| --- | --- |
| **Solution as proposed** | «the operator's framing» |
| **Problem it implies** | «what the solution suggests is wrong today» |
| **"So that what?" chain** | «step → step → step» |

**Where the chain ended:** «the deepest answer reached»

**Honest assessment:** «if the problem sounds trivial when stated plainly, say so here»

---

## 4. Context

<!-- Pass 3. Every row answered or marked ASKED. Nothing guessed. -->

| Dimension | Value | Source |
| --- | --- | --- |
| Jurisdiction | «country/region» | operator / stated in idea / **ASKED** |
| Segment | «who specifically» | operator / stated in idea / **ASKED** |
| User | «who uses it» | operator / stated in idea / **ASKED** |
| Buyer | «who pays» | operator / stated in idea / **ASKED** |
| Incumbent | «what they use today» | operator / stated in idea / **ASKED** |
| Setting | «where and how it is used» | operator / stated in idea / **ASKED** |
| Regulated | «yes/no — which regime» | operator / stated in idea / **ASKED** |

<!-- Any row marked ASKED is a blocking question in section 7. -->

---

## 5. Value Hypothesis

| | |
| --- | --- |
| What changes for the user | «outcome» [tag] |
| Type of value | «time / money / risk / capability» |
| Large enough to change behavior? | «assessment» [tag] |
| Who else benefits | «secondary beneficiary» |

---

## 6. Assumptions

<!-- Pass 4. At least one per category. All written to state.assumptions. -->

| # | Category | Assumption | Why believed | If false | Validation |
| --- | --- | --- | --- | --- | --- |
| A1 | User | «statement» | «basis» | «consequence» | «method» |
| A2 | Problem | «statement» | «basis» | «consequence» | «method» |
| A3 | Demand | «statement» | «basis» | «consequence» | «method» |
| A4 | Willingness to pay | «statement» | «basis» | «consequence» | «method» |
| A5 | Behavior | «statement» | «basis» | «consequence» | «method» |
| A6 | Technical | «statement» | «basis» | «consequence» | «method» |
| A7 | Access | «statement» | «basis» | «consequence» | «method» |

**Most load-bearing assumption:** «which one, and what breaks if it is wrong»

---

## 7. Questions for the Operator

<!-- Pass 5. Blocking first, and few. Each must pass the asking test. -->

### Blocking

| # | Question | Why it changes the work | Answer |
| --- | --- | --- | --- |
| Q1 | «question» | «what it determines» | «pending» |

### Deferrable

| # | Question | Assumption carried if unanswered | Answer |
| --- | --- | --- | --- |
| Q«n» | «question» | «A«n»» | «pending» |

---

## 8. Scope

<!-- Pass 6. -->

**In scope**

- «what this product addresses»

**Out of scope**

| Not this | Why |
| --- | --- |
| «capability» | «reason» |

**Adjacent, deliberately parked**

- «what it could become later»

**One product or several?** «assessment — if the idea bundles several products, say so»

---

## 9. Existence Check

<!-- From 09-Research-Methodology.md. Shallow by design. -->

| | |
| --- | --- |
| Searched using | «operator's terms» / «domain's terms» |
| Similar products found | «list, or "none found"» [tag] |
| Abandoned attempts found | «list, and why they stopped, if findable» [tag] |
| Conclusion | «solved / partially served / apparent gap / could not check» |

**Domain vocabulary learned:** «terms that will improve later research»

<!-- If retrieval was unavailable, say so plainly and tag as assumption.
     Do not fabricate findings. -->

---

## 10. Obvious Blockers

| Blocker | Type | Severity | Notes |
| --- | --- | --- | --- |
| «what could prevent this existing» | regulatory / technical / structural | «high/med/low» | «detail» [tag] |

«Or: "None identified at this stage."»

---

## 11. Adversarial Review

<!-- From engine/review-loop.md pass 3. Must not be empty. -->

**Strongest case against this idea:** «the best argument that it should not be built»

**Which assumption is the weak link:** «A«n»»

**What a domain expert would immediately correct:** «best guess»

**Resolved?** «how it was addressed, or "carried forward as a risk"»

---

## 12. Handoff to 02-market

| Field | Value |
| --- | --- |
| Problem statement | «one sentence» |
| Jurisdiction | «value» |
| Segment | «value» |
| Scope boundary | «what defines the market edge» |

**Blocking questions outstanding:** «count — if greater than zero, do not proceed»

---

## 13. Evidence Standing

| | Count |
| --- | --- |
| Verified claims | «n» |
| Inferred claims | «n» |
| Open assumptions | «n» |
| Blocking questions | «n» |

**Confidence:** «high / medium / low»

«One sentence: how much weight this brief can bear.»

---

<!-- COMPLETION CHECK — remove before marking complete
- [ ] Raw idea verbatim and unedited
- [ ] Sharpened sentence passes the cold-read test
- [ ] Solution and problem stated separately
- [ ] Every context row answered or marked ASKED — none guessed
- [ ] At least one assumption per category
- [ ] At least five qualifying questions
- [ ] Scope includes an explicit out-of-scope list
- [ ] Existence check performed or honestly marked unavailable
- [ ] Adversarial review non-empty
- [ ] Every claim carries exactly one evidence tag
- [ ] Every placeholder replaced, every guidance comment removed
-->
