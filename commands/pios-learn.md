---
description: Turn this run's friction log into a framework improvement proposal and open a pull request against the Product Intelligence OS repository. Captures gates that could not be passed honestly, template sections that could not be filled, and checks that failed correct work. Strips every project detail before anything leaves the machine. Use `preview` to see what would be proposed without opening anything.
argument-hint: "[preview | apply | status]"
---

# PIOS — Contribute What This Run Taught

Read `state.friction_log` from a completed or in-progress run, turn it into a framework
defect proposal, and open a pull request.

Action: $ARGUMENTS (defaults to `preview`)

| Mode | Behavior |
| --- | --- |
| `preview` | Show the proposal that would be opened. Write nothing, push nothing. **Default.** |
| `apply` | Write the proposal, fork if needed, branch, commit, open a PR |
| `status` | Show this run's friction entries and which have already been contributed |

---

## Two rules that are not negotiable

### 1. Nothing is written to the framework

**You may not edit any file under `framework/`, either skill, or any validator — not on this
machine, not in a branch, not "temporarily to test it".**

A skill or framework that rewrites itself during a run makes every installation diverge,
conflicts on `git pull`, and quietly gives one operator a different method from everyone
else. `validate.py` fails the build on self-modification instructions, and that check exists
because this is the failure it is guarding against.

What you produce is **a proposal file and a pull request.** The maintainer merges, or does
not. Your local framework is unchanged either way.

If the operator asks you to "just fix it locally," say what this rule is and why, then offer
the PR instead.

### 2. Nothing about the project leaves the machine

**A run carries real market research, named customers, pricing and someone's unreleased
strategy. None of it is yours to publish.**

Before any text enters the proposal, it passes this filter. Remove, do not paraphrase:

| Never appears | Not even as |
| --- | --- |
| The product, project or company name | "a scheduling tool", if that is identifying |
| The market, sector or geography | "a regulated market in South Asia" |
| Any customer, competitor or person | "the incumbent", if there is one obvious one |
| Any figure — price, TAM, headcount, revenue | a rounded or approximate version |
| The idea itself, in any recognizable form | a "similar but different" example |

**Runs are identified as Run 1, Run 2 — nothing else about them is stated.**
[`proposals/2026-08-02-framework-design-review.md`](../proposals/2026-08-02-framework-design-review.md)
is the worked example: eight framework changes derived from 23 friction entries across two
completed runs, and no project, market, figure or customer is named anywhere in it.

**If a defect cannot be described without naming the project, it is not yet a framework
defect.** Say so and drop it — a defect that only makes sense with one particular run in
front of you is not a change anyone else can evaluate.

---

## What qualifies

Accept only what would affect **every** operator:

| Accept | Reject |
| --- | --- |
| A gate criterion that could not be passed honestly by a competent run | A gate you found annoying |
| A template section that could not be filled, and the reason | A section you did not want to fill |
| A validator check that fails correct work | A check that caught a real defect in your run |
| A criterion that is impossible to satisfy without damaging the artifact | A criterion that made your run slower |
| A controlled-vocabulary value with no way to record it | A value you would have preferred |
| A path, prerequisite or cross-reference that does not resolve | A typo — open a PR directly |

**A reject is never silently dropped.** Show it under a `## Not proposed` heading with the
reason, so the operator sees the whole log was read.

---

## Method

### 1. Locate the run and read its friction log

Resolve `<RUNS>` exactly as `/pios` does — plugin, in-repo, then `PIOS_HOME`. Read
`state.friction_log` from the run the operator named, or the only run present.

**An empty friction log is a valid result.** Say so and stop. Do not go looking through the
deliverables for something to complain about — friction is recorded during the run, at the
moment it is felt, and reconstructing it afterwards produces plausible fiction.

### 2. Classify each entry

For every entry, record:

- **What was being attempted** — the module and the criterion, by id
- **What made it impossible** — stated so a stranger could reproduce the situation
- **What the operator did instead** — the workaround, or that the run stopped
- **Which framework file owns it** — the module, the gate, the template, the check
- **Blast radius** — one file, one module, or the constitution

### 3. Apply both filters

Rule 2 first, then the qualification table. Report what each removed.

### 4. Write the proposal

One file at `proposals/<YYYY-MM-DD>-<short-slug>.md`, following the structure of the
existing proposal in that directory: a decision summary table first, then one section per
item, each carrying what it changes, why, blast radius, and a recommendation.

**State plainly that nothing in `framework/` has been changed.** The existing proposal opens
with exactly that line, and it is what makes the document safe to read.

### 5. Open the pull request

```bash
gh repo fork iamibrahimriaz/pios --clone=false --remote=false   # once, if needed
git checkout -b proposal/<short-slug>
git add proposals/<file>
git commit
gh pr create --repo iamibrahimriaz/pios --base main
```

**One proposal per PR.** The PR body is the decision summary table plus a link to the file.

**Only the maintainer merges.** You open the PR; you never push to `main`, and you never
merge your own.

### 6. Record what was contributed

Append the proposal path to `state.friction_log[].contributed` on each entry that went in, so
a later `/pios-learn` on the same run does not propose it twice.

This is the only write this command makes, and it is inside the run — never the framework.

---

## Before you finish

- [ ] No file under `framework/`, `skills/` or any validator was modified
- [ ] No project, market, customer, competitor, figure or recognizable idea appears
- [ ] Every rejected entry is listed with its reason
- [ ] The proposal states that nothing in `framework/` has been changed
- [ ] `python3 framework/engine/validate.py` still exits 0
- [ ] The operator has seen the complete proposal before the PR was opened

**Then tell the operator what to do next** — the PR link, or the one thing blocking it.
