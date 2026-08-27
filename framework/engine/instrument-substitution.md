# Instrument Substitution — validating when the specified method is impossible

A validation test names a method: interview ten operators, run a pricing survey, watch five people
attempt the task. **Then the operator says they cannot do it** — no access to those people, no
budget, no standing to ask, or simply not the kind of person who will cold-call strangers.

**That is the common case, not the exception.** And the framework's answer cannot be "the validation
does not happen", because the alternative to a substituted instrument is not a better instrument.
It is an unvalidated build.

> **A test is defined by what it measures, not by how it measures it.**
>
> A test recorded only as a method cannot be substituted, because there is nothing to compare
> against except the method that is unavailable.

**This is the file that makes a swap legitimate rather than convenient.** It is not a lower bar —
substituting an instrument is *harder* than running the specified one, because the equivalence has
to be argued before any data arrives.

**Related:** `remote-validation.md` covers a *research question* that cannot be closed from public
sources. This covers a *validation test* whose instrument the operator cannot operate. A run often
needs both, and they are not the same problem: the first is about the edge of what is knowable, the
second is about who can do the knowing.

---

## The three fields every test needs before it can be substituted

**Write these when the test is designed, not when the substitution is proposed.** A test that
records only its procedure has already lost the information a substitute would be judged against.

| Field | Content | Why it is the load-bearing one |
| --- | --- | --- |
| **`measures`** | The claim the test establishes, stated with no reference to method | *"Whether a seller will pay money for this"* survives a change of instrument. *"Ten interviews"* does not |
| **`claim_class`** | Which of the six claims (see `evidence-policy.md`) | A substitute that measures a different claim is not a substitute, however good it is |
| **`threshold`** | The decision rule, and the volume floor below which it may not be read | An instrument change that quietly changes the threshold has changed the test |

---

## When a substitution is permitted

**All four. Any one missing and this is not a substitution, it is a different test with the
original's name on it.**

1. **The specified instrument is genuinely unavailable to this operator** — not merely
   inconvenient, slow, or uncomfortable. Difficulty is not impossibility, and the distinction is
   the same one `remote-validation.md` draws.
2. **The substitute measures the same claim class.** Not an adjacent one. Not a proxy for one.
3. **An equivalence argument is written down BEFORE the instrument runs**, naming what the
   substitute measures well, what it measures worse, and in which direction it is biased.
4. **The threshold is carried across unchanged, or a justified equivalent is derived and the
   derivation is shown.** "Same proportion, higher price floor, because the lower floor could not
   clear the revenue ceiling" is a derivation. "Roughly similar" is not.

---

## What makes an equivalence argument real

**The three questions, answered in writing, in this order:**

**1 — What does the substitute measure well?** Name the property that carries across. A public
complaint and an interview both record that a person had a problem and thought it worth the effort
of describing.

**2 — What does it measure worse, and in which direction?** This is the part that gets skipped, and
it is the whole value of the exercise. Public complaint corpora are biased toward people angry
enough to post and toward products with enough users to have a forum. Neither bias is symmetric,
and both flatter the same conclusion.

**3 — What can it not measure at all?** Say it plainly and stop claiming it. **A corpus of public
complaints cannot establish willingness to pay.** No amount of coding converts one into the other,
and the attempt is the most common way a validation week produces a confident wrong answer.

> **Confidence moves down, and the move is recorded.** A substituted instrument that clears its
> threshold produces a weaker finding than the specified instrument clearing the same threshold.
> If confidence did not move, the substitution was free — and a free substitution means the
> original instrument was never load-bearing, which is its own finding.

---

## Public and user-generated evidence — the coding standard

**The most common substitute, because it is the one always available.** Support forums, plugin and
app reviews, community discussions, issue trackers, public Q&A, comments.

**It is real evidence and it is routinely overcounted.** The discipline below is what separates a
corpus from a pile of quotes.

> **Ten comments are not ten incidents. Ten incidents are not ten reporters.**
>
> A framework that cannot tell those three numbers apart will report the largest one.

### Firsthand versus secondary

| Class | Definition | Counts toward an incident floor |
| --- | --- | --- |
| **Firsthand** | The author is describing something that happened to a system they operate or use. *"My client's site"* qualifies — they were there | **Yes** |
| **Secondary** | The author is relaying, summarizing, agreeing, or describing a known pattern. *"This happens a lot"*, *"I've read that…"*, a vendor summarizing tickets | **No.** Recorded separately, reported separately |
| **Vendor-originated** | Issues, posts or tickets filed by the product's own staff or automation | **No.** Frequently the majority of an issue tracker, and invisible unless the account is checked |

**Check the author, not the wording.** A single tracker where two vendor accounts filed most of the
issues reads as a large user corpus until somebody counts by author.

### Deduplication, and what a reporter is

**Deduplicate before counting anything.**

- **The same person describing the same failure twice is one incident.** Cross-posting, a follow-up
  thread, and a review that repeats a forum post are all one.
- **A reposted, quoted or aggregated report is not an independent case.** Review aggregators and
  syndicated forums make one report look like four.
- **Two people hitting the same failure are two incidents and two reporters.** That is the number
  that means something.
- **Report both counts, always:** incidents, and distinct reporters. A corpus of 40 incidents from
  6 reporters and one of 40 incidents from 38 reporters support entirely different conclusions, and
  the single number cannot distinguish them.

