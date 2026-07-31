---
Title: References
Module: 04-problem
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what verified means here, and route each validation method to what it can establish.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - ../constitution/resources/18-References.md
Outputs:
  - Source routes for problem validation
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Problem
  - References
  - Reference
---

# References

---

# Overview

This module decides what the framework claims to know. That makes the definition of `[verified]` the most consequential definition in the
run.

---

# What `[verified]` Means Here

> A **retrievable source**: something a reader could go and check.

It does not mean convincing, consistent with experience, or agreed by everyone present.

| Passes | Fails |
| --- | --- |
| "Timestamp export, «practice», 12 weeks, 1 clinician" | "User interviews" |
| "«Published statistic», «publisher», «date»" | "Industry research shows" |
| "Observed: 3 consultations, «date», keywords written on paper" | "Clinicians report frustration" |
| "5 interviews, single-handed GPs in «region», «date»" | "Users we spoke to" |

The pattern in the failing column is that nothing can be returned to. A reader cannot check it, disagree with it, or find that it says
something different.

---

# Method → What It Can Establish

Each method has a narrow reach, and using one outside its reach produces confident nonsense:

| Method | Establishes | Cannot establish |
| --- | --- | --- |
| **Existing data** — exports, logs, records | Frequency, duration, volume, error rates — actual | Why |
| **Observation** | What happens, including workarounds | Prevalence |
| **Interviews** | That the problem exists for this person; the workflow; the cost in their terms | How common; what they would pay; whether they will switch |
| **Surveys** | Incidence, if the population and response rate are stated | Why; cost; willingness to pay |
| **Prototype** | Comprehension; task completion; whether output is acted upon | Adoption |
| **Wizard of Oz** | Whether human-quality output is useful and trusted | Whether a model can reach that quality |
| **MVP** | Sustained use; willingness to pay | Anything cheaper could have answered |
| **Public feedback** | That a complaint pattern exists | Incidence, ever |

**Start with existing data.** It is the cheapest source of `[verified]` evidence in the framework and the most consistently overlooked,
because interviews are the habitual first move. One timestamp export outranks fifty recollections.

---

# The Ordering Rule for Sources

> Cheapest test of the most load-bearing belief.

Not the easiest, and not the order things were discovered. The question is: if this is false, what else collapses?

For the worked example, that ordering put a three-day Wizard of Oz test first — ahead of interviews that were easier and ahead of an MVP that
would have answered later at ten times the cost.

---

# Source Tiers, Applied

| Tier | At the problem stage |
| --- | --- |
| **Primary** | The user's own data. Direct observation. Named interviews with a stated sample |
| **Industry** | Published operational statistics — occasionally establishes incidence at population level |
| **Academic** | Rarely decisive; sometimes the only source for prevalence |
| **Product and technical** | Incumbent support forums and reviews — `Feedback.md`'s corpus, dated |
| **Community** | Practitioner forums. Strong for workarounds, worthless for incidence |
| **AI-assisted** | Generating candidate problems and interview questions. **Never a verification** |

The last row is the specific risk in this module. A model asked whether a problem is real will produce a plausible affirmative account.
That is `[inferred]` from the model's training, it has no retrievable source, and tagging it `[verified]` is the manufactured-validation
failure in its most modern form.

---

# Writing Criteria Before Gathering

Every test's invalidating result is written **and dated** before any data arrives.

```
T1  Would invalidate: 3 or more of 5 re-read every draft in full.
    Criteria written «date», before gathering.
```

Afterwards, every threshold becomes negotiable and every result becomes interpretable. This is not a matter of honesty — it is how
interpretation works, and the timestamp is the only real defense.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| `[verified: interviews]` with no sample | Nothing retrievable; the gate passes on nothing |
| Consistency mistaken for verification | Five agreements to one leading question is one artifact |
| Stated preference tagged as evidence | The weakest signal available, promoted |
| Population claim verifying a segment problem | True generally, unverified here |
| Skipping existing data | The cheapest `[verified]` source, unused |
| Criteria written after results | The test confirms whatever was already believed |
| Model output as validation | Fabrication that survives every downstream review |

---

> **Resource Note**
>
> `[verified]` means someone else could go and check it. Nothing weaker
> qualifies, however convincing.
>
> And before planning a single interview, ask what they can already
> export.
