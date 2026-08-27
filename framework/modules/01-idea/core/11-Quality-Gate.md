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

# Criterion 1 — Raw idea restated in one sentence naming who it is for, what it does and what changes

**Passes when:** the sentence names **who it is for**, **what it does**, and **what changes
for them**. Three components. All present is a pass.

**Test:** strike out each of the three in turn. If the sentence still identifies the same
product without one of them, that component was decoration and is missing.

| Fails | Passes |
| --- | --- |
| "A tool to help doctors with their work." | "A consultation-time note capture tool for solo GPs in «jurisdiction» that removes typing during patient visits." |

## This criterion does NOT test differentiation, and must not be used to

**A sentence can name all three components and still describe a category with several
existing entrants.** That is not ambiguity. **It is an idea that has not committed to a
differentiating position — which is criterion 9's subject, and criterion 9 permits it.**

**Both defects present identically to a cold read.** "Could this describe three different
products?" returns yes for a genuinely vague sentence *and* for a perfectly clear sentence
in a saturated category, and the two need opposite responses:

| The sentence | Response |
| --- | --- |
| Does not identify who, what or the change | **Fail here.** More words from the operator fix it |
| Identifies all three, and several products already match it | **Pass here.** Record the stance at criterion 9 and let the research find the position |

> **This cost a completed run a gate cycle.** The gate failed a healthy idea for not having
> decided something it was never asked to decide, and reversed only because this criterion's
> own passing example — read closely — contains no differentiator either. **The reverse
> outcome is equally available: a run that over-applies it and never reverses halts a valid
> idea at the first gate, and the operator is told their idea is defective when what it
> actually is, is early.**

---

# Criterion 2 — Geography / market and regulatory jurisdiction named

**Passes when:** `state.project.jurisdiction` is set from an operator answer, or the
idea itself states it unambiguously.

**Fails when:** it is inferred, defaulted, or left empty.

This criterion has no partial credit. A jurisdiction guessed because it seemed likely is
a failure even if the guess is correct — the process that produced it will be wrong next
time, and nothing downstream will catch it.

---

# Criterion 3 — Delivery surface named by the operator — web, mobile, desktop, API or other

**Passes when:** `state.project.delivery_surface` holds an operator answer naming what the
product physically is. Where more than one surface is named, their **order** is recorded
too — which ships first, and which follows.

**Fails when:** it is inferred from the idea, defaulted to a web application, or deferred
to the technical module.

**Ask it in the operator's own terms**, not in ours:

> **What should this actually be?** A website they open in a browser · a phone app they
> install · both · a desktop program · something with no interface that other software
> talks to · something else. **And if more than one — which one do you want first?**

**This is not a technology question and it does not belong to `09-technology`.** By the
time that module runs, eight others have already assumed an answer:

| Module | What it silently assumed |
| --- | --- |
| `02-market` | Device ownership as a sizing input. A phone app in a market with low smartphone ownership has a smaller addressable base than the population |
| `03-user` | Where the person is standing, what they are holding, and whether they have a signal |
| `05-competition` | Where competitors are even found — an app store, a search result, or a procurement list |
| `06-business` | The billing rail, and whether a platform takes a cut of it |
| `08-product` | Whether offline behavior is a requirement or a non-goal |
| `11-growth` | Whether the channel is an app store listing, search, or a sales conversation |

**A wrong answer here is not corrected later — it is inherited.** Nothing downstream
re-examines it, because each module reads the surface as settled context rather than as a
decision, and the error surfaces as a plan that is internally consistent and built for the
wrong thing.

| Fails | Passes |
| --- | --- |
| Silence, then a stack chosen in module 09 | "Web first for the «primary user», then Android. iOS later. Confirmed by the operator" |
| "A mobile-friendly platform" | "A phone app the «user» installs. No desktop version at any milestone" |
| "Web app" inferred because the idea said "software" | "Operator asked; answered: a desktop program, because the «setting» has no reliable connectivity" |

---

# Criterion 4 — Buyer and user distinguished (may be the same, must be stated)

**Passes when:** the brief states who uses the product and who pays for it, even where
they are the same person. Saying "the same person" explicitly is a pass. Silence is not.

**Why it matters:** where they differ, every later module carries a second audience —
different criteria, different objections, different sales motion. Discovering that at
module 06 means re-running 03 and 04.

---

# Criterion 5 — >= 5 clarifying questions asked, each satisfying the asking test

**Passes when:** five or more questions exist and each satisfies the asking test in
`08-Questions-To-Answer.md`.

> **This criterion is evaluated at the frame checkpoint, where the questions have just been
> asked and NONE can yet be answered.** It previously required them to be "answered or
> explicitly deferred", which is unsatisfiable at the only moment it is checked — the agent
> either failed a gate it could not pass or recorded a deviation by hand.
>
> **Resolution is checked at module close, not here.** A question that is still open at the
> frame checkpoint is the normal state, and it is what the checkpoint exists to surface.

**At module close**, each question must additionally carry either an operator answer or a
recorded deferral with an accompanying assumption. A question deferred without an assumption
has been dropped rather than deferred.

**The asking test:** would a different answer produce a different product?

