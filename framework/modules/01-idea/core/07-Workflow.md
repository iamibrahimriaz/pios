---
Title: Workflow
Module: 01-idea
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Idea module.
Audience:
  - AI Agents
Prerequisites:
  - 01-idea/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/01-idea.md
  - state.outputs.idea_brief
Related Modules:
  - 02-market
Tags:
  - Idea
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method. This document is the procedure — what to do,
in what order, what to write where, and when to stop.

Follow it literally. This module runs first, has no upstream dependencies, and ends at
a mandatory human checkpoint.

---

# Position in the Run

```
[ START ] → 01-idea → ⏸ HUMAN CHECKPOINT → 02-market → ...
```

| | |
| --- | --- |
| Stage | `frame` |
| Depends on | nothing |
| Consumes | `state.project.raw_idea` |
| Produces | `idea_brief`, `clarifying_questions`, `initial_assumptions`, `scope_boundaries` |
| Ends at | human checkpoint — **mandatory** |

---

# Step 1 — Initialize

1. Create `projects/<slug>/` if it does not exist.
2. Create `state.yaml` from `engine/state-schema.yaml`.
3. Derive `slug` from the idea — kebab-case, short, recognizable.
4. Write the operator's idea **verbatim** to `state.project.raw_idea`.
5. Set `state.run.current_stage: frame`.

> Do not edit the raw idea. Not for grammar, not for clarity, not for length.

---

# Step 2 — Read Before Writing

Read, in this order:

1. `constitution/core/` — the governing principles
2. `engine/evidence-policy.md` — the tagging rules
3. `01-idea/core/03-Core-Principles.md` — how to think here
4. `01-idea/core/06-Framework.md` — the six passes
5. `01-idea/core/08-Questions-To-Answer.md` — the interrogation bank
6. `01-idea/knowledge/` — as needed for concepts

Do not begin generating before this. An agent that writes first produces a restatement
of the idea in more confident language, which is worse than nothing because it looks
like progress.

---

# Step 3 — Run the Six Passes

Execute `06-Framework.md` in order. Write as you go — do not hold six passes in working
memory and produce them all at the end.

| Pass | Write to |
| --- | --- |
| 1. Capture | `state.project.raw_idea` |
| 2. Separate | draft brief — problem statement |
| 3. Locate | `state.project.jurisdiction`, draft brief — context |
| 4. Surface | `state.assumptions` |
| 5. Interrogate | `state.open_questions` |
| 6. Bound | draft brief — scope |

## Ask the differentiation question during pass 2

**Criterion 9, and it is an operator question, not an inference.** Pass 2 separates the
solution from the problem, which is the moment the absence of a differentiating position
becomes visible — and the moment you will be most tempted to supply one.

Ask it in their words:

> **Do you already know what will make this different from what exists — or do you want the
> research to work that out?** Either answer is fine. If you have a view, I will record it as
> a claim the research can refute rather than as a premise.

| Their answer | Record |
| --- | --- |
| A differentiating thesis | `differentiation_stance: committed`, thesis **verbatim** in `differentiation_thesis`, tagged `[assumption: needs validation]` |
| "I don't know yet — find it" | `differentiation_stance: category`, their words in the brief |
| A sentence that does not identify who it is for, what it does, or what changes | Not a stance answer — that is criterion 1, and the fix is more words from them |

**Do not infer it from how the idea reads.** A clear sentence about a crowded category reads
exactly like a vague one, and the two need opposite responses. **`category` is a valid
starting state**; supplying a differentiator on their behalf creates a premise eleven modules
inherit.

**Say the obligation out loud when they answer `category`:** *"Then 07-strategy has to name
which option supplies it, or report that the research found none — and I'll carry that
forward."*

---

# Step 4 — Assemble the Idea Brief

Fill `13-Template.md` into `projects/<slug>/research/01-idea.md`.

