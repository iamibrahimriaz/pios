# «product name» — «jurisdiction»

<!-- fill: This file is written to the RUN ROOT, named by whatever convention the operator's
     tool expects — CLAUDE.md, AGENTS.md, or another. Ask; do not guess. CLAUDE.md if they
     have no preference.

     The test this file has to pass: an operator opens the folder, types "analyze this project
     and start developing", and that is enough. If they have to remember a paragraph of
     context first, the file has failed and no amount of detail inside it compensates. -->

**Read this file completely before doing anything else in this folder.**

Whenever you are asked to *start*, *continue*, *build the next thing*, *analyze this project*,
*set it up*, *pick up where we left off*, or anything that means the same — however it is
phrased — **this file is the answer to "what do I do?".** Follow it before acting on any other
instruction in this folder.

---

## 0. STOP — the current state of this project

<!-- fill: Only present when something blocks the build. When it does, it goes FIRST and it is
     unambiguous. An agent that reads three sections of context before learning the gate is
     closed has already started planning the work.

     If nothing blocks the build, replace this whole section with a one-line statement that
     the build is authorized and which milestone is current. Never leave the reader to infer
     which situation they are in. -->

> **«what may not be done, in one sentence — e.g. no application code is to be written»**
>
> «why: which gate has not passed, and what would close it»
>
> **«any second, independent blocker — e.g. a decision that is a one-way door»**

**«what may be done today», and nothing else:**

1. «the permitted work»
2. «the permitted work»

---

## 1. What this is

«two or three sentences: who it is for and what it does»

1. «capability»
2. «capability»
3. «capability»

**What this is not: «the adjacent thing it will be mistaken for».** «why — the finding that
rules it out»

**Everything else in this folder follows from that.** «the trade-off that decides arguments —
e.g. where a feature would make the product more capable and X slower, the feature loses»

**Research verdict: «verdict». Confidence: «level».**

---

## 2. What is in this folder

<!-- fill: every directory, explained. A run directory contains research the builder does not
     need on day one, and an unexplained folder gets either ignored or read at the wrong
     moment. -->

| Path | What it is | How to treat it |
| --- | --- | --- |
| `phases/README.md` | **The board.** Every phase, its status, and which one is current | **Start here.** Work only the current phase |
| `phases/phase-NN-*.md` | One document per milestone — scope, what is excluded, definition of done, acceptance test | Read the current one. Ignore the rest until it closes |
| `deliverables/` | **The specification**, in five folders — «n» artifacts | **The source of truth.** Read; never edit — see §8 |
| `deliverables/00-decision/` | The recommendation and what it rests on | Read once, before forming an opinion about scope |
| `deliverables/01-research/` | The evidence base and its limits | **Not needed on day one.** Go here to check *why* |
| `deliverables/02-product/` | What the product is, who for, how it wins | Reference while building |
| `deliverables/03-technical/` | Data model, API contract, architecture | **Working reference.** Open constantly |
| `deliverables/04-delivery/` | Build handoff, engineering setup, roadmap, operations | **Read the handoff and the setup in full** — see §3 |
| `research/` | The module working documents behind the specification | **Not needed on day one.** Go here only to check *why* a decision was made |
| `state.yaml` | The run's audit trail — evidence, assumptions, gates, decisions, corrections | **Read-only.** It is what makes the output auditable |
| `DECISION.md` | The one-page verdict, for whoever decides | Reference |
| `proposal/proposal.html` | The funding proposal, for whoever approves this | Reference |
| `presentation/engineering-kickoff.pptx` | The engineering kickoff deck, with speaker notes | Reference |
| `milestone-zero/` | «the validation package, or delete this row if the run committed to none» | «execute before any build phase, or n/a» |
| `PROGRESS.md` | The working log of what has actually been done | **Create it and maintain it** — see §8 |
| «code directories, or a note that none exist yet» | «» | «» |

---

## 3. Read this first, in this order

**Do not skim these. The first two are the instruction; the rest are reference.**

| # | File | Why |
| --- | --- | --- |
| 1 | `deliverables/04-delivery/12-Build-Handoff.md` | **In full.** Self-contained: what to build, in what order, what "correct" means, and what is blocked |
| 2 | `deliverables/04-delivery/16-Engineering-Setup.md` | How to set the repository up, every environment variable, the test suites, what CI blocks a merge |
| 3 | `deliverables/01-research/10-Risks-and-Assumptions.md` | **Why this product might not exist.** Read it before forming an opinion about scope |
| 4 | `phases/README.md`, then the phase marked current | What you may start, and what is deliberately not in it |

**Reference, consulted when the question arises — not read end to end:**

| Question | File |
| --- | --- |
| «question» | «file» |

**Research, behind the specification rather than instruction in it** — «which files, and when
to go there».

