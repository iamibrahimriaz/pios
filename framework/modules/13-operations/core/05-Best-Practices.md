---
Title: Best Practices
Module: 13-operations
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced operators do when planning operations that inexperienced ones do not.
Audience:
  - AI Agents
  - Operators
  - Founders
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - Higher-quality operations plans
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Best Practices
---

# Best Practices

---

# 1. Ask Who Runs This Before Writing Anything

One question, before the first owner is typed.

Every owner, target and rota in the document depends on the answer, and a document full of invented
owners cannot be corrected — only rewritten.

---

# 2. Ask What Hours Can Actually Be Covered, Not What Would Be Good

The operator knows what they can staff. The framework does not.

Asked the second way, the answer is aspirational and becomes a promise to users. Asked the first way,
it becomes a plan.

---

# 3. Write the Volume Estimate With Its Basis in the Same Cell

"≈3 tickets per 100 users weekly `[assumption]` — basis: the confusion points in the flow analysis."

The basis is what lets the number be argued with. Without it, the figure acquires authority by being
repeated.

---

# 4. Imagine Every Support Request Two Hundred Times

At that volume, "how do we answer this?" becomes "why does this happen?"

The second question belongs on the roadmap, and asking it before launch is much cheaper than asking it
after two hundred tickets.

---

# 5. Write Severity Levels in the User's Words

"Users cannot save work." "A core job cannot be completed." "Degraded, but there is a workaround."

Written in component terms, severity requires an architect at the exact moment nobody has time to
consult one.

---

# 6. Put the Status Message Author in the Table

Not "we will communicate" — a role, a channel, and the minute at which it happens.

An outage with silence costs more trust than the outage. It is the cheapest fix in this document.

---

# 7. Separate Mitigate From Resolve on the Page

Two rows, two owners, two timeboxes.

Kept together, incidents stay open — and users stay broken — while somebody looks for a root cause.

---

# 8. Write Runbook Steps as Three Columns

Do this · expect this · if different.

The three-column form makes an incomplete step visibly incomplete. Prose lets "investigate the issue"
look like an instruction.

---

# 9. Name the Access Needed at the Top of Every Runbook

Which credentials, which system, and where to obtain them.

The most common 3am blocker is not knowledge. It is not having a login.

---

# 10. Write the "Do Not Do" Line

Every system has one tempting action that makes things worse — restarting mid-migration, clearing a
queue, re-running a job that is not idempotent.

Someone helpful will attempt it. One line prevents it.

---

# 11. Walk One Runbook Before Declaring the Set Finished

Even in staging, even partially.

The first walk always finds two missing steps, and it converts the whole set from theory into
something with evidence behind it.

---

# 12. Give Every Alert a Runbook Before Giving It a Threshold

If no runbook can be written, the recipient has no action, and the alert should not exist.

That test removes about a third of proposed alerts, which is the point.

---

# 13. Build the Obligation Schedule From the Obligation Trace, Row by Row

`09-technology` already listed every obligation and its mechanism. Copy that list; do not re-derive it.

Re-deriving loses rows, and the lost ones are the obscure obligations that matter most.

---

# 14. Write the Evidence Column Before the Cadence

What artifact does this produce, and where is it kept?

An obligation that produces nothing cannot be demonstrated, and the cadence is then just a calendar
entry.

---

# 15. Ask When Restore Was Last Tested, and Write the Answer

Including "never".

It is the single most consequential untested assumption in operations, and writing "never" is what
turns it into a scheduled task rather than a surprise.

---

# 16. Cost the Human Time Explicitly

Support hours per week × the rate. Compliance hours per month × the rate.

Left out, the cost model is an infrastructure bill and the product looks far cheaper to run than it
is.

---

# 17. Divide the Complete Total by Launch Users and Read the Ceiling

One line of arithmetic against a number from `06-business`.

It is the last of the framework's three checks against the business model, and the only one that
includes people.

---

# 18. Never Reduce the Support Estimate to Make It Fit

The estimate came from response targets the operator approved.

Lowering it silently withdraws the commitment, and the withdrawal appears later as broken promises
instead of a revised plan.

---

# 19. Play the Rota Forward to Month Three

Month one works because everything is new and volume is low.

Coverage claims fail in month three, which is why they are usually made without concern.

---

# 20. State the Limit Rather Than the Ambition

"Weekday hours, best effort, and here is what happens when I am away."

An understated limit can be improved later. An overstated one can only be apologized for, repeatedly,
to the people who relied on it.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Owners invented before asking | The document cannot be corrected, only rewritten |
| Coverage designed rather than asked | It becomes a promise nobody can staff |
| Volume figures with no basis | Authority by repetition |
| Support burden answered rather than examined | A fixable defect becomes permanent cost |
| Severity in component terms | An argument during the incident |
| "We will communicate" | Nobody does |
| Mitigate merged with Resolve | Users stay broken during diagnosis |
| Runbook steps as prose | "Investigate the issue" looks like an instruction |
| Access requirements omitted | The 3am blocker is a missing login |
| No "do not do" line | Someone helpful makes it worse |
| Runbooks never walked | Two missing steps, discovered live |
| Alerts before runbooks | A third of them have no action |
| Obligation list re-derived | The obscure rows go missing |
| Cadence without evidence | A calendar entry, not a control |
| Restore status left blank | Discovered during recovery |
| Human time uncosted | An infrastructure bill masquerading as a cost model |
| Estimate lowered to fit | A withdrawn commitment nobody announced |
| Rota judged on month one | It fails in month three |
| Ambition stated as capability | Apologies, repeatedly |

---

# Self Assessment

- Did I ask who runs this before writing an owner?
- Did I ask what hours can be staffed, not what would be ideal?
- Does every forecast carry its basis?
- Which support request did I imagine two hundred times?
- Are severity levels in the user's words?
- Does the status message have an author and a minute?
- Are Mitigate and Resolve separate rows?
- Are runbook steps in three columns?
- Does every runbook name the access needed?
- Did I write the "do not do" line?
- Have I walked at least one runbook?
- Does every alert have a runbook?
- Did I copy the obligation trace rather than re-derive it?
- Does every obligation name its artifact?
- Did I write when restore was last tested?
- Is human time in the cost model?
- Did I divide by users and read the ceiling?
- Did any estimate fall to make it fit?
- Does the rota survive month three?
- Did I state the limit or the ambition?

---

> **Practice Principle**
>
> Two practices here take one question each: who runs this, and what
> hours can they cover.
>
> Every other practice in this document is downstream of those two
> answers, and inventing them invalidates all of it.
