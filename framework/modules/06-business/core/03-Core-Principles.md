---
Title: Core Principles
Module: 06-business
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when modeling a business.
Audience:
  - AI Agents
  - Founders
  - Researchers
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent business judgment
Related Modules:
  - 07-strategy
Tags:
  - Business
  - Principles
---

# Core Principles

---

# Principle Statement

> A business model is a set of beliefs about money, arranged as arithmetic.
>
> The arithmetic is the easy part and the least important.

---

# Principle 1 — Arithmetic Does Not Create Evidence

A calculation is exactly as reliable as its least reliable input.

`LTV:CAC = 4.2` looks like a finding. If price, margin, acquisition cost and churn were all
chosen rather than established, it is a guess with a decimal point — and it will be quoted
in a pitch as though it were measured.

Tag every input. Let the reader see what the number is made of.

---

# Principle 2 — Value Before Price

Establish what the problem costs today, then decide what to charge for removing it.

A price chosen first and justified afterward is a preference wearing a business model. The
justification will always be found, because a number can be argued toward from any
direction.

---

# Principle 3 — Willingness, Ability and Authority Are Three Things

A user who wants it, in an organization that can afford it, still needs someone with the
authority to sign.

Products die at each of these separately. Collapsing them into "would they pay?" hides two
of the three ways the sale fails.

---

# Principle 4 — The Alternative Is Usually Free

The status quo costs nothing, is already installed, and carries no approval risk.

Every price must therefore answer a harder question than "is this cheaper than a
competitor?" It must answer "why pay anything at all?"

A price justified only against paid competitors has not met its hardest objection.

---

# Principle 5 — Derive the Margin

"80% gross margin, standard for software" is an assertion, and in products with real
infrastructure or per-operation AI costs it is often wrong by enough to invert the verdict.

Build cost to serve from components: infrastructure, support, third-party operations,
allocated compliance. Then compute the margin from it.

---

# Principle 6 — A Benchmark Is Evidence About Somebody Else

Industry churn figures are `[verified]` claims about an industry and `[assumption]` claims
about this product.

The benchmark supports a plausible range. It does not establish a value. Tagging the
distinction is the difference between a model and a wish.

---

# Principle 7 — Two Inputs Cannot Be Known Yet

Acquisition cost and churn depend on a channel never run and a product not built.

No amount of research resolves this. The mature response is to model them as ranges, name
which one the verdict depends on, and show what happens when it moves.

Filling them in with confident single values is the module's characteristic failure.

---

# Principle 8 — Sensitivity Is More Honest Than Precision

Where most inputs are assumed, a point estimate is false precision.

A table showing the verdict flipping between viable and not viable across a plausible range
tells the reader the truth: this business works under some assumptions and not others, and
here is which.

---

# Principle 9 — Solving Backwards Is Legitimate, Undeclared Backwards Is Not

Asking "what acquisition cost can this model tolerate?" produces a **budget**, which is
useful and actionable.

Presenting that derived figure as though it were researched is a fabrication. Declare the
direction of the reasoning.

---

# Principle 10 — Ten Names Beat a Channel Strategy

"Content marketing, SEO and partnerships" is not a route to revenue. It is a list of
categories.

Ten specific organizations, or profiles specific enough to go and find, is a plan someone
could start executing tomorrow. If ten cannot be produced, that is the finding.

---

# Principle 11 — The Cost to Serve Is a Constraint on Engineering

The per-customer infrastructure budget derived here becomes a design constraint in module
09.

Without it, the architecture is optimized for elegance or scale and the margin quietly
disappears. Hand it forward explicitly.

---

# Principle 12 — "Not Viable" Is a Result

A run that concludes the business does not work at any price this segment would pay has
delivered its most valuable finding.

Softening it to preserve momentum converts a week of analysis into a year of building.

---

# Principle Hierarchy

```
Who signs
   ↓
What it is worth to them
   ↓
What we charge
   ↓
What it costs us to serve
   ↓
What it costs to acquire
   ↓
Whether the arithmetic survives its assumptions
```

Each level constrains the next. A price set before value, or a margin assumed before cost,
breaks the chain silently.

---

# Common Violations

- Choosing a price and justifying it afterward.
- Presenting untagged arithmetic as a finding.
- Assuming the user is the payer without asking.
- Justifying price only against paid competitors.
- Asserting a standard margin.
- Citing a benchmark as though it described this product.
- Giving CAC and churn single confident values.
- Publishing a point estimate where the verdict flips across the range.
- Listing channels in place of customers.
- Dropping the cost-to-serve constraint before module 09.

---

# Self Assessment

- Can a reader see what every number is made of?
- Did value precede price?
- Did I distinguish willingness, ability and authority?
- Can I answer "why pay when free exists"?
- Did I derive the margin from components?
- Did I name the assumption the verdict rests on?
- Did I show sensitivity rather than precision?
- Could I hand someone the first ten customers today?

---

> **Core Principle**
>
> Nobody has ever been misled by a model that showed its assumptions.
>
> Almost everybody has been misled by one that showed only its conclusion.
