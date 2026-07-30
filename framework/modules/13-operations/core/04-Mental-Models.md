---
Title: Mental Models
Module: 13-operations
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which an operations plan should be examined.
Audience:
  - AI Agents
  - Operators
  - Founders
Prerequisites:
  - 13-operations/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of the operations plan
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Mental Models
---

# Mental Models

---

# Model Statement

> An operations plan is tested only when everything has gone wrong.
>
> These lenses are ways of running that test while it is still cheap.

---

# 1. The 3am Read

**Reveals:** every place a runbook assumes its author.

Read it as someone who did not build the system, was asleep ten minutes ago, and has nobody to ask.
At each step, ask: do I know exactly what to type or click, and what I should see?

**Hides:** it tests followability, not correctness. A perfectly clear runbook can perform the wrong
recovery.

---

# 2. The Person Who Noticed

**Reveals:** severity levels that need an architect.

Someone reports a problem. Could they assign a severity in ten seconds, knowing nothing about the
internals?

If not, the grading is component-based, and the argument about whether this is an S1 will happen
during the S1.

**Hides:** user impact is not the only axis. A silent data-integrity fault has low visible impact and
very high severity.

---

# 3. The Silent Outage

**Reveals:** the missing communication stage.

Imagine the product is down for two hours and users are told nothing. Then imagine the same two hours
with a status message at minute five.

The technical outcome is identical. The trust outcome is not, and the difference costs one sentence
written in advance.

**Hides:** communication does not fix anything. It buys patience, which is finite.

---

# 4. The Ticket That Repeats

**Reveals:** support burden that is really a product defect.

Take the request you expect most often. Now imagine receiving it two hundred times.

At that volume the question changes from "how do we answer this?" to "why does this happen?" — and
that is the question worth asking before the two hundred, not after.

**Hides:** some repeated questions are inherent to the domain. The lens asks the question; it does
not presume the answer is always a fix.

---

# 5. The Unowned Obligation

**Reveals:** compliance that will lapse.

For each recurring obligation, name the person. Then ask whether that person knows.

An obligation with a role in the owner column and nobody informed is indistinguishable, in practice,
from one nobody wrote down.

**Hides:** an informed owner can still be too busy. Cadence and workload need checking together.

---

# 6. The Auditor's Request

**Reveals:** compliance that cannot be demonstrated.

An auditor asks for evidence that access logs were reviewed for the last twelve months. What do you
hand them, and how long does producing it take?

Being compliant and being able to show it are different achievements. This lens tests the second,
which is the one that is actually assessed.

**Hides:** evidence can exist and be inadequate. Volume of artifacts is not quality of control.

---

# 7. The Restore That Was Never Run

**Reveals:** the most consequential untested assumption in operations.

Backups are configured. Has anyone restored from one? Into what? Verified how?

Extend it to the siblings: has a rollback been rehearsed, has a runbook been walked? All three are
cheap to close and all three are discovered open during the incident that needed them.

**Hides:** a restore tested once, long ago, on a much smaller dataset, is weaker evidence than it
feels.

---

# 8. The Holiday

**Reveals:** single-person dependencies.

The person who knows the system is unavailable for two weeks. Which alerts have no recipient, which
obligations lapse, and which runbooks cannot be executed?

Everything the answer names is a dependency, and most of it is fixable by writing something down.

**Hides:** documentation reduces the dependency without removing it. Some knowledge only transfers by
doing.

---

# 9. The Third Month

**Reveals:** unsustainable coverage.

The rota worked in month one because it was new and the volume was low. Play it forward to month
three, with real users, at the stated response targets.

Coverage claims fail in month three, not month one, which is why they are usually made without
concern.

**Hides:** volume may also be lower than feared. The point is to know which assumption the plan is
resting on.

---

# 10. The Complete Bill

**Reveals:** whether the business survives being operated.

Add every line — infrastructure, third parties, measurement, support time, compliance time — and
divide by launch users. Then read `06-business`'s ceiling.

This is the last of the framework's three arithmetic checks against the business model, and the only
one that includes human time.

**Hides:** early support cost is unusually high per user and falls with scale. Check both launch and
target.

---

# 11. The Alert Nobody Reads

**Reveals:** monitoring that trains people to ignore monitoring.

For each alert, ask what the recipient does when it fires. If the honest answer is "looks at it and
closes it", the alert is teaching a habit that will one day be applied to a real one.

**Hides:** some alerts are informational by design. Those belong in a dashboard, not in a channel
that pages someone.

---

# 12. The Limit Stated Plainly

**Reveals:** the most useful thing this module can produce.

Rather than asking what coverage to promise, ask what coverage is actually true. Then write that.

"Weekday hours, best effort, four-hour response during business hours, and here is what happens when
I am away" is a plan someone can run and users can rely on. An aspirational table is neither.

**Hides:** nothing. Understated limits can be improved later, and overstated ones can only be
apologized for.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking runbooks | The 3am Read |
| Checking severity | The Person Who Noticed |
| Checking incident communication | The Silent Outage |
| Checking support burden | The Ticket That Repeats |
| Checking obligation ownership | The Unowned Obligation |
| Checking audit readiness | The Auditor's Request |
| Checking recovery | The Restore That Was Never Run |
| Checking dependencies | The Holiday |
| Checking sustainability | The Third Month |
| Checking the business | The Complete Bill |
| Checking alert hygiene | The Alert Nobody Reads |
| Checking honesty | The Limit Stated Plainly |

Apply The Ticket That Repeats early — it changes what goes on the roadmap. Apply The Complete Bill and
The Limit Stated Plainly last, on the finished plan.

---

# Self Assessment

- Where would a stranger get stuck at 3am?
- Could whoever noticed assign a severity?
- What do users read during the first ten minutes of an outage?
- Which repeated ticket should be a roadmap item?
- Which owner has not been told?
- What would I hand an auditor, and how long would it take?
- Has anyone ever restored from a backup?
- What lapses when the key person takes two weeks off?
- Does this rota survive month three?
- What is the complete bill per user?
- Which alert gets looked at and closed?
- What coverage is actually true?

---

> **Mental Model Principle**
>
> The Limit Stated Plainly is the lens that produces the most value
> and feels like the least work.
>
> An understated limit can be improved. An overstated one can only
> be apologized for, repeatedly.
