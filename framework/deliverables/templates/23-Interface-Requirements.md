---
Artifact: interface-requirements
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [01-idea, 03-user, 08-product]
---

<!-- fill: This artifact exists because the delivery surface is named at 01-idea and was,
     until this artifact existed, consumed by nothing. A specification can otherwise be
     complete on every functional axis and tell a builder nothing about what the product
     looks like, how it behaves at the narrowest width it supports, whether a keyboard can
     operate it, or how fast it has to be.

     REQUIREMENTS, NOT VERIFICATION. What must be true — never how it will be checked.
     A test suite, a pipeline gate or a review step belongs to whoever builds the product.
     See constitution/core/00-Purpose.md.

     If the delivery surface has no rendered interface, fill §0 and delete the rest. That is
     a pass, not a gap.
     Remove every <!-- fill --> comment before delivery. -->

# Interface Requirements — «Product Name»

## 0. Delivery surface, and what it implies

| | |
| --- | --- |
| Surface named at `01-idea` | «web · mobile · desktop · API · CLI · library · other» |
| Has a rendered interface | «yes / no» |
| Reachable by a crawler | «yes / no — and which parts» |

<!-- fill: If "has a rendered interface" is NO, write one sentence naming the surface as the
     reason no further section applies, and stop. Criterion 7 passes on that sentence. -->

> **Not applicable statement, if used:** «this product is delivered as «surface», so no view
> exists for which layout, interaction-state or accessibility requirements could be stated».

---

## 1. Interaction states

<!-- fill: Every component class the product ships, and the states it must define.
     The happy path is the one nobody forgets. The rest is where products are lost. -->

| Component class | States it must define |
| --- | --- |
| «class» | «default · hover · focus · active · disabled · loading · error · empty — or the subset that applies, with the exclusions named» |

**States that must exist somewhere in this product, with the view that owns each:**

| State | Owning view | What it says |
| --- | --- | --- |
| Empty — nothing yet | «view» | «why it is empty and what to do next» |
| Empty — nothing matched | «view» | «distinguished from the above, because they are different problems» |
| Loading | «view» | «what is shown, and whether it reserves the final layout» |
| Error, recoverable | «view» | «what failed and the recovery path» |
| Error, unrecoverable | «view» | «what failed and who to tell» |
| Insufficient data to answer | «view» | «stated as unknown, and never rendered as zero» |

> **The distinction that is easiest to lose:** «nothing yet», «nothing matched», «we could not
> load it» and «zero is the true answer» look identical if they are not specified apart.

---

## 2. Layout across the supported range

| | |
| --- | --- |
| Narrowest supported width | «n» CSS pixels |
| Widest layout before content stops widening | «n» |
| Breakpoints | «list, with what changes at each» |

**Per view, the behavior that changes — not merely that it "responds":**

| View | At the narrowest width | Above «breakpoint» |
| --- | --- | --- |
| «view» | «what it becomes» | «what it becomes» |

<!-- fill: Anything tabular, dense or multi-column needs a stated strategy at the narrow end.
     "It scrolls horizontally" is the absence of a strategy, not a strategy. -->

---

## 3. Accessibility

| | |
| --- | --- |
| Conformance target | «standard, version, level» |
| Assessed against | «the specific criteria this product can fail — listed, not the standard cited whole» |

| Criterion | Why this product can fail it | Requirement |
| --- | --- | --- |
| «id and name» | «the specific way this product would fail it» | «what must be true» |

> **The requirement most often lost:** where the product qualifies a figure — a denominator, a
> confidence, a sample caveat — **the qualification must be conveyed to assistive technology as
> part of the same statement.** A qualifier that is only visually adjacent delivers the bare
> figure the product intended not to give.

---

## 4. Performance

<!-- fill: Budgets with a measurement condition. An adjective is not a budget, and the
     banned-word scan in 08-product's Criterion 2 applies here in full. -->

| Metric | Budget | Measured on | Percentile |
| --- | --- | --- | --- |
| «metric» | «number and unit» | «client class and network» | «n»th |

**Payload budgets, if the surface has them:** «what, and the limit».

---

## 5. Supported clients

| | |
| --- | --- |
| Policy | «the rule — a named feature baseline, a version window, or a stated minimum» |
| Evidence or assumption behind it | «what it rests on, tagged per engine/evidence-policy.md» |
| Reopens | «the date or the event that makes this question live again» |
| Explicitly unsupported | «what, and the consequence for anyone on it» |

---

## 6. Crawlable surfaces

<!-- fill: Only if anything is reachable by a crawler. Two lists, never one. -->

| Indexable | Not indexable |
| --- | --- |
| «path or surface» | «path or surface» |

> **No authenticated path appears in the left column.** A product that leaks a customer
> identifier into a search index has failed a privacy requirement before it has failed an
> SEO one.

---

## 7. What is deliberately excluded

| Excluded | Why | What would unlock it |
| --- | --- | --- |
| «requirement» | «reason» | «trigger» |

<!-- fill: Scope discipline. A theme, a localization, an offline mode and a device class are
     each easy to add here and expensive to build. Exclusions with triggers are how this
     artifact stays a specification rather than a wish list. -->

---

## 8. Evidence standing

<!-- fill: Per engine/evidence-policy.md. Most of this artifact is [assumption] until
     something is put in front of a person, and saying so is the point. -->

| Claim | Tag |
| --- | --- |
| «claim» | «[verified: source] · [inferred: basis] · [assumption: needs validation]» |
