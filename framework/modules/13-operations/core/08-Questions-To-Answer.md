---
Title: Questions To Answer
Module: 13-operations
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Operators
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Questions
---

# Questions To Answer

---

# Overview

This module has more **OPERATOR** questions than any other except `01-idea`, because most of what
it plans is someone's time.

Two of them cannot be worked around at all: who runs this, and what hours they can cover. Every
owner, target and rota in the document depends on the answers, and inventing them produces a plan
that reads well and belongs to nobody.

---

# 1. Inherited Inputs

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What are the non-negotiables from `09-technology` §10? | Security rules become preferences |
| 1.2 | What obligations exist, and what mechanism meets each? | Compliance is never scheduled |
| 1.3 | What is the data-loss position? | S1 is undefined |
| 1.4 | What are the RPO and RTO? | Recovery expectations are invented during recovery |
| 1.5 | What are the retention periods per data class? | The data lifecycle has no policy |
| 1.6 | What are the counter-metric thresholds from `12-metrics`? | Nothing becomes an alert |
| 1.7 | What does the infrastructure cost at launch? | The cost model has no starting line |
| 1.8 | What is the cost-to-serve ceiling? | Nothing to check the total against |
| 1.9 | Are there regulatory notification deadlines? | A legal deadline gets missed |
| 1.10 | **OPERATOR** — who will run this after launch? | Every owner in the document is fictional |
| 1.11 | **OPERATOR** — what hours can genuinely be covered? | Response targets are promises made for them |

---

# 2. Support

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | Through what channels do users get help? | They use whatever they can find |
| 2.2 | **OPERATOR** — what first response time is acceptable to commit to? | The framework commits on their behalf |
| 2.3 | What resolution target, per severity? | Every ticket is equally urgent |
| 2.4 | Who staffs it, by name or role? | Nobody |
| 2.5 | What is the escalation path, and when is it used? | Everything escalates, or nothing does |
| 2.6 | What volume is expected, and on what basis? | A staffing decision resting on a guess |
| 2.7 | **What will users most often need help with?** | The largest ongoing cost is unexamined |
| 2.8 | **For each: what product change would remove it?** | A fixable defect becomes a permanent staffing line |
| 2.9 | What burden is permanent, and why is that correct? | Everything looks like a defect |

---

# 3. Severity

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What does each level mean **in the user's terms**? | Severity arguments during incidents |
| 3.2 | Could the person who noticed assign a level in ten seconds? | The grading needs an architect |
| 3.3 | Is data loss S1? | The worst failure is triaged as ordinary |
| 3.4 | What is the first response time per level? | Response by mood |
| 3.5 | **Who is woken, per level?** | Coverage is claimed but not owned |

---

# 4. Incidents

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | How is an incident detected? | By a user, eventually |
| 4.2 | Who triages, and within what time? | It waits |
| 4.3 | **Who tells users, through what channel, and when?** | Users experience the outage plus silence |
| 4.4 | What does mitigation mean here, separately from resolution? | Incidents stay open while somebody diagnoses |
| 4.5 | Who resolves, and who reviews? | No learning |
| 4.6 | Is the review blameless, and within what window? | It does not happen |
| 4.7 | Who can declare an incident? | Nobody dares |
| 4.8 | **What regulatory notification deadline applies, and who starts the clock?** | A legal failure, not a technical one |

---

# 5. Runbooks

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | What operational events are foreseeable? | Every incident is improvised |
| 5.2 | For each: what is the precise trigger? | The reader does not know it applies |
| 5.3 | For each step: what exactly do I do? | "Investigate the issue" |
| 5.4 | For each step: what should I see? | No way to know it worked |
| 5.5 | For each step: what if it differs? | A dead end at 3am |
| 5.6 | What access is needed, and where is it obtained? | The most common 3am blocker |
| 5.7 | **How is recovery verified?** | "Done" means "I ran the steps" |
| 5.8 | Who is escalated to, and how are they reached? | The runbook ends in silence |
| 5.9 | **What is the tempting action that makes it worse?** | Somebody helpful does it |
| 5.10 | Has anyone actually walked this runbook? | It is a theory |

---

