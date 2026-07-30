---
Title: Research Methodology
Module: 08-product
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how claims in a specification are sourced, labeled and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 08-product/core/06-Framework.md
Outputs:
  - Sourced, correctly labeled specification
Related Modules:
  - 09-technology
Tags:
  - Product
  - Methodology
  - Evidence
---

# Research Methodology

---

# What "Evidence" Means in a Specification

A requirement cannot be verified against a source. Nobody can produce a citation for
"the system must let the user save a draft".

So the evidence question changes shape here. For every statement in this document, exactly
one of three things is true:

| Kind | Meaning | How it is labeled |
| --- | --- | --- |
| **Derived** | It follows from a finding in an earlier module | `derived: 04-problem P2` |
| **Design decision** | A judgment made in this module | `design decision` — and registered in §12 |
| **External standard** | A domain, regulatory or interoperability requirement | `[verified: source]` |

Statements about the world — the problem, the user, the workflow, the market — keep the tags
they had in their source module. They are not re-evidenced here, and they are not upgraded.

> A precisely written requirement serving an assumed problem is precisely written and still
> assumed. Specificity is not evidence.

---

# The Derivation Chain

Every MUST requirement must be traceable along this chain, and the chain must be writable
without gaps:

```
verified / inferred / assumed problem   (04-problem)
        ↓
job and workflow step                   (03-user)
        ↓
capability above the MVP line           (07-strategy)
        ↓
requirement                             (here)
```

If any link cannot be named, the requirement is an orphan. Delete it.

**The confidence rule that follows.** A requirement inherits the weakest tag in its chain. A
requirement derived from a problem tagged `[assumption: needs validation]` is written
normally — but §15's confidence assessment counts it as resting on an assumption, and §7
marks it. This is how module 04's honesty survives two modules of translation.

---

# Design Decisions Are Assumptions

Specification requires judgment that no research produced. How many items on a page. Whether
a step is one screen or three. Whether an action is reversible. What the default is.

These are legitimate and unavoidable. What is not legitimate is presenting them as though
they were derived.

**Handling:**

1. Label it `design decision` in the requirement's basis field.
2. Record it in §12 with the alternative it rejected — universal gate U4.
3. If it is **load-bearing** — the product is materially different if it is wrong — append it
   to `state.assumptions` with a validation method, per U5.

| Test for load-bearing | |
| --- | --- |
| Would a different choice change what gets built, not just how it looks? | Load-bearing |
| Would a user notice and care? | Load-bearing |
| Is it reversible after launch at low cost? | Not load-bearing |

---

# When External Lookup Is Legitimate

Most of this module is derivation. But some requirements are constrained by facts that exist
outside the run, and inventing them is a serious defect rather than a stylistic one:

| Class | Examples | Why it must be looked up |
| --- | --- | --- |
| Regulated content | Fields a record must legally contain, retention periods, consent wording | Getting these wrong makes the product unlawful, not merely wrong |
| Interoperability formats | Exchange standards, file formats, identifier schemes | The format is defined by someone else |
| Domain conventions | Units, coding systems, established terminology, rounding rules | Practitioners will reject a product that gets these wrong |
| Accessibility requirements | Applicable conformance level and its criteria | It is a specification, not a preference |
| Platform requirements | Store rules, permission models, review policies | They gate distribution |

**Source hierarchy for these claims**

| Tier | Source | Use |
| --- | --- | --- |
| 1 | The regulation, standard or specification itself | Definitive |
| 2 | The issuing body's own guidance | Definitive |
| 3 | Official implementation guides | Strong |
| 4 | Professional body guidance | Strong for conventions |
| 5 | Established textbook or reference work | Adequate for conventions |
| 6 | Practitioner community consensus | Indicative — tag `[inferred]` |
| 7 | A competitor's implementation | Establishes what they do, never what is correct |
| 8 | Recollection | Not a source. Look it up or mark it open |

Tier 7 deserves the emphasis. That a competitor's form has nine fields tells you their
product has nine fields. It does not tell you the ninth is required, correct, or legal.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| Invent a regulated field, code or retention period | It reads as authoritative and is actionable — the worst combination |
| Invent a domain workflow the user was never observed performing | The whole product is then built on a fictional process |
| State a threshold, limit or unit from memory | Wrong numbers in a spec become wrong numbers in a product |
| Write a design decision as though derived | The reader cannot tell what is settled |
| Restate an assumed problem in the certain register | Confidence laundering, one module downstream |
| Use a competitor's behavior as a correctness argument | Copies their mistakes with none of their context |

Where a needed fact cannot be established: write the requirement with the fact marked
`[assumption: needs validation]`, add the lookup to `state.open_questions`, and say in §12
that the requirement is blocked on it. A specification with an honest hole is buildable
around. A specification with an invented fact is not.

---

# Precision Without Evidence Is a Real Failure

The characteristic error of this module is not vagueness. It is **confident detail**.

A specification that states response times, field lengths, limits and retention periods
reads as thoroughly researched. If those numbers were chosen because a number was needed,
the document is worse than one that left them open — the builder implements them, the tester
tests them, and nobody discovers they were invented until a user does.

| Number in the spec | Must be one of |
| --- | --- |
| A regulatory or standards figure | `[verified: source]` |
| Derived from a research finding | `derived: «module» «finding»` |
| A chosen default | `design decision`, and registered |
| Otherwise | Not in the document |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Traceability | 04-problem | A requirement has no parent problem |
| Coverage | 04-problem, 07-strategy | A problem above the line serves nothing |
| Boundary | 07-strategy `mvp_definition` | A MUST sits below the line |
| Confidence | 04-problem tags | §15 confidence exceeds the underlying problems |
| Cost fit | 06-business | The requirement set breaks the cost-to-serve ceiling |
| Environment fit | 03-user | Requirements assume conditions the user does not have |
| Regulatory fit | 02-market | A requirement contradicts a stated constraint |

---

# Self Assessment

- Can I write the full derivation chain for every MUST?
- Is every design decision labeled as one and registered?
- Did I look up every regulated fact, or did I recall one?
- Is any number in this document there because a number was needed?
- Did I use a competitor's implementation as evidence of correctness?
- Does my confidence statement exceed the confidence of my inputs?

---

> **Methodology Principle**
>
> This module cannot make anything more certain than it arrived.
>
> It can only make it more precise — and precision is very good at
> looking like certainty.
