---
Title: Workflow
Module: 14-ai-systems
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the AI Systems module.
Audience:
  - AI Agents
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/14-ai-systems.md
  - state.outputs.evaluation_plan
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Justification. This document is the procedure.

This module runs in the `specify` stage, alongside `09-technology`. It decides which parts of the
product are served by a model rather than by deterministic logic, and what happens when those parts
are wrong.

---

# Position in the Run

```
08-product ┐
09-technology ┴→ [ 14-ai-systems ] → 12-metrics
                                   → 13-operations
```

| | |
| --- | --- |
| Stage | `specify` |
| Depends on | `08-product`, `09-technology` |
| Consumes | `feature_spec`, `data_model`, `jobs_to_be_done` |
| Produces | `ai_opportunities`, `model_strategy`, `data_requirements`, `evaluation_plan`, `failure_modes` |
| On fail | return to `08-product` |
| Human checkpoint | none |

---

# Step 0 — Establish Whether This Module Applies

Before anything else, ask whether any requirement in `08-product` genuinely calls for a model.

```
Does any requirement need judgment, generation, extraction or prediction
that cannot be specified as a rule?
  ├─ no  → state that plainly, fill §1 and §2, and exit
  └─ yes → continue
```

> A run with no AI component is a complete run. This module is not an obligation to add one, and
> recording "no AI capability is justified for this product" is a legitimate output.

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `08-product` and `09-technology` are in `state.run.completed_modules`.
2. Read `08-product` §7 — the requirements. Any capability must serve one.
3. Read `08-product` §8 — the edge cases and the failure-state expectations.
4. Read `03-user` — the jobs, and the persona's tolerance for error in their real context.
5. Read `09-technology` §3 — the **data model and its classification**: which fields are PII and
   which are regulated.
6. Read `09-technology` §8 — the architecture, so the capability is placed rather than invented.
7. Read `09-technology` §12 — the cost model this module will add a line to.
8. Read `02-market` — the regulatory landscape, including any disclosure obligations.
9. Read `06-business` — **revenue per user per month**, for the cost ratio.
10. Read `10-execution` §4, if complete — the latency and flow expectations.

Record before proposing anything:

| Inherited | Consequence |
| --- | --- |
| Requirements | Every capability must serve one |
| Data classification | Regulated fields may not become model inputs |
| Architecture | The capability is placed inside it |
| Regulatory disclosure obligations | May require telling the user AI was involved |
| Revenue per user | The denominator of the cost ratio |
| Persona's error tolerance | Governs autonomy more than accuracy does |

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `14-ai-systems/core/03-Core-Principles.md`
3. `14-ai-systems/core/06-Framework.md` — the Six Moves
4. `14-ai-systems/core/08-Questions-To-Answer.md`
5. `14-ai-systems/knowledge/` — AI-Use-Cases, AI-Risks, Evaluation, Automation, LLM,
   Prompt-Engineering, and whichever of OCR, Voice, Prediction, Recommendation apply
6. `framework/deliverables/templates/15-AI-Strategy.md`

---

# Step 3 — Propose

Move 1.

List candidate capabilities generously. Each names the job from `03-user` and the requirement from
`08-product` it would serve.

A candidate serving no requirement is an orphan — and here it usually arrives from what is
technically possible rather than from the research. Remove it, or take it to `08-product` as a
missing requirement.

---

# Step 4 — Compare

Move 2. The move that decides the module.

For each candidate, write the **honest non-AI alternative**: a rule, a lookup, a sorted list, a
better form, a default, or asking a different party for structured input.

Then run the **advocate check**:

```
Can a competent person argue for the alternative in one honest sentence?
  ├─ no  → the alternative is a straw man. Rewrite it, then compare again
  └─ yes → compare, and record the verdict
```

| Verdict | Action |
| --- | --- |
| AI wins | Keep, with the reasoning |
| The alternative wins | **Drop**, and record what was adopted instead |

Dropping is a successful outcome. Record the dropped rows with the simpler thing that replaced them
— that record is what stops the capability being re-proposed as an obvious omission.

Where the alternative wins on quality but loses on effort, say exactly that. What must not happen is
scoring the alternative badly to make the choice look better.

---

# Step 5 — Ground

Move 3.

1. List every data need: source, volume, quality.
2. **Confirm availability now**, with evidence. "We will have this" is not availability.
3. List unconfirmed needs as **blockers**, not risks.
4. State cold-start behavior — how it works before data accumulates.
5. Answer the data-rights questions: the regime, consent, whether data leaves the system, and
   whether provider training on it is contractually disabled.
6. Run the regulated-input check:

```
List regulated and PII fields from 09-technology §3
Check each against every model input
  ├─ overlap → FAIL. Remove it, redact it, or the gate fails
  └─ none    → record "none — verified"
```

Step 5.6 is mechanical, and it is the same check `12-metrics` runs against event properties. The
list is the same list.

---

# Step 6 — Bound

Move 4.

For each kept capability:

1. Answer the **wrongness cost**: what one wrong output costs, who bears it, and **whether the user
   can detect it**.
2. Choose the autonomy level, justified against those answers.
3. Apply the rule: where the user bears the cost and cannot detect the error, autonomy above
   "suggests" requires a mechanism that makes the error visible.
4. Specify oversight: who reviews, whether review is always or sampled, whether the user can
   override, and whether the override is recorded.
5. Specify transparency: disclosure, labeling, whether the user can see why — and any regulatory
   obligation from `02-market`.
6. State **who judges quality and what qualifies them**. In a domain product this must usually be a
   domain expert.

---

# Step 7 — Evaluate

Move 5, and it happens **before** the capability is committed to.

1. Per capability: metric, method, passing bar, sample size, cadence.
2. Describe the golden set — how it is built from real cases, and how it is kept honest by never
   being used for tuning.
