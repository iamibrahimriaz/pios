---
Title: Learning Objectives
Module: 13-operations
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a learner should know and be able to do after the Operations module.
Audience:
  - Product Managers
  - Founders
  - Operators
Prerequisites:
  - 13-operations/learn/01-Why-It-Matters.md
Outputs:
  - Operations planning competencies
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Objectives
  - Learn
---

# Learning Objectives

---

# Overview

> After this module you should be able to write a runbook a stranger could follow at 3am,
> compute what it truly costs to serve one customer, and put a person's name against every
> obligation.

---

# Knowledge Objectives

You should understand:

- What the **3am test** requires, and why access comes first in a runbook
- The four fields every obligation carries: cadence, owner, evidence, location
- The three things every alert needs, and why a missing one is worse than no alert
- What belongs in the true cost to serve, including human time at a real rate
- Why a support burden is a product signal before it is a staffing question
- Why a ceiling breach regresses rather than adjusts

---

# Thinking Objectives

The shift is from *how will we support this* to *what happens at 3am, and who does it*.

Instead of asking:

> "What is our support plan?"

ask:

- Who is awake, and what have we actually committed to?
- What does this cost per customer, including my own hours?
- Whose name is against this obligation, and what does it leave behind?
- What is the tempting action that makes this incident worse?
- Which of these support requests is a design defect?

---

# Skill Objectives

You should be able to:

- Write commitments the operator has actually agreed to, and label forecasts separately
- Grade severity by user impact, assignable in ten seconds
- Write a runbook with access, three columns, verification and a "do not do" line
- Give every obligation a cadence, an owner, evidence and a location
- Specify alerts with all three components, and delete the ones with no action
- Compute the true cost to serve and compare it with module 06's ceiling
- Report a breach as a regress with a recommendation

---

# Analytical Objectives

You should develop the ability to:

- Tell a commitment from a forecast, and notice when a document mixes them
- Recognize a runbook step that requires diagnosis rather than action
- Spot the obligation with no mechanism behind it
- Identify the dominant cost line, which is rarely the expected one

---

# Judgment Objectives

**What to commit to.** Only what the operator agreed to. A response target written on
someone's behalf is a promise that breaks during the first incident.

**Which burdens are permanent.** Some manual work is correct — high-touch onboarding in a
trust-sensitive segment, for example. The judgment is distinguishing that from work
created by an unclear interface, and pricing the first while fixing the second.

---

# You Have Learned This When

| Signal | What it indicates |
| --- | --- |
| Your cost model includes your own hours | The dominant cost is visible to you |
| Every obligation has a person's name | "The team" no longer reads as an owner |
| Your runbooks start with access | The 3am test is internalized |
| You have deleted an alert | Fatigue is understood as an accumulation |
| A breach makes you revisit price or scope | The regress rule holds under pressure |

---

# What This Module Does Not Teach You

It does not teach incident response practice at scale — this is a plan, not a discipline.
It does not build the mechanisms; module 09 did. It does not set the price; it reports
when the price does not work.

---

> **Objectives Principle**
>
> The skill is answering, in advance, the questions that are impossible to answer during
> an incident.
>
> Everything in this module is written to be read by someone who is tired, alone, and
> has no context.
