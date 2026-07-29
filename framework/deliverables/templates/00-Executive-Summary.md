---
Artifact: executive-summary
Project: «project name»
Version: 1.0
Date: «ISO date»
Confidence: «high | medium | low»
Prepared by: Product Intelligence OS
---

<!-- fill: This is the only document some readers will open. It must be able to stand alone.
     Write it LAST, after every other artifact exists. Nothing may appear here that is not
     established in a supporting artifact. Target: five minutes to read.
     Remove every <!-- fill --> comment before delivery. -->

# Executive Summary — «Product Name»

## Recommendation

<!-- fill: Lead with the verdict. Never bury it. One of: BUILD / BUILD WITH CHANGES /
     DO NOT BUILD / INSUFFICIENT EVIDENCE. Then two or three sentences of why.
     If the honest answer is "do not build", say so. A framework that only ever
     says "build" is a rubber stamp and is worth nothing. -->

**«BUILD | BUILD WITH CHANGES | DO NOT BUILD | INSUFFICIENT EVIDENCE»**

«Two to three sentences. What should happen next and why.»

**Confidence in this recommendation: «high | medium | low»**
«One sentence on what would raise it.»

---

## The Idea

<!-- fill: Restate what was proposed, in one sentence, in the operator's own framing.
     Then state what the research says it should actually become, if that differs.
     The gap between those two sentences is often the most valuable thing in this document. -->

**As proposed:** «one sentence»

**As researched:** «one sentence — the sharpened version, or "unchanged"»

---

## The Problem Worth Solving

<!-- fill: One problem. The sharpest one, from 02-Problem-Validation. Not a list.
     State who has it, how often, what it costs them, and what they do today instead. -->

«Who» experiences «what», «how often». Today they «current workaround», which costs
them «quantified cost» [tag].

Why this problem and not the others: «one sentence»

---

## The Opportunity

| | |
| --- | --- |
| Market | «definition and boundary» |
| Size | «SAM figure» [tag] |
| Segment targeted first | «segment» — «why first» |
| Buyer | «who pays» |
| Price point | «figure» [tag] |
| Primary competitor | «name, or "status quo"» |
| The gap | «one sentence» |

---

## What We Would Build

<!-- fill: The MVP, in plain language, in under 100 words. No feature list — the shape
     of the thing. A reader should be able to picture using it. -->

«Description»

**Deliberately not in scope:** «the two or three most notable non-goals»

---

## Why This Could Work

<!-- fill: The strongest case FOR. Two to four points, each anchored to evidence. -->

1. «Point» [tag]
2. «Point» [tag]
3. «Point» [tag]

## Why This Could Fail

<!-- fill: The strongest case AGAINST — from the adversarial review pass. This section
     is not optional and must not be softened. If it reads weaker than the section above,
     the adversarial pass was not done honestly. -->

1. «Point» [tag]
2. «Point» [tag]
3. «Point» [tag]

---

## The Three Assumptions That Matter Most

<!-- fill: From state.assumptions, ranked by what breaks if they are wrong.
     These are the things to go and test before committing budget. -->

| # | Assumption | If wrong | Cheapest way to test |
| --- | --- | --- | --- |
| 1 | «statement» | «consequence» | «test» |
| 2 | «statement» | «consequence» | «test» |
| 3 | «statement» | «consequence» | «test» |

---

## What Happens Next

<!-- fill: Concrete. Named actions, not "conduct further research". -->

**Before writing code:** «the validation step that should happen first»

**First milestone:** «from the roadmap»

**Time to first shippable version:** «estimate» [tag]

---

## Evidence Standing

<!-- fill: Be straight about this. It is the difference between a research document
     and a confident guess. -->

| | Count |
| --- | --- |
| Claims verified against sources | «n» |
| Claims inferred | «n» |
| Open assumptions | «n» |
| Blocking open questions | «n» |

«One sentence: what the biggest evidence gap is, and what would close it.»

---

## Supporting Artifacts

| Document | Answers |
| --- | --- |
| `01-Research-Dossier.md` | Market, users, competition — with sources |
| `02-Problem-Validation.md` | Which problems are real |
| `03-PRD.md` | What we are building |
| `04-Feature-Spec.md` | In what order, and where the MVP line falls |
| `05-Data-Model.md` | The data shape |
| `06-API-Contract.md` | The interfaces |
| `07-Architecture.md` | How it is built |
| `08-UX-Flows.md` | How it is used |
| `09-Roadmap.md` | The sequence |
| `10-Risks-and-Assumptions.md` | What could go wrong |
| `11-Success-Metrics.md` | How we know it worked |
| `12-Build-Handoff.md` | Start building from here |

---

<!-- ACCEPTANCE — remove before delivery
- [ ] Opens with the recommendation
- [ ] States confidence and what would raise it
- [ ] Readable in under five minutes
- [ ] "Why this could fail" is as strong as "why this could work"
- [ ] Three most threatening assumptions listed with tests
- [ ] No claim appears here that is not established in a supporting artifact
- [ ] Every fill comment removed
-->