3. State the **ship gate**: the result required before users see this.
4. State what happens if the bar is missed. The answer is that it does not ship.
5. State the regression check for model or prompt changes.
6. Write both kinds of acceptance criterion:

| Type | Goes to |
| --- | --- |
| Statistical — a bar over a sample | This document, and `12-metrics` |
| Per-instance — always true | `08-product`'s acceptance criteria |

The per-instance guarantees are where most real safety lives: always dismissible, always labeled,
always bounded. Those are testable conventionally, and they hold on every single output regardless
of quality.

---

# Step 8 — Fail

Move 6.

1. Write failure modes **specific to this product**. "The model may hallucinate" fails this step.
2. Per mode: likelihood, what it costs the user, **detection**, and the guardrail.
3. State the **worst realistic outcome** plainly.
4. Answer whether you would know it happened. "No" is a common and important answer.
5. Identify **silent failures** — plausible wrong output with no signal.
6. Specify the **non-AI fallback** as a requirement, and hand it to `08-product`.
7. Fill model strategy: version pinned and cited, deprecation exposure, fallback model, vendor
   lock-in.
8. Hand the failure modes that need alerts, runbooks or support scripts to `13-operations`.

---

# Step 9 — Cost

1. Cost per operation, cited with a date.
2. Operations per user per month, with its basis.
3. AI cost per user per month.
4. Divide by revenue per user from `06-business` — **the share**.
5. State whether it is acceptable. If the share is large, say so plainly: the options are a cheaper
   approach, fewer operations, a higher price, or dropping the capability.
6. Hand the figure to `09-technology` §12 and `13-operations` §11.

---

# Step 10 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/14-ai-systems.md`. Write §1 last.

```yaml
outputs:
  ai_opportunities:   # §2 — kept and dropped, with the comparisons
  model_strategy:     # §5 — approach, version, fallback, lock-in
  data_requirements:  # §6 — availability, cold start, rights
  evaluation_plan:    # §8 — bars, golden set, ship gate, both criterion types
  failure_modes:      # §9 — specific, with detection and guardrails
```

Append every quality expectation, operation count, latency figure and cost estimate to
`state.assumptions` — U5. Append each kept-or-dropped verdict to `state.decisions` with the
alternative it rejected — U4. Append unconfirmed data needs and unresolved rights questions to
`state.open_questions` as blockers.

---

# Step 11 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which capability did I keep because it was expected rather than because it won?
- Which non-AI alternative did I write weakly on purpose?
- Which data need did I assume rather than confirm?
- Am I sending a regulated field to a third party?
- Which autonomy level did I choose without asking whether the user could detect an error?
- Would the build team be judging quality they are not qualified to judge?
- Did I set the bar before or after seeing what the model could do?
- Which failure mode is generic enough to apply to any product?
- Which failure would we never find out about?
- What share of revenue is this consuming, and did I check?

The coherence pass: does the latency budget fit `10-execution`'s flow, does the cost fit
`06-business`'s ceiling, and does the autonomy level fit the persona's real error tolerance from
`03-user`? A capability that acts autonomously for a user whose work is regulated and audited is a
contradiction, not an efficiency.

---

# Step 12 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Hand to `12-metrics` and `13-operations` |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

---

# Step 13 — Hand Off

1. Append `14-ai-systems` to `state.run.completed_modules`.
2. Hand per-instance guarantees and non-AI fallbacks to `08-product` as requirements.
3. Hand the cost line to `09-technology` and `13-operations`.
4. Hand quality metrics to `12-metrics`.
5. Hand failure modes needing alerts or runbooks to `13-operations`.
6. Note whether the AI strategy deliverable is in scope — it is optional in the manifest.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `08-product` | Per-instance guarantees, non-AI fallbacks | Ordinary requirements and acceptance criteria |
| `09-technology` | Model placement, data flow, cost line | Architecture and the cost model |
| `12-metrics` | Quality metrics and bars | Instrumentation and monitoring |
| `13-operations` | Failure modes, fallbacks | Alerts, runbooks, support scripts |
| `12-Build-Handoff.md` | Guardrails, output constraints, fallbacks | What must hold at build time |
| `15-AI-Strategy.md` | All outputs | The shipped AI artifact, when in scope |

`08-product` is an unusual consumer here: this module hands *back* to a module that has already
completed. The per-instance guarantees and the non-AI fallback are ordinary requirements, and they
belong where every other requirement lives rather than in an AI annex nobody reads at build time.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Every proposed capability kept | Comparison was decorative | Rewrite the alternatives honestly |
| Alternatives that could not be argued for | Straw men | Apply the advocate check |
| A capability serving no requirement | Proposed from what is possible | Drop it, or take it to `08-product` |
| Data assumed to exist | Availability not confirmed | Confirm, or record a blocker |
| Cold start unaddressed | Steady state assumed | State the behavior with no data |
| Regulated field in a model input | Classification not checked | Remove or redact it |
| Autonomy without detectability | Wrongness cost not asked | Reduce autonomy or add visibility |
| Build team judging domain quality | Reviewer unqualified | Name a domain expert |
| Bar set after seeing outputs | Evaluation deferred | Set it before commitment |
| Golden set used for tuning | Honesty lost | Rebuild it, and quarantine it |
| "The model may hallucinate" | Generic failure mode | Make it specific to this product |
| No answer for silent failure | Detectability ignored | Identify it and design a guardrail |
| Fallback described as a contingency | Not treated as scope | Make it a requirement |
| Cost ratio never computed | Step 9 skipped | Compute it; it has killed products |

---

> **Workflow Principle**
>
> Step 4 is the whole module.
>
> Everything after it is care taken over capabilities that survived
> one honest question.
