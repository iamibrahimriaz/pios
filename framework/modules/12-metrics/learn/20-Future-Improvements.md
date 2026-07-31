---
Title: Future Improvements
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Metrics module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 09-technology
  - 13-operations
Tags:
  - Metrics
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The computation test is not mechanized.** Every metric should trace to fields in module
09's data model. Nothing performs the trace, so a metric requiring an unrecorded field
passes the gate and fails at launch.

**The gaming question has no required output.** It is the module's best idea and it lives
in guidance. A metric adopted without it looks identical to one that survived it.

**Definition completeness is unchecked.** "Every metric has a definition, source and
target" does not require population, window and exclusions — which is where every
two-analysts disagreement actually lives.

**The regulated-property check depends on a list that is a convention.** Module 09
produces the list in prose, so this check is performed against whatever the reader
infers.

**Quality has no home.** Most metric sets measure usage because usage is cheap to
instrument. Quality requires product changes — capturing edits, corrections, reversals —
and the framework has no structure that makes that omission visible.

**Nothing distinguishes a guardrail from a metric.** A guardrail has a threshold and
exists to prevent damage; a metric has a target and exists to be improved. Treated
identically, guardrails become second objectives, which is the two-primaries failure by
another route.

**No review cadence for the north star itself.** Metrics outlive their reasons and the
module has no mechanism that asks, after two quarters, whether moving this number
corresponded to the product being better.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A required field trace per metric | The computation test becomes real | Small, and the highest-value change here |
| A required `gaming_response` per metric | The module's best question stops being optional | Small |
| A structured definition — population, event, window, exclusions | Two-analysts disagreements largely disappear | Small |
| A `guardrail` type distinct from a metric | Guardrails stop becoming second objectives | Small |
| A quality-metric prompt | The most-skipped dimension gets asked about | Moderate; it often requires a product change |
| A north star review cadence | Metrics stop outliving their reasons silently | Small, and it needs an owner in module 13 |

Four of these are small schema changes and together they would close most of the module's
real gaps. That is unusual in this framework — most modules' limitations are disciplines
rather than fields.

---

# What Should Not Change

**Exactly one north star.** Every review proposes a balanced set. A balanced set relocates
the priority decision into whichever meeting the conflict surfaces in.

**Instrumentation stays specified here.** Moving it to build means specifying events from
the built product rather than from the decisions, which is how metric sets end up
measuring what was convenient.

**The event-property check stays in this module.** Analytics is a data export and this is
the only place in the framework positioned to notice.

**The reasoning for the north star stays a required output.** It is what makes the metric
revisitable rather than inherited, and it costs two sentences.

---

> **Improvements Principle**
>
> This module's best instrument — asking what a person optimizing this would do — is
> currently guidance.
>
> Making it a required field would change more product outcomes than any other single
> change proposed across these fourteen modules.
