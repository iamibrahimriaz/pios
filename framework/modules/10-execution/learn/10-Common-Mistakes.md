---
Title: Common Mistakes
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in delivery planning and flow design.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 10-execution/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of execution-stage failure patterns
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

These failures are visible earlier than most in the framework — usually within the first
two weeks of building — which makes them cheaper than they look, provided anyone is
watching.

---

# 1. The Flow That Starts at a Screen

**What it looks like.** "User opens the app and taps Record."

**Why it is tempting.** That is where your product's involvement begins, so it feels like
the natural starting point.

**What it costs.** The interesting decisions happen before: what triggered this, what
they were doing, what is in their hands, whether they are standing up. Module 03
documented a workflow that starts earlier, and a flow ignoring it produces a product that
fits a moment that does not occur.

**Instead.** Start where the user's situation starts. The first two steps are usually
outside your software, and they determine whether the third one is reachable.

---

# 2. Only the Populated State Is Designed

**What it looks like.** Screens designed against realistic test data.

**Why it is tempting.** It is what the product looks like when it is working, and it is
the version worth showing people.

**What it costs.** Every user's first session is the empty state, and if it shows a blank
area with no action, the session ends there. This is the most common reason a product
with real value gets no adoption.

**Instead.** Design the empty state first, with one obvious action. Then the partial
state, then the failure state. The populated state is the easiest of the four and it
designs itself.

---

# 3. Milestones That Are Layers

**What it looks like.** "M1: data layer. M2: API. M3: interface."

**Why it is tempting.** It matches how the work decomposes technically and each phase has
a coherent owner.

**What it costs.** Nothing is demonstrable until M3, integration risk is concentrated at
the end, and progress cannot be verified until the last third. This is the structure
under most projects that are 90% complete for two months.

**Instead.** Vertical slices. One narrow capability working end to end beats three
complete layers, because it is the only thing that produces information.

---

# 4. The Handoff That Needs Its Author

**What it looks like.** A document that is complete to everyone who was in the meetings.

**Why it is tempting.** It is written by someone with full context, and the gaps are
invisible to them by definition.

**What it costs.** The build proceeds at the rate the author can answer questions. Worse,
the questions that do not get asked get answered by assumption.

**Instead.** Give it to someone who was not there and watch where they stop. That is the
only reliable test, and it takes twenty minutes.

---

# 5. A Definition of Done That Restates the Task

**What it looks like.** "Done when the approval flow is implemented."

**Why it is tempting.** It is technically accurate.

**What it costs.** It carries no information. Done includes: the acceptance criteria met,
the edge cases handled, the failure states in place, the instrumentation emitting, and
somebody other than the author having used it.

**Instead.** Derive it from module 08's acceptance criteria. If those were observable, the
definition of done is mostly a transcription; if they were aspirational, this is where
that bill arrives.

---

# 6. Milestone Zero Scheduled Late

**What it looks like.** Validation planned for after the first release.

**Why it is tempting.** Building feels like progress and validating feels like delay. The
team wants to make something.

**What it costs.** The entire point. A validation that runs after the build cannot change
what was built; it can only produce a finding that has to be reconciled with a product
that already exists.

**Instead.** If module 04 declared a shortfall, the validation goes first. In the worked
example, that sequencing is why a service was delivered before a model was trained — and
why the run had real data by the time it needed it.

---

# 7. Accessibility Deferred to a Later Pass

**What it looks like.** "Accessibility audit scheduled before launch."

**Why it is tempting.** It sounds responsible and it removes work from now.

**What it costs.** Most accessibility is structural — focus order, semantics, labels,
contrast, keyboard paths. Retrofitting it means rebuilding the flows rather than
adjusting them, which is why the later pass usually becomes a list of known violations
instead.

**Instead.** It belongs in the flow. Keyboard path and focus order are part of designing
the flow, not a review of it.

---

# 8. QA Planned After the Build

**What it looks like.** A test plan written once there is something to test.

**Why it is tempting.** It seems more efficient to test what exists.

**What it costs.** A test plan derived from the build tests what was built, including its
misreadings of the specification. The information you wanted — does this match what was
decided — is exactly what it cannot produce.

**Instead.** Derive tests from module 08's acceptance criteria and module 09's failure
modes, now, before either has been interpreted by an implementation.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Flow starts at a screen | Designing from the product's perspective |
| Only populated state | Designing the version worth showing |
| Milestones as layers | Sequencing by technical decomposition |
| Handoff needs its author | Writing from full context |
| Done restates the task | Carrying no information forward |
| Milestone Zero late | Building feels like progress |
| Accessibility deferred | Treating structure as review |
| QA after the build | Testing what exists rather than what was decided |

Half of these come from designing outward from the product rather than inward from the
user's situation. The other half come from optimizing the feeling of progress over the
production of information.

---

> **Mistakes Principle**
>
> Every failure here is visible in the first fortnight of building, if anyone is
> looking.
>
> That makes this the cheapest module in the framework to be wrong in — and the most
> wasteful one to be wrong in unnoticed.
