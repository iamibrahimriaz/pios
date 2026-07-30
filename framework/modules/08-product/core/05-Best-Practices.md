---
Title: Best Practices
Module: 08-product
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced practitioners do when specifying a product that inexperienced ones do not.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - Higher-quality specifications
Related Modules:
  - 09-technology
Tags:
  - Product
  - Best Practices
---

# Best Practices

---

# 1. Write the Job Walk Before Any Requirement

Number the steps of the core job first, then write requirements against the steps.

Requirements written first get mapped to steps afterwards, and the mapping always succeeds —
which is why it proves nothing.

---

# 2. Fill the Parent Column Before the Requirement Text

Literally: write the problem ID, then write the requirement.

Doing it in that order means the parent was chosen. Doing it the other way means the parent was
found, and something can always be found.

---

# 3. Derive the MUST List From Module 07, Not From Judgment

Copy the above-the-line capabilities across as MUST candidates and work from that list.

Deriving MUST by asking "how important is this?" reproduces module 07's decision from memory,
badly, and produces a larger list every time.

---

# 4. Keep a Ledger Open While Specifying

Every capability that comes to mind while writing goes into it immediately, with a reason.

Deciding what to do with an idea in the moment is how it becomes a MUST. Writing it in a
ledger costs ten seconds and defers the decision to a point where the whole list is visible.

---

# 5. Name the Divergence Point, Do Not Ask If It Is Clear

For each behavior description, finish the sentence: "two engineers could differ on…".

If the sentence completes, rewrite. If it genuinely cannot be completed, the requirement is
done. This converts an unanswerable question into a specific edit.

---

# 6. Write Behavior as Trigger, Input, Response, State, Feedback

Five slots. Fill all five.

Most underspecified requirements are missing the same two: what is now true afterwards, and
how the user knows it worked. Missing feedback is a real product defect, not a documentation
gap.

---

# 7. Write the Five Edge Categories as Empty Rows First

Create the table with all five rows before filling any of them.

Asking "what could go wrong?" returns the same two or three cases every time. An empty row
labeled *Permission* is uncomfortable to leave blank, which is the point.

---

# 8. Answer the Data-Loss Question Explicitly Every Time

Per requirement: what can be lost, and when.

"Nothing can be lost" is a strong and useful answer. The absence of the answer is the
problem — it means the question was not asked, and it is the question users judge products by.

---

# 9. Write Criteria in Given / When / Then, Without Exception

The form does the work. It is difficult to write "the flow is intuitive" inside it, because
the `then` clause demands something observable.

---

# 10. Run the Banned-Word Scan Mechanically

Search the document for: fast, performant, intuitive, easy, user-friendly, seamless, robust,
reliable, appropriate, sensible, smooth, clean.

Do not read for them — search. They are invisible on a read-through, because they are the
words specifications are normally written in.

---

# 11. Write One Criterion Per Failure State

If a requirement has five edge cases and four criteria, the criteria are testing success only.

Failure behavior that is specified but not verified is failure behavior that will not exist in
the built product.

---

# 12. Attach an Origin to Every Number as You Write It

Not afterwards. Next to the figure: standard, finding, or decision.

Retrofitting origins produces plausible attributions for numbers that were invented, and by
then the writer no longer remembers which were which.

---

# 13. Look Up Regulated Facts, Every Time

Required fields, retention periods, consent wording, coding systems, units.

Recollection is not a source. An invented regulated field reads as authoritative and is
directly actionable, which is the worst combination a specification can produce.

---

# 14. Run the Cut Diff as a List Comparison

Put module 07's above-the-line list beside the MUST list and compare them as lists.

Reading each addition and judging whether it is reasonable will pass every addition, because
each one is reasonable. That is the mechanism, not an accident.

---

# 15. Regress Loudly

When specification proves the approved cut cannot complete the core job, say so plainly and
surface it — even though this module has no checkpoint.

The operator approved a specific commitment of money and time. A cut that moved is theirs to
know about, and this is the only module positioned to tell them.

---

# 16. Write §1 Last

The three-sentence summary is only accurate once the requirements exist.

Written first, it becomes the thing the requirements are shaped to match.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Requirements before the job walk | Steps get mapped retrospectively; holes survive |
| Parent assigned after the requirement | Every requirement finds a parent |
| MUST derived from importance | Reproduces module 07's decision badly, always larger |
| Deciding about new ideas in the moment | They become MUSTs |
| "Is this clear?" as the review question | The author is the one person who cannot answer it |
| Happy path only | Half the product unspecified |
| Aspirational criteria | Cannot fail, so nothing is verified |
| Numbers without origins | Invented figures get built and tested |
| Regulated facts from memory | Authoritative and wrong |
| Judging additions individually | Every addition passes; the cut moves |
| Quietly widening scope instead of regressing | The operator's decision is overwritten |

---

# Self Assessment

- Did I walk the job before writing requirements?
- Did I write parents before requirement text?
- Did I derive MUST from module 07's list?
- Was the ledger open the whole time?
- Can I name a divergence point anywhere?
- Are all five behavior slots filled everywhere?
- Did I create the edge rows before filling them?
- Did I answer the data-loss question every time?
- Did I search for the banned words rather than read for them?
- Does every failure state have a criterion?
- Does every number have an origin written beside it?
- Did I look up every regulated fact?
- Did I diff the lists?

---

> **Practice Principle**
>
> Almost every practice here is mechanical.
>
> That is deliberate. Judgment is what put the scope back, made the
> number up, and passed the criterion that cannot fail.
