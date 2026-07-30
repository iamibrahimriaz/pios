---
Title: Prompt Engineering
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat the prompt as versioned product logic, and never as a guardrail.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/Evaluation.md
Outputs:
  - Prompt approach within model_strategy
Related Modules:
  - 09-technology
Tags:
  - AI
  - Prompts
  - Concept
---

# Prompt Engineering

---

# What It Is

The instruction given to the model — and the framework's position on it is two-part.

**It is product logic.** A prompt determines behavior, so it is versioned, reviewed and regression-tested like code.
`Evaluation.md`'s regression check exists because a prompt change alters behavior invisibly.

**It is not a guardrail.**

> A better prompt is not a guardrail.

| A prompt can | A prompt cannot |
| --- | --- |
| Improve average output quality | Guarantee anything |
| Set format and tone | Prevent a failure mode |
| Supply context and grounding | Enforce a limit |
| Reduce a class of error | Make an error detectable |

Guarantees come from the **per-instance criteria** in `Evaluation.md`: a bounded output, a required citation, a mandatory dismissal path,
a validated structure. Those hold every time; a prompt holds usually.

---

# When It Applies

In Move 5 and Move 6, as part of `model_strategy` — after the capability is justified and its autonomy bounded.

---

# How to Apply It Here

**Version prompts and store them where changes are reviewable.** A prompt edited in a console is an unversioned production change.

**Re-run the golden set on every prompt change.** It is the only way to know whether an improvement for one case degraded another, and
`09-technology/knowledge/CI-CD.md` is where that runs.

**Validate the output structurally rather than trusting the instruction.** If the output must be JSON with three fields, parse and check it.
An instruction to produce JSON is not a schema.

**Keep untrusted content clearly separated from instructions.** Any user or third-party text in the prompt is an injection surface, and
`AI-Risks.md` requires it registered.

**Put grounding data in the prompt rather than relying on recall.** Retrieved, cited context is both more accurate and more checkable —
which serves detectability, which `Automation.md` says governs autonomy.

---

# Where It Misleads

**Prompt improvement is offered where a guardrail is needed.** "We will instruct it not to do that" is the most common inadequate answer in
this module. Instructions are followed usually; guardrails hold always.

**Prompts are treated as configuration rather than logic.** They are edited without review, without versioning and without re-evaluation, and
behavior changes with no record of why.

**Improvement is measured on the cases someone was looking at.** Without the golden set, a prompt change is a hypothesis tested on a sample of
one.

**Provider defaults are assumed stable.** A model version change, a default parameter change, or a system-prompt change on the provider's side
can alter behavior with no change on your side. Version pinning is the mechanism `AI-Risks.md` requires.

**Complexity accumulates.** A prompt grown by accretion becomes unmaintainable and its clauses start conflicting. Length is not
sophistication.

---

# Related

| | |
| --- | --- |
| `Evaluation.md` | The golden set and the per-instance criteria |
| `AI-Risks.md` | Injection, and why prompts are not guardrails |
| `LLM.md` | The capability class this mostly applies to |
| `09-technology` | Version pinning and regression checks |

---

> **Concept Note**
>
> A prompt is product logic — version it, review it, regression-test
> it.
>
> And it is never a guardrail. Instructions are followed usually;
> guardrails hold every time.
