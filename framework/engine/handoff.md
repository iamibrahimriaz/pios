# Handoff — getting the artifacts to whoever builds

The run does not end when `validate-run.py` exits 0. It ends when the artifacts are in the
hands of the person or agent who will build from them, in a form they will actually read.

**Without a defined step here, every run invents one.** The invented version is different
each time, and the most common improvisation — copying the specification documents into a
staging folder inside the run directory — creates two copies of the same file in one
repository with nothing keeping them in sync. The build then proceeds from whichever copy
was stale.

This step runs **after** the validator passes and **after** the delivery checkpoint. It
produces no new findings. It is packaging, and packaging is where a correct run still fails
to reach anyone.

---

## What a handoff is

Three things, and it is worth being precise about which is which.

| | What it is | Where it lives |
| --- | --- | --- |
| **The specification** | A subset of `deliverables/` | Copied into the build repository at `docs/` |
| **The entry file** | New. Tells an agent what to read and in what order | Written by this step |
| **The readme** | New. Orients a human arriving at the repository | Written by this step |

**Only the second and third are authored here.** The specification is copied, never
re-written for the developer — a spec paraphrased for readability is a second source of
truth, and the two disagree within a week.

---

## Which artifacts go, and which do not

Default: **the build subset**, not the whole set.

| Goes | Why |
| --- | --- |
| `03-PRD.md` | What is required |
| `04-Feature-Spec.md` | The MVP cut line, and what was deliberately cut |
| `05-Data-Model.md` | Schema and constraints |
| `06-API-Contract.md` | Interfaces |
| `07-Architecture.md` | The decisions and their reasons |
| `08-UX-Flows.md` | How it is used |
| `09-Roadmap.md` | Sequence and decision points |
| `12-Build-Handoff.md` | **The entry point.** Start here |
| `16-Engineering-Setup.md` | Setup, tests, CI, release |

| Stays | Why |
| --- | --- |
| `00-Executive-Summary.md` | Contains the build-or-not verdict. An operator conversation |
| `01-Research-Dossier.md`, `02-Problem-Validation.md` | Evidence, not instruction |
| `10-Risks-and-Assumptions.md` | Carries the case for stopping |
| `11-Success-Metrics.md`, `13-Growth-Plan.md`, `14-Operations-Plan.md` | Post-launch |

This is a default, not a rule. **A tech lead who asks for the whole set should get it** —
the split exists to keep a builder's context clear, not to withhold anything. State the
split to the operator rather than applying it silently.

> A developer given seventeen documents reads none of them. A developer given nine, with
> one marked "start here", reads that one.

---

## The entry file

Agentic build tools read a conventional file at the repository root — `CLAUDE.md`,
`AGENTS.md`, or whatever the operator's tool expects. **Ask which; do not guess**, and if
the operator has no preference, write `CLAUDE.md` and say so.

Its job is that a bare instruction — *"analyze this project and start developing"* — is
enough. If the operator has to remember a paragraph of context, the file has failed.

It carries, in this order:

1. **A standing instruction**, written to trigger on any phrasing of "start" or
   "continue": what to read, in what order, before writing code.
2. **How to check what already exists**, so a second session continues rather than restarts.
3. **The current milestone, and only that one**, with its end-to-end acceptance test.
4. **The order of work inside that milestone.**
5. **The non-negotiables**, each with the cost of breaking it. A rule whose reason is
   absent gets refactored away by someone who assumes it was arbitrary.
6. **The blocked list** — what the builder must ask about rather than decide.
7. **A progress file to maintain**, so the next session picks up cleanly.

**Point 5 is the one that decays.** Copy the constraint and its consequence together, or
the constraint travels alone and does not survive contact with a package that suggests
otherwise.

---

## Where it goes

**A separate repository from the run.** Not a subdirectory of it.

The run directory is private and gitignored; the build repository is the team's and is
committed. Keeping the specification inside the run couples the team's build to the
operator's research notes, and the team cannot clone what they cannot see.

Copy the specification subset directly from `deliverables/` at setup time. **Do not stage a
second copy inside the run directory** — that is the improvisation this step exists to
prevent.

---

## The snapshot rule

The build repository holds a **snapshot**, and that is deliberate: a specification that
shifts under a team mid-milestone is worse than one that is slightly out of date.

When a deliverable is genuinely revised — most often after a re-derivation, see
`gates.yaml` `late_answer_rederivation` — copy that one file across and **commit it there
with a message saying what moved and why.**

> The commit is the signal that something changed. A silent file replacement is not, and a
> team that discovers a moved requirement by reading it is a team that stopped trusting the
> document.

---

## What the operator still owes

The handoff names what the build cannot start or finish without, taken from
`12-Build-Handoff.md`'s blocked work: account access, a vendor quote, a legal opinion,
domain-language copy, a decision the run recorded as decision-dependent.

**Each with an owner and the point at which it bites** — "before the first paying customer"
is a different urgency from "before the first line of code", and a list that does not
distinguish them gets treated as uniformly ignorable.

---

## Checklist

- [ ] Validator exits 0, and the delivery checkpoint has been presented
- [ ] The operator has confirmed the target repository and the entry-file convention
- [ ] Build subset copied from `deliverables/` — no second copy staged inside the run
- [ ] Entry file written, and a bare "start developing" would be sufficient
- [ ] Non-negotiables carry their consequences, not just their rules
- [ ] Blocked work listed with owners and the moment each one bites
- [ ] Readme orients a human who has never seen the run
- [ ] The split — what went and what stayed — stated to the operator, not applied silently

---

> **Handoff Principle**
>
> A specification nobody reads is indistinguishable from one that was never written.
>
> The last step of a run is not producing the artifacts. It is putting them where the work
> happens, in the order the builder needs them, with the reasons attached to the rules.
