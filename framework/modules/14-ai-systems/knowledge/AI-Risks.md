---
Title: AI Risks
Module: 14-ai-systems
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Specify product-specific failure modes with detection and guardrail columns.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/Evaluation.md
Outputs:
  - failure_modes
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - AI
  - Risk
  - Method
---

# AI Risks

---

# What It Is

How this capability goes wrong, **here, in this product.**

| Generic, and useless | Specific, and designable |
| --- | --- |
| "The model may hallucinate" | "The model may invent a drug interaction that does not exist, which a rushed clinician could accept" |
| "Output quality may vary" | "For handwritten notes the extraction drops silently to partial, and the missing fields look like fields the user left blank" |

## The plausibility problem

> A model's errors are fluent. They arrive in the same register as its correct answers.

This is why detectability outranks error rate — and it is the same failure the framework's own evidence policy exists to prevent: *an
assumption must never be smoothed into a fact.* A model does exactly that by default, in every sentence it produces.

So the required columns are **detection** and **guardrail**, not just likelihood and consequence. And two questions answered plainly:

| | |
| --- | --- |
| Worst realistic outcome | Stated, not softened |
| Would we know it happened | Frequently no, which is itself the finding |

> **The non-AI fallback is a requirement, not a contingency.** The provider will have an outage, the model will be deprecated, and the
> capability will sometimes be wrong. What the user does then belongs in `08-product`'s requirements.

---

# When It Applies

In Move 6 (Fail), producing `failure_modes` and `model_strategy`.

---

# How to Apply It Here

**Write each failure as something that happens to this user, in this job.** The specific version is designable; the generic version is a
disclaimer.

**Fill the detection column honestly, including "no".** A failure nobody can detect is the most serious entry available, and its guardrail
has to be structural — a per-instance constraint from `Evaluation.md`, not a better prompt.

**Specify the silent-degradation case.** Partial output that looks complete is the characteristic AI failure in extraction and summarization,
and it is the one users never report because they cannot see it.

**Make the fallback a requirement in `08-product`.** Provider outage, deprecation, and low-confidence output each need a specified user
experience, not an operational note.

**Pin versions and date every claim.** Model capabilities and prices are version-scoped and change — cite them with a version and a date,
exactly as `09-technology` requires of every technology claim.

---

# Where It Misleads

**Generic risk language is used and satisfies nobody.** "Hallucination" as a listed risk generates no design work. The specific sentence
generates a guardrail.

**Prompt improvements are offered as guardrails.** A better prompt is not a guardrail. A bounded output, a required citation, a mandatory
dismissal path and a human review step are.

**Prompt injection is omitted for products that take user text.** Any capability passing user or third-party content to a model has that
surface, and `09-technology/knowledge/security/OWASP.md` notes the classic web catalog does not cover it.

**Provider dependency is treated as low risk.** `05-competition` identified supplier power as structural: terms change, prices change, and
versions are deprecated — all three happen with model providers.

**The worst outcome is softened.** In a clinical or financial product it should be written plainly, because that sentence is what justifies
the guardrails to whoever wants to remove them for speed.

---

# Related

| | |
| --- | --- |
| `Automation.md` | Detectability, and the autonomy ceiling |
| `Evaluation.md` | The per-instance guarantees that act as guardrails |
| `08-product` | Where the fallback becomes a requirement |
| `13-operations` | Incident handling when it fails in production |

---

> **Concept Note**
>
> A model's errors arrive in the same voice as its correct answers.
>
> That is the framework's own prohibition — an assumption smoothed into a
> fact — happening automatically, in every sentence.
