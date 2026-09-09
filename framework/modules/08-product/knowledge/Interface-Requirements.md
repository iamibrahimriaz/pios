---
Title: Interface Requirements
Module: 08-product
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Turn the delivery surface named at 01-idea into the requirements it implies, and stop at the boundary where verification begins.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - interface_requirements
Related Modules:
  - 01-idea
  - 03-user
  - 09-technology
Tags:
  - Product
  - Requirements
  - Interface
  - Knowledge
---

# Interface Requirements

---

# The defect this method exists to close

**The operator is asked at `01-idea` what the product is delivered through.** The answer is
recorded in `state.project.delivery_surface`.

**Until this method existed, nothing consumed it.** A run could answer "web" at the first gate
and hand a builder a specification with no layout behavior, no interaction states beyond the
happy path, no accessibility target, no performance budget and no supported-client policy —
and pass all fourteen gates on the way, because no gate criterion mentioned any of them.

> The question was asked, recorded, and dropped.

`08-product/learn/20-Future-Improvements.md` had named the underlying cause independently:
non-functional requirements had no home, and arrived at `09-technology` as architecture
concerns, **which is too late for the ones that change what gets specified.**

---

# The mapping

**Read the surface. Take the rows it triggers. For each row, either specify it or record that
it does not apply and why.**

| Surface | Triggers |
| --- | --- |
| **Anything a person looks at** — web, mobile, desktop, embedded UI | Interaction states · layout across the supported range · accessibility conformance target · perceived-performance budgets · supported-client policy |
| **Anything reachable by a crawler** | Indexable and non-indexable surfaces, listed separately |
| **Anything a person operates without seeing** — voice, CLI | Interaction states and accessibility, in their own idioms. **Not layout** |
| **API, library, batch job, scheduled task** | **Frequently none of the above** |

**A product whose surface triggers nothing passes this criterion on one sentence.** Say which
surface, and that no view exists for which these could be stated. That is a pass and it should
be written without hedging.

---

# The line this method must not cross

> **Requirements, not verification.**

**`constitution/core/00-Purpose.md` ends the framework at the pre-development package.** The
distinction is sharp and it is easy to lose here, because interface quality is the area where
specification and process blur most readily.

| In scope — what must be true | Out of scope — how it is checked |
| --- | --- |
| A conformance target, and the criteria this product can fail | An automated scan in a pipeline |
| A budget with a measurement condition | A performance test suite |
| The narrowest supported width, and the behavior at it | A device matrix run before release |
| The states every component class must define | A visual review step |
| Which surfaces are indexable | A crawl audit |

**Both columns are worth having. Only the left one is this framework's.** The right belongs to
whoever receives the package, and adding it here converts a research framework into a
half-built engineering one governed by evidence rules that cannot judge whether code works.

---

# Writing requirements that can fail

**`08-product`'s Criterion 2 banned-word scan applies to this artifact in full.** The words
that fail there fail here, and this is the artifact most likely to attract them.

| Fails | Passes |
| --- | --- |
| "Modern, clean interface" | "«component class» defines default, hover, focus, active, disabled, loading, error and empty" |
| "Responsive" | "Supported from «n» CSS pixels. At that width no view scrolls horizontally, and «component» becomes «stated form»" |
| "Accessible" | "Conformance target «standard version level». The criteria this product can fail are «listed», each with the failure mode and the requirement" |
| "Fast" | "«view» renders first meaningful content within «n»s at the «n»th percentile on «client class» over «network»" |
| "Works on all modern browsers" | "«named policy». Rests on «evidence or assumption, tagged». Reopens «date or event»" |
| "SEO optimized" | "Indexable: «list». Not indexable: «list». No authenticated path appears in the first list" |

---

# Two requirements that carry more weight than they look

**The qualified figure.** Where a product qualifies a number — a denominator, a sample caveat,
a confidence — **the qualification must reach assistive technology as part of the same
statement.** A qualifier that is merely adjacent on screen delivers the bare number the product
intended not to give. **A product whose differentiation is honesty about its own data can lose
that differentiation entirely to this one implementation detail.**

**The four states that look alike.** *Nothing yet* · *nothing matched* · *we could not load it*
· *zero is the true answer.* **They render identically unless they are specified apart**, and
the fourth being mistaken for the third is how a user stops trusting a number that was correct.

---

# When this artifact is written

**At `08-product`, alongside the feature specification — not at `09-technology`.**

Accessibility changes which components exist. A narrow supported width changes what a view can
contain. A performance budget changes what a view may load. **Each of those is a specification
decision, and reaching them as architecture concerns means reaching them after the thing they
would have changed was already specified.**

---

> **Interface Requirements Principle**
>
> A surface named and never consulted is a question the run asked itself and refused to answer.
>
> Specify what must be true of it, or state that nothing must — and stop before deciding how
> anyone will check.
