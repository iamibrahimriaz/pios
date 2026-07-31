---
Title: Quality Gate
Module: 01-idea
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Idea module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 01-idea/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 02-market
Tags:
  - Idea
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the gate criteria. This document explains how to evaluate each one,
what passing actually requires, and what a failure looks like.

The gate is not a formality. It is the mechanism that stops a vague idea from consuming
four modules of research before anyone notices.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

An agent that wants to proceed will find reasons to call a criterion satisfied. The
correct posture is the opposite: assume failure and require the evidence that overturns it.

---

# Criterion 1 — Raw idea restated in one unambiguous sentence

**Passes when:** the sentence names who it is for, what it does, and what changes for
them — and two different readers would picture the same product.

**Test:** remove the sentence from its context and read it cold. Could it describe three
different products? Then it is ambiguous.

| Fails | Passes |
| --- | --- |
| "A tool to help doctors with their work." | "A consultation-time note capture tool for solo GPs in «jurisdiction» that removes typing during patient visits." |

---

# Criterion 2 — Geography / market and regulatory jurisdiction named

**Passes when:** `state.project.jurisdiction` is set from an operator answer, or the
idea itself states it unambiguously.

**Fails when:** it is inferred, defaulted, or left empty.

This criterion has no partial credit. A jurisdiction guessed because it seemed likely is
a failure even if the guess is correct — the process that produced it will be wrong next
time, and nothing downstream will catch it.

---

# Criterion 3 — Buyer and user distinguished (may be the same, must be stated)

**Passes when:** the brief states who uses the product and who pays for it, even where
they are the same person. Saying "the same person" explicitly is a pass. Silence is not.

**Why it matters:** where they differ, every later module carries a second audience —
different criteria, different objections, different sales motion. Discovering that at
module 06 means re-running 03 and 04.

---

# Criterion 4 — >= 5 clarifying questions asked and answered or explicitly deferred

**Passes when:** five or more questions exist, each satisfies the asking test in
`08-Questions-To-Answer.md`, and each has either an operator answer or a recorded
deferral with an accompanying assumption.

**The asking test:** would a different answer produce a different product?

Questions that fail the asking test do not count toward the five. An agent that pads to
five with cosmetic questions has failed this criterion while appearing to satisfy it.

| Counts | Does not count |
| --- | --- |
| "Solo practitioners or multi-doctor clinics?" | "What should we call it?" |
| "Replacing their current system, or alongside it?" | "What is your long-term vision?" |
| "Which country's regulations apply?" | "How big is the market?" (researchable) |

---

# Criterion 5 — All initial assumptions tagged per engine/evidence-policy.md

**Passes when:** every factual claim in the brief carries exactly one tag, every
assumption appears in `state.assumptions` with a validation method, and no hedging
language stands in for a tag.

**Common failure:** the brief reads confidently because the assumptions were written as
statements. Search the brief for sentences that assert something about users, demand, or
willingness to pay. Each one needs a tag.

---

# Criterion 6 — The single load-bearing assumption named among those tagged

**Passes when:** one assumption is marked as the one the premise rests on, and removing it
would change what the run is about.

**Fails when:** every assumption is tagged and none is distinguished. Module 07 then has to
rediscover which one mattered, usually by finding out the hard way.

**The removal test.** Delete the named assumption. If the idea still stands, it was not the
load-bearing one.

---

# Criterion 7 — A pre-mortem recorded — what would make this idea not worth doing — before research begins

**Passes when:** a short list exists, written before module 02 starts, of the conditions
under which this idea should not be pursued.

**Fails when:** it is written after the research, or contains only conditions the operator
already believes to be false.

**Why before.** Compared afterward against what modules 02–06 actually found, this list is
the cheapest calibration available. Written afterward it is a summary, and calibrates
nothing.

---

# Universal Gates

In addition to the five above, `engine/gates.yaml` U1–U7 apply. For this module the ones
most often missed:

| | |
| --- | --- |
| **U2** | Every output in `produces` exists in `state.outputs` — including `scope_boundaries`, which is the one most often forgotten |
| **U5** | Every assumption has a validation method, not just a statement |
| **U6** | The brief is written for someone with no access to this conversation |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Evaluate universal gates U1–U7.
3. Evaluate criteria 1–5 above.
4. Record the verdict in `state.run`.

```yaml
gate:
  module: 01-idea
  attempt: 1
  criteria:
    unambiguous_sentence: pass
    jurisdiction_named: fail
    buyer_user_distinguished: pass
    five_questions: pass
    assumptions_tagged: pass
  universal: [U1 pass, U2 pass, U3 pass, U4 pass, U5 pass, U6 pass, U7 pass]
  verdict: fail
  reason: "Jurisdiction inferred from context rather than confirmed by the operator."
  action: "Add as blocking question at the checkpoint."
```

---

# On Failure

`module.yaml` sets `on_fail: halt and request input from the human operator`.

This module is unusual: it has no upstream module to regress to. A failure here is
almost always a missing operator answer, not a research defect.

| Attempt | Action |
| --- | --- |
| 1 | Revise and re-evaluate |
| 2 | Revise and re-evaluate |
| 3 | Halt. Escalate with the specific unanswered question |

Do not attempt to satisfy a failed criterion by weakening it. If the jurisdiction is
unknown, the gate fails — writing "global" to make it pass is a fabrication.

---

# What a Passing Module 01 Looks Like

- The brief describes a product, not an aspiration.
- Someone in the domain would recognize the problem as one they have.
- The context is specific enough that module 02 knows exactly what market to size.
- The assumptions are visible, and there are more of them than felt comfortable to write.
- The questions asked are ones only the operator could answer.
- A reader can tell what is known from what is believed.

---

> **Gate Principle**
>
> The cheapest module to fail is the first one.
>
> Every criterion here exists because failing it silently costs four modules of research.