Questions that fail the asking test do not count toward the five. An agent that pads to
five with cosmetic questions has failed this criterion while appearing to satisfy it.

| Counts | Does not count |
| --- | --- |
| "Solo practitioners or multi-doctor clinics?" | "What should we call it?" |
| "Replacing their current system, or alongside it?" | "What is your long-term vision?" |
| "Which country's regulations apply?" | "How big is the market?" (researchable) |

---

# Criterion 6 — All initial assumptions tagged per engine/evidence-policy.md

**Passes when:** every factual claim in the brief carries exactly one tag, every
assumption appears in `state.assumptions` with a validation method, and no hedging
language stands in for a tag.

**Common failure:** the brief reads confidently because the assumptions were written as
statements. Search the brief for sentences that assert something about users, demand, or
willingness to pay. Each one needs a tag.

---

# Criterion 7 — The single load-bearing assumption named among those tagged

**Passes when:** one assumption is marked as the one the premise rests on, and removing it
would change what the run is about.

**Fails when:** every assumption is tagged and none is distinguished. Module 07 then has to
rediscover which one mattered, usually by finding out the hard way.

**The removal test.** Delete the named assumption. If the idea still stands, it was not the
load-bearing one.

---

# Criterion 8 — A pre-mortem recorded — what would make this idea not worth doing — before research begins

**Passes when:** a short list exists, written **before this module's own existence check**, of
the conditions under which this idea should not be pursued.

**Fails when:** it is written after the research, or contains only conditions the operator
already believes to be false.

**"Before module 02 starts" is not the bar, and reading it that way is how this criterion was
failed while passing.** The existence check in this module is research. A pre-mortem written
during Brief Assembly comes after it, so the template's own *"recorded before research began"*
field could only ever be answered No — which a run duly did, then passed the criterion anyway
because nothing tied the two together.

**`12-Checklist.md` now runs a Pre-Mortem pass before the existence check, and §11 of the
working document is written there and never revisited.** Evaluate this criterion against that
ordering: if §11 was filled at assembly, it fails, whatever it says.

**Why before.** Compared afterward against what modules 02–06 actually found, this list is
the cheapest calibration available. Written afterward it is a summary, and calibrates
nothing.

---

# Criterion 9 — Differentiation stance recorded as vague, category or committed, with a committed thesis stated verbatim

**Passes when:** `state.project.differentiation_stance` holds one of three values, set from
what the operator actually said rather than from how the idea reads.

| Stance | Means | Gate |
| --- | --- | --- |
| **`vague`** | The sentence does not identify who it is for, what it does, or what changes | **Fail.** This is criterion 1, and more words from the operator fix it |
| **`category`** | The idea names its category clearly and has **no differentiating position yet**, deliberately — *"I don't know the differentiation; I want the research to find it"* | **Pass** |
| **`committed`** | The operator has a differentiating thesis | **Pass.** Record it verbatim in `differentiation_thesis` |

**Fails when:** the stance is inferred from the idea's wording rather than established with
the operator, or when `committed` is recorded without the thesis in their own words.

## Why `category` is a valid starting state and not a defect

**In a saturated category it is the honest one.** An operator who has noticed a real problem
and has not yet decided how to attack it differently is describing the normal condition of a
pre-research idea. **Requiring a differentiator at module 01 requires them to invent one
before any evidence exists — and an invented differentiator is worse than an absent one,
because eleven modules inherit it as a premise.**

**`category` is an obligation, not a waiver.** It converts into a specific requirement
downstream: **07-strategy must record which option supplies the differentiation, or state
that the research found none.** An idea that entered undifferentiated and exits
undifferentiated has produced a finding — a category with no available position is a real
and useful answer — but it must be said, not left as a gap nobody notices.

## A committed thesis is a claim, not a preference

**Record it verbatim and tag it.** *"We will win because we are faster"* is an
`[assumption: needs validation]`, and 05-competition is where it gets tested. **A thesis
paraphrased into the brief loses the ability to be refuted**, because what gets refuted is
the paraphrase.

| Fails | Passes |
| --- | --- |
| Stance left empty because the idea "obviously" has a differentiator | `committed`, thesis recorded verbatim, tagged `[assumption]` |
| `vague` recorded for an idea whose sentence names all three components | `category`, with the operator's own words on why it is unset |
| `category` recorded and never resolved at 07-strategy | `category` at 01, `differentiation_resolved_by: 07-strategy` at close |

---

# Universal Gates

In addition to the nine above, `engine/gates.yaml` U1–U7 apply. For this module the ones
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
3. Evaluate criteria 1–9 above. **All of them.** The count here must equal the number in
   `module.yaml`; `validate.py` fails the build when it does not.
4. Record the verdict in `state.run`.

```yaml
gate:
  module: 01-idea
  attempt: 1
  criteria:
    who_what_change_named: pass
    jurisdiction_named: fail
    buyer_user_distinguished: pass
    five_questions: pass
    assumptions_tagged: pass
    delivery_surface_named: pass
    load_bearing_assumption_named: pass
    premortem_recorded: pass
    differentiation_stance_recorded: pass
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
