---
Title: Usability
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Test whether someone can complete the task unaided, and keep it distinct from wanting to.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/validation/Prototype.md
Outputs:
  - Usability method within validation_plan
Related Modules:
  - 10-execution
Tags:
  - Problem
  - Usability
  - Method
---

# Usability

---

# What It Is

Observation of a real person attempting a real task, unaided, with the observer silent.

It answers exactly one question: **can they do it without help?** That question is separate from whether they
want to, whether they would pay, and whether they would return — and conflating them is the error this file
exists to prevent.

| Usability testing answers | It does not answer |
| --- | --- |
| Where they stop, hesitate, or go the wrong way | Whether the problem is real |
| What they expected to happen | Whether they would adopt it |
| Which words they did not understand | Whether it is worth the switching cost |
| Whether the task completes at all | How it performs at scale or under interruption |

---

# When It Applies

In Stage 6 where the load-bearing belief concerns comprehension or completion — typically alongside a prototype.
Its findings become flow constraints in `10-execution` and requirements in `08-product`.

---

# How to Apply It Here

**Give a task, not a tour.** "Record what this patient told you and finish the note" is a task. "Have a look
around and tell me what you think" produces opinions about the interface, which are the least useful output
available.

**Stay silent, including when it is uncomfortable.** The pause before someone finds the button is the finding.
Filling it destroys the measurement, and the instinct to fill it is strong.

**Record where they stopped, not what they said afterward.** Post-hoc explanations are rationalizations —
people construct a reason for behavior they cannot introspect. The hesitation is the data.

**Test under the real conditions where possible.** `03-user`'s environment findings apply: one hand, gloves,
noise, someone waiting. A task that completes at a quiet desk and fails in a clinic has passed the wrong test.

**Five people is usually enough for this question.** Comprehension failures repeat quickly. This is the one
method where a small sample is genuinely sufficient — and it is why the sample size cannot be borrowed to
answer incidence questions.

---

# Where It Misleads

**Usability findings get mistaken for validation of the idea.** A person can complete every task fluently and
have no use for the product. Ease of use is necessary and nowhere near sufficient, and a smooth session is
seductive evidence of nothing.

**A poor result is read as a rejected concept.** Almost always it is a rejected interface. The two need
separating explicitly, because interfaces are cheap to change and concepts are not.

**Participants try to succeed.** They are being watched and want to do well, which makes them more persistent
than a real user on a bad day. Real-world abandonment is always higher than observed abandonment.

**Testing your own design suppresses the finding.** The designer knows where the button is, explains
instinctively, and interprets charitably. Where possible, have someone else run it; where not, write the tasks
in advance and read them verbatim.

**It gets scheduled after the requirements are frozen**, at which point it can only produce a list of things
nobody will change. Its value is highest while `08-product` is still open.

---

# Related

| | |
| --- | --- |
| `Prototype.md` | The artifact usually being tested |
| `Feedback.md` | Opinions, and what they are worth |
| `03-user` | The conditions the test should reproduce |
| `10-execution` | Where findings become flows |

---

> **Concept Note**
>
> One task, no help, silence.
>
> The pause before they find it is the entire finding — and everything
> they say afterward is a story about the pause.
