# Projects

One directory per run. Generated, never part of the framework.

    projects/<slug>/
      state.yaml        # engine/state-schema.yaml
      research/         # working notes per module
      deliverables/     # the output — see framework/deliverables/manifest.yaml

This directory is gitignored, and a structural check fails the build if any run
content is tracked. Runs belong to the operator, not the framework — they carry
real research, named customers and unreleased strategy, and none of it is this
project's to publish.

Move a run you want to keep and learn from into `examples/`, which is private for
the same reason. See [examples/README.md](../examples/README.md) for how a lesson
from a run becomes a framework change without the run going anywhere.
