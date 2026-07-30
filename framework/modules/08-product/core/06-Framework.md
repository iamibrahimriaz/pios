---
Title: Framework
Module: 08-product
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which a committed direction becomes a buildable specification.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 08-product/core/03-Core-Principles.md
  - 07-strategy gate passed
Outputs:
  - prd_body
  - feature_spec
  - acceptance_criteria
  - prioritization
  - edge_cases
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Framework
  - Method
---

# Framework — The Translation

---

# The Method

> Module 07 decided what to build. This module makes that decision unambiguous.
>
> Nothing new is chosen here. Something already chosen is made precise.

The Translation is six moves, in order. Each takes the previous move's output as its input,
and the order is load-bearing.

```
        Trace  →  Specify  →  Behave  →  Break  →  Order  →  Prove
          │         │           │         │         │         │
       parents   priority    behavior   failure   sequence  criteria
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Trace | What is in scope, and what does each thing serve? | The traceability spine |
| 2. Specify | What must the product do, and how strictly? | Requirements with priority |
| 3. Behave | What exactly happens, from the user's side? | Behavior descriptions |
| 4. Break | What happens when it goes wrong? | Edge and failure states |
| 5. Order | What gets built before what? | Prioritization and dependency order |
| 6. Prove | How would we know it works? | Acceptance criteria |

---

# Move 1 — Trace

**Build the spine before writing a single requirement.**

Take three inputs and lay them against each other:

| Input | From | Role |
| --- | --- | --- |
| Ranked problems | 04-problem | The parents. Nothing exists without one |
| Core job, step by step | 03-user | The spine. Every step is served or explicitly left alone |
| MVP line | 07-strategy | The boundary. Above it is MUST territory; below it is not |

Then produce the spine as a table: each step of the job, the problem it belongs to, and
whether this release serves it.

**Why first.** A requirement written before the spine exists gets its parent assigned
afterwards, which is how unattached features acquire retrospective justification. Building
the spine first means the parent is chosen before the requirement is written, not after.

**Two failures this move catches**

| Failure | What it looks like | What it means |
| --- | --- | --- |
| Orphan | A capability with no parent problem | It came from somewhere other than the research. Delete it |
| Unserved problem | A ranked problem above the line with no capability | Either the cut was wrong or the spec is incomplete |

An orphan is deleted, not justified. That rule matters because an orphan can almost always
be justified — the justification is written after the fact and sounds entirely reasonable.

---

# Move 2 — Specify

**Write requirements, with priority language that means something.**

| Level | Meaning — exactly |
| --- | --- |
| MUST | The release does not ship without it |
| SHOULD | The release ships without it, and is weaker for it |
| COULD | Genuinely optional. If it never happens, nothing is lost |

Two rules govern MUST, and both are gate criteria:

1. **MUST is reserved for capabilities above module 07's MVP line.** Nothing below the line
   may be a MUST, however sensible it looks while writing.
2. **If nearly everything is a MUST, the labels are decoration.** A specification where the
   MUST list equals the requirement list has not prioritized; it has relabeled.

**The inflation problem.** Specifying invites completeness. Working through a requirement in
detail reveals adjacent things the product "obviously" also needs, and each addition is
individually reasonable. This is how a spec grows past a cut that was made carefully a day
earlier.

> **Scope laundering.** Module 07 drew a line. This module quietly moves it, one reasonable
> addition at a time, and the cut that the operator approved is no longer the cut being
> built.

The handling is fixed: a capability discovered here goes to the **deferral ledger**, not the
MUST list. If it is genuinely load-bearing for the core job — the job cannot complete
without it — that is not an addition. It is module 07's end-to-end test failing, and the
correct action is a **regress to 07-strategy**, recorded.

---

# Move 3 — Behave

**Describe what happens, from the user's point of view.**

Not implementation. Not screens. What the user does, what the system does, and what state
they are in afterwards.

The standard is objective:

> **The two-builder test.** Would two independent engineers, given only this text, build the
> same behavior?

If they would differ, the requirement is underspecified — and the question "is this clear?"
will not detect it, because the writer already knows the answer they meant. The two-builder
test asks something checkable instead: name the point where two readings diverge.

**What behavior must state**

| Element | Why |
| --- | --- |
| Trigger | What starts it |
| Input | What the user provides, and what is optional |
| System response | What happens, including anything the user does not see |
| Resulting state | What is now true that was not before |
| What the user sees | How they know it worked |

**What behavior must not state.** Framework, database, screen layout, component names. Those
belong to `09-technology` and to design. A requirement that names a technology has removed a
decision from the module that should make it.

---

# Move 4 — Break

**Specify the unhappy paths. There are more of them than happy paths.**

A requirement with only happy-path behavior is roughly half specified, and the missing half
is where products fail in front of real users.

Five categories, worked for every MUST requirement:

| Category | The question |
| --- | --- |
| Empty | First use. No data yet. What does the user see, and what do they do next? |
| Invalid | Wrong, incomplete or impossible input. What are they told, and what is preserved? |
| Failure | The operation cannot complete. Is work lost? Can they retry? |
| Permission | The user is not allowed. What do they see — and does it reveal something it should not? |
| Limit or conflict | Too many, too large, two at once, offline, interrupted |

"Not applicable — «reason»" is an acceptable answer. A blank is not: a blank is
indistinguishable from not having considered it.

**The data-loss position.** State plainly what can be lost and when. This is the single most
consequential edge-state answer in most products, and it is almost never written down until
it happens.

---

# Move 5 — Order

**Score, then sequence.**

Scoring makes the ordering arguable rather than asserted. One method, applied to every row —
an inconsistently applied method is worse than none, because it looks like analysis.

| Factor | Meaning |
| --- | --- |
| Problem weight | Rank of the problem it serves — from 04-problem |
| Reach | Share of the primary segment affected |
| Confidence | Evidence standing of the underlying problem |
| Effort | Build cost |

**Where the score and the tier disagree, say so.** A high-scoring requirement below the line
is legitimate — module 07's cut outranks this module's arithmetic — but the disagreement is
recorded, not hidden by adjusting the score until it agrees.

Then sequence: what must exist before what, the critical path, and the **first shippable
slice** — the smallest subset a real user could actually use. That slice is what
`10-execution` plans around.

---

# Move 6 — Prove

**Write acceptance criteria that could fail.**

A criterion is acceptable only if a person with no context could observe the system and say
yes or no without interpretation.

The form that produces this reliably:

> **Given** «state», **when** «action», **then** «observable result».

**The banned words.** These cannot appear in an acceptance criterion, because none of them
can be observed:

| Banned | Replace with |
| --- | --- |
| fast, performant | a figure — "within «n» seconds" |
| intuitive, easy, user-friendly | a completion rate, or a step count |
| seamless | the absence of a specific interruption |
| robust, reliable | behavior under a named failure |
| appropriate, sensible | the specific thing that happens |

This is not a style preference. An aspirational criterion cannot be failed, and a criterion
that cannot be failed is not a criterion — it is a hope in checkbox form.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Specify before tracing | Requirements whose parents are assigned retrospectively |
| Write behavior before priority | Effort spent detailing things that will not ship |
| Write criteria before behavior | Criteria that test the description rather than the product |
| Order before breaking | Estimates that ignore the unhappy paths, which is most of the work |
| Skip Break entirely | A spec that passes review and fails on contact with users |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| Whether to build this at all | 07-strategy — settled |
| What the MVP contains | 07-strategy — binding |
| How it is built | 09-technology |
| Entity shape and relationships | 09-technology, from the data implied here |
| Screens and visual design | Design, from the behavior described here |
| Milestone dates | 10-execution |
| Metric targets | 12-metrics |

---

# Self Assessment

- Did I build the spine before writing requirements?
- Does every requirement name a parent problem?
- Is every problem above the line served, or its deferral recorded?
- Is any MUST below module 07's line?
- Would two engineers build the same thing from my behavior text?
- Did I work all five edge categories, or only the ones that came to mind?
- Can every acceptance criterion actually fail?
- Did anything grow past the cut while I was specifying?

---

> **Framework Principle**
>
> This module adds no new judgment about what to build.
>
> Every place it feels like it needs to is a place where the previous
> module's work was incomplete — and that is a regress, not a decision.
