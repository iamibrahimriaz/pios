---
Title: Problem Discovery
Module: 04-problem
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Collect candidate problems without filtering, and classify them before scoring.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - problem_inventory
Related Modules:
  - 03-user
Tags:
  - Problem
  - Discovery
  - Method
---

# Problem Discovery

---

# What It Is

The collection of every candidate problem, followed by the sort that decides which of them are
problems at all.

Three categories, and the distinction between them prevents most of the damage this module can do:

| Type | Definition | Test |
| --- | --- | --- |
| **Problem** | Something costs them time, money, risk, or wellbeing | Is there a cost when it is not solved? |
| **Symptom** | A visible effect of a problem underneath | Ask "why does that matter?" — if there is an answer, it is a symptom |
| **Preference** | A wish with no cost attached | Nothing bad happens if it is never satisfied |

| Statement | Type | Reasoning |
| --- | --- | --- |
| "The export takes four clicks" | Symptom | Why does that matter? → they miss their accountant's deadline. *That* is the problem |
| "I do notes at home after clinic" | Problem | Costs unpaid hours and family time |
| "I wish it had dark mode" | Preference | No cost when unmet |

---

# When It Applies

In Stage 1 (Harvest) and Stage 2 (Classify), working entirely from `03-user`'s outputs — the friction
in `current_workflow`, jobs served poorly, switching-cost pain, and the immovables.

---

# How to Apply It Here

**Do not filter while collecting.** Filtering during collection loses the problem nobody was looking
for, which is frequently the sharpest one. Harvest first, classify second.

**Record each in the person's own framing.** "I end up doing notes at home after clinic" is more useful
than "documentation burden" — the cleaned-up version has already lost the cost, the setting and the
specificity that make it scorable.

**For every symptom, carry the problem beneath it forward instead.** The symptom stays on the page as
the observed evidence; what gets scored is the thing underneath.

**Keep excluded preferences visible.** They will be re-proposed in `08-product`, and a written record
of why they were excluded settles that argument once rather than repeatedly.

**Attribute each problem to a persona.** A problem that cannot be attached to a specific person from
`03-user` is a general observation, and it usually means the persona was too vague — which is one of the
triggers for returning to module 03.

---

# Where It Misleads

**Symptoms present themselves and problems do not.** People report what is visible and immediate — the
clicks, the slowness, the layout. The cost sits one question below, and the question has to be asked
deliberately every time.

**A cleaned-up problem statement is easier to agree with and harder to test.** Abstraction rises through
this module unless resisted: "documentation burden" cannot be scored for frequency or cost, so the
abstraction quietly becomes unfalsifiable.

**Preferences arrive from the most articulate sources.** Reviews and forums self-select for people
motivated to write, and irritation is more writable than a normalized cost. Weight accordingly.

**An empty harvest is a real result.** A run reaching this module and finding nothing painful has learned
something valuable — provided it says so rather than manufacturing a problem to justify continuing.

---

# Related

| | |
| --- | --- |
| `Problem-Tree.md` | Structuring symptoms above their causes |
| `Root-Cause.md` | How far down to go |
| `Evidence.md` | What each statement is worth |
| `03-user` | Where every source in the harvest comes from |

---

> **Concept Note**
>
> Ask "why does that matter?" of every complaint, and score the
> answer rather than the complaint.
>
> A product built on symptoms optimizes four clicks and leaves the
> missed deadline in place.
