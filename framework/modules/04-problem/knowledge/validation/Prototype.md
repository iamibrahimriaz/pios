---
Title: Prototype
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use a prototype to test a specific belief, not to preview a product.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Validation.md
Outputs:
  - Prototype method within validation_plan
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - Problem
  - Prototype
  - Method
---

# Prototype

---

# What It Is

Something built cheaply enough to be thrown away, shown to real people, to test one belief.

A prototype's purpose is to convert a question into an observation. What it can observe depends on what kind it
is:

| Kind | What it can test |
| --- | --- |
| **Sketch or wireframe** | Whether the concept is understood at all |
| **Clickable mock** | Whether someone can complete the task without help |
| **Wizard of Oz** — humans behind the curtain | Whether the output is good enough to act on, before building the mechanism |
| **Landing page** | Whether the proposition attracts attention from the right people |

The Wizard of Oz variant is the most under-used and the most valuable for AI products: it tests whether people
accept and act on the output, without committing to the model, the data pipeline, or the cost.

---

# When It Applies

In Stage 6, for beliefs about comprehension, task completion, and output acceptability. `08-product`'s
requirements and `10-execution`'s Milestone Zero both depend on the answers.

---

# How to Apply It Here

**State the belief the prototype tests, in one sentence, before building it.** A prototype without a named
belief becomes a preview, and previews collect praise.

**Make it obviously unfinished.** Rough artifacts get honest reactions; polished ones get either compliments or
critiques of the polish. This is a feature of roughness, not a limitation.

**Give the person a real task and stay silent.** What they do unaided is the data. Explaining the interface
destroys the only thing being measured.

**For AI capabilities, fake the mechanism.** Produce the output by hand and observe whether it is trusted, edited,
or ignored. Whether the model can generate it is `14-ai-systems`' question; whether anyone would use it is this
one, and it is the cheaper of the two to answer.

**Record what they did before what they said.** Same discipline as `03-user`'s `Behaviors.md`: the action is the
evidence, the commentary is interpretation.

---

# Where It Misleads

**Prototype reactions predict comprehension well and adoption badly.** Someone can complete a task easily and
never adopt the product, because adoption is governed by switching cost — which is `03-user`'s number, not
something a prototype can measure.

**Enthusiasm in a prototype session is nearly worthless.** The participant is being helpful, the artifact is new,
and nothing is at stake. Only a decision with a cost attached carries signal.

**A prototype quietly becomes the specification.** Screens made to test one belief get treated as the intended
design, and decisions taken for speed become requirements in `08-product` that nobody chose. Say plainly that
it is disposable.

**The Wizard of Oz result gets over-read.** It proves the output is useful *at human quality*. Whether a model
reaches that quality is a separate question, and `14-ai-systems`' acceptance criteria are where it is answered.

**Building the prototype becomes building the product.** The distinguishing test is whether it will be thrown
away. If it will not, this is not validation — it is early construction, and `10-execution` should be told.

---

# Related

| | |
| --- | --- |
| `MVP.md` | Where a real cost is introduced |
| `Usability.md` | Task completion, examined properly |
| `Interviews.md` | What to ask before showing anything |
| `14-ai-systems` | Where output quality becomes a criterion |

---

> **Concept Note**
>
> Name the belief before you build the artifact.
>
> For an AI feature, fake the mechanism first — whether the output is
> trusted is cheaper to learn than whether it can be produced.
