---
Title: Common Mistakes
Module: 07-strategy
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures at the strategy stage, starting with confidence laundering.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 07-strategy/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of strategy-stage failure patterns
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - Strategy
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

The failures here are worse than elsewhere in the framework, because this module's
output is a decision and a bad decision is elaborated by six more modules before anyone
tests it.

---

# 1. Confidence Laundering

**What it looks like.** A thorough options analysis whose winner is the option the team
arrived with.

**Why it is tempting.** It is barely a choice to make it. Someone has a view — often a
good one — and the analysis is performed around it. Nobody decides to launder anything.

**What it costs.** The framework's central defense is that a choice can be argued with.
A laundered choice presents as argued-with and is not, so the disagreement that would
have improved it never happens. Six downstream modules then elaborate it faithfully.

**Instead.** Two procedural defenses, because there is no analytical one: set the
weights before scoring, and include an option you would be genuinely disappointed to
pick. If the result never surprises anybody, the process is decorative.

---

# 2. Three Options That Are One Option

**What it looks like.** Web, mobile, or both. Build now, build later, build a subset.

**Why it is tempting.** It satisfies the gate's count and requires no reconsideration of
the premise.

**What it costs.** The shared assumption — that you are building this kind of thing at
all — goes untested. In the worked example, the option that won was "deliver it as a
service," which no variant of the tool would have surfaced.

**Instead.** Include an option that does not involve building software, and one that
involves someone else's distribution. At least one of the three should make the team
uncomfortable.

---

# 3. Weights Set After Scores

**What it looks like.** A weighted comparison where the weights are reasonable and the
winner is comfortable.

**Why it is tempting.** Weights feel like a technical detail to be tuned until the
model is right — and "right" is unconsciously defined as "agrees."

**What it costs.** It is confidence laundering with arithmetic, and it is more
persuasive because it has numbers.

**Instead.** Write each weight and its justification before any option is scored. A
weight justified by an upstream finding — a declared shortfall, a high switching cost, a
regulatory constraint — is defensible. A weight justified by nothing is a preference.

---

# 4. The MVP That Is a Small Product

**What it looks like.** The full plan with the harder half removed.

**Why it is tempting.** It is shippable, it looks like progress, and everything in it
is wanted.

**What it costs.** An MVP exists to resolve an uncertainty. A small version of the
product resolves nothing — it launches, gets modest use, and generates no information
about whether the premise holds.

**Instead.** State what the MVP must teach you and cut to the smallest thing that
teaches it. Sometimes that is not software.

---

# 5. Non-Goals Nobody Wanted

**What it looks like.** "We will not build a mobile app, an API, or an enterprise
tier" — in a run where none of those had been proposed.

**Why it is tempting.** The gate asks for non-goals, and safe ones cost nothing.

**What it costs.** The list does not hold. Real scope pressure comes from things
somebody genuinely wants, and those were not addressed, so they re-enter at module 08 as
obvious requirements.

**Instead.** Every non-goal should be something you would be tempted by. If cutting it
did not hurt, it was never in scope.

---

# 6. Deferred Recorded as Rejected, or the Reverse

**What it looks like.** A phase-two list that is really a rejection list, or a rejection
that keeps coming back.

**Why it is tempting.** "Phase two" is the diplomatic way to say no, and it avoids an
argument.

**What it costs.** Both directions cost. A rejection filed as a deferral reappears every
quarter as an obvious omission. A deferral filed as a rejection loses something the
roadmap needed.

**Instead.** Two lists, explicitly. Module 14's example is the model: a capability
"recorded as rejected, not deferred, so it is not re-proposed as an obvious omission."

---

# 7. Scope Laundering

**What it looks like.** An MVP cut where nothing is actually cut — everything remains,
relabeled as phases.

**Why it is tempting.** It resolves the disagreement in the room without anyone losing.

**What it costs.** Module 08 inherits an MVP that is the whole product, module 10
sequences it, and the first honest estimate arrives in build. The cut has to happen
eventually and it happens under time pressure with less information.

**Instead.** Something must be genuinely out. If the phase-one list has everything in
it, no decision was made.

---

# 8. Risks Without Owners

**What it looks like.** A register listing likelihood, impact and a mitigation.

**Why it is tempting.** Three fields feel complete, and naming an owner turns a document
into an obligation.

**What it costs.** A mitigation nobody owns does not happen. The register then serves as
documentation that the risk was known — which is worse than not having listed it, in
every setting where that document is later read.

**Instead.** A name. "The team" is not one.

---

# 9. The Shortfall Not Weighted

**What it looks like.** Module 04 declared a shortfall; this module's comparison is
identical to what it would have been without one.

**Why it is tempting.** The declaration was made two modules ago and reads like a
caveat.

**What it costs.** Everything the declaration was for. The run now has documentation of
rigor and behaved as though nothing was unknown, which is strictly worse than never
having declared it.

**Instead.** A shortfall should visibly move a weight. If it moved nothing, say so and
explain why — that is at least an argument someone can check.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Confidence laundering | Documenting a decision instead of making one |
| Three fake options | Satisfying a count |
| Weights after scores | Tuning until it agrees |
| MVP as small product | Shipping instead of learning |
| Safe non-goals | Cutting where it does not hurt |
| Deferred vs rejected confusion | Avoiding the argument |
| Scope laundering | Resolving disagreement by including everything |
| Ownerless risks | Documenting instead of assigning |
| Shortfall unweighted | Carrying a finding as a caveat |

Seven of the nine avoid a decision while producing a document that appears to contain
one. That is this module's characteristic failure and it is the most expensive in the
framework, because the six modules after it are extremely good at elaborating whatever
they are given.

---

> **Mistakes Principle**
>
> The document produced by a real decision and the document produced by a laundered one
> are indistinguishable.
>
> Which means the only available defenses are procedural, and they have to be applied
> before you know the answer.
