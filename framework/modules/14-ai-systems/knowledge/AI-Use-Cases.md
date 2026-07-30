---
Title: AI Use Cases
Module: 14-ai-systems
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Propose candidates generously, then justify each against a genuine non-AI alternative.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - ai_opportunities
Related Modules:
  - 07-strategy
  - 08-product
Tags:
  - AI
  - Use Cases
  - Method
---

# AI Use Cases

---

# What It Is

The candidate list, and the comparison that decides its fate.

> Every capability in this module has to earn its place against something simpler. **The module succeeds when it drops most of what it
> proposed.**

| Capability | The honest alternative |
| --- | --- |
| Suggest the likely diagnosis code | A searchable list ordered by that clinician's own recent usage |
| Summarize the consultation | A structured form with four fields |
| Extract data from a document | A better upload format, or asking the sender for structured data |
| Predict which record is needed next | Sorting by most-recently-used |

> **The advocate check.** For each capability kept, could a competent person argue for the alternative in one honest sentence? If not, the
> alternative was a straw man and the comparison proved nothing.

> **Capability theater.** A model added because it is expected rather than because it wins. It costs money per operation, needs evaluation
> nobody scheduled, fails in ways nobody predicted, and replaces a form field that would have worked.

**If the product has no AI component, that is a complete answer.** State it and stop.

---

# When It Applies

In Move 1 (Propose) and Move 2 (Compare) — the second move decides the fate of everything else.

---

# How to Apply It Here

**Tie every candidate to a job and a requirement.** From `03-user` and `08-product`. A capability serving no requirement is the same orphan
problem modules 08 and 09 guard against, arriving from a different direction: not from the research, but from what is currently possible.

**Propose generously, then be strict.** The discipline belongs in Move 2, and it works better on real candidates than on a pre-filtered list.

**Write the alternative as its advocate would.** If the sentence defending the form field is not one a competent person would say, the
comparison is theater.

**Record the dropped rows with the simpler thing adopted instead.** Those records are what stop the same capability being re-proposed every
quarter as an obvious omission.

**Where the alternative wins on quality but loses on effort, say exactly that.** It is a legitimate reason to build the model version. What
is not legitimate is scoring the alternative badly to make the choice look better.

---

# Where It Misleads

**The mechanism is chosen before the problem is examined.** Then every option requires a model, the comparison has no non-AI arm, and the
method cannot run. `07-strategy/knowledge/solutions/AI-Opportunities.md` names this as the most common way an AI product becomes
unjustifiable.

**Capability is confused with value.** That a model can produce something says nothing about whether anyone acts on it —
`04-problem`'s Wizard of Oz method answers the second question far more cheaply.

**Keeping everything is read as ambition.** A module that proposes five and keeps one has done its job. Keeping five means Move 2 did not run.

**"AI-powered" is treated as positioning.** `05-competition`'s test applies: if the model were free tomorrow, nothing about it would
distinguish the product.

**Dropped capabilities are deleted rather than recorded.** Then the argument repeats, and the next person has no idea it was already
decided.

---

# Related

| | |
| --- | --- |
| `Automation.md` | How much autonomy a kept capability gets |
| `Evaluation.md` | The bar it must clear |
| `07-strategy` `solutions/AI-Opportunities.md` | Where candidates originate |
| `08-product`, `03-user` | The requirement and the job |

---

> **Concept Note**
>
> Write the alternative as its advocate would write it. If nobody
> competent would say that sentence, the comparison proved nothing.
>
> Dropping four of five is the module working, not failing.
