---
Artifact: prd
Project: «project name»
Version: 1.0
Date: «ISO date»
Confidence: «high | medium | low»
Modules: [07-strategy, 08-product, 12-metrics]
---

<!-- fill: The Product Requirements Document. Read by engineering, design, and delivery
     agents. Every requirement must trace to a ranked problem in 02-Problem-Validation.
     A requirement with no problem behind it is scope creep with a straight face.
     Remove every <!-- fill --> comment before delivery. -->

# Product Requirements — «Product Name»

## 1. Summary

«Three sentences. What this is, who it is for, and what it changes for them.»

---

## 2. The Problem

<!-- fill: Carried from 02-Problem-Validation. Do not restate it more optimiztically
     than that document does. If the problem is assumed rather than validated, say so here. -->

«The sharpest problem, restated in one paragraph.» [tag]

**Evidence standing:** «validated | assumed»

---

## 3. Users

| Persona | Segment | Primary job | Success looks like |
| --- | --- | --- | --- |
| «name» | «segment» | «J«n» from the dossier» | «their outcome» |

**Primary persona:** «name» — everything below optimizes for this person.

**Buyer, if different:** «who signs off, and what they need to see»

---

## 4. Goals

<!-- fill: What this product must achieve. Each goal maps to a success metric in
     11-Success-Metrics.md. Goals are outcomes, not features. -->

| # | Goal | Measured by |
| --- | --- | --- |
| G1 | «outcome» | «metric» |
| G2 | «outcome» | «metric» |

## 5. Non-Goals

<!-- fill: Explicit. This section prevents six months of argument.
     State what this product deliberately does NOT do, and why. -->

| Not doing | Why |
| --- | --- |
| «capability» | «reason — out of segment, post-MVP, competitor's strength, regulatory cost» |

---

## 6. Scope

### 6.1 In Scope (MVP)

«One paragraph describing the MVP as a whole, so a reader can picture it before
reading the requirement list.»

### 6.2 Out of Scope (this release)

«What is deferred, with a pointer to where it lives in 09-Roadmap.md»

---

## 7. Requirements

<!-- fill: The core of the document. Every requirement:
       - traces to a problem (P«n») and a job (J«n»)
       - has testable acceptance criteria — a machine or a QA engineer could verify it
       - has a priority: MUST (MVP), SHOULD (fast-follow), COULD (later)
     "The system should be fast" is not a requirement. "Search returns in under 300ms
     at p95 with 10k records" is. -->

### R1 — «requirement name»

| | |
| --- | --- |
| Priority | MUST |
| Traces to | P«n», J«n» |
| Persona | «name» |

**Behavior:** «what the system does, in plain language»

**Acceptance criteria:**
- [ ] «testable condition»
- [ ] «testable condition»
- [ ] «testable condition»

**Edge cases:**
- «case» → «expected behavior»

**Failure states:**
- «what goes wrong» → «what the user sees» → «how they recover»

---

### R2 — «requirement name»

<!-- fill: Repeat the block above for each requirement. Keep MUST requirements few.
     If everything is a MUST, the MVP has not been cut. -->

---

## 8. Traceability

<!-- fill: The audit table. Every requirement must appear here with a problem behind it.
     A requirement with no problem is scope creep — remove it or justify it. -->

| Requirement | Problem | Job | Priority | Evidence standing |
| --- | --- | --- | --- | --- |
| R1 | P1 | J1 | MUST | verified |
| R2 | P2 | J1 | MUST | assumed |

---

## 9. Constraints

| Type | Constraint | Source |
| --- | --- | --- |
| Regulatory | «requirement» | «regime, from the dossier» |
| Technical | «constraint» | «reason» |
| Commercial | «constraint» | «reason» |
| Timeline | «constraint» | «reason» |

---

## 10. Dependencies

| Dependency | Type | Owner | Risk if unavailable |
| --- | --- | --- | --- |
| «external system / API / data source» | «integration» | «who» | «impact» |

---

## 11. Success Metrics

<!-- fill: Summary only — the full definitions live in 11-Success-Metrics.md.
     Every goal in section 4 must appear here. -->

| Goal | Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- | --- |
| G1 | «metric» | «current» | «target» | «by when» |

**North star:** «the single metric» — «why it is the right one»

---

## 12. Open Questions

<!-- fill: From state.open_questions. Anything unresolved that affects the build.
     Mark blocking questions clearly — they must be answered before that work starts. -->

| # | Question | Blocking? | Owner | Needed by |
| --- | --- | --- | --- | --- |
| Q1 | «question» | yes | «who» | «milestone» |

---

## 13. Assumptions

<!-- fill: Everything this PRD rests on that is not established.
     Full detail in 10-Risks-and-Assumptions.md. -->

| # | Assumption | If wrong | Validation |
| --- | --- | --- | --- |
| A1 | «statement» | «consequence» | «test» |

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Problem, users, jobs, scope and explicit non-goals present
- [ ] Every requirement traces to a ranked problem in the traceability table
- [ ] Acceptance criteria testable, not aspirational
- [ ] Edge cases and failure states specified per requirement
- [ ] MUST requirements are few — the MVP is genuinely cut
- [ ] Success metrics defined with baselines and targets
- [ ] Blocking open questions flagged
- [ ] Every fill comment removed
-->
