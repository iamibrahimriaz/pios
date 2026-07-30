---
Title: Anti-Examples
Module: 01-idea
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show idea briefs that look complete and are wrong, with the reason each fails.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - Recognition of plausible-but-wrong idea briefs
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Idea
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

Each of these looks like a completed idea brief. Each would pass a casual review. Each fails the module's gate for a reason worth
recognizing, because these are the shapes a real run produces.

---

# Anti-Example 1 — The Solution Wearing a Problem's Clothes

## ❌ Looks complete

```
Problem:   Clinicians need an AI tool that transcribes consultations
           and generates structured notes automatically.
Hypothesis: If we build this, clinicians will save time.
Segment:   Healthcare professionals.
```

**Why it fails**

- **The problem names the solution.** "Need an AI tool that transcribes" is a mechanism. The problem is whatever the transcription is
  *for*, and stating it this way pre-empts `14-ai-systems`, whose entire method is to compare mechanisms and sometimes drop the AI one.
- **The hypothesis is unfalsifiable.** "Will save time" has no amount, no baseline and no population. Nothing could disprove it.
- **The segment is a category.** "Healthcare professionals" spans a hospital consultant and a locum GP, who have different problems,
  different budgets and different buyers.

## ✅ Passes

```
Problem:   Single-handed GPs complete consultation notes after their last
           patient leaves, in unpaid time.
Hypothesis: If notes could be completed during the consultation, GPs would
           leave the practice at their scheduled finish time.
           [assumption: needs validation]
Segment:   Single-handed general practices, «named jurisdiction».
Not solving: Note quality, coding accuracy, referral letters.
```

---

# Anti-Example 2 — The Confident Brief

## ❌ Looks complete

```
Problem:      Clinicians spend 90 minutes a day on documentation.
Market:       £2.4bn globally.
Success:      80% of users complete notes before the patient leaves.
Confidence:   High.
```

**Why it fails**

- **Every number is untagged and none has a source.** The 90 minutes, the £2.4bn and the 80% are indistinguishable from measurements. One
  of them may be researched; the reader cannot tell which.
- **80% is invented in the first hour** and will be quoted as a commitment. `01-idea/knowledge/Success-Metrics.md` forbids naming the
  number; name the observable and stop.
- **"Confidence: High" on an unresearched brief** is the framework's central failure in one word. Confidence at this stage describes
  enthusiasm.

## ✅ Passes

```
Problem:    Documentation continues after the last patient leaves.
            [inferred: three of four GPs interviewed described this]
Market:     Not yet sized — 02-market.
Success:    Observable: notes reaching completed state before the
            appointment ends. Target set in 12-metrics.
Confidence: Low. The problem is reported, not observed. Nothing is quantified.
```

---

# Anti-Example 3 — The Vision as Scope

## ❌ Looks complete

```
Vision:  The operating system for modern primary care.
Mission: Empowering clinicians with intelligent tools across the
         entire practice workflow.
MVP:     Notes, coding, referrals, prescriptions, dashboards, patient
         messaging.
```

**Why it fails**

- **The vision justifies everything.** Six MVP items follow from a vision large enough to accommodate any of them, and each was
  individually reasonable. `01-idea/knowledge/Vision.md` names this as the framework's primary scope-creep vector.
- **The mission is future tense and unfalsifiable.** It cannot be checked against a requirement list, which is the only thing a mission is
  good for.
- **The MVP was decided here.** `07-strategy` draws that line, from evidence this module does not have yet.

## ✅ Passes

```
Vision:  Nobody writes up notes after hours.
Mission: We help single-handed GPs complete consultation notes during
         the appointment.
MVP:     Not decided here — 07-strategy, after the problem is ranked.
```

---

# Anti-Example 4 — The Unstated Operator Goal

## ❌ Looks complete

```
Idea:     Clinical documentation tool for solo GPs.
Segment:  Single-handed practices, «jurisdiction».
Goals:    Grow to 10,000 practices; become the category leader;
          raise a Series A within 18 months.
```

**Why it fails**

- **The operator was never asked.** These goals were supplied by convention. `01-idea/knowledge/Goals.md` calls the operator's own goal the
  most consequential unstated input in the framework — replace a salary, venture scale, or sell to one known buyer produce three different
  products from this idea.
- **The consequence is invisible and large.** Venture-scale goals make `02-market`'s sizing decisive and push `06-business` toward growth
  over margin. If the operator actually wants to replace a salary, every one of those decisions is wrong.

## ✅ Passes

```
Operator goal: Replace a salary within two years, single operator,
               no external funding. [verified: operator]
Consequence:   06-business optimizes margin, not growth.
               11-growth needs no venture-scale channel.
               A narrow tool serving 40 practices at a real price may
               be sufficient — 07-strategy to weigh.
```

---

# Anti-Example 5 — The Assumption Ledger That Isn't

## ❌ Looks complete

```
Assumptions
- Clinicians want to reduce documentation time.
- The market is large.
- AI is good enough for this.
- Practices have budget for software.
```

**Why it fails**

- **None is falsifiable and none has a test.** Each is a sentence someone would agree with, which is why they survive unexamined.
- **"AI is good enough" is load-bearing and vague.** Good enough for what, at what accuracy, judged by whom? `14-ai-systems` cannot act on
  this.
- **No basis, no owner, no validation route.** `04-problem` needs each of these to become a test with an invalidating result.

## ✅ Passes

```
Assumptions
1. Single-handed GPs complete notes outside session time
   [assumption] — validate: ask 10 GPs about last week specifically.
2. They would accept a draft note without reading it line by line
   [assumption] — LOAD-BEARING. If false, no time is saved.
   Validate: Wizard of Oz, hand-written drafts, 5 GPs.
3. Practices can authorize a £40/month purchase without a committee
   [assumption] — validate: ask who signs.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Solution stated as problem | The mechanism appears in the problem sentence |
| Untagged numbers | Measurements and guesses look identical |
| Confidence without evidence | "High" on an unresearched brief |
| Vision used as scope | A large destination justifying a wide MVP |
| Operator goal assumed | Growth-shaped defaults nobody chose |
| Assumptions without tests | Agreeable sentences with no invalidating result |

Every one of these passes a casual read. That is what makes them worth recognizing.

---

> **Resource Note**
>
> A brief that reads confidently is the failure mode, not the goal.
>
> The honest version looks less finished and is worth more, because every
> weak claim is visible to the modules that have to build on it.
