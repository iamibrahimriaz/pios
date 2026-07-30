---
Title: Best Practices
Module: 09-technology
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced engineers do when designing a system that inexperienced ones do not.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - Higher-quality technical designs
Related Modules:
  - 10-execution
Tags:
  - Technology
  - Best Practices
---

# Best Practices

---

# 1. Do the Load Arithmetic Before Anything Else

Multiply it out on the first page: users, sessions, requests, peak ratio.

Almost every architecture argument dissolves once the number is visible, and the number takes
two minutes. Doing it after the design exists means defending the design instead of sizing it.

---

# 2. Extract the Nouns From the Requirement Text Literally

Read module 08 §7 and list every noun the requirements act on before deciding what an entity is.

Working from the text produces entities the requirements need. Working from a picture of the
product produces entities that products like this usually have.

---

# 3. Write the Column Type in the Same Keystroke as the Column Name

Never a name alone, not even in a draft.

A column list with no types is the single most common form of an unbuildable data model, and it
happens because names come to mind and types require decisions.

---

# 4. State the On-Delete Behavior as a Business Rule

Not "cascade" alone — "cascade, because a deleted consultation's notes have no meaning
independently".

It is a product decision about what happens to real data. Written as a database keyword, it gets
chosen by whoever writes the migration.

---

# 5. Write Every Index With the Query It Serves

If the query cannot be named, the index is a guess.

Indexes cost writes and storage. An index with a named query is a decision; an index without one
is a habit.

---

# 6. Draw the Forbidden Transitions Explicitly

Draw the legal state diagram, then list the arrows that must never exist, and for each say what
prevents it.

"Nothing prevents it, but nobody would do that" is the sentence that precedes the incident.

---

# 7. Convert Every Edge Case Into a Status Code as You Read It

Work through module 08 §8 row by row and assign each a status and an error code.

Done as a separate pass later, the mapping is incomplete, and the missing cases are the ones
module 08 worked hardest to find.

---

# 8. Decide Idempotency Per Write, Not Globally

Retries are universal — clients retry, proxies retry, users press buttons twice.

The question is not whether retries happen. It is what the second identical request does, and it
has a different answer per operation.

---

# 9. Write the Obligation Trace as a Table, Never as Prose

Obligation, mechanism, enforcement point, citation. Four columns.

Prose lets an obligation be met by a reassuring sentence. A table with an empty mechanism column
is visibly unmet, which is the point.

---

# 10. Name the Enforcement Point for Every Control

Not "authorization is role-based" — "the query layer applies a clinician predicate to every
patient read".

A control without a location cannot be implemented, reviewed or tested, and it is the most
common serious gap in designs of this kind.

---

# 11. Ask the One Security Question That Matters

*What would it take for one user of this product to see another user's data?*

Then walk the path through this design. That single question, answered honestly, is worth more
than a generic vulnerability checklist.

---

# 12. Choose the Shape Before the Technology, and Write the Date

Shape follows load and team. Then technology, with its version.

Recording the version matters: a capability claim without one is unverifiable a year later, when
someone needs to know whether it was ever true.

---

# 13. Write the Rejected Alternatives Before the Chosen One

Fill in what was rejected and why, then write the choice.

Working the other way produces excellent justifications unrelated to the actual reason — which is
often familiarity, and would have been a perfectly acceptable reason to state.

---

# 14. Make the Trade-off Column Say Something Bad

Every choice is worse at something. If the trade-off column reads as a mild caveat, it has not
been filled in.

"Slight learning curve" is a benefit with a hedge. "Cannot do «X» without «Y»" is a trade-off.

---

# 15. Cost the Things Nobody Remembers

Egress, backups, log retention, staging environments, monitoring, the free tier expiring.

A cost model missing these is not conservative — it is wrong in the direction that matters, and
it is what makes a design look affordable.

---

# 16. Divide by Users and Compare to the Ceiling

One line of arithmetic: total cost, divided by launch users, against the ceiling from
`06-business`.

It is the most decisive sentence in the document, and it cannot be argued with.

---

# 17. Sort Decisions by Cost of Reversal, Then Spend Accordingly

Cheap, needs-a-migration, one-way. Put the strongest arguments on the third group.

Attention naturally follows how interesting a decision is, which correlates poorly with how
expensive it is to undo.

---

# 18. Look Up Every Version Claim, Every Time

Capabilities, limits, quotas, prices, deprecations.

These change, they are version-scoped, and they are the statements most likely to be written
from memory with complete confidence.

---

# 19. Write What You Are Not Building For

Three sentences: the scale, the capability, the environment.

They cost nothing and prevent a category of rework, because the first engineer to hit a limit
otherwise treats it as an oversight and removes it.

---

# 20. Say Whether Restore Has Been Tested

An untested restore is not a backup. If it has not been tested, say so and make it a task.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Choosing the stack first | The requirements bend to fit it |
| Modeling from a picture of the product | Produces conventional entities, not needed ones |
| Column names without types | The most common unbuildable model |
| On-delete as a keyword | A product decision made in a migration file |
| Indexes without queries | Cost with no named benefit |
| Only the legal state diagram | Forbidden transitions become defects |
| Edge cases mapped in a later pass | The hardest-won cases are the ones missed |
| Global idempotency assumption | Duplicates in production |
| Compliance in prose | Obligations met by reassurance |
| Controls without enforcement points | Cannot be implemented or tested |
| Generic threat lists | Examines nothing about this system |
| Justification written after the choice | Excellent reasoning, wrong reason |
| Trade-offs that are benefits with hedges | Nothing was weighed |
| Cost models missing egress and backups | Affordable on paper only |
| Even rigor across all decisions | The one-way doors get the least attention |
| Version claims from memory | The most reliably wrong statements in the document |
| No stated non-goals for scale | Every limit reads as an accident |

---

# Self Assessment

- Did I do the arithmetic before designing?
- Did I extract entities from the requirement text?
- Does every column have a type written beside its name?
- Is every on-delete behavior stated as a business rule?
- Does every index name a query?
- Did I draw the forbidden transitions and what prevents them?
- Did every edge case become a status code?
- Did I decide idempotency per operation?
- Is my obligation trace a table with no empty mechanisms?
- Does every control name where it is enforced?
- Did I walk the cross-user data path?
- Did I write the rejections before the choice?
- Does every trade-off say something bad?
- Did I cost egress, backups and log retention?
- Is the cost per user inside the ceiling?
- Do the one-way doors carry the strongest arguments?
- Did I look up every version claim?
- Did I say what this is not built for?
- Did I say whether restore has been tested?

---

> **Practice Principle**
>
> Two practices here are arithmetic and one is a single question
> about security.
>
> Those three catch more real defects than the other seventeen
> combined — and all three take under ten minutes.
