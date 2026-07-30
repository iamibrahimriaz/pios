---
Title: Jobs To Be Done
Module: 03-user
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State jobs as jobs, and keep solutions out of them.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/User-Journey.md
Outputs:
  - jobs_to_be_done
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - User
  - Jobs
  - Method
---

# Jobs To Be Done

---

# What It Is

A statement of what the person is trying to get done, in a form that survives changes of solution.

```
When «situation», I want to «motivation», so I can «outcome».
```

> **The test: if the sentence names a solution, it is not a job.**

| Not a job | A job |
| --- | --- |
| "I want a prescription-writing tool" | "When a patient describes symptoms, I want to capture what they said without breaking eye contact, so I can stay present in the consultation" |
| "I want a dashboard" | "When I start my week, I want to know which accounts are at risk, so I can act before they churn" |

A job is stable. Solutions change; the job outlives them — which is what makes jobs the right thing
for `08-product` to build against.

---

# When It Applies

In Move 5 (Job), **after** Move 4 (Observe). Jobs are interpretation, and interpretation must follow
evidence — a job written before the workflow describes the intended product.

---

# How to Apply It Here

**Derive each job from a step or a friction in the journey.** If a job cannot be pointed back to
something observed, it is an `[assumption]`, and it should carry the tag.

**Record three things per job:** how often it occurs, what satisfies it today, and how well. Frequency
drives `07-strategy`'s prioritization; "what satisfies it today" is what the product must beat.

**Include the functional and the non-functional together.** The functional job is capturing the note.
The emotional one — not appearing distracted in front of a patient — is often what actually decides
adoption, and it disappears if only the functional half is written.

**State which jobs the product will not serve.** Unbounded job lists become unbounded feature lists in
`08-product`. This is the boundary that prevents it.

**Keep the outcome clause in the user's terms.** "So I can act before they churn" is theirs. "So the
product delivers value" is ours, and it makes the whole sentence useless.

---

# Where It Misleads

**Solutions hide in the "I want to" clause.** "I want to automatically generate a summary" reads like
a job and has already chosen the mechanism — which pre-empts `14-ai-systems`, whose entire method is to
compare mechanisms and sometimes drop the AI one.

**Jobs get written at the wrong altitude.** "I want to run a good practice" is too broad to build
against; "I want to click save" is a step, not a job. The workable level is the one where the outcome
changes if it goes unmet.

**A tidy job statement can launder an assumption.** The template is persuasive, and filling it in
feels like research. Untagged jobs derived from nothing observed are the module's quietest failure.

**Jobs framed as ours rather than theirs.** A job describing what the business needs the user to do —
onboard, invite a colleague, upgrade — has inverted the concept. Those are `11-growth`'s objectives,
not the user's jobs.

---

# Related

| | |
| --- | --- |
| `User-Journey.md` | The evidence jobs must derive from |
| `Behaviors.md` | Why observation precedes interpretation |
| `Goals.md` | The user's ends, more broadly |
| `08-product` | Where jobs become traceable requirements |

---

> **Concept Note**
>
> If the sentence contains the product, delete the product and try
> again.
>
> A job that names a solution has ended the inquiry before module 07
> was allowed to make the decision.
