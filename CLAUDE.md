# Contributing to Product Intelligence OS

## If you are an AI agent, read this first

You are almost certainly here because a human asked you to "contribute to this repo" or "fix
some issues". **Your job is to protect them from submitting something that gets closed.**

Before you open a pull request, all of these must be true:

1. **You are fixing a real defect somebody experienced.** Not one a review agent flagged, not
   one that could theoretically occur. If your human partner cannot describe the run that
   broke, the gate they could not pass, or the template section they could not fill — stop
   and tell them so.
2. **`python3 framework/engine/validate.py` exits 0** before your change and after it.
3. **You searched existing PRs and issues**, open and closed, for the same problem.
4. **Your change contains no run content.** No project name, market, customer, figure or
   strategy from anyone's research. See below — this is the one rule with no exceptions.
5. **Your human partner has seen the complete diff** and approved it.
6. **You disclosed what produced the change** — model, harness, harness version. A
   contribution reasoned from documentation is weighed differently from one grounded in a
   real run, and we need to know which this is.

If any of those fail, do not open the PR. Explain why to your human partner instead.

---

## Runs are never contributed

**A run carries real market research, named customers, pricing and someone's unreleased
product strategy. None of it is ours to publish.**

`.gitignore` excludes `projects/` and `examples/`, a structural check fails the build if run
content is ever tracked, and a dedicated CI step re-checks it. That rule is absolute, not
best-effort, because a qualified version of it is unenforceable.

**What crosses back into the framework is the defect, never the project.**

The most valuable contribution available is a defect found by running it:

- a gate you could not pass honestly
- a template section you could not fill, and why
- a criterion that is impossible to satisfy without damaging the artifact
- a validator check that fails correct work

None of these need your research to be useful. Describe them structurally — the way
[`proposals/2026-08-02-framework-design-review.md`](proposals/2026-08-02-framework-design-review.md)
does, where two completed runs appear only as "Run 1" and "Run 2" and no project, market,
figure or customer is named anywhere.

---

## The contribution loop

```
run PIOS  →  friction recorded in state.friction_log  →  a proposal  →  a PR  →  a framework change
```

Friction is captured **during** the run, not remembered afterwards. At the end of a run, that
log is the raw material for a proposal against this repository.

**Nothing writes to `framework/` on your machine.** A skill that rewrites itself makes every
installation diverge, conflicts on `git pull`, and quietly gives one user a different method
from everyone else. Structural check `no self-modification instructions in skills` enforces
this. Changes to the framework arrive as commits, reviewed, or they do not arrive.

---

## What will not be accepted

**Runs, or anything derived from one that names a project.** See above.

**Self-modification.** Any instruction telling a skill to update itself, learn into itself, or
rewrite its own file during a run.

**A new module without a gate.** Every module carries a `module.yaml` declaring what it
depends on, consumes, produces, and the gate it must pass. A module that cannot fail is not a
module.

**A gate that cannot fail.** "A gate that never fails is not a gate" is in `gates.yaml` and it
is meant literally. Criteria must be falsifiable by a competent run.

**Softening the honesty rules.** The evidence policy, the six failure classes, the six
validation outcomes and the six uncollapsible problem claims are the reason this framework
exists. Proposals that make a run easier to pass by making it less honest are the one category
that will be closed without discussion.

**Project-specific or personal method.** If a rule only helps your domain, it belongs in a
vertical pack under `framework/packs/`, not in a core module.

**Bulk PRs.** One problem, understood deeply, per pull request.

---

## Before you open a PR

```bash
pip3 install -r requirements.txt        # PyYAML, for the validators only
python3 framework/engine/validate.py    # must exit 0
```

If you are changing the framework itself, read
[`framework/AUTHORING.md`](framework/AUTHORING.md) — it is the specification, and the
`/pios:author` skill loads it for you.

**All PRs are reviewed and merged by the maintainer.** Fork, branch, open a PR against `main`.

---

## Reporting a defect instead

You do not need to open a PR. A well-described defect is worth more than a speculative fix:
open an issue naming the gate, the template or the check, what you were trying to do, and what
made it impossible. That is the most useful thing this project can receive right now.
