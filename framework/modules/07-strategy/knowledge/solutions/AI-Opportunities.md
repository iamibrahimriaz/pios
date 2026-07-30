---
Title: AI Opportunities
Module: 07-strategy
Section: knowledge/solutions
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Identify where AI might help without committing to it, and leave the justification to module 14.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/solutions/Solution-Exploration.md
Outputs:
  - Candidate AI opportunities within solution_options
Related Modules:
  - 14-ai-systems
Tags:
  - Strategy
  - AI
  - Concept
---

# AI Opportunities

---

# What It Is

Places in the chosen approach where an AI mechanism **might** be the right answer — recorded as candidates, not
decisions.

`14-ai-systems` owns the decision. Its method compares each proposed capability against a non-AI alternative, and
**dropping is a successful outcome**. This module's job is to notice the candidates and pass them on with the problem
attached.

The shapes where AI tends to earn its place:

| Shape | Why AI fits |
| --- | --- |
| Unstructured input becoming structured | Rules cannot enumerate the variation |
| Long text becoming short | Judgment about salience, not extraction |
| Matching or ranking against fuzzy criteria | The criteria resist specification |
| Anomaly surfacing in a large volume | Nobody can look at all of it |

And where it tends not to:

| Shape | Why not |
| --- | --- |
| A calculation with defined rules | Deterministic code is cheaper, faster and auditable |
| Validation against a known list | A lookup |
| Anything where a wrong answer is undetectable and costly | Autonomy cannot be justified — `14-ai-systems`' central rule |

---

# When It Applies

In Move 1 (Diverge) and Move 4 (Cut). A candidate above the MVP line becomes a proposal `14-ai-systems` must justify
or drop.

---

# How to Apply It Here

**Record the problem, not the mechanism.** "Clinicians cannot type during a consultation" is the entry.
"Use speech-to-text with an LLM summarizer" is a mechanism, and naming it here pre-empts module 14's comparison.

**Note whether the data exists, and say how you know.** `14-ai-systems` requires data availability **confirmed, not
projected** — unconfirmed data is a blocker there. Flagging it now avoids an option built on data nobody has.

**Flag the detectability question early.** If a user cannot tell when the output is wrong, autonomy above "suggests"
will need a visibility mechanism. That constraint shapes the option's value, and it is cheaper to know now.

**Keep the non-AI version of each candidate alive.** `Alternative-Solutions.md` requires it, and module 14 requires
it to be a real alternative rather than a straw man.

**Cost it roughly.** Per-use inference cost against `06-business`'s margin per user. An option whose mechanism
consumes the margin is not an option, and the arithmetic is available now.

---

# Where It Misleads

**AI gets chosen as the shape of the solution before the problem is examined.** Then every option requires it, the
comparison has no non-AI arm, and module 14's method cannot run. This is the most common way an AI product becomes
unjustifiable.

**Capability is confused with value.** That a model can produce something says nothing about whether anyone acts on
it. `04-problem`'s Wizard of Oz test answers the second question for a fraction of the cost.

**The plausible output problem is underestimated.** A confident wrong answer is worse than no answer in professional
work, and it is the failure mode most likely to appear in the tail rather than the demo.

**"AI-powered" is treated as positioning.** `05-competition`'s test applies: if the model were free tomorrow, nothing
about it would distinguish the product. The workflow, data and trust would.

**A candidate becomes a commitment by being written down.** These are opportunities. Module 14 exists to reject the
ones that do not survive comparison, and a run where nothing is ever dropped has not been running the method.

---

# Related

| | |
| --- | --- |
| `Automation.md` | Automation without AI |
| `Alternative-Solutions.md` | The alternative each candidate must beat |
| `05-competition` `AI-Comparison.md` | What survives commoditization |
| `14-ai-systems` | Where each candidate is justified or dropped |

---

> **Concept Note**
>
> Record the problem and pass it on. The mechanism is module 14's
> decision, and dropping it is a valid outcome there.
>
> An option set where every option needs AI is an option set with one
> option.
