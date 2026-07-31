---
Title: References
Module: 01-idea
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Say where this module's answers come from, since almost none are researchable.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - ../constitution/resources/18-References.md
Outputs:
  - Source routes for idea-stage questions
Related Modules:
  - 02-market
  - 03-user
Tags:
  - Idea
  - References
  - Reference
---

# References

---

# Overview

This file does not list citations. It says **where the answers to this module's questions actually come from** — and the notable thing
about module 01 is how few of them are researchable at all.

The constitution's `18-References.md` sets the source hierarchy and evaluation criteria for the whole framework. This file applies it to
the idea stage.

---

# What Cannot Be Researched Here

| Question | Source | Why no external source exists |
| --- | --- | --- |
| What is the operator's goal? | **The operator** | It is a private intention. No document contains it |
| Which jurisdiction? | **The operator** | A decision, not a finding |
| What runway exists? | **The operator** | Same |
| Which segment first? | The operator, provisionally | `03-user` decides it defensibly later |
| What is the vision? | The operator | An intention, checked for falsifiability |

These are the module's `NEEDS USER` questions, and the correct handling is to ask rather than to infer. A brief that supplies its own
answers to these has invented the most consequential inputs in the run.

---

# What Can Be Established Cheaply

| Question | Route | Standing it yields |
| --- | --- | --- |
| Does anyone describe this problem publicly? | Professional forums, practitioner communities, review sites | `[verified: source]` for the *existence of the complaint*, not its prevalence |
| Does the category have a name? | How practitioners and suppliers describe it | `[verified]` — and its absence is itself a finding |
| Has someone tried this? | Product searches, dead projects, abandoned repositories | `[verified]`, and the reason they stopped is the valuable part |
| What do practitioners call the work? | Their own writing | The vocabulary `09-technology` and `10-execution` will use |

Note what none of these establishes: **how common the problem is.** That is `02-market`'s and `03-user`'s work, and no amount of forum
reading substitutes for it.

---

# Source Tiers, Applied

Following the constitution's hierarchy:

| Tier | At the idea stage |
| --- | --- |
| **Primary** | The operator. Professional bodies' published guidance. Regulatory registers |
| **Industry** | Sector publications, practitioner press — useful for vocabulary and direction |
| **Academic** | Rarely decisive this early; occasionally establishes the problem exists at population level |
| **Product and technical** | Competitor documentation, changelogs — mostly `05-competition`'s |
| **Community** | Forums and practitioner discussion — strong for the complaint, weak for prevalence |
| **AI-assisted** | Useful for orienting and for generating candidate questions. **Never a citation** |

The last row matters at this stage specifically, because an idea brief is easy to generate and hard to source. A model's account of what
clinicians struggle with is `[inferred]` at best, and it should be labeled as the model's inference rather than as a finding.

---

# Verification Discipline

**Date anything time-sensitive.** A complaint pattern from four years ago may describe software that has since changed —
`05-competition` makes the same point about reviews.

**Distinguish the complaint from its incidence.** Ten forum posts prove ten people wrote about it. That is real evidence of existence and
no evidence of prevalence, and conflating them inflates the idea.

**Prefer what people did to what they said.** The constitution's evidence hierarchy and `03-user/knowledge/Behaviors.md` agree: a
workaround someone built and shared outranks any number of opinions.

**Record the search that found nothing.** An absent category name, an absent competitor, an absent discussion — each is a finding, and
`02-market` will need it when it asks why a gap persists.

---

# Cross-References Within the Framework

The most useful references for this module are internal:

| Need | Where |
| --- | --- |
| The evidence tagging rules | `framework/constitution` |
| What a validated problem requires | `04-problem/knowledge/Evidence.md` |
| Why the operator goal matters | `01-idea/knowledge/Goals.md` |
| How the vision escapes its role | `01-idea/knowledge/Vision.md` |
| What the brief must produce | `01-idea/module.yaml` |

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| Inferring the operator's goal | The most consequential input in the framework, invented |
| Citing a model's summary as research | A fabricated finding, undetectable downstream |
| Treating forum volume as incidence | An inflated problem that `02-market` cannot reconcile |
| Undated sources | Evidence about a product or practice that has changed |
| No record of fruitless searches | `02-market` re-runs them, or worse, assumes a gap |

---

> **Resource Note**
>
> The three questions that matter most here have no external source. They
> have an operator.
>
> Ask them. A brief that answers them on the operator's behalf has
> guessed the inputs everything else depends on.
