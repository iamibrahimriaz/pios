---
Title: Best Practices
Module: 14-ai-systems
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced practitioners do when building on models that inexperienced ones do not.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - Higher-quality AI plans
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Best Practices
---

# Best Practices

---

# 1. Write the Simpler Alternative First, in the Same Row

Before describing the capability, describe the least clever thing that would mostly work.

Written afterwards, the alternative is shaped to lose. Written first, it sometimes wins — which is the
outcome the module exists to allow.

---

# 2. Read the Alternative Aloud as Its Advocate

One honest sentence in its favor.

If the sentence will not come, the alternative was decoration and the comparison established nothing.
This costs ten seconds and it is the module's only real safeguard.

---

# 3. Count the Records Before Claiming the Data

"4,100 records in «source», sampled «date»" rather than "we have historical data".

The difference between those two sentences is the difference between a plan and a hope, and it is
usually one query away.

---

# 4. Write the Day-One Behavior Beside the Steady-State Behavior

Two columns, always.

Cold start planned as an afterthought becomes a first impression nobody chose, at the moment the
product has the least credit with its users.

---

# 5. Ask Whether the User Can Tell, Before Choosing the Autonomy Level

Not after. The autonomy level is an output of that question.

Chosen first, it rises to whatever seems impressive and then acquires a justification.

---

# 6. Describe What a Wrong Output Looks Like

Literally write an example of the capability being wrong.

Doing that once usually settles the autonomy argument, because a plausible wrong example is far more
persuasive than a discussion about accuracy percentages.

---

# 7. Set the Bar in Writing Before Any Prototype Exists

A metric, a figure, a sample size.

Set afterwards, the bar becomes a description of what was achieved — and everyone involved will
sincerely believe it was the plan.

---

# 8. Ask What You Would Do at One Point Below the Bar

If the answer is "ship it and iterate", the bar is not a bar.

Finding that out today costs nothing. Finding it out at launch costs the evaluation's entire purpose.

---

# 9. Name the Reviewer, Not the Function

A person or a specific role with a stated qualification — not "the team will review quality".

In a domain product, the build team cannot assess correctness, and their confidence in an output is
evidence about its fluency only.

---

# 10. Build the Golden Set From Real Cases and Then Lock It

Real inputs, real edge cases, and a rule that it is never used for tuning.

A golden set that has been optimized against measures how well the capability was fitted to the golden
set.

---

# 11. Write the Per-Instance Guarantees, Then the Statistical Bar

Always dismissible. Always labeled. Always bounded. Always cited.

Those hold on every single output. An accuracy figure holds on average, and users experience instances
— so the guarantees carry more real safety than the number does.

---

# 12. Send the Per-Instance Guarantees Back to `08-product`

They are ordinary requirements and belong with the others, where they will be built and tested.

Left in an AI document, they are read once during planning and never during implementation.

---

# 13. Make the Failure Mode Name a Person and a Consequence

"A rushed clinician accepts an invented interaction" rather than "hallucination risk".

The specific version can be designed against. The generic version can only be acknowledged.

---

# 14. Distinguish Guardrails From Prompts, Explicitly

A guardrail is a constraint on output, a required citation, a confidence floor, a validation against a
real source, or a confirmation step.

A prompt is how the capability works. If the mitigation column contains prompt engineering, the failure
is unmitigated.

---

# 15. Ask Whether You Would Even Know

For each failure mode: would this show up anywhere?

"No" is a common answer, and it is the finding that produces the detection column — which is the column
that matters most.

---

# 16. Make the Fallback a Requirement With an Identifier

Not "we would fall back to manual entry" — a requirement number in `08-product`.

The provider will have an outage. That path either has an identifier and gets built, or it does not
exist.

---

# 17. Pin the Version and Write the Date Beside It

Every capability claim, limit and price.

Unpinned, the product's behavior changes without a deployment and the evaluation results expire without
anyone being told.

---

# 18. Compute the Share of Revenue on the First Page

Cost per operation, operations per user, revenue per user.

It is two multiplications and one division, and it occasionally ends the conversation — which is much
cheaper on the first page than in the second quarter.

---

# 19. Say How Many Capabilities You Dropped

In the document, as a number.

It is the clearest possible signal that the comparison was real, and a module that dropped nothing
should have to explain itself.

---

# 20. If Nothing Justifies a Model, Write That Sentence

"No AI capability is justified for this product, and here is the comparison that established it."

It is a complete, legitimate and often correct output. Leaving the section blank instead makes it look
like the question was never asked.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Alternative written after the capability | It is shaped to lose |
| Alternative never advocated | The comparison establishes nothing |
| "We have the data" | Untested until implementation week one |
| Cold start deferred | A first impression nobody chose |
| Autonomy chosen before detectability | It rises to whatever is impressive |
| Accuracy discussed instead of shown | A percentage persuades less than a wrong example |
| Bar set after a prototype | The result becomes the standard |
| No answer for one point below the bar | The bar is decorative |
| "The team will review quality" | Fluency assessed, correctness assumed |
| Golden set used for tuning | It measures fit to itself |
| Only a statistical bar | Nothing holds on the individual output |
| Guarantees left in the AI document | Never built |
| "Hallucination risk" as a failure mode | Acknowledged, not designed against |
| Prompt engineering as mitigation | The failure is unmitigated |
| Detection column left empty | Nobody ever learns it went wrong |
| Fallback without a requirement number | It does not exist |
| Unpinned model | Behavior changes with no deployment |
| Cost ratio computed late, or never | A margin problem found by an accountant |
| No dropped capabilities and no explanation | The comparison was decorative |
| Empty module instead of a stated conclusion | Reads as an omission |

---

# Self Assessment

- Did I write the alternative first?
- Could I advocate for it?
- How many records, and who counted them?
- What happens on day one?
- Did detectability decide the autonomy level?
- Did I write an example of the capability being wrong?
- Was the bar written before any prototype?
- What would I do one point below it?
- Is the reviewer named and qualified?
- Is the golden set locked?
- Are the per-instance guarantees in `08-product`?
- Does every failure mode name a person and a consequence?
- Is anything in my mitigation column just a prompt?
- Would I know when each failure happened?
- Does the fallback have a requirement number?
- Is the version pinned and dated?
- Did I compute the share of revenue?
- How many capabilities did I drop?

---

> **Practice Principle**
>
> Three practices here take under a minute: advocate for the simpler
> thing, write an example of the output being wrong, and divide the
> cost by revenue.
>
> Between them they resolve most arguments this module can have.
