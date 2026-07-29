---
Title: Research Methodology
Module: 03-user
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how to research users honestly, including when no user can be reached.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - engine/evidence-policy.md
  - 03-user/core/06-Framework.md
Outputs:
  - Evidence-tagged user findings
  - state.evidence_log entries
Related Modules:
  - 04-problem
Tags:
  - User
  - Research
  - Methodology
---

# Research Methodology

---

# Overview

This module has a problem the others do not: **the agent cannot meet the user.**

Module 02 can read a regulation. Module 05 can read a pricing page. This module needs to
know what a person does on a Tuesday morning, and no document states that directly.

The temptation — and the failure — is to write a plausible persona anyway. It will read
well, propagate into the PRD, and nobody downstream will be able to tell it was invented.

This document defines how to research users without access to users, and how to be honest
about the difference.

---

# Methodology Statement

> An inferred user, labeled as inferred, is useful.
>
> An inferred user presented as observed is a fabrication that six modules will trust.

---

# The Three Research Modes

Declare the mode before generating anything. Record it in the analysis header.

| Mode | Condition | Strongest tag available |
| --- | --- | --- |
| **Primary** | Real users consulted — interviews, surveys, observation | `[verified: interview, n=N, date]` |
| **Proxy** | Retrieval available, no user access | `[verified: <source>]` for what the source says; `[inferred: <basis>]` for what it implies |
| **Inferred** | No retrieval | `[assumption: needs validation]` only |

Most agent runs are **Proxy**. That is acceptable. Concealing it is not.

**Confidence ceiling:** in Proxy mode, confidence cannot exceed `medium`. In Inferred mode
it cannot exceed `low`.

---

# Proxy Research — Where Real User Evidence Hides

Users leave written traces. These are the places to look, roughly in order of value.

## 1. Reviews of competing products

The single richest source. People describe their actual workflow while complaining about
a tool that fails at it.

Read the **three-star reviews** first. Five-star reviews are enthusiasm; one-star reviews
are often a single bad support experience. Three-star reviews contain the specific,
qualified complaints of people who use the product daily and have thought about it.

Look for: what they were trying to do, what took too long, what they still do manually,
what they had to work around.

## 2. Support documentation and community forums

Vendor help centers reveal what users repeatedly fail at — every article exists because
enough people got stuck.

Community forums and subreddits reveal the workarounds people build. A widely-shared
workaround is a product gap with evidence attached.

## 3. Published studies and professional surveys

In regulated or professional domains, someone has usually measured the workflow. Time
studies, burnout surveys, workforce reports, and academic papers often contain the
quantified friction this module needs.

These are the best source of a `[verified]` tag on a claim like "clinicians spend N hours
per day on documentation".

## 4. Job postings

Underused and surprisingly informative. A job posting states which tools a role uses,
which tasks consume time, and what an organization is trying to fix by hiring.

## 5. Competitor onboarding and demo material

Shows the workflow the vendor believes their user has — and by omission, what they have
decided not to serve.

## 6. Trade press and practitioner blogs

Practitioners writing for practitioners describe reality more accurately than vendors
writing for buyers.

---

# What Each Source Can and Cannot Support

| Source | Can support | Cannot support |
| --- | --- | --- |
| Product reviews | What frustrates users of that product | What the whole segment thinks |
| Forums | That a workaround exists | How common it is |
| Studies | Quantified, generalizable claims | Anything outside the studied population |
| Job postings | Which tools an organization uses | How individuals feel about them |
| Vendor material | What the vendor believes | What is true |

The most common error is generalizing from a self-selected population. People who write
reviews are not representative — they are the annoyed and the delighted. Tag accordingly:

```
[inferred: from 14 three-star reviews of «product», Q1 2026 — review writers
 are self-selected and may over-represent frustration]
```

---

# The Quote Rule

**Never invent a user quote.**

