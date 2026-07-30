---
Title: Evidence
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what verification means here, and why validated and assumed problems stay visually separate.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - evidence_log
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Evidence
  - Concept
---

# Evidence

---

# What It Is

The record of what is actually known, and how well — the module's central output and the reason it exists.

`[verified]` in this framework means **a retrievable source**: something a reader could go and check. It does
not mean convincing, consistent with experience, or agreed by everyone present.

| Tag | Meaning here |
| --- | --- |
| `[verified: source]` | A named, retrievable source — an observation, a document, a dataset, a named interview |
| `[inferred: basis]` | A reasoned conclusion from something verified, with the basis stated |
| `[assumption: needs validation]` | Plausible, unevidenced, and awaiting a test in the validation plan |

Stage 4 then splits the scored problems into two lists — **validated** and **assumed** — and keeps them
visually separate for the rest of the document.

> Blending the two in prose is how an assumed problem becomes an established one — not through dishonesty, but
> through paragraph structure.

---

# When It Applies

Throughout, and decisively in Stage 4 (Sort) and Stage 5 (Sharpen). The gate requires at least three problems
carrying `[verified]` evidence, and unvalidated problems listed explicitly as such.

---

# How to Apply It Here

**Keep the two lists in separate sections, not separate sentences.** A reader must be able to tell at a glance.
This separation is the module's core deliverable — more than the ranking.

**If the validated list is empty, say so.** Do not promote assumed problems to populate the section. An empty
validated list is a finding that changes the roadmap: **Milestone Zero becomes validation rather than
building**, and `10-execution` enforces that.

**Treat assumed problems as equal in importance and unequal in standing.** They may be the most valuable
problems identified. They are simply unproven, and the reader must never have to work out which is which.

**Rank the evidence itself.** A built workaround outranks a reported frustration, which outranks a stated
preference, which outranks a prediction. `03-user`'s `Behaviors.md` sets the order; this module inherits it.

**State the evidence standing of the sharpest problem plainly.** If it is assumed rather than verified, that is
a critical finding. It does not stop the run — the framework permits a `declared_shortfall` here, uniquely — but
it must propagate, and every module downstream must be able to see it.

---

# Where It Misleads

**Volume of evidence gets read as strength of evidence.** Ten stated preferences do not equal one observed
workaround. A long evidence log with nothing retrievable in it is weaker than a short one with two sources.

**Consistency is mistaken for verification.** Five people saying the same thing in interviews is five reports,
and if all five were asked a leading question it is one artifact of the question. `validation/Interviews.md`
covers why.

**An inference tagged once becomes a fact when quoted.** The tag lives on the claim, not on the paragraph, and
the claim travels. Repeat the tag wherever the claim appears.

**Verified can be true and irrelevant.** A well-sourced fact about a segment you are not serving is verified
and worthless. Evidence has to be evidence *for the specific claim* being made.

---

# Related

| | |
| --- | --- |
| `Validation.md` | How assumptions become verified |
| `Current-Solutions.md` | The strongest kind of evidence here |
| `03-user` | Where the evidence ranking is set out |
| `10-execution` | Where an empty validated list becomes Milestone Zero |

---

> **Concept Note**
>
> Two lists, visibly separate, all the way to the end of the
> document.
>
> An assumption must never be smoothed into a fact — and the usual
> instrument is not a lie, it is a paragraph.
