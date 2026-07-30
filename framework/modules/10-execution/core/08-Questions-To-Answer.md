---
Title: Questions To Answer
Module: 10-execution
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Delivery Leads
Prerequisites:
  - 10-execution/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - Execution
  - Questions
---

# Questions To Answer

---

# Overview

Every question here is one that would otherwise be answered on the first morning of work, by
whoever is available, under time pressure.

Questions marked **OPERATOR** cannot be answered by inference. Two of them — team facts and
launch constraints — change the plan completely, and the framework has no way to guess either.

---

# 1. Inherited Inputs

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What is the first shippable slice? | The first milestone is invented |
| 1.2 | What is the critical path from module 08? | Sequencing has no basis |
| 1.3 | Which technical decisions are one-way doors? | The irreversible ones get committed late |
| 1.4 | Is Milestone Zero required? | Building may start on an assumed problem |
| 1.5 | What are the persona's real operating constraints? | Flows assume conditions that do not exist |
| 1.6 | What open questions and blockers arrived from modules 08 and 09? | They end up inside build instructions |
| 1.7 | **OPERATOR** — what team will build this? | Durations become fiction |
| 1.8 | **OPERATOR** — is there a fixed launch date or external deadline? | The plan may be sequenced against the wrong constraint |

---

# 2. Flows

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | Which two or three paths carry the product? | Everything is mapped and nothing is read |
| 2.2 | For each: what triggers it, and how often does the user do it? | Frequency drives design weight |
| 2.3 | What does the user see, do, and get, at each step? | Screens invented during build |
| 2.4 | What can fail at each step? | Failure behavior improvised |
| 2.5 | For each failure: what is the recovery path? | The user is stuck at the first error |
| 2.6 | For each failure: **is their work preserved?** | Silent data loss, the fastest way to lose trust |
| 2.7 | How many steps does the core job take? | Nothing to reduce |
| 2.8 | Does each design principle name the finding it came from? | Platitudes that constrain nothing |

---

# 3. First Value

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What exactly is "first value" for this product? | The most predictive adoption number is undefined |
| 3.2 | How many steps to reach it? | Cannot be shortened |
| 3.3 | How many minutes? | No target |
| 3.4 | What is the longest unavoidable step, and why can it not be removed? | The obvious improvement is never examined |
| 3.5 | Is migration required before first value? | The largest drop-off point unplanned |
| 3.6 | What does a brand new user see before any data exists? | The first screen is empty and unexplained |

---

# 4. Screens and States

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What screens exist, and why does each exist? | Screens accumulate |
| 4.2 | For each: what shows when there is no data, and what action is offered? | Dead ends at first use |
| 4.3 | For each: what shows while waiting? | Perceived failure |
| 4.4 | For each: what shows on error, and how does the user recover? | Error text written by whoever builds it |
| 4.5 | For each: what shows when the user lacks permission? | Authorization behavior invented |
| 4.6 | What accessibility standard applies, and how is it verified? | An aspiration |
| 4.7 | What does the persona's physical context require concretely? | Built for an office by someone in an office |

---

# 5. Slicing

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | For each milestone: **what can you show a real user doing?** | Layers disguised as milestones |
| 5.2 | Could delivery stop after this milestone and leave something usable? | Nothing is independently shippable |
| 5.3 | Is the first milestone built around module 08's first shippable slice? | The plan starts somewhere arbitrary |
| 5.4 | Does any milestone deliver only infrastructure? | Learning deferred to the end |
| 5.5 | What does each milestone teach about the product? | Work in the dark, unnoticed |

---

