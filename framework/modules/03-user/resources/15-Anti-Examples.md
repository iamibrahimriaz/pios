---
Title: Anti-Examples
Module: 03-user
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show personas and journeys that look researched and are invented.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - Recognition of fabricated user research
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - User
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

This module can produce the framework's only undetectable error. A fabricated persona reads as research, propagates into the PRD, and
nobody downstream can tell it was invented. Every example below is the shape that error takes.

---

# Anti-Example 1 — The Fabricated Quote

## ❌ Looks researched

```
Dr Sarah Chen, 42, single-handed GP

"I spend two hours every evening finishing my notes. It's stealing time
 from my family and I'm exhausted. If something could just write them
 for me, I'd pay anything."

Goals:  reduce admin, spend more time with patients, avoid burnout
Frustrations: legacy software, too much typing, no time
```

**Why it fails**

- **The quote was invented.** It is the most damaging output this module can produce: it reads as primary evidence, it will appear verbatim
  in the PRD, and **nobody downstream can tell.** If no real voice exists, the correct output is the sentence "no primary voice was
  located."
- **"I'd pay anything" is a fabricated willingness-to-pay signal**, which `06-business` may build a price on.
- **Every row is plausible and none is tagged.** Time-poor, frustrated by legacy software, wants more patient time — true of almost every
  clinician, which means it constrains no product decision.
- **The name and photo-style detail add credibility without adding evidence.**

## ✅ Passes

```
PERSONA — Single-handed GP  [represents segment A]

Role and setting     single-handed practice, ~1,800 patients
                     [verified: «register» category]
Sessions per week    8–9 [inferred: standard contract terms]
Records system       «named system», cannot be replaced
                     [verified: operator's own practice]
When notes happen    after the last patient, at the practice or at home
                     [reported: 3 of 4 GPs known to the operator]
Time taken           unknown — not measured [GAP]
What they are measured on   UNKNOWN [GAP — highest-value missing row]
Who signs a purchase        UNKNOWN [GAP — blocks 06-business]

Primary voice: none located. No GP outside the operator's network has
been spoken to. Three reported statements are paraphrased in the
workflow section and are labeled as reports.

Gaps section is the actionable part of this persona.
```

---

# Anti-Example 2 — Two Personas Who Are One Person

## ❌ Looks researched

```
Segment 1: Dr James, 35, urban practice, tech-comfortable
Segment 2: Dr Margaret, 58, rural practice, less tech-comfortable
```

**Why it fails**

- **Demographic splits that change no behavior create the appearance of segmentation without its value.** Both would buy the product for
  the same reason, at the same price, through the same channel.
- **Age and location are proxies.** The thing that actually varies is whether there is a practice manager who runs procurement — and that
  is not visible in either persona.
- **It produces two personas that are the same person**, which is the module's named failure.

## ✅ Passes

```
Segment A  No practice manager. The GP is user, buyer and approver.
           Decision in one conversation. ~«n» practices.
Segment B  Has a practice manager. Purchase requires their sign-off and
           an information-governance check. Decision in 6–12 weeks.

These differ on who signs, which changes the product (audit and admin
views), the price, and the sales motion — 06-business.

Prioritized: A. Faster to first customer, no procurement.
Why not B, which is larger: the sales cycle exceeds the runway.
Given up by choosing A: the larger segment, and any multi-clinician
  workflow requirement. Recorded so it is not quietly reversed in 08.
```

---

# Anti-Example 3 — The Idealized Journey

## ❌ Looks researched

```
1. GP opens the records system
2. GP selects the patient
3. GP conducts the consultation
4. GP enters clinical notes
5. GP saves and closes
```

**Why it fails**

- **This is the documented process, not the observed one.** The gap between them is frequently the opportunity, and it is invisible here.
- **No tools named, no durations, no friction.** Step 4 is the entire problem, compressed into four words.
- **No workarounds and no unhappy paths.** A five-step journey with no friction has been summarized rather than recorded, and the
  opportunity sits in the transitions this removes.

