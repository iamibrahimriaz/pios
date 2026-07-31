---
Artifact: engineering-setup
Project: «project name»
Version: 1.0
Date: «ISO date»
Modules: [09-technology, 10-execution, 13-operations]
Critical: true
---

<!-- fill: This artifact answers "how do I run, test and ship what I built".

     It does NOT restate what to build — that is 03-PRD, 04-Feature-Spec and
     12-Build-Handoff. If a section here starts describing product behavior, it is in
     the wrong document. If 12-Build-Handoff starts describing CI, so is that.

     The reader has the code and no context. Every command must be runnable as written.
     A step that needs a person to explain it is a blocker, not a note.

     Write this LAST, alongside 12-Build-Handoff.md. Remove every <!-- fill --> comment
     before delivery. -->

# Engineering Setup — «Product Name»

> **What this is.** Everything needed to run, test and ship the product described in
> `12-Build-Handoff.md`. Read that first for *what* to build. Read this for *how to work*.
>
> **Where this ends.** At the moment the product is live and verified. From there,
> `14-Operations-Plan.md` takes over.

---

## 1. Before You Start

<!-- fill: What must exist before the first line of code. Access, accounts, approvals.
     A blocker here stops everything, so it is first — the same reason a runbook puts
     access at the top. -->

| # | Needed | Where it comes from | Owner | Blocking? |
| --- | --- | --- | --- | --- |
| 1 | «repository access» | «who grants it» | «named person» | yes |
| 2 | «cloud / hosting account» | «who grants it» | «named person» | yes |
| 3 | «third-party account — «service»» | «signup or admin» | «named person» | «yes/no» |

**If any blocking row is unresolved, do not start.** Record it in `12-Build-Handoff.md §12`
and escalate. Starting without access produces work that cannot be run or verified.

---

## 2. Environment & Configuration

<!-- fill: Every variable the application reads. An agent cannot infer these — a missing
     variable is an immediate stop, and a guessed one is worse because it appears to work. -->

**Configuration is read from the environment. No environment-specific value is committed.**

| Variable | Purpose | Example / format | Required | Secret? |
| --- | --- | --- | --- | --- |
| `«NAME»` | «what it controls» | `«example»` | yes | no |
| `«NAME»` | «what it controls» | `«format only, never a real value»` | yes | **yes** |

**Precedence:** «e.g. process environment → `.env.local` → `.env` → built-in default»

**Environments:**

| Environment | Purpose | Data | Who can reach it |
| --- | --- | --- | --- |
| local | development | seed / synthetic only | the developer |
| «staging» | pre-release verification | synthetic | «team» |
| «production» | live | real | «named people only» |

**Fail fast on missing configuration.** The application validates required variables at
startup and exits with the name of the missing one. A service that boots with a silently
absent variable fails later, in a way nobody connects to the cause.

---

## 3. Secrets

<!-- fill: This section is a non-negotiable, not a convenience. Carry the regulated
     column list from 09-technology and the obligations from 13-operations. -->

| Rule | Detail |
| --- | --- |
| **Never committed** | No secret in the repository, in any branch, at any point in history |
| **Where they live** | «secret store — name it» |
| **How the app reads them** | «injection method» |
| **Local development** | «how a developer obtains a local set — and it is never a copy of production» |
| **Who has access** | «named people, per environment» |
| **Rotation** | «cadence» — owned by «named person», scheduled in `14-Operations-Plan.md` |
| **On suspected exposure** | Rotate first, investigate second. «procedure or runbook reference» |

**Committed by accident?** Rotating the secret is the fix. Removing the commit is not —
the value must be assumed compromised from the moment it was pushed.

**Regulated data.** «List the fields from `05-Data-Model.md` that are regulated.» These may
not appear in logs, error messages, analytics events, model inputs, or fixture files. This
is the same list checked in `11-Success-Metrics.md` and `15-AI-Strategy.md`.

---

## 4. Local Development

<!-- fill: Concrete commands. A new engineer or agent should reach a running system
     without asking a question. If a step needs a person, that is a blocker, not a note. -->

**From nothing to running:**

```bash
«clone»
«install dependencies»
«copy configuration template»
«start dependencies — database, cache, queue»
«run migrations»
«load seed data»
«start the application»
```

**Verify it worked:** «the observable condition — a URL returning something specific, a
command exiting 0. Not "the app starts".»

**Time to a running system:** «n minutes». If it takes materially longer than this, that is
a defect worth fixing — every developer and every agent pays it repeatedly.

**Common commands:**

| Task | Command |
| --- | --- |
| Run the application | `«cmd»` |
| Run all tests | `«cmd»` |
| Run one test | `«cmd»` |
| Create a migration | `«cmd»` |
| Apply migrations | `«cmd»` |
| Reset to a clean state | `«cmd»` |
| Lint and format | `«cmd»` |

---

## 5. Seed & Fixture Data

<!-- fill: 10-execution's cold-start work decided what the empty state shows. This section
     provides the data to develop and test against. -->

