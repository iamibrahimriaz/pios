---
Title: Best Practices
Module: 04-problem
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced practitioners do when validating problems that inexperienced ones do not.
Audience:
  - AI Agents
  - Researchers
  - Product Managers
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - Higher-quality problem evidence
Related Modules:
  - 07-strategy
Tags:
  - Problem
  - Best Practices
---

# Best Practices

---

# 1. Harvest From Handoffs, Not Tasks

Friction concentrates where work passes between steps, people, or tools — re-entering
data, waiting for approval, remembering what the system did not carry forward.

Read the workflow from `03-user` looking at the arrows, not the boxes.

---

# 2. Follow the Workaround to Its Cost

Finding a workaround is the start, not the finish. Ask what the workaround itself costs.

A spreadsheet that solves the problem but must be rebuilt every month is a problem with
an extra step attached — and that monthly rebuild is often the more tractable target.

---

# 3. Search for the Word "Just"

"I just export it and paste it in." "We just do that manually."

"Just" marks a step someone has normalized. It is where absorbed costs hide, and it is a
reliable signal in reviews, forum posts, and interview transcripts.

---

# 4. Look for Roles That Exist to Absorb a Problem

If an organization employs someone primarily to bridge two systems, reconcile two
records, or chase a process, the problem has a salary attached.

That is the strongest cost evidence available, and it appears in job postings.

---

# 5. Count Out-of-Hours Work

Work that spills past the end of the day is rarely reported as a product problem, and is
almost always among the most painful.

"I do notes at home after clinic" outranks every in-hours annoyance on severity, and it
appears constantly in forums while appearing almost never in feature requests.

---

# 6. Read Competitor Changelogs

A feature that keeps being fixed release after release marks a problem the vendor cannot
solve structurally.

That is a validated problem, evidenced by someone else's engineering budget.

---

# 7. Search for the Graveyard Deliberately

Query for shutdowns, not launches: "shutting down", "sunset", "no longer maintained",
plus the category name.

Then find out why. A failed predecessor is the cheapest lesson in the run, and the reason
is usually structural rather than executional.

---

# 8. Score Before You Choose

The instinct is to know which problem matters and score afterward to confirm it.

Score everything first, then look at the table. Occasionally the top scorer is not the
interesting one — and that discovery is the module doing its job.

---

# 9. Write the Assumed List First

Start by assuming nothing is verified. Then promote only what has a retrievable source at
evidence rank 1–3.

Working in this direction makes promotion an active decision. Working the other way makes
demotion feel like losing ground, and things quietly stay put.

---

# 10. Quantify With a Derivation

`"Costs about 90 minutes a day"` invites the question: how do you know?

```
90 min/day = 15 patients/day [verified: «source»]
           × 6 min/note [verified: time study, «source»]
```

Same discipline as module 02. A cost that shows its arithmetic can be argued with, and
therefore trusted.

---

# 11. Name the Silent Group

Every source is self-selected. State who is missing.

"Practitioners who accept this process as normal are absent from these sources" is a real
finding — that group is usually the majority and the hardest to sell to.

---

# 12. Design Tests That Could Embarrass You

The test of a validation plan is whether a result could make you abandon the idea.

"Interview 10 solo GPs. If fewer than 6 describe after-hours work unprompted, the
assumption is invalidated" is a real test. It has a number, a method, and a way to lose.

---

# 13. Put the Cheapest Test First

The most load-bearing assumption is usually willingness to pay or top-three status —
neither of which requires a build to test.

A conversation, a landing page, or a survey answers more per hour spent than any
prototype.

---

# 14. State the Verdict Before the Analysis

Put the verdict in section 1. A reader who stops after thirty seconds should leave with
the judgment, not with the impression that a lot of work was done.

Burying an `UNVALIDATED` verdict at the end is how it gets missed by the person who most
needed to see it.

---

# 15. Deliver Bad News Plainly

If the problem is not proven, write that it is not proven. Do not soften it with hedging,
and do not bury it under the problems that were verified.

The finding costs a week now. Not finding it costs a year later. Delivering it clearly is
the single most valuable thing this module does.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Harvesting only from complaints | Misses absorbed costs nobody reports |
| Treating agreement as validation | People agree with everything |
| Scoring after choosing | Confirms a decision instead of informing it |
| Promoting inference to fill the validated list | Undetectable downstream |
| Asserting cost without derivation | Cannot be challenged, so cannot be trusted |
| Vague validation plans | Nobody can act on them |
| Tests with no failure condition | Prove nothing |
| Softening the verdict | Defeats the purpose of the module |

---

# Self Assessment

- Did I harvest from handoffs, not just tasks?
- Did I cost the workaround as well as finding it?
- Did I look for absorbed costs and out-of-hours work?
- Did I read competitor changelogs and search the graveyard?
- Did I score before choosing?
- Did I start from "assumed" and promote deliberately?
- Do my cost figures show arithmetic?
- Could any of my tests embarrass me?
- Is the verdict in section 1, stated plainly?

---

> **Practice Principle**
>
> The problems worth building for are usually the ones people have stopped
> complaining about — because they stopped expecting them to be fixed.
