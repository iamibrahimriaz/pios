# Producing the Decision Report

**One page, written for the person who decides in five minutes.** Template:
`deliverables/templates/20-Decision-Report.md`. Output: `projects/<slug>/DECISION.md`, at the
run root.

---

## Why this exists

The proposal is the right document for an approval meeting and **the wrong one for the first
thirty seconds.** A founder opens the folder, reads something, and decides whether to open
anything larger. Without a page written for that moment, they make the decision from the
executive summary's opening paragraph — **which was written to introduce a document, not to be
the whole answer.**

**This artifact came from operator feedback on a completed run**, where it had to be requested
by hand after delivery. It is required now because the request was predictable and the run
should not have needed asking.

---

## The one hard constraint

**One page. Everything else is negotiable and this is not.**

When it will not fit — and it will not, the first time — **cut content, never sections and
never qualifiers.** A recommendation stripped of its condition is a different recommendation.
A confidence level with its basis removed is a mood.

**What to cut, in order:** the second and third rows of every table · the "what could still go
wrong" prose down to two bullets · the open-questions section entirely, if none are
operator-owned · adjectives.

**What never gets cut:** the recommendation's qualifiers · the confidence level · the condition
attached to a conditional recommendation · the owner column.

---

## Derived, never re-researched

**Every figure on this page already exists in `deliverables/`.** Nothing is computed here,
nothing is estimated, and no deliverable is edited to match this page.

**If the page needs a number the artifact set does not carry, write that it is not
established.** That sentence is a finding. A number invented at the last step, on the page most
likely to be quoted, is the worst possible place for the framework's evidence discipline to
fail.

---

## The recommendation is copied, not restated

**Word for word from `00-Executive-Summary.md`.** Not paraphrased, not tightened, not made more
decisive because a one-pager feels like it wants a punchier verdict.

> **This is the failure mode the artifact set exists to prevent, arriving through the back
> door.** Two documents stating the verdict differently is bad in any pair. It is worse here,
> because this is the page that gets forwarded, quoted and remembered — so a softened line here
> becomes the run's verdict regardless of what the other sixteen documents say.

`final_gate` checks the two match.

---

## Write it last, and write it in this order

1. **Copy the recommendation** from the executive summary. Do not edit it.
2. **Confidence, and one clause on why not higher.** Take the basis from
   `state.run.confidence_basis`.
3. **The load-bearing assumptions** — only the ones that decide the outcome. `state.assumptions`
   with `load_bearing: true`, and no others. Three to five.
4. **What could still go wrong** — two or three sentences a person would actually say. Not the
   risk register reformatted.
5. **Next actions with owners.** An action with no owner is not an action; write `NOT ASSIGNED`
   rather than leaving it blank, because a blank reads as an oversight and `NOT ASSIGNED` reads
   as the finding it is.
6. **Operator-owned open questions**, or delete the section.
7. **Read it once as the founder.** If acting on this page alone would mislead them, it is
   wrong — and the fix is a missing qualifier, not more content.

---

## The test

> **A reader who reads only this page, and acts on it, has not been misled.**

Not "has been fully informed" — that is what the other seventeen documents are for, and a page
that tries for it stops being one page. **Not misled is the bar**, and it is a higher one than
it sounds, because it forbids every convenient omission.

---

> **Decision Report Principle**
>
> The shortest document is the one most likely to be believed.
>
> Write it with the same discipline as the longest, and copy the verdict rather than
> restating it.