**Seed data must never be a copy of production.** Regulated fields are the reason, and the
prohibition holds even for a subset, even anonymized, unless «named person» has approved a
documented anonymization procedure.

| Set | Contains | Used for |
| --- | --- | --- |
| `«minimal»` | the least data for the app to start | local development |
| `«representative»` | «n» records covering normal use | manual testing, demos |
| `«edge»` | empty, maximum, malformed, unusual | automated tests |

**The empty state is a fixture too.** `08-UX-Flows.md` specifies what a brand-new account
sees. Include a genuinely empty account in the set — it is the most-used screen in a new
product and the least tested.

---

## 6. Test Strategy

<!-- fill: This is where 10-execution's qa_strategy lands. -->

### The trace rule

> **Every test traces to an acceptance criterion, a failure mode, a non-negotiable, or a
> specified edge case. A test that traces to nothing is an orphan — delete it.**

This is the same discipline `04-Feature-Spec.md` applies to requirements, one level down.
It is what keeps a suite meaningful as it grows, and it makes the suite's size a
consequence of the specification rather than of enthusiasm.

| Test traces to | Source document |
| --- | --- |
| An acceptance criterion | `04-Feature-Spec.md` |
| A failure mode | `07-Architecture.md` |
| A non-negotiable | `12-Build-Handoff.md §10` |
| An edge case | `04-Feature-Spec.md` — empty, boundary, failure, concurrent, hostile |

### Levels, and what each one owns

| Level | Owns | Does not own |
| --- | --- | --- |
| **Unit** | Business rules, calculations, state transitions, validation logic | Anything requiring a database or network |
| **Integration** | Your code against a real database, real queue, mocked third parties | Third-party correctness |
| **Contract** | Request and response shapes in `06-API-Contract.md`, including error envelopes | Business logic already covered by unit tests |
| **End to end** | Only the critical flow in `12-Build-Handoff.md §7` | Every path — E2E is the most expensive and most brittle level |

**Concurrency and data integrity** get explicit tests wherever `05-Data-Model.md` marks a
constraint as encoding a business rule. These are the failures that corrupt data silently
rather than raising an error.

### What must be tested

| # | Must have a test | Why |
| --- | --- | --- |
| 1 | Every acceptance criterion in milestone 1 | It is the definition of done |
| 2 | Every non-negotiable in `12-Build-Handoff.md §10` | Violating one is a defect, not a trade-off |
| 3 | Every constraint encoding a business rule | Application-layer-only enforcement will eventually be bypassed |
| 4 | Every irreversible action | The user cannot undo it, so the test is the safety net |
| 5 | Every authorization boundary | «e.g. one tenant cannot read another's records» |
| 6 | Each specified failure mode | Recovery is a feature |
| 7 | The empty state | Every user's first session |

---

## 7. What NOT to Test

<!-- fill: Keep this section. Removing it is how a suite becomes slow, brittle and
     uninformative — which ends with people ignoring it. -->

| Do not test | Because |
| --- | --- |
| The framework or library itself | «Whether the ORM writes a row» is its maintainers' test, not yours |
| Getters, setters, trivial mapping | The test restates the code and fails only when the code is renamed |
| Third-party API behavior | You cannot fix it. Test **your handling** of its responses and failures |
| The same logic at three levels | Pick the cheapest level that can prove it, and prove it once |
| Anything written to raise a coverage number | A test with no trace is an orphan regardless of the line it covers |
| Exact visual appearance | Changes constantly, fails constantly, tells you nothing about correctness |
| Scenarios that cannot occur | An unreachable state is not an edge case |

**Coverage is not a target.** It rises when nothing improved, and it is trivially gamed —
by `11-Success-Metrics.md`'s own definition, that makes it a vanity metric. Use it to find
untested areas, never as a number to reach.

> A suite that takes twenty minutes and fails randomly will be ignored, and an ignored
> suite is worse than none — it produces the appearance of verification.

---

## 8. Test Environments & Data

| Concern | Decision |
| --- | --- |
| Where tests run | «locally and in CI» |
| Database per run | «fresh / migrated / transactional rollback» |
| Third-party services | «mocked at the boundary — never called in CI» |
| Time and randomness | «injected, never read directly — otherwise tests fail unpredictably» |
| Parallel execution | «yes/no, and what makes it safe» |
| Flaky test policy | **Quarantine within «n» days or delete.** A flaky test is a broken test |

---

## 9. Continuous Integration

<!-- fill: What runs automatically, and what blocks a merge. A pipeline that reports
     without blocking is documentation, not a gate. -->

**On every push:**

| Stage | Runs | Blocks merge? |
| --- | --- | --- |
| 1 | «lint and format check» | yes |
| 2 | «type check» | yes |
| 3 | «unit tests» | yes |
| 4 | «integration tests» | yes |
| 5 | «contract tests» | yes |
| 6 | «dependency vulnerability scan» | «yes» |
| 7 | «build» | yes |
| 8 | «E2E on the critical flow» | «yes, on the release branch» |