---

## 4. Before you do anything, check what already exists

**A second session continues; it does not restart.** In this folder:

```
ls -la                    # has any code directory appeared?
cat PROGRESS.md           # what was done, and what was left mid-flight
«a command that shows whether the build has started»
git log --oneline -20     # only if this folder has been made a git repository
```

**If `PROGRESS.md` does not exist, nothing has been built.** Create it (§8) before your first
action, so the next session can see what you did.

---

## 5. The current phase — «phase-NN, milestone id», and only that one

<!-- fill: ONE phase. Listing the whole roadmap here invites an agent to work ahead, and
     working ahead is how a milestone's gate gets skipped.

     NAME IT AND POINT AT IT. Do not restate its scope, its definition of done or its
     acceptance test — those are in `phases/phase-NN-«slug».md`, which was itself copied from
     the roadmap. Restating them here creates a third copy, and the three disagree within a
     week. The one open on the agent's screen wins, and that is this file. -->

**Current phase:** «phase-NN — «name»», specified in `phases/phase-NN-«slug».md`

**Read that document before starting.** It carries the scope, what is deliberately excluded,
the definition of done copied from the roadmap, and the end-to-end acceptance test.

**When it closes:** mark it done in `phases/README.md`, move `current` to the next phase, and
stop. **Do not begin the next phase in the same session** — the board is what tells the next
session where work actually stands.

### «kill criterion or stop conditions, if the milestone has any»

«verbatim from the roadmap»

### What "start building" means today

<!-- fill: only when the build is blocked. Give the agent the exact words to say, so a
     refusal is informative rather than obstructive. -->

If you are asked to start building, say this and stop:

> «the refusal, plus the two things you can do instead»

---

## 6. The order of work

**«risk order, dependency order, or whatever the roadmap states — and why»**

1. «step»
2. «step»

«the one ordering decision that looks wrong and is not, with its reason»

**Set the repository up from `deliverables/04-delivery/16-Engineering-Setup.md`, not from memory
or habit.**

---

## 7. Non-negotiables, each with the cost of breaking it

**Copy the reason wherever you copy the rule.** A constraint that travels without its
consequence gets refactored away by someone who assumes it was arbitrary.

| # | Rule | What breaks if you break it |
| --- | --- | --- |
| 1 | «rule» | «consequence, and where it is enforced» |

---

## 8. Rules for you, the agent working here

**Maintain `PROGRESS.md` at this folder's root.** Create it if it is absent. It carries: the
current milestone and what gates it, what has been done, what is in flight, what is blocked and
on whom, and any specification defect found. **Point at files; do not duplicate their content.**

**Never edit anything in `deliverables/`, and never edit `state.yaml`.** They are the record of
what the research established and believed, and editing them in place destroys the only thing
that makes this output auditable. **If a deliverable is wrong, say so in `PROGRESS.md` and raise
it** — do not correct it.

**Never invent a value the specification does not carry.** Every version, variable name, suite
name, endpoint and constraint comes from an artifact. If something genuinely is not specified,
record it as a gap and ask — do not choose silently and leave the choice invisible.

**Ask about the blocked list; do not decide it.** §9.

**Nothing outside this folder is needed.** This folder is self-contained and every path named
here resolves from its root. It works in place, copied to another machine, or with `git init`
run inside it.

---

## 9. Blocked work — ask, do not decide

<!-- fill: from 12-Build-Handoff.md's blocked work. Each with an owner and the point at which
     it bites. "Before the first paying customer" is a different urgency from "before the first
     line of code", and a list that does not distinguish them is treated as uniformly
     ignorable. -->

| Blocked | Waiting on | Owner |
| --- | --- | --- |
| «what» | «what, and when it bites» | «who» |

---

## 10. If your tool expects a different entry filename

This file is `«filename»`. If the tool you are using looks for another convention, **copy this
file to that name rather than writing a second one.** Two entry files disagree within a week,
and the build proceeds from whichever went stale.

<!-- ACCEPTANCE — remove before delivery.

  [ ] A bare "analyze this project and start developing" would be sufficient
  [ ] The standing instruction triggers on any phrasing, not one exact sentence
  [ ] Every path named resolves from the run root — CHECKED, not assumed
  [ ] Nothing points outside the run directory
  [ ] Reading order stated: instruction, reference, research
  [ ] Every directory in the folder is explained
  [ ] How to check what already exists is present
  [ ] The current milestone only, with its end-to-end acceptance test
  [ ] Non-negotiables carry their consequences
  [ ] Blocked work has owners and the moment each bites
  [ ] The specification and audit trail are marked not-to-be-edited-in-place, with the reason
  [ ] Where the verdict blocks the build, that is the first thing the file says
-->