Every claim carries an evidence tag. At this stage most will be
`[assumption: needs validation]` — that is correct. Do not manufacture verified claims
to make the brief look stronger.

---

# Step 5 — Write to State

```yaml
outputs:
  idea_brief:           # path + one-paragraph summary
  clarifying_questions: []
  initial_assumptions:  []
  scope_boundaries:     {}
```

Append every assumption to `state.assumptions` and every question to
`state.open_questions`. The brief is a document; state is the memory. Later modules read
state, not prose.

---

# Step 6 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module asks specifically:

- Is this idea a solution I accepted without finding the problem?
- Which context dimension did I guess rather than ask?
- What assumption am I making that is so obvious I did not write it down?
- If this whole idea is misconceived, which sentence in my brief is the giveaway?

Record the verdict. `revise` loops back to Step 3. `regress` is impossible here — this
module has no upstream.

---

# Step 7 — Gate

Evaluate against `11-Quality-Gate.md` and the universal gates in `engine/gates.yaml`.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 8 |
| Fail | Return to Step 3. Maximum three attempts, then halt and escalate |

---

# Step 8 — Human Checkpoint

**Stop here.** This is not optional.

Present to the operator:

1. **The brief** — what you understood the idea to be
2. **Blocking questions** — must be answered before research begins
3. **Deferrable questions** — will proceed on a recorded assumption if unanswered
4. **The assumptions** — what you are about to build research on
5. **What happens next** — which module runs, and what it will produce
6. **A closing line naming what you need** — the questions, numbered, and *"Answer these and
   I'll start the research."* The operator must be able to close the message and know the
   ball is in their court

Then wait.

**Three answers are blocking without exception:** the **jurisdiction**, the **payer**, and
the **delivery surface** — website, phone app, both, desktop program, or no interface at
all, and if more than one, which ships first. Ask the surface question in the operator's own
words, not as a technology question. It is not module 09's to settle: six later modules read
it as settled context and none re-examines it.

**Number the questions, one idea each, in the operator's language**, and give each a
fallback — what you will assume if they say "I don't know", and what that assumption costs.
An operator who cannot answer must never be stuck, but must see the price of the default
before it is applied.

Do not proceed past a blocking question by selecting the more plausible answer. The whole
purpose of this checkpoint is that the operator knows things you cannot research: their
market, their access, their constraints, their intent.

---

# Step 9 — Incorporate and Hand Off

When the operator responds:

1. Update `idea_brief` with the answers.
2. Move answered questions out of `open_questions`, preserving the answer.
3. Where an answer contradicts an assumption, add a superseding entry — mark the old one
   invalidated, do not delete it.
4. Re-run the gate if the answers materially changed the brief.
5. Append `01-idea` to `state.run.completed_modules`.
6. Hand off to `02-market`.

---

# Handoff Contract

`02-market` will read:

| Field | Used for |
| --- | --- |
| `idea_brief.problem_statement` | Defining the market boundary |
| `idea_brief.context.jurisdiction` | Regulatory landscape research |
| `idea_brief.context.segment` | Sizing SAM and SOM |
| `scope_boundaries` | Keeping the market definition bounded |

If any of these is missing or vague, `02-market` will fail its gate and return here.
Better to catch it now.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Brief reads like the original idea | Pass 2 skipped | Re-run Separate; keep asking "so that what?" |
| Fewer than five questions | Questions too broad | Work `08-Questions-To-Answer.md` section by section |
| Jurisdiction unset | Guessed or ignored | Ask. Never assume |
| No assumptions recorded | Not looking | Work the Pass 4 categories one at a time |
| Gate fails three times | The idea may be too vague to research | Escalate with a specific question |

---

# Effort Expectation

This module is fast — it is thinking, not researching. Most elapsed time will be the
operator answering questions.

If the module completed in seconds, it did not run. It restated.

---

> **Workflow Principle**
>
> This module's job is to stop the run before it wastes effort.
>
> Every question asked here saves a module of research pointed in the wrong direction.