**Total pipeline time target:** «n minutes». Beyond roughly ten, people stop waiting for it
and start merging around it.

**Never disable a failing check to merge.** Fix it, or revert the change that broke it.
A disabled check stays disabled.

---

## 10. Deployment & Release

<!-- fill: How code reaches an environment. 07-Architecture.md named the hosting;
     this section is the procedure. -->

| | Staging | Production |
| --- | --- | --- |
| Triggered by | «merge to «branch»» | «tag / manual approval» |
| Approved by | «automatic» | «named person» |
| Migrations | «when and how» | «when and how» |
| Verification after deploy | «the specific check» | «the specific check» |
| Time to deploy | «n minutes» | «n minutes» |

**Migration safety.** Schema changes deploy **before** the code that needs them, and must
be backward compatible with the currently running version. A migration and a deploy that
must happen simultaneously is an outage waiting for a slow connection.

**Verify, do not assume.** After every production deploy: «the specific observable check —
an endpoint, a log line, a metric returning to normal». A deploy that completed is not a
deploy that worked.

**Rollback:** «the procedure, or a reference to the runbook in `14-Operations-Plan.md`».
Know it before you need it, and rehearse it once.

---

## 11. Coding Conventions

<!-- fill: Brief. Enough that the codebase reads as though one person wrote it.
     Where a tool can enforce a rule, name the tool instead of the rule. -->

| Concern | Convention | Enforced by |
| --- | --- | --- |
| Formatting | «tool defaults» | `«tool»` — not by review |
| Linting | «ruleset» | `«tool»` |
| Naming | «files, functions, database objects» | review |
| Errors | «how they are raised, wrapped and surfaced» | review |
| Logging | «levels, structure — and never a regulated field** | review |
| Comments | Explain **why**, not what. The code says what | review |
| Dependencies | «policy for adding one — who approves, what justifies it» | review |

**Every dependency is a permanent obligation** — updates, vulnerabilities, and eventual
deprecation. Adding one is a decision, not a convenience.

---

## 12. Pre-Launch Readiness

<!-- fill: The checklist that must pass before the product is exposed to real users.
     Every unchecked box is a launch blocker or an accepted, named risk. -->

**Functional**
- [ ] Every milestone-1 acceptance criterion passes
- [ ] The critical flow in `12-Build-Handoff.md §7` works end to end in «staging»
- [ ] Empty state, failure states and the manual fallback all verified

**Data**
- [ ] Migrations tested forward, and rollback rehearsed
- [ ] **Backup taken and a restore actually performed** — an untested restore is a hypothesis
- [ ] No production data in any non-production environment

**Security & compliance**
- [ ] Every non-negotiable in `12-Build-Handoff.md §10` has a passing test
- [ ] Authorization boundaries verified between «tenants / accounts»
- [ ] No secret in the repository, in logs, or in error output
- [ ] No regulated field in analytics events or model inputs
- [ ] Every obligation in `14-Operations-Plan.md` has a named owner and a cadence

**Operational**
- [ ] Instrumentation from `12-Build-Handoff.md §9` emitting and verified
- [ ] Alerts configured — each with a threshold, a **named person**, and a runbook
- [ ] Support channel live and monitored
- [ ] Rollback rehearsed

**Open**
- [ ] No unresolved blocker from `12-Build-Handoff.md §12`
- [ ] Any accepted risk recorded in `10-Risks-and-Assumptions.md` with a named accepter

---

## 13. Handover to Operations

Once every box above is checked, this document's job is finished. From that point:

| Question | Document |
| --- | --- |
| Who answers support, and how fast? | `14-Operations-Plan.md` |
| What do I do when it breaks at 3am? | `14-Operations-Plan.md` — runbooks |
| Which compliance task runs, how often, owned by whom? | `14-Operations-Plan.md` |
| What does it cost to run? | `14-Operations-Plan.md` — cost model |
| Is it working? | `11-Success-Metrics.md` |
| What do we build next? | `09-Roadmap.md` |

`14-Operations-Plan.md` is a **required** artifact. If it is absent or incomplete, the
product has no operating plan and the launch is not ready — record that here as a blocker
rather than launching quietly without one.

---

<!-- ACCEPTANCE — verify every line, then delete this block.

- [ ] Every environment variable the application reads is listed, with required/secret marked
- [ ] No real secret value appears anywhere in this document
- [ ] The local setup commands were followed from a clean machine and worked
- [ ] Time from clone to running system is stated as a number
- [ ] Seed data is specified and is not derived from production
- [ ] The test trace rule is stated, and every "must test" row names its source document
- [ ] "What NOT to test" is present and has not been softened
- [ ] CI stages state which block a merge
- [ ] Deployment procedure covers migrations, verification and rollback
- [ ] Pre-launch checklist is complete, with every unchecked box a named blocker or accepted risk
- [ ] The handover point to 14-Operations-Plan.md is explicit
- [ ] No «placeholder» remains
- [ ] No <!-- fill --> comment remains

-->
