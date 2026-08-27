# Acceptance — «folder id»

<!-- fill: One of these is written into every folder under deliverables/ that received at
     least one artifact. Name the file exactly `_acceptance.md` — the leading underscore
     sorts it to the top of the folder, which is the only reason it is named that way.

     THIS FILE ESTABLISHES NOTHING. Every criterion below is copied out of
     framework/deliverables/manifest.yaml, character for character, including the awkward
     wording and the criteria you disagree with. validate-run.py compares them exactly.

     If a criterion looks wrong while you are copying it, copy it and say so somewhere the
     operator will read. Do not improve it here. A criterion softened on the way into the
     folder is the version the builder works to, and nothing downstream can see that it
     drifted. -->

**Purpose of this folder:** «purpose, from the manifest's folder_layout»

**Who reads it:** «reader, from the manifest's folder_layout»

This file is a copy. `framework/deliverables/manifest.yaml` is the source of truth, and
nothing here was written for this run.

---

# «NN-Artifact-Name.md»

**Audience:** «audience, from the manifest»

**Status:** «complete | incomplete — and if incomplete, which criterion is unmet»

| | Criterion | Met |
| --- | --- | --- |
| 1 | «criterion, copied from the manifest verbatim» | «yes / no» |
| 2 | «criterion, copied from the manifest verbatim» | «yes / no» |

<!-- fill: Repeat the block above once per artifact in this folder, in the folder's own
     file order. An artifact that is absent because it is conditional and its condition
     was not met gets a block too, saying so — otherwise its absence looks like a gap
     rather than a correct outcome. -->

---

# Unmet criteria

<!-- fill: List every `no` from the tables above, with what is missing and whose it is to
     supply. An empty section here is a claim that the folder is complete, so leave it
     empty only when it is.

     A folder that reports every criterion met while the run's confidence is low is not a
     contradiction — the criteria ask whether the document does its job, not whether the
     evidence behind it is strong. Say which one you mean. -->

- «criterion» — «what is missing» — «owner»

---

> **Folder Acceptance Principle**
>
> A folder that cannot say which of its own criteria it fails is a folder that will be
> reported as finished by whoever opens it last.
