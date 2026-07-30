---
Title: Framework
Module: 14-ai-systems
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method for deciding where a model genuinely improves the product.
Audience:
  - AI Agents
  - Engineers
  - Product Managers
Prerequisites:
  - 14-ai-systems/core/03-Core-Principles.md
  - 08-product and 09-technology gates passed
Outputs:
  - ai_opportunities
  - model_strategy
  - data_requirements
  - evaluation_plan
  - failure_modes
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Framework
  - Method
---

# Framework — The Justification

---

# The Method

> Every capability in this module has to earn its place against something simpler.
>
> The module succeeds when it drops most of what it proposed.

Six moves. The second one decides the fate of everything, and the fifth happens before any
commitment is made.

```
  Propose  →  Compare  →  Ground  →  Bound  →  Evaluate  →  Fail
     │         │           │         │          │           │
  candidates  the test   the data  autonomy   the bar    the wrongness
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Propose | Where might a model help? | `ai_opportunities` |
| 2. Compare | Does it beat the non-AI alternative? | The kept-and-dropped list |
| 3. Ground | Does the data exist, and may we use it? | `data_requirements` |
| 4. Bound | How much autonomy is justified? | Autonomy levels and oversight |
| 5. Evaluate | What bar must it clear before users see it? | `evaluation_plan` |
| 6. Fail | What happens when it is wrong? | `failure_modes`, `model_strategy` |

**If the product has no AI component, that is a complete answer.** State it and stop. This module
is not an obligation to include one.

---

# Move 1 — Propose

**List candidate capabilities, each tied to a job.**

Every candidate names the job from `03-user` and the requirement from `08-product` it would serve.
A capability serving no requirement is the same orphan problem modules 08 and 09 each guard
against — and here it usually arrives from a different direction: not from the research, but from
what is currently possible.

Propose generously at this stage. The next move is where the discipline happens, and it works
better with real candidates than with a pre-filtered list.

---

# Move 2 — Compare

**Every capability is justified against a genuine non-AI alternative.**

This is the module's defining discipline and its gate criterion:

| Capability | The honest alternative |
| --- | --- |
| Suggest the likely diagnosis code | A searchable list ordered by that clinician's own recent usage |
| Summarize the consultation | A structured form with four fields |
| Extract data from a document | A better upload format, or asking the sender for structured data |
| Predict which record is needed next | Sorting by most-recently-used |

**The advocate check.** For each capability kept, could a competent person argue for the
alternative in one honest sentence? If not, the alternative was a straw man and the comparison
proved nothing. This is `07-strategy`'s advocate test, applied to a different kind of choice.

> **Capability theater.** A model added because it is expected rather than because it wins. It
> costs money per operation, needs evaluation nobody scheduled, fails in ways nobody predicted, and
> replaces a form field that would have worked.

**Dropping is success.** A module that proposes five capabilities and keeps one has done its job,
and the dropped rows are recorded with the simpler thing adopted instead. Those records are what
stop the same capability being re-proposed every quarter as an obvious omission.

**Where the alternative wins on quality but loses on effort**, that is a legitimate reason to build
the model version — stated that way. What is not legitimate is scoring the alternative badly to
make the choice look better.

---

# Move 3 — Ground

**Confirm the data. Do not assume it.**

> The most common way an AI capability fails is that it fails before it starts, because the data it
> needed did not exist in the form it needed.

| Per data need | |
| --- | --- |
| Source | Where it comes from |
| Available **now** | Confirmed, with evidence — not "we will have this" |
| Volume | Enough for the approach chosen |
| Quality | Assessed, not assumed |
| Blocker | What stands in the way |

**Unconfirmed data needs are blockers, not risks.** A capability resting on data nobody has checked
for is a capability that cannot be estimated, scheduled or built.

**Cold start.** How does the capability behave before any data has accumulated? Most model-served
features are at their worst exactly when the product is newest and users are least tolerant — and
the answer is usually a non-AI path for the first period, which is a design decision rather than a
disappointment.

## Data Rights Are a Legal Question

Whether the product *may* use this data this way is not a technical matter:

| Question | Why |
| --- | --- |
| Do we have the right, under which regime? | Consent for treatment is not consent for model input |
| Does the data leave our systems? | To whose infrastructure, in which jurisdiction |
| Are regulated or PII fields in the input? | Check `09-technology` §3 mechanically |
| Is provider training on our data disabled? | And is that contracted, or assumed? |

> Sending a regulated field to a model provider is the same class of exposure as putting one in an
> analytics event property.

This is the fourth appearance of one discipline in the framework: `09-technology` traces obligations
to mechanisms, `12-metrics` checks event properties, `13-operations` schedules the review, and this
module checks model inputs. The regulated column list is the same list every time.

---

# Move 4 — Bound

**Decide how much autonomy is justified, from the cost of being wrong.**

The ladder, in increasing order of consequence:

| Level | The model | The user |
| --- | --- | --- |
| Suggests | Offers an option | Chooses |
| Drafts | Produces something | Edits and approves |
| Acts with confirmation | Proposes an action | Confirms |
| Acts autonomously | Does it | Finds out afterwards |

## The Wrongness Cost

Three questions decide the level, and the third is the one usually skipped:

| Question | |
| --- | --- |
| What does one wrong output cost? | In the user's terms |
| Who bears that cost? | The user, the operator, or a third party |
| **Can the user detect it is wrong?** | This is the decisive one |

> Where the user bears the cost and cannot detect the error, autonomy above "suggests" is not
> permitted without a mechanism that makes the error visible.

Detectability governs autonomy more than accuracy does. A capability that is right 99% of the time,
whose 1% is undetectable and consequential, is more dangerous than one that is right 90% of the time
and visibly wrong the rest.

**Oversight and transparency follow from the level.** Who reviews, whether the user can override,
whether the override is recorded, whether AI involvement is disclosed, and whether a regulatory
regime requires that disclosure.

**Who reviews matters as much as whether.** In a domain product, quality review requires a domain
expert. The build team cannot assess clinical, legal or financial correctness, and their confidence
in an output is not evidence about it — the same reason `03-user` forbids inventing user quotes.

---

# Move 5 — Evaluate

**Define the bar before committing to the capability.**

"We will evaluate it" is not a plan. What is:

| Element | |
| --- | --- |
| Metric | What quality means for this capability |
| Method | Golden set, human review, A-B |
| Passing bar | A figure |
| Sample size | Enough to mean something |
| Cadence | How often it is re-checked |
| **Ship gate** | The result required before users see it |
| What happens if the bar is missed | The capability does not ship — stated |
| Regression check | How a model or prompt change is re-evaluated |

**The golden set must stay honest** — constructed from real cases, and never used for tuning. A
golden set that has been optimized against measures how well the capability was fitted to it.

## Acceptance Criteria for Something Nondeterministic

`08-product` requires acceptance criteria that can fail, and its `Given / when / then` form assumes
the same input produces the same output. A model-served capability breaks that assumption, so it
needs both kinds of criterion:

| Type | Form | Example |
| --- | --- | --- |
| **Statistical** | A bar over a sample | "≥95% of 200 golden-set cases judged correct by a «domain expert»" |
| **Per-instance** | Always true, every time | "Output never exceeds «n» characters" · "Output always contains a citation" · "The user can always dismiss it" |

The per-instance guarantees are ordinary requirements and belong in `08-product`'s criteria, where
they can be tested conventionally. They are also where most real safety lives: an output that must
always be dismissible, always labeled, and always bounded is safe in ways no accuracy figure
provides.

---

# Move 6 — Fail

**Specify how it goes wrong, here, in this product.**

| Generic, and useless | Specific, and designable |
| --- | --- |
| "The model may hallucinate" | "The model may invent a drug interaction that does not exist, which a rushed clinician could accept" |
| "Output quality may vary" | "For handwritten notes the extraction drops silently to partial, and the missing fields look like fields the user left blank" |

## The Plausibility Problem

> A model's errors are fluent. They arrive in the same register as its correct answers.

This is why detectability outranks error rate, and it is worth noticing that it is the same failure
the framework's own evidence policy exists to prevent: *an assumption must never be smoothed into a
fact.* A model does exactly that by default, in every sentence it produces.

So the required columns are **detection** and **guardrail**, not just likelihood and consequence.
And two questions must be answered plainly:

| | |
| --- | --- |
| Worst realistic outcome | Stated, not softened |
| Would we know it happened | Frequently no, which is itself the finding |

**The non-AI fallback is a requirement, not a contingency.** The provider will have an outage, the
model will be deprecated, and the capability will sometimes be wrong. What the user does then is
part of the product, and it belongs in `08-product`'s requirements rather than in an operational
note.

**Model strategy belongs to this move**, because it is mostly about failure: version pinning,
deprecation exposure, the fallback model, and vendor lock-in. Model capabilities and prices are
version-scoped and change — cite them with a version and a date, exactly as `09-technology` requires
of every technology claim.

---

# The Cost Ratio

One arithmetic check, feeding the framework's larger ones:

```
cost per operation × operations per user per month = AI cost per user per month
AI cost per user ÷ revenue per user = the share
```

A capability consuming a significant fraction of revenue per user is a margin problem, and the
options are a cheaper approach, fewer operations, a higher price, or dropping it. This figure goes to
`09-technology` §12 and `13-operations` §11 as a line in the cost to serve — where the framework's
three cost checks will find it.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Compare after grounding | Data work done for capabilities that should have been dropped |
| Bound before comparing | Autonomy decisions about features that will not exist |
| Evaluate after building | A bar set to whatever was achieved |
| Choose the model before the capability | The capability shaped to what the model does well |
| Skip Move 6 | A product whose failures are discovered by users |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| The architecture | `09-technology` — the model is placed inside it |
| Prompt text and implementation | Build time, within the constraints set here |
| Metric instrumentation | `12-metrics` |
| Alerts, runbooks and support scripts | `13-operations` |

---

# Self Assessment

- Did I propose generously, then compare honestly?
- Could someone argue for each non-AI alternative in one sentence?
- What did I drop, and what simpler thing replaced it?
- Is any data need unconfirmed?
- May we legally use this data this way?
- Does any model input carry a regulated field?
- Can the user detect a wrong output?
- Is the autonomy level justified by the wrongness cost?
- Did I set the bar before committing?
- Are my failure modes specific to this product?
- What is the non-AI fallback, and is it a requirement?
- What share of revenue does this consume?

---

> **Framework Principle**
>
> This is the last module in the framework, and it is the one most
> likely to be run for the wrong reason.
>
> Its discipline is a single question asked without flinching:
> would something simpler have worked?
