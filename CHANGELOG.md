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
ls "$P/skills"                            # pios · pios-author
```

**A version bump with no framework change is still a release**, and is the right move whenever
a skill, template or check changes — those are the method too.

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
