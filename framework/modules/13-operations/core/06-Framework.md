---
Title: Framework
Module: 13-operations
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which a shipped product becomes something a person can actually run.
Audience:
  - AI Agents
  - Operators
Prerequisites:
  - 13-operations/core/03-Core-Principles.md
  - 10-execution gate passed
Outputs:
  - support_model
  - runbooks
  - incident_process
  - compliance_operations
  - cost_model
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Framework
  - Method
---

# Framework — The Watch

---

# The Method

> Most blueprints stop at launch. That is why so many products become
> unmaintainable in month three.
>
> This module answers a different question from every module before it: not what to
> build, but who answers when it breaks.

Six moves. The first five make the product runnable; the sixth reveals what running it costs.

```
  Support  →  Grade  →  Respond  →  Write  →  Comply  →  Cost
     │         │          │          │         │         │
  the queue  impact   the process  runbooks  schedule  the truth
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Support | Who answers users, how fast, and about what? | `support_model` |
| 2. Grade | How bad is it, in the user's terms? | Severity levels |
| 3. Respond | What happens, in what order, owned by whom? | `incident_process` |
| 4. Write | Could a stranger fix it at 3am? | `runbooks` |
| 5. Comply | What recurring obligations exist, and who owns each? | `compliance_operations` |
| 6. Cost | What does keeping this alive actually cost? | `cost_model` |

---

# Move 1 — Support

**Define the channel, the hours and the response expectation — then find the burden.**

Two kinds of statement live in this move, and they carry different standing:

| | Nature | Standing |
| --- | --- | --- |
| Channels, hours, response targets | **Commitments** | Operator decisions — `[verified: operator]` |
| Ticket volume, staffing need | **Forecasts** | Assumptions before launch |

A response target the operator has not agreed to is a promise made on their behalf. A volume
estimate presented as a plan is a staffing decision made on a guess.

## The Support Burden Is a Product Signal

The most common support request is usually a design defect with a queue attached.

So each expected burden names two things: why it will happen — from `10-execution`'s flow
analysis — and **the product change that would remove it**. Those changes go to the roadmap.

| Expected burden | Product change |
| --- | --- |
| "How do I get my existing records in?" | Import tooling, or a guided migration step |
| "Why can't I edit this?" | The state machine's rule made visible in the interface |
| "It didn't save" | The failure state from `08-product` §8, actually implemented |

A support burden accepted without asking this question becomes a permanent staffing line paid
for a fixable defect. Some burdens genuinely are permanent — say which, and why that is correct.

---

# Move 2 — Grade

**Severity is defined by user impact, not by which component failed.**

| Wrong | Right |
| --- | --- |
| "The database is down" | "Users cannot save work" |
| "The queue is backed up" | "Notes take an hour to appear" |
| "An integration is failing" | "Referral letters cannot be sent" |

Component-based severity produces an argument during the incident, which is the worst possible
time to be having it. Impact-based severity can be assigned by whoever noticed, in seconds.

**Data loss is always S1**, using the data-loss position `09-technology` was required to state.
That definition already exists; this module makes it operational.

Each level states the first response time, the resolution target, and **who is woken** — which
is where a coverage claim becomes a person's night.

---

# Move 3 — Respond

**Every stage has an owner and a timebox.**

```
Detect → Triage → Communicate → Mitigate → Resolve → Review
```

Two stages are routinely missing, and both are the ones users notice:

**Communicate.** Users experiencing an outage with no word about it are having a worse incident
than the outage itself. Name the channel, the person who writes it, and the point at which they
do.

**Mitigate, separately from Resolve.** Stopping the harm is not the same as fixing the cause,
and conflating them produces incidents that stay open — and users who stay broken — while
somebody diagnoses.

**Regulatory notification obligations** belong here. Where a regime imposes a breach
notification deadline, name the deadline and who starts the clock. A deadline nobody knows is a
deadline that gets missed, and the failure is legal rather than technical.

---

# Move 4 — Write

**The runbooks, to one standard.**

> **The 3am test.** Could someone who did not build this system follow this, alone, half awake,
> with nobody to ask?

That is the defining standard of this module, and it is the operational sibling of
`10-execution`'s cold-start test.

| Not a step | A step |
| --- | --- |
| "Investigate the issue" | "Run «command». If the output shows «pattern», go to step 4" |
| "Check the logs" | "Open «location». Search for «string» in the last 15 minutes" |
| "Restart the service" | "Run «command». Wait for «observable». If it does not appear within 60 seconds, escalate" |

**Every runbook needs four things beyond its steps:**

| Element | Why |
| --- | --- |
| The precise trigger | So the reader knows this is the right runbook |
| What access is needed, and where to get it | The most common 3am blocker is a credential |
| A recovery verification | Otherwise "done" means "I ran the steps" |
| An escalation | Because the runbook will sometimes not work |

And one more that experience adds: **"do not do"** — the tempting action that makes it worse.
Every system has one, and it is usually attempted by somebody helpful.

Runbooks come from `09-technology`'s failure modes and `08-product`'s edge cases. Those documents
already enumerated what can go wrong; this move makes each one survivable by a stranger.

---

# Move 5 — Comply

**Turn obligations into a schedule.**

This is the third stage of a chain that runs through the whole framework:

| Module | What it does with an obligation |
| --- | --- |
| `02-market` | Finds it |
| `09-technology` | Builds the mechanism that meets it |
| **`13-operations`** | **Runs it — owner, cadence, evidence produced** |

> Compliance is a schedule, not a state.

A mechanism that exists but is never exercised — a log nobody reviews, a training nobody
repeats, a restore nobody tests — satisfies an auditor for exactly as long as nobody looks.

**Every recurring obligation states four things:** the cadence, a **named owner**, the evidence
it produces, and where that evidence is kept. The evidence column is what makes audit readiness
real: being compliant and being able to *show* you were compliant are different achievements, and
only the second one survives an audit.

**Alert hygiene belongs to this move too.** Every alert needs a threshold, a named person, and a
runbook. An alert missing any of the three is worse than no alert:

> A tolerated alert teaches the team to tolerate all of them.

So the rule is stated explicitly: an alert nobody acts on is **deleted**, not ignored. And what
is deliberately not alerted on is named, usually because there is no action to take.

---

# Move 6 — Cost

**Complete the cost to serve.**

`09-technology` costed the infrastructure and checked it against `06-business`'s ceiling. That
check was necessary and incomplete — it omitted the two lines this module can finally supply:

| Line | Why it was missing |
| --- | --- |
| Support staffing | Volume was unknown until the flow analysis and burden existed |
| Compliance operations | The recurring obligations were not yet a schedule |

With both, the **true cost per user** exists for the first time in the run. Set it against the
ceiling from `06-business`.

**If it exceeds the ceiling, that is a regress** — to `06-business` for the price or
`07-strategy` for the scope. The thing that must not happen is absorbing it by assuming support
takes less time than the plan just stated.

This is the last of the framework's three arithmetic checks against the business model:

| Module | Check |
| --- | --- |
| `09-technology` | Infrastructure cost per user against the ceiling |
| `11-growth` | Implied CAC against the payback ceiling |
| **`13-operations`** | **True cost to serve against the ceiling** |

---

# The Rota Question

One question sits behind everything above, and it is the one most often left unasked:

> Who is on call, and can they sustain it?

| | |
| --- | --- |
| A rota of one | Not a rota |
| Coverage claimed but unstaffed | A promise that will be broken during the first incident |
| No answer for that person's absence | An operational risk, not a detail |

For a solo operator this is the most important section in the document, and the honest answer —
"weekday hours only, best effort, and here is what happens when I am unavailable" — is worth more
than a coverage table nobody can staff.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Write runbooks before grading severity | Runbooks with no sense of urgency attached |
| Grade before understanding the support burden | Severity levels for the wrong failures |
| Build the incident process after the runbooks | Steps with no owner and no communication |
| Schedule compliance last | Obligations with mechanisms nobody exercises |
| Cost first | The two largest lines missing |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| The security controls themselves | `09-technology` — carried, then operated |
| What the product does | `08-product` — settled |
| Build sequence | `10-execution` |
| Metric definitions | `12-metrics` — thresholds carried, then alerted on |
| Model monitoring and fallback | `14-ai-systems` |

---

# Self Assessment

- Are the response targets the operator's, or mine?
- Does every expected support burden name the product change that removes it?
- Is severity defined by user impact?
- Does every incident stage have a named owner and a timebox?
- Do users get told anything during an incident?
- Would a stranger get through my runbooks at 3am?
- Does every alert have a threshold, a person and a runbook?
- Does every obligation have an owner, a cadence and evidence?
- Has restore ever been tested?
- Does the true cost per user fit inside the ceiling?
- Can one person actually sustain this rota?

---

> **Framework Principle**
>
> Twelve modules asked what the product should be.
>
> This one asks who gets woken up, and that question has an
> answer whether or not anybody writes it down.
