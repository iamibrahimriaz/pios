# Changelog

All notable changes to Product Intelligence OS are recorded here.

This project uses [semantic versioning](https://semver.org). For a framework rather than a
program, the versions mean:

| Bump | Means |
| --- | --- |
| **major** | A completed run written against the previous version would no longer validate |
| **minor** | New modules, gates, artifacts or checks. Existing runs stay valid |
| **patch** | Corrections, clarifications, documentation |

**`state.version` records the schema era a run was written against.** Checks introduced after
a run was produced are reported as out of scope for it rather than failing it. A run is a
historical record; a validator that grew later must not be able to fail one retroactively.

---

## Releasing

**An installed plugin is cached by version, not by commit.** `claude plugin install` unpacks
the repository into `~/.claude/plugins/cache/pios/pios/<version>/` and reads from there. So a
`git push` alone reaches nobody: the cache key did not change, and every existing install keeps
serving the files it already has.

**That makes the version bump the release, and pushing merely the delivery.** Ship a framework
change without bumping and installs silently continue on the old method — the worst kind of
failure here, because the operator gets a complete, confident run produced by a version you
believed you had replaced.

**And the bump is mandatory, not good practice.** `claude plugin update` compares version
numbers and nothing else: run it against an unchanged version and it prints *"already at the
latest version"* and refreshes no files, even after `claude plugin marketplace update` has
pulled the new commit. This was found the hard way — a README rewrite and this very section
were pushed, CI went green, and the installed plugin kept serving the previous README until
the version moved.

**There is no way to force a refresh without a bump** short of uninstalling and reinstalling.
Treat every push that changes what an operator reads or what an agent executes as a release.

### The ritual

```bash
# 1. The framework must be sound before the version claims anything about it.
python3 framework/engine/validate.py            # must exit 0

# 2. Bump all four manifests to the same version. They are checked, not trusted —
#    `install manifests agree on one version` fails if you miss one.
#      .claude-plugin/plugin.json       version
#      .claude-plugin/marketplace.json  plugins[0].version
#      package.json                     version
#      gemini-extension.json            version

# 3. Move the Unreleased section under the new number, with today's date.
#    Write what changed for an operator, not what changed in the diff.

python3 framework/engine/validate.py            # again, after the bump

# 4. Commit, tag, push. The tag and the manifests must agree.
git commit -am "Release vX.Y.Z: <one line>"
git tag -a vX.Y.Z -m "vX.Y.Z"
git push && git push --tags
gh release create vX.Y.Z --notes-from-tag
```

### Verifying the release actually shipped

**Do this from a directory that is not the repository.** A release that only works where you
built it is not a release.

```bash
claude plugin marketplace update pios     # refresh the clone
claude plugin update pios@pios            # move to the new version
claude plugin list                        # must print the NEW version, not the old one
```

If `claude plugin list` still shows the old number, the bump did not land in all four
manifests — or did not reach the remote. It is not a caching problem to wait out.

Then confirm the framework travelled with it, which is the failure that looks like success:

```bash
P=~/.claude/plugins/cache/pios/pios/<version>
find "$P/framework" -type f | wc -l       # expect the full framework, not a handful
ls "$P/skills"                            # author · research
```

**A version bump with no framework change is still a release**, and is the right move whenever
a skill, template or check changes — those are the method too.

---

## [0.3.0] — 2026-09-09

Ten defects found by auditing one completed run against the framework that produced it. Nine
are fixed here. **Every new check is gated on the version a run was written against, so a run
produced under 0.2.x is not failed by any rule added in this release.**

### Added

- **`23-Interface-Requirements.md`, a conditional artifact fed by `08-product`.** The delivery
  surface has been asked at `01-idea` since 0.1.0 and, until now, consumed by nothing. A run
  could answer "web" at the first gate and hand a builder a specification with no layout
  behavior, no interaction states beyond the happy path, no accessibility target, no
  performance budget and no supported-client policy — and pass all fourteen gates on the way,
  because no gate criterion mentioned any of them.

  **A product with no rendered interface passes the new criterion on one sentence** naming the
  surface and saying no view exists. That is a pass, not a gap, and the template says so.

  The accompanying method draws the boundary the constitution draws: **a conformance target is
  a requirement; a pipeline scan is verification** and belongs to whoever receives the package.

- **A downstream-invalidation check.** Modules completed before a strategy change were silently
  stale. Runs now record when each module completed, and a run does not pass while a module's
  outputs predate the chosen approach they were supposed to serve.

- **A second search vocabulary, required at `02-market`.** A run could record that a category
  has no established name and then search it with one set of words — which is the situation
  where a single vocabulary is least trustworthy.

- **A source-contradiction question in the adversarial review pass.** Nothing previously asked
  whether a cited source contradicts the conclusion drawn from it.

- **A data-subject row in `01-idea`'s context table**, for a person whose data the product uses
  but who is neither the user nor the buyer. A product built on other people's data recorded
  them nowhere.

- **Corroboration for single-read external figures.** A load-bearing number could rest on one
  read of one page. Three misreads occurred in a single run; one was caught only because a
  monthly price exceeded the annual one.

- **`recorded_before: execution` on a substituted instrument's equivalence argument.** The rule
  that the argument comes first was unenforceable after the fact.

- **A structural check that `state-schema.yaml` and `manifest.yaml` agree on the version.**
  They had drifted, with nothing watching.

### Changed

- **`AGENTS.md` gains a re-entry subsection and a `state.yaml` editing procedure.** The state
  file is large, single, and has no structural protection against a bad edit anchor; one such
  edit removed roughly 1,950 lines. The procedure is to back up, anchor on a line that is
  unique, and parse before writing.

### Known limitations

- **`01-idea` records `verdict: fail` on every correct first run.** It grades itself before the
  operator has answered the questions only they can answer. Nothing downstream is harmed, but
  the first line of every project's history reads as a failure that did not occur. The fix
  touches either gate vocabulary or gate evaluation order and is deferred rather than rushed.

---

## [0.2.1] — 2026-09-08

Documentation only. No module, gate, template or check changed, so a run written against
0.2.0 is unaffected.

### Added

- **A tagline: "Research that can say no."** Every tool in this space will write you a
  specification. The one that will also tell you not to build is the thing worth leading with,
  and it claims a behavior that can be checked in the code rather than an outcome that cannot.

- **A "Who this is for" section**, between what-it-is and Install, so the decision happens
  before the two commands rather than after the first checkpoint. Someone who cannot yet name
  their buyer or jurisdiction will hit module 01 and conclude the tool is broken, when the
  refusal to guess is the design.

- **`reference-run/`** — the home for one published run on an invented operator in a real
  market, so a reader can see the output before spending hours producing their own. The run
  itself is not produced yet and the directory says so. Its README carries the rules,
  including the one that has to be decided in advance: the verdict published is whatever the
  run reached, `do not build` included.

- **A CI step that lints any reference run** with `validate-run.py`, skipping cleanly while
  none exists. A reference run that would not pass as a delivered run cannot sit in the
  repository teaching otherwise.

### Changed

- **The privacy paragraph now separates the two cases it was collapsing.** Your runs are never
  published; a synthetic reference run is published deliberately and has no owner to protect.
  `projects/` and `examples/` stay gitignored with the structural check and the CI step intact.

### Fixed

- **CONTRIBUTING claimed a branch protection rule that was not enforced** — "no direct pushes,
  review required... nothing bypasses that." Protection cannot be enabled on a private
  repository on a free plan, and the 0.2.0 release went straight to `main`. The repository is
  public now and protection is on: the validator must pass before a pull request merges, force
  pushes and branch deletion are refused. The maintainer keeps direct push for releases, and
  the paragraph now says so rather than describing a stricter rule nobody was held to.

---

## [0.2.0] — 2026-09-08

### Changed

- **The commands lost their stutter.** A plugin already namespaces everything it ships, so
  prefixing each skill and command with `pios-` applied the name twice and the palette read
  `/pios:pios`, `/pios:pios-author`, `/pios:pios-learn`. The prefix is gone:

  | Was | Now |
  | --- | --- |
  | `/pios:pios` | `/pios:research` |
  | `/pios:pios-author` | `/pios:author` |
  | `/pios:pios-learn` | `/pios:learn` |

  **This renames the commands you type.** The old names no longer resolve. Nothing about a
  run changes — `state.yaml`, the artifact set and the gates are untouched, and a run written
  against 0.1.x still validates — so this is a minor bump under the scheme above, not a major
  one. Update any notes, aliases or scripts that invoke the old names.

- **The main skill is `research`, not `run`.** Claude Code ships a built-in skill named `run`.
  Namespaced as `/pios:run` there would have been no conflict, but the global install
  (`scripts/install-skill.sh`) symlinks the skill unnamespaced into `~/.claude/skills/`, where
  it would have collided. `research` also says what the skill does.

- **The global install now links to `~/.claude/skills/research`.** Re-run
  `./scripts/install-skill.sh` after updating, then remove the stale `~/.claude/skills/pios`
  symlink by hand — the installer creates the new link but will not delete the old one.

- **The command name now differs by install mode**, which USAGE.md did not previously have to
  say. As a plugin it is `/pios:research`; installed globally or run from inside the repository
  it is a plain `/research`. Same file, same behaviour, different prefix.

### Fixed

- **The documented output tree did not match the one a run produces.** README omitted the
  `deliverables/` level entirely and USAGE showed the artifacts as a flat list, so neither
  matched `manifest.yaml`, which groups them into `00-decision/` · `01-research/` ·
  `02-product/` · `03-technical/` · `04-delivery/`. The worst of it was a copy-paste line in
  the README — `Read pios/<slug>/12-Build-Handoff.md` — that pointed at a path no run ever
  creates. Both trees now match the manifest, and both say that filenames keep their global
  numbering wherever they sit.

- **`cp .../deliverables/*.md` cannot copy a tree of five folders.** USAGE's "moving the output
  into your build" step now uses `cp -R`, and the agent prompt that follows it points at
  `04-delivery/12-Build-Handoff.md` rather than a flat filename.

- **Two stale counts in USAGE**: 611 markdown files (it is 623) and 22 structural checks (it is
  40). README and CONTRIBUTING already had both right, which is how they were caught.

- **A CI comment referred to "Check 22 above"** by position in a list that has since grown. It
  now names the check instead.

---

## [0.1.1] — 2026-08-27

### Changed

- **README rewritten around what PIOS does.** It opened with Vision, Mission and Philosophy
  and did not reach an install command until line 246 of 593. Now: what it is, install, how
  to use it, what you get, how it works, then the rules it refuses to break. The output tree
  moved near the top, because the folder of documents is the product. 593 lines to 310.
- **The release ritual is documented above**, including the finding that forced this release:
  a plugin is cached by version, and `claude plugin update` without a bump refreshes nothing.

### Fixed

- **Prerequisites now resolve with the strictest filesystem's case rules.** Four paths in
  `01-idea` named `01-Idea/README.md`; macOS and Windows resolve that against `01-idea`,
  Linux does not. Every local check passed and CI failed on the first push. `exists_exact()`
  walks each path component against the real directory listing, so the author finds their own
  defect instead of the Ubuntu runner finding it.
- Structural check count corrected from 41 to 40 in the README and CONTRIBUTING.
- Removed `npx pios-framework init` from the install docs — `package.json` declares no `bin`,
  so the command did not exist.

---

## [0.1.0] — 2026-08-27

Initial packaging. The framework is complete and structurally validated; **no claim about
outcomes has been tested by a published run.**

### Added

- **14 lifecycle modules**, four layers each — `core/` (how to think), `knowledge/` (what to
  know), `resources/` (templates and anti-examples), `learn/` (human curriculum).
- **17 deliverable templates**, 15 required, grouped into `00-decision/` · `01-research/` ·
  `02-product/` · `03-technical/` · `04-delivery/`.
- **Five completion artifacts**, one per audience — decision report, HTML proposal,
  engineering kickoff deck, phase board, AI entry file. Produced on every completed run,
  including one that concludes *do not build*.
- **The evidence policy** — every factual claim carries exactly one tag: `verified`,
  `inferred`, or `assumption`. An untagged claim is a defect.
- **Seven universal gates (U1–U7)** applied to every module on top of its own criteria.
- **Six failure classes**, so a shortfall reports what it actually is rather than a single
  undifferentiated "did not pass".
- **Six validation outcomes**, keeping `inconclusive` and `blocked` distinct from `fail`.
- `validate.py` — 40 structural checks on the framework.
- `validate-run.py` — lints a finished run for deliverability.
- `/pios` and `/pios-author` skills.
- **Installable as a Claude Code plugin.** `.claude-plugin/plugin.json` and
  `marketplace.json`; the framework resolves from `$CLAUDE_PLUGIN_ROOT` and runs land in
  `./pios/<slug>/` in the operator's own project.
- `gemini-extension.json` and `package.json` for Gemini CLI and npm distribution.

### Framework portability

- Framework detection now checks **plugin mode first**, then in-repo, then `PIOS_HOME`.
- **Every framework path is written repo-relative and resolved against `<FRAMEWORK>`.** Two
  new structural checks enforce it: one rejects any non-canonical form (`./framework/`,
  `../framework/`, absolute), the other requires the resolution rule to be taught in both
  places an agent starts reading.

  Without this, an installed plugin reads gate criteria pointing at method documents that do
  not resolve from the operator's working directory — and the run continues without the
  method, reaching delivery having silently skipped the document that would have failed it.

### Known limitations

- **No reference run is published.** Runs are private and stay that way; a synthetic example
  run is the next milestone.
- `framework/packs/` — vertical knowledge packs are declared and not built.
- A full run is slow. Roughly 410k tokens of framework reading before any research begins.
