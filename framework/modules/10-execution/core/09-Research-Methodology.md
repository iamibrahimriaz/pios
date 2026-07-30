---
Title: Research Methodology
Module: 10-execution
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how planning claims are sourced, labeled and bounded — especially estimates.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 10-execution/core/06-Framework.md
Outputs:
  - Honestly bounded execution plan
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - Methodology
  - Evidence
---

# Research Methodology

---

# What Can Be Established Here, and What Cannot

This module's evidence problem is unusual: most of what a plan contains is about the future,
and the future has no sources.

| Claim | Status |
| --- | --- |
| "M2 depends on M1" | **Derivable** — from the data model and the contract |
| "M1 is smaller than M3" | **Derivable** — from the requirement count and complexity |
| "This is the longest chain" | **Derivable** — from the dependency graph |
| "M1 takes three weeks" | **Not derivable** — requires team facts nobody has supplied |
| "Launch in Q3" | **Not derivable** — a commitment, not a finding |

The framework can establish **order, dependency and relative size** from documents it has. It
cannot establish duration, velocity or dates, because those are properties of a team it has
never met.

---

# The Estimate Boundary

> An estimate with no stated team is not an estimate. It is a number that will be treated as
> one.

This is the module's central honesty mechanism, and it exists because plans are *expected* to
carry dates. The pressure to produce them is real, and the cost of inventing them is paid by
someone else, months later.

**The rule**

| Situation | What the plan says |
| --- | --- |
| Operator supplied team size and composition | Durations, tagged, with the assumed team stated |
| Operator supplied a deadline but no team | The deadline, as a constraint — and relative sizes only |
| Neither supplied | Sequence, dependency and S / M / L. No durations anywhere |

**Never** produce a duration by analogy to unnamed projects. "A feature like this usually
takes two weeks" is a sentence with no subject: usually for whom, with what codebase, at what
quality bar.

Where the operator supplies estimates, they are recorded as operator input — not laundered into
the framework's own voice. The distinction matters when the estimate proves wrong: a number the
operator gave is a plan to revise, and a number the framework invented is a document nobody
trusts again.

---

# Three Kinds of Statement in a Plan

| Kind | Example | Label |
| --- | --- | --- |
| **Derived** | "M2 cannot start before M1 — it needs the consultation entity" | `derived: 09-technology §3` |
| **Judgment** | "De-risk earliest, rather than value earliest" | `judgment` — with the alternative recorded |
| **Operator input** | "Two engineers, one designer, starting «date»" | `[verified: operator]` |

The dangerous class is a judgment written as a derivation. "M1 must come first" reads as a
constraint; if it is actually a preference about sequencing, the plan cannot be re-ordered by
someone who has a good reason to.

---

# Flows Are Derived, Not Designed

The critical paths in this module come from `03-user`'s observed workflow and `08-product`'s
requirements. They are not invented here.

| Element | Source |
| --- | --- |
| The steps of the job | `03-user` workflow, `08-product` §5 |
| What the system does per step | `08-product` §7 behavior |
| What can fail | `08-product` §8 edge cases |
| What the response is | `09-technology` §6 failure responses |
| The persona's physical constraints | `03-user` |

**The prohibition.** Do not invent a workflow step the user was never observed performing. A
plausible step inserted into a critical path becomes a screen, then a requirement in the next
revision, and the product acquires a process nobody does.

Where a step is genuinely unknown, mark it `[assumption: needs validation]` and put it in the
open questions. A flow with an admitted gap can be validated. A flow with an invented step
cannot, because nobody knows which step to doubt.

**Design principles must cite their finding.** A principle traced to a research finding
constrains real decisions. A generic principle constrains nothing and survives every review,
which is why documents fill up with them.

---

# The Cold-Start Standard

The build handoff is the only deliverable the manifest marks `critical`, and its standard is
about the reader rather than the writer:

> Could an agent or engineer open this file, with no access to the research and no other
> document, and start writing correct code today?

**What this forbids**

| Never | Why |
| --- | --- |
| "As discussed" / "per the research" / "as we agreed" | The reader was not there |
| Assuming other documents will be opened first | They will not be |
| An unresolved `[assumption]` in a build-blocking position | It becomes an invisible decision by whoever builds it |
| A reference to a document that does not exist | The reader stops, or guesses |
| "The team will decide" on anything build-blocking | Nobody is "the team" |

**What it requires**

Essentials carried inline, with references for depth. The first task nameable in one sentence.
A definition of done for the first milestone. And everything genuinely undecided moved to
**Blocked Work with a named owner** — which is the mechanism that keeps evidential honesty from
turning into a stalled team.

---

# Verification Claims

| Requirement | |
| --- | --- |
| Every MUST requirement traces to at least one verification | Otherwise it ships unverified |
| Every verification traces to a criterion or an edge case | Otherwise it tests something nobody asked for |
| Exclusions are stated, not implied | An unstated exclusion reads as coverage |

**Do not claim a coverage level.** "Comprehensive test coverage" is the same class of statement
as "intuitive interface" — unobservable, unfalsifiable, and reassuring. What can be stated is
which requirements are verified, at which level, and which are not.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| State a duration without a stated team | The number outlives the caveat |
| Present an operator's estimate as the framework's finding | Nobody can tell whose number failed |
| Invent a workflow step | It becomes a screen, then a requirement |
| Write a design principle with no source | It constrains nothing and cannot be argued with |
| Claim a coverage level | Unobservable and reassuring |
| Leave an assumption in build instructions | It becomes a silent decision |
| Assign a blocker to "the team" | Unowned work is unstarted work |
| Put a date on deferred scope | Dates on unvalidated scope are fiction |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| First milestone | `08-product` §11 | It is not the first shippable slice |
| Requirement coverage | `08-product` §7 | A MUST requirement is in no milestone |
| Edge coverage | `08-product` §8 | An edge case appears in no flow and no test |
| One-way doors | `09-technology` §13 | An irreversible decision is committed late |
| Milestone Zero | `07-strategy` | The problem is assumed and M0 is absent |
| Persona constraints | `03-user` | The flows assume conditions the user lacks |
| Non-negotiables | `09-technology` §10 | A security or regulatory rule is absent from the plan |
| Deferred scope | `08-product` §10 | A deferred capability appears nowhere |

---

# Self Assessment

- Did I state any duration without knowing the team?
- Is every operator-supplied number attributed to the operator?
- Is every sequencing judgment labeled as a judgment?
- Did I invent any step in any flow?
- Does every design principle cite a finding?
- Did I claim coverage, or list it?
- Is there any assumption left in the build instructions?
- Does every blocker have a person's name against it?

---

> **Methodology Principle**
>
> This module is asked for dates it cannot know.
>
> Refusing to invent them is the whole of its integrity — and the
> sequence, which it *can* establish, is what the team actually needs.