This is the most damaging thing this module can produce. A fabricated quote reads as
primary evidence, is repeated in the Research Dossier, informs the PRD, and cannot be
detected downstream.

If a real quote is found, attribute it:

```
"I spend more time typing than talking to patients."
[verified: review of «product», «platform», 2025-11]
```

If none is found, write exactly that:

```
No primary user voice located. Persona attributes below are inferred from
proxy sources listed in §11.
```

The same rule applies to invented statistics, invented interview counts, and invented
customer names.

---

# Building a Persona From Proxy Evidence

Work attribute by attribute, not narratively. Narrative invites invention — the story
wants to be coherent, and coherence gets filled in where evidence is missing.

For each row: what does a source actually say, and what am I inferring from it?

| Attribute | Evidence pattern |
| --- | --- |
| Context | Job postings, professional body descriptions |
| Typical day | Time studies, workflow research |
| Frustration | Three-star reviews, forum threads |
| Constraints | Regulation from module 02, professional standards |
| Technical comfort | Support forum language, tooling mentioned in postings |
| Decision trigger | Reviews describing why they switched |
| Decision blocker | Reviews describing why they did not |

Then write the **gaps section**. What is not known about this person is as useful to
module 04 as what is — it becomes the validation list.

---

# Researching the Current Workflow

The highest-value output of this module, and the hardest to obtain by proxy.

Reconstruct it from:

- Competitor onboarding sequences — they mirror the workflow being replaced
- Support articles describing "how to import from X"
- Reviews that describe the before-and-after
- Published process or time studies
- Regulatory requirements that mandate certain steps

Then state the confidence per step. A workflow where step 3 is well-evidenced and step 4
is guessed should say so.

---

# Researching Switching Cost

Look for:

| Cost | Where the evidence is |
| --- | --- |
| Data migration | Competitor export documentation, migration guides, complaint threads |
| Retraining | Vendor training material length, certification requirements |
| Workflow disruption | Reviews mentioning implementation, "we lost a week" posts |
| Contractual lock-in | Vendor terms, minimum contract lengths on pricing pages |
| Risk | Forum discussions about failed migrations |

Migration complaint threads are especially valuable. People describe in detail exactly
what went wrong when they last switched — which is the cost your product will have to
overcome.

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| Ranking and quantifying problems | `04-problem` |
| Competitor feature comparison | `05-competition` |
| Willingness to pay | `06-business` |
| Wireframes and screen design | `10-execution` |
| Acquisition channels | `11-growth` |

This module establishes **who** and **what they do now**. Module 04 establishes what hurts.

---

# When No Retrieval Is Available

Inferred mode. Everything is an assumption.

1. Build the persona from the idea brief plus general domain reasoning.
2. Tag every attribute `[assumption: needs validation]`.
3. Set confidence to `low`.
4. State in the header that no user was consulted and no proxy source was read.
5. Add to `state.open_questions`: "Interview N «segment» to validate persona and workflow"
   — as the **first** validation task in the run.

A blueprint built on an admittedly-inferred user can still be built. The team simply knows
what to check first.

---

# Recording

| Destination | What |
| --- | --- |
| `state.evidence_log` | Every claim, tag, source, load-bearing flag |
| `state.assumptions` | Every inferred persona attribute, with a validation method |
| `state.open_questions` | User research tasks, ordered by what matters most |
| Analysis §11 | Sources table — every `[verified]` resolves here |
| Analysis §12 | Research mode and honest confidence |

---

# Self Assessment

- Did I declare my research mode before writing?
- Did I invent any quote, statistic, or detail?
- Does every persona row carry a tag or an explicit inference marker?
- Did I read three-star reviews, not just the extremes?
- Did I note where my sources are self-selected?
- Is my confidence level consistent with my mode?
- Did I write the gaps section, or only what I could fill?

---

> **Research Principle**
>
> You will not meet this user.
>
> Find their traces, reason from them carefully, and never let an inference
> wear the clothes of an observation.