## ✅ Passes

```
1. Opens «records system» — 20–40s, slow to load [reported]
2. Finds the patient — searches by name; duplicates are common
   FRICTION: picks wrong record occasionally; checks DOB to confirm
3. Consultation — 10 min slot, frequently overruns
   TOOL: nothing. Listens, remembers.
   WORKAROUND: scribbles keywords on a paper pad  ← strongest evidence
4. Writes the note — NOT NOW. Deferred to after the session.
   FRICTION: the transition is the problem. Recall degrades between
   step 3 and step 4, and the paper pad exists to bridge it.
5. After last patient — works through the pad, writing each note
   Duration: unknown [GAP]
   Interruptions: phone, results, staff [reported]

Unhappy path: interrupted mid-note → the record is left part-written and
  they cannot tell later which are finished.

SWITCHING COST
  Data migration   none — notes live in the records system, not with us
  Retraining       one person, minutes
  Disruption       a consultation is not a safe place to try new software
                   ← the real barrier
  Lock-in          none
  Risk             a missed note is a clinical and medico-legal event
  Bar to clear: must work first time, in a live consultation, with no
  rehearsal. That is a high bar and it belongs in 07-strategy.
```

---

# Anti-Example 4 — The Job That Names a Solution

## ❌ Looks researched

```
Jobs to be done
- "I want an AI assistant that writes my notes for me"
- "I want a dashboard showing my outstanding documentation"
- "I want voice recognition that understands medical terms"
```

**Why it fails**

- **All three name solutions.** The test is explicit: if the sentence names a solution, it is not a job. Each of these has already chosen
  the mechanism, which pre-empts `14-ai-systems`.
- **Written before the workflow was observed.** Interpretation before evidence produces jobs describing the intended product.
- **The emotional half is missing**, and for this segment it is decisive: not appearing distracted in front of a patient.

## ✅ Passes

```
Job 1  When a patient is describing symptoms, I want to capture what they
       said without breaking eye contact, so I can stay present in the
       consultation.
       Frequency: every consultation, ~140/week
       Satisfied today by: memory plus a paper pad. Poorly.
       Emotional: not appearing distracted matters as much as accuracy.

Job 2  When my last patient leaves, I want the record already complete,
       so I can go home.
       Frequency: 8–9 sessions/week
       Satisfied today by: nothing. They stay.

NOT serving: coding accuracy, referral letters, prescribing.
```

---

# Anti-Example 5 — Missing the Immovables

## ❌ Looks researched

```
The product will replace the practice's current documentation workflow
with a streamlined AI-first experience.
```

**Why it fails**

- **The records system cannot be replaced.** It is the system of record, contractually and clinically. A product requiring it to move does
  not get adopted, however good it is.
- **The immovables question was never asked**, and it is the most predictive question in the module.

## ✅ Passes

```
IMMOVABLES — what will not change regardless of product quality
  1. «Records system» stays. Policy and contract. → we sit alongside it
  2. The 10-minute appointment. Structural. → nothing may lengthen a
     consultation, even slightly
  3. A clinician signs the record. Regulatory. → 14-ai-systems autonomy
     ceiling is "drafts", not "acts"
  4. Patients can see the screen. → nothing sensitive displayed by default
  5. No personal phone in consultation at some sites. → voice input may
     be unavailable for part of the segment
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Fabricated quote | A first-person voice with no source |
| Demographic segmentation | Two personas who would buy identically |
| Idealized journey | Five tidy steps with no friction |
| Solution-shaped jobs | "I want a tool that…" |
| Immovables unasked | A plan that requires the unchangeable to change |

---

> **Resource Note**
>
> The passing persona has three rows marked UNKNOWN and no quotes.
>
> It is worth more than the complete-looking one, because every module
> after it can see exactly what has not been established.