# 6. Alerting

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | What conditions fire an alert? | Nothing is detected |
| 6.2 | For each: what severity? | All alerts are equal, so none matter |
| 6.3 | For each: **which named person receives it?** | It goes to a channel nobody owns |
| 6.4 | For each: **which runbook does it point to?** | The recipient improvises |
| 6.5 | Which counter-metrics from `12-metrics` became alerts? | Thresholds defined and never watched |
| 6.6 | What is deliberately not alerted on, and why? | Noise, and eventual blindness |
| 6.7 | What happens to an alert nobody acts on? | It is tolerated, and trains everyone to tolerate the rest |

---

# 7. Compliance Operations

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | What obligations recur, and at what cadence? | Compliance is a state nobody maintains |
| 7.2 | **Who owns each, by name?** | An unowned obligation is an unmet one |
| 7.3 | **What evidence does each produce, and where is it kept?** | Compliant but unable to demonstrate it |
| 7.4 | For each non-negotiable: how does a breach become visible? | A rule with no visibility is a preference |
| 7.5 | What would an auditor ask for? | Discovery during the audit |
| 7.6 | How long would producing it take? | An answer given under pressure |
| 7.7 | Is retention automated? | A policy nobody executes |
| 7.8 | How is a deletion or subject access request handled, and by when? | An obligation half met |
| 7.9 | **Has restore ever been tested?** | Backups that may not restore |
| 7.10 | Has rollback ever been tested? | The same assumption, at deploy time |

---

# 8. Release

| # | Question | If unanswered |
| --- | --- | --- |
| 8.1 | How often is there a release? | Whenever someone feels ready |
| 8.2 | What gate stands before production? | Whatever the deployer decides |
| 8.3 | Who can deploy? | Anyone, or one person |
| 8.4 | How is a release rolled back, and how long does it take? | Improvised during the incident |
| 8.5 | Are migrations reversible? | A one-way deploy discovered at the worst moment |
| 8.6 | Who removes a feature flag once it is settled? | Flags accumulate into permanent complexity |

---

# 9. Cost

| # | Question | If unanswered |
| --- | --- | --- |
| 9.1 | What does infrastructure cost at launch? | Carried from `09-technology` |
| 9.2 | What does measurement cost? | Carried from `12-metrics` |
| 9.3 | **What does support staffing cost?** | The largest omitted line |
| 9.4 | **What does compliance operation cost in time?** | The second largest |
| 9.5 | What is the total, and the true cost per user? | The cost to serve is still unknown |
| 9.6 | **Does it fit inside `06-business`'s ceiling?** | The business model may already be broken |
| 9.7 | If not, what changes — price, scope or operations? | It gets absorbed silently |

---

# 10. The Rota

| # | Question | If unanswered |
| --- | --- | --- |
| 10.1 | How many people are on the rota? | A coverage claim with nobody behind it |
| 10.2 | **Is it sustainable?** | The first month works and the third does not |
| 10.3 | What happens when the on-call person is unavailable? | Nothing happens, which is the problem |
| 10.4 | What single-person dependencies exist? | One illness becomes an outage |
| 10.5 | What is the early warning for each? | The dependency is discovered by failing |

> For a solo operator, 10.2 is the most important question in the module. "Weekday hours, best
> effort, and here is what happens when I am away" is a real operations plan. A four-hour response
> target staffed by one person is not.

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 1 | §2 Inherited Inputs |
| 2 | §3 Support Model |
| 3 | §4 Severity Levels |
| 4 | §5 Incident Process |
| 5 | §6 Runbooks |
| 6 | §7 Monitoring and Alerting |
| 7 | §8, §9 Compliance operations and data lifecycle |
| 8 | §10 Release Process |
| 9 | §11 Running Cost |
| 10 | §12 Operational Risks |

---

# Self Assessment

- Did I ask 1.10 and 1.11 before writing any owner or target?
- Does every row of 2.7 have an answer to 2.8?
- Could the person who noticed answer 3.1 in ten seconds?
- Is 4.3 answered with a person, a channel and a moment?
- Would a stranger get stuck anywhere in section 5?
- Does every alert answer 6.3 and 6.4?
- Does every obligation answer 7.2 and 7.3?
- Is 7.9 answered honestly?
- Did I include 9.3 and 9.4 in the total?
- Is 10.2 answered, rather than implied?

---

> **Question Principle**
>
> Most of this module is someone's evenings and weekends.
>
> Questions about that cannot be answered by inference, and a plan
> that answers them anyway is a plan the operator never agreed to.