# 6. Sequencing

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | What principle governs the order? | The order is arbitrary and looks deliberate |
| 6.2 | Why that principle and not the alternative? | Cannot be re-evaluated later |
| 6.3 | Is Milestone Zero first, where the problem is assumed? | Building before validating |
| 6.4 | Where does each one-way door get committed, and why there? | The most consequential sequencing decision is implicit |
| 6.5 | Which milestones can ship independently? | Everything waits for everything |
| 6.6 | What could run in parallel, and what would that require? | Compression options invisible |
| 6.7 | What is the longest chain? | No critical path |
| 6.8 | At what points is the plan re-evaluated against real data? | The plan is executed on faith |
| 6.9 | At each decision point, is "stop" a possible outcome? | A decision point with one outcome is a checkpoint in name only |

---

# 7. Done

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | For each milestone: which acceptance criteria must pass? | "Done" is an opinion |
| 7.2 | What is the non-functional bar — tests, environment, review? | Done means "it works on my machine" |
| 7.3 | **What is explicitly not done at this point?** | The done milestone that needs three more weeks |
| 7.4 | Who decides that a milestone is done? | Nobody, then everybody |

---

# 8. Verification

| # | Question | If unanswered |
| --- | --- | --- |
| 8.1 | What is tested at each level? | Everything tested twice, or not at all |
| 8.2 | **Does every MUST requirement have at least one verification?** | Requirements shipped unverified |
| 8.3 | Are the five edge categories per requirement covered? | Failure behavior exists in documents only |
| 8.4 | What cannot be automated, and who does it manually? | Manual work assumed and never scheduled |
| 8.5 | **What is deliberately not tested, and why?** | An implied claim of full coverage |
| 8.6 | How is a failure recognized and reported? | Failures observed and forgotten |

---

# 9. Estimates

| # | Question | If unanswered |
| --- | --- | --- |
| 9.1 | **OPERATOR** — what is the team's size and composition? | Durations are meaningless |
| 9.2 | Where does each duration come from? | Numbers treated as commitments |
| 9.3 | What is most likely to take longer than stated, and why? | Estimation risk unnamed |
| 9.4 | If no team facts exist, does the plan carry relative sizes only? | The estimate boundary was crossed |

> 9.1 is the question that determines whether this module may state durations at all. Without
> it, the honest output is sequence, dependency and relative size.

---

# 10. Blockers and Readiness

| # | Question | If unanswered |
| --- | --- | --- |
| 10.1 | What cannot start until a question is answered? | A team stalls silently |
| 10.2 | For each blocker: who owns it, and which milestone needs it? | "The team" owns it, so nobody does |
| 10.3 | Can the first milestone proceed with all blockers unresolved? | The whole plan may be blocked and look fine |
| 10.4 | Is the first task nameable in one sentence? | Day one is spent deciding |
| 10.5 | Does every reference resolve to a document that exists? | The reader is sent nowhere |
| 10.6 | **Is there any unresolved assumption in a build-blocking position?** | Someone guesses, and never says so |
| 10.7 | **Could a builder with no context start today?** | The handoff is a summary |
| 10.8 | What rules must hold regardless of implementation choices? | Non-negotiables treated as preferences |

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 1 | §2 Inherited Inputs |
| 2 | §3, §4 Principles and critical paths |
| 3 | §5 Time to First Value |
| 4 | §6 Screens and States |
| 5 | §7 Milestones |
| 6 | §8, §9 Sequence and decision points |
| 7 | §7 Definitions of done |
| 8 | §10 Verification |
| 9 | §14 Estimate Basis |
| 10 | §12, §13, §16 Blocked work, non-negotiables, readiness |

---

# Self Assessment

- Did I answer 2.6 for every failure?
- Is 3.1 a specific moment, or a vague benefit?
- Did I answer 4.2 through 4.5 for every screen?
- Did I write the answer to 5.1 down, for every milestone?
- Is 6.4 answered with reasoning, not just a position?
- Did I answer 7.3, or only 7.1?
- Did I answer 8.5 honestly?
- Did I ask 9.1 before writing any duration?
- Is 10.6 genuinely no?

---

> **Question Principle**
>
> Two questions here are for the operator and cannot be inferred:
> who is building this, and by when.
>
> Guessing either produces a plan that reads well and cannot be run.
