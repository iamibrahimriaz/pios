---
Title: Framework
Module: 10-execution
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which a specification becomes something a team can start today.
Audience:
  - AI Agents
  - Delivery Leads
Prerequisites:
  - 10-execution/core/03-Core-Principles.md
  - 09-technology gate passed
Outputs:
  - ux_flows
  - delivery_plan
  - milestones
  - build_handoff
  - qa_strategy
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - Execution
  - Framework
  - Method
---

# Framework — The Handover

---

# The Method

> Everything is now specified. Nothing has been started.
>
> This module turns a complete description into a first task, an order, and a
> definition of finished.

Six moves. The first three shape the work, the last three make it startable.

```
   Flow  →  Slice  →  Sequence  →  Define  →  Verify  →  Hand Over
    │        │          │           │          │           │
  paths    units      order       done       proof       start
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Flow | What does the user actually walk through? | `ux_flows` |
| 2. Slice | What are the independently shippable units? | `milestones` |
| 3. Sequence | In what order, and why that order? | `delivery_plan` |
| 4. Define | What does "done" mean, per unit? | Definitions of done |
| 5. Verify | How would we know it works? | `qa_strategy` |
| 6. Hand Over | Could someone start today? | `build_handoff` |

---

# Move 1 — Flow

**Map what the user walks through, end to end.**

Module 08 specified requirements. Requirements are not a route. A user does not experience a
requirement list; they experience a sequence of screens and states, and products are lost in
the parts of that sequence nobody specified.

**Two or three critical paths only.** The flows that carry the product. Mapping every path
produces a document nobody reads and hides the two that matter.

Per path: trigger, each step, what the user sees, what they do, what the system does, and
what can fail. Then the failure and recovery table — module 08 found those edge cases, and
this is where they become something a person experiences rather than a status code.

**Design principles must derive from findings.** This is the difference between useful and
decorative:

| Finding | Principle |
| --- | --- |
| The user is interrupted constantly | Every action must survive being abandoned halfway |
| They work one-handed while standing | No interaction requires two-handed precision |
| Connectivity is unreliable in the setting | The core path completes offline and reconciles later |

"Keep it simple" derives from nothing and constrains nothing.

**Time to first value is a number.** From arrival to the moment the user gets something they
actually wanted, in steps and in minutes. It predicts adoption better than any feature
comparison, and it cannot be improved without being measured.

**Every screen needs its unpopulated states.** Empty, loading, error, permission. A screen
specified only in its populated state ships broken, because the populated state is the one
that occurs least often at the beginning.

---

# Move 2 — Slice

**Cut the work into units that each end with something a person can do.**

The test is objective, and it is this module's defining standard:

> **The demo test.** At the end of this milestone, what can you show a real user doing?

If the answer describes a layer — the schema is complete, the API is finished, the design
system is built — it is not a milestone. It is a stage of one.

| Horizontal, and wrong | Vertical, and right |
| --- | --- |
| M1: data layer · M2: API · M3: UI | M1: a doctor can open a patient, dictate a note, and see it saved to that patient's history |

Horizontal slicing feels efficient and defers all learning to the end. Nothing is
demonstrable until everything is, so the first honest feedback arrives after the budget is
spent. Vertical slicing repeats some work across milestones and is still faster, because it
starts producing information immediately.

**Independently shippable** means the milestone could stop there and leave a usable product.
Not a complete one — a usable one.

---

# Move 3 — Sequence

**Order the units, and state what governs the order.**

The common sequencing principles conflict, and a plan that switches between them silently is
incoherent:

| Principle | Orders by | Right when |
| --- | --- | --- |
| De-risk earliest | Biggest unknown first | Uncertainty is high |
| Learn earliest | Fastest feedback first | The problem is assumed |
| Value earliest | User benefit first | The problem is proven |
| Dependency order | What is technically required first | Constraints dominate |

Pick one, say why, and apply it consistently.

**Milestone Zero comes first when the sharpest problem is assumed.** This is the third module
in which that mechanism appears — declared in `04-problem`, made binding in `07-strategy`,
and here it becomes the first row of the actual plan. Building before it completes is the
expensive mistake the framework exists to prevent.

**One-way doors are placed deliberately.** `09-technology` identified the decisions that
cannot be cheaply reversed. Each must be committed early enough to be built on and late
enough to be informed — and the reasoning for where it sits belongs in the plan, because it
is the sequencing decision with the largest consequences.

---

# Move 4 — Define

**Define done, per milestone, including what is not done.**

Three parts, and the third is the one usually missing:

| Part | Source |
| --- | --- |
| Acceptance criteria, listed explicitly | `08-product` §7 |
| The non-functional bar — tests, environment, review | Stated here |
| **What is explicitly not done at this point** | Stated here |

The third part prevents the "done" that needs three more weeks. A milestone marked complete
while a reader assumes it included error handling, or migration, or an admin view, produces a
dispute nobody can settle. Naming the absences settles it in advance.

**Each milestone also states what it teaches.** A milestone that answers no question about
the product is work being done in the dark — which is legitimate for infrastructure, and
worth noticing.

---

# Move 5 — Verify

**State what gets tested, and what does not.**

The coverage rule mirrors every other module's traceability discipline: every MUST
requirement has at least one verification, and every verification traces to a criterion or an
edge case.

| Level | Covers |
| --- | --- |
| Unit | Business rules and the constraints in the data model |
| Integration | The interface contract |
| End to end | The critical paths from Move 1 |
| Manual | What cannot be automated — and why |

**State what is deliberately not tested.** An honest exclusion is worth more than an implied
claim of full coverage, and it is the only version of this section that survives contact with
a real schedule.

**The edge cases must appear.** Module 08 worked five categories per requirement and
`09-technology` mapped them to failure responses. If they are not verified, they exist in
three documents and in no running system.

---

# Move 6 — Hand Over

**Make it startable by someone who was never here.**

The build handoff is the only deliverable the manifest marks `critical`, and its standard is
the strictest in the framework:

> **The cold-start test.** Could an agent or engineer open this file, with no access to the
> research and no other document, and start writing correct code today?

Not "could understand the project". Could **start**.

| Requirement | Why |
| --- | --- |
| No "as discussed" or "per the research" | The reader was not there |
| Essentials carried inline, references for depth | They will not open five documents first |
| **No unresolved assumption in a build-blocking position** | Someone will guess, and never say so |
| The first task nameable in one sentence | Otherwise the first day is spent deciding |
| A definition of done for the first milestone | Otherwise "done" is whoever's opinion prevails |

**Unresolved questions go to Blocked Work with a named owner.** That is the mechanism which
keeps the framework's honesty about evidence from becoming a stalled team: the builder can see
exactly what cannot start, who owns it, and which milestone needs it. An assumption left in
the build instructions instead becomes an invisible decision.

---

# The Estimate Boundary

This module is where fabricated confidence is most tempting, because plans are expected to
carry dates.

> The framework does not know the team. It cannot produce durations.

| Can be established here | Cannot |
| --- | --- |
| Sequence | Calendar dates |
| Dependency | Durations in weeks |
| Relative size — S / M / L | Team velocity |
| Critical path | Delivery commitments |

A duration is either an operator input, with the assumed team stated, or an
`[assumption: needs validation]`. Never a derived figure. An estimate with no stated team is
not an estimate — it is a number that will be treated as one.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Slice before flowing | Milestones that miss whole parts of the user's route |
| Sequence before slicing | An order over units that are not shippable |
| Define done before slicing | "Done" applied to layers |
| Verify before defining done | Tests for the description rather than the criteria |
| Hand over before verifying | A start with no definition of correct |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| Architecture, schema, contract | `09-technology` — settled |
| Metric definitions and targets | `12-metrics` |
| On-call, support, incident response | `13-operations` |
| Channels and launch marketing | `11-growth` |
| Visual design | Design, from the flows here |

---

# Self Assessment

- Did I map paths, or restate requirements in order?
- Does every design principle name the finding it came from?
- Does every milestone pass the demo test?
- Is my sequencing principle stated, and applied consistently?
- Is Milestone Zero first, where the problem is assumed?
- Does every definition of done say what is **not** done?
- Does every MUST requirement have a verification?
- Have I stated what is not tested?
- Is any duration here unsupported by a stated team?
- Could someone with no context start today?

---

> **Framework Principle**
>
> Nine modules produced descriptions. This one produces a first task.
>
> The measure of it is not how complete the plan looks — it is
> whether work can begin tomorrow morning without a meeting.