### Severity and business impact

**Severity is coded from what the author states, never from how upset they sound.** Tone is a
property of the writer.

| Code | Requires |
| --- | --- |
| **Business impact stated** | The author names a consequence: money refunded, a customer or user lost, data gone, hours spent repairing. **This is the number that matters and it is always far smaller than the incident count** |
| **Incident, no consequence stated** | Something broke. What it cost is unknown — record it as unknown, not as zero |
| **Not an incident** | A question, a feature request, a pre-sales enquiry, a configuration error resolved in thread |

**Do not infer a cost the author did not state.** The inference is always available and always
points the same way.

### The corpus itself must be justified

**Covered in full by `modules/04-problem/knowledge/Corpus-Selection.md`.** The short version, because
it is the failure that invalidates everything above it: **a corpus chosen because a product is large
is not evidence that the product is problem-heavy.** Size drives raw complaint volume. Normalize, or
say you could not.

### What to record so the coding can be argued with

**Every incident keeps its source URL or identifier, its date, and its author handle.** A coded
result whose rows cannot be re-read is a result nobody can disagree with, which is not a strength.

**Publish the coding rule with the counts.** Someone re-coding the same corpus under the same rule
should land within a few percent. If they cannot, the rule was judgment wearing a procedure's name.

---

## The willingness-to-pay ladder

**Willingness to pay is the claim most often substituted for, and the substitutions are the least
equivalent.** These rungs are not interchangeable, and each one costs more to run than the one above
it — which is precisely why the weak ones are so attractive.

| # | Instrument | What it establishes | What it does not |
| --- | --- | --- | --- |
| 1 | **Stated interest** — "would this be useful?" | Almost nothing. Near-universal yes | Anything about money |
| 2 | **Stated price** — "would you pay $X?" | A ceiling. Treat every figure as the most that could ever be true | What anyone will actually pay |
| 3 | **Registration with friction** — an email plus a real effort cost | That the problem is worth minutes | That it is worth money |
| 4 | **Refundable reservation or deposit** | That it is worth money *and* the effort of a payment method | That it is worth the full price |
| 5 | **Card authorization, never captured** | Genuine purchase intent, with no money moved, no tax event, no refund obligation and no chargeback exposure | Retention, or that the price is right |
| 6 | **Real purchase or pre-order** | Willingness to pay, fully | Nothing above it — this is the top of the ladder |

**Rungs 4 and 5 are the practical target for a product that does not exist yet.** Rung 5 in
particular buys most of rung 6's signal at a fraction of its liability.

> **Where stated and revealed willingness to pay disagree, revealed governs.**
>
> Recorded before the result, never chosen after it. Stated intent that no payment follows is the
> single most common way a validation test flatters a product, and the disagreement is not noise —
> it is the finding.

### Non-negotiable when a payment instrument is used for validation

**These are not tone preferences. A validation test that misleads its subjects has produced
contaminated data and a genuine harm, in that order of visibility and the reverse order of
importance.**

- **State that the product does not exist**, above the fold, in the subject's own reading path.
- **No delivery date**, and no implication that the build is certain.
- **Nobody is charged for something that is not built.** With an uncaptured authorization, say
  exactly that the hold is never captured and when it releases.
- **No manufactured urgency or scarcity.** There is nothing to be scarce, and inventing it corrupts
  the exact number the test exists to measure.
- **Say that a "no" is as useful as a "yes".** It is true, and it measurably raises response from
  people who assume they are being sold to.

---

## When the substitute is worse and there is no better one

**Say so, run it, and report both the result and the shortfall.** A substituted instrument that
cannot fully carry its claim is still worth running when the alternative is nothing — but the
weakness travels with the finding, into `state.validation[].confidence_effect` and into every
document that cites the result.

**What must not happen is the shortfall being recorded once and then dropped.** A finding that
arrives qualified and is cited unqualified three documents later has laundered itself, and nothing
in the chain looks wrong at any single step.

**And where no substitute measures the claim at all — as with willingness to pay from a public
corpus — the honest output is `blocked`, not a weak `pass`.** See `gates.yaml`
`validation_outcomes`: a test that could not run has produced no evidence about the product.

---

## Checklist

- [ ] The test records what it **measures**, independently of method, and its claim class
- [ ] The specified instrument is genuinely unavailable, not merely difficult
- [ ] The substitute measures the **same** claim class
- [ ] The equivalence argument was written **before** the instrument ran
- [ ] It names what the substitute measures well, worse, and not at all
- [ ] The threshold is carried across, or its equivalent is derived and the derivation shown
- [ ] Confidence moved down, and by how much is recorded
- [ ] Firsthand, secondary and vendor-originated evidence are counted separately
- [ ] Duplicates and reposts are removed before any count is stated
- [ ] Incidents and distinct reporters are both reported
- [ ] Business impact is coded from stated consequences, never inferred from tone
- [ ] The corpus's own selection is justified independently of the product hypothesis
- [ ] Every coded row keeps a retrievable source, a date and an author

---

> **Instrument Substitution Principle**
>
> A validation plan that only one kind of operator can execute has not been designed for the
> operators who exist.
>
> The substitution is legitimate when the equivalence is argued in advance and the shortfall
> travels with the finding. It is laundering when the method changes and the confidence does not.
