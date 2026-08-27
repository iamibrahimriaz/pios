# Remote Validation — working to the edge of public evidence, and saying where it is

The framework assumes primary research is available: interviews, observation, a conversation with
someone who has the problem. **For most operators at the idea stage it is not** — not before some
desk work justifies the trip, and sometimes not at all.

That condition is normal, not degraded. What is missing is not capability but **access to people**,
and the framework has to be able to say so precisely rather than treating every unreachable claim as
a research failure.

> **"The internet cannot answer this" is a finding, not an apology.**
>
> Reaching the edge of public evidence and naming the edge is a completed piece of work. It tells
> the operator what the trip is for, and it is frequently evidence about the market in its own right.

---

## When this mode applies

**Per question, not per run.** A single run will answer most of its questions remotely and hit the
wall on two or three.

| Applies | Does not apply |
| --- | --- |
| Primary research is unavailable **for this question**, now | The agent has no retrieval capability at all — that is `degraded_mode` in `gates.yaml` |
| The claim needs a person, and no person is reachable yet | The evidence exists publicly and has not been looked for. **Difficulty is not impossibility** |
| The operator will do fieldwork later and needs to know what to ask | The missing input is a decision — that is `decision_dependent_failure` |

---

## The ladder

**Cheapest first, and each rung records what it returned — including nothing.**

| # | Rung | Reaches | Typically answers |
| --- | --- | --- | --- |
| 1 | **Official and regulatory publications** | What is required, counted or licensed | Obligations, dated cycles, population counts, definitions |
| 2 | **Competitor published material** — pricing pages, documentation, FAQs, demos, changelogs, terms | What vendors believe their buyers want | Price bands, feature baselines, positioning, **what the category is actually called** |
| 3 | **Public discussion** — forums, groups, review aggregators, Q&A sites | What users say unprompted | Complaints, workarounds, switching triggers |
| 4 | **Hiring signals** — job postings, org pages | What companies are staffing toward | Internal priorities, stack, scale, roles a product would touch |
| 5 | **Trade press and industry reporting** | What the sector talks about | Structural trends, closures, funding, regulation in flight |

**A rung that returns nothing is recorded as attempted and empty. It is not skipped silently**, and
it is not retried in a different phrasing until it produces something agreeable.

**Stop climbing when the remaining rungs cannot carry the class of evidence you need.** A
per-customer cost figure is not in trade press or job postings; continuing up the ladder to be able
to say you did is theatre, and the exhaustion record should say why you stopped instead.

---

## What it must produce

**Two outputs. The second is the one that matters.**

### 1 — What was established remotely

Ordinary evidence, tagged per `evidence-policy.md`. No special treatment: a claim sourced from a
regulator is `[verified]` whether or not the run also wanted an interview.

### 2 — `remote_validation_limit` — what cannot be established without contact

For each question that hit the wall:

| Field | Content |
| --- | --- |
| **question** | The specific claim or quantity, not the topic |
| **why_remote_cannot_close_it** | **Structural.** Which source types remain, and why each cannot carry this class of evidence |
| **cheapest_method_that_would** | The specific method — not "research", not "talk to users" |
| **cost** | In days, and what it requires the operator to have |

**This output is the fieldwork plan.** It is not a list of regrets; it is derived from what the desk
work could not reach, so the trip has a defined purpose before anyone books it.

**Where a gate fails on one of these questions**, this output becomes the seed of the Research
Exhaustion Report required by `conditional_continuation` in `gates.yaml`. The two are the same
finding at different levels of formality — do not write them independently and let them disagree.

---

## The absence is itself evidence

**This is the part most likely to be discarded, and it is frequently the most valuable thing the
mode produces.**

When a category has no public discussion, no review corpus, no indexed community and no comparison
content, that is not merely inconvenient. **It is a finding about how the market's buyers behave**,
and it has direct consequences:

- Review-mining, search-driven acquisition and content marketing are **unavailable, not merely
  underused.**
- Whatever channel does reach these buyers is **load-bearing rather than favorable**, because
  nothing is waiting behind it.
- A competitor's silence on a topic is **absence of supply, not presence of demand** — and the
  distinction must be stated every time, because the two are easy to conflate in the direction that
  flatters the idea.

**Record the negative result with what was searched**, so it is auditable. "No corpus found" with no
record of the attempt is indistinguishable from not looking, and it will be read as the latter by
anyone reviewing the run later.

---

## What this mode does not license

- **It does not lower the evidence bar.** A claim reached remotely is tagged by its source, exactly
  as it would be otherwise.
- **It does not make a gate passable.** Reaching the edge of public evidence does not satisfy a
  criterion that requires evidence beyond it. See `conditional_continuation`.
- **It does not excuse a shallow search.** Five minutes per rung and a declaration of exhaustion is
  the failure this mode exists to prevent. The record has to show what was searched.
- **It does not replace fieldwork.** It tells you what the fieldwork is for.

---

## Checklist

- [ ] The mode was applied per question, not declared for the whole run
- [ ] Every rung attempted is recorded, including the ones that returned nothing
- [ ] Each empty result states **what was searched**, not just that nothing was found
- [ ] Stopping early is justified structurally — which rungs remain and why they cannot help
- [ ] `remote_validation_limit` names each unreachable question, its cheapest closing method, and the cost
- [ ] Any absence of a public corpus is recorded as a finding with its channel consequences
- [ ] Nothing was tagged `[verified]` on the strength of having searched hard

---

> **Remote Validation Principle**
>
> A research method that cannot report its own limit will always report success.
>
> The purpose of this mode is not to find more. It is to know precisely where finding more stops
> being possible, and to hand that boundary to the person who can cross it.
