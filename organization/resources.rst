.. _doc_resources:

Resources
=========

This section lists resources that can be useful when contributing to Godot.
Most of these resources are part of the `Godot organization on GitHub <https://github.com/godotengine>`__,
but some are hosted elsewhere.

Resources are listed in alphabetical order.

Benchmarks (long-term performance tracker)
------------------------------------------

- **Link:** `benchmarks.godotengine.org <https://benchmarks.godotengine.org/>`__
- `Source code <https://github.com/godotengine/godot-benchmarks/tree/main/web>`__
  (maintained by `Calinou <https://github.com/Calinou>`__)

The `godot-benchmarks <https://github.com/godotengine/godot-benchmarks>`__
are run daily on a dedicated server. This makes it possible to track
performance improvements and regressions over time.

Class reference status
----------------------

- **Link:** `godotengine.github.io/doc-status <https://godotengine.github.io/doc-status/>`__
- `Source code <https://github.com/godotengine/doc-status>`__
  (maintained by `Calinou <https://github.com/Calinou>`__)

Tracks the documentation coverage of the class reference.
This can be useful to ensure that all of Godot's classes and functions
are adequately documented.

Commit artifacts
----------------

- **Link:** `godotengine.github.io/godot-commit-artifacts <https://godotengine.github.io/godot-commit-artifacts/>`__
- `Source code <https://github.com/godotengine/godot-commit-artifacts>`__
  (maintained by `akien-mga <https://github.com/akien-mga>`__)

Lists downloadable GitHub Actions build artifacts for every branch in the
Godot repository. This can be used to quickly download a build of the ``master``
branch and test recent changes, without needing to compile from source.

Note that these builds are *not* compiled with full optimizations. As a result,
they will be slower than official releases.

Godot builds
------------

- **Link:** `github.com/godotengine/godot-builds <https://github.com/godotengine/godot-builds>`__

Lists all official Godot builds, including development builds. This also contains
information on which commit was used to compile each version, which is useful for
:ref:`bisecting regressions <doc_bisecting_regressions>`.

Interactive changelog
---------------------

- **Link:** `godotengine.github.io/godot-interactive-changelog <https://godotengine.github.io/godot-interactive-changelog/>`__
- `Source code <https://github.com/godotengine/godot-interactive-changelog>`__
  (maintained by `Repiteo <https://github.com/Repiteo>`__ and `akien-mga <https://github.com/akien-mga>`__)

Provides a way to visualize an automatically generated changelog between two
Godot versions. The changelog can be viewed as rich text or raw Markdown,
with headings present in every list item, or lists under headings for each section.

This is used to automate changelog creation, as well as provide a basis
for highlights in release blog posts.

Issue statistics
----------------

- **Link:** `godotengine.github.io/issue-stats <https://godotengine.github.io/issue-stats/>`__
- `Source code <https://github.com/godotengine/issue-stats>`__
  (maintained by `Calinou <https://github.com/Calinou>`__)

Provides hardware and software statistics based on recent GitHub issue reports.
Since Godot does not contain telemetry, this allows getting an idea of what kind
of hardware is being used to run Godot.

However, since it is purely based on voluntary issue reports, it is *not* fully
representative of what the community is using as a whole (let alone players
of games made with Godot).

Proposals viewer
----------------

- **Link:** `godot-proposals-viewer.github.io <https://godot-proposals-viewer.github.io/>`__
- `Source code <https://github.com/godot-proposals-viewer/godot-proposals-viewer.github.io>`__
  (maintained by `Calinou <https://github.com/Calinou>`__)

A web viewer for the `Godot proposals <https://github.com/godotengine/godot-proposals>`__
repository. Unlike GitHub issue search, this viewer makes it possible to search
across all issue titles and author names without any pagination. It also provides
automatic sorting by popularity (based on reactions and comment count).

Pull requests by file
---------------------

- **Link:** `godotengine.github.io/godot-prs-by-file <https://godotengine.github.io/godot-prs-by-file/>`__
- `Source code <https://github.com/godotengine/godot-prs-by-file>`__
  (maintained by `akien-mga <https://github.com/akien-mga>`__)

Lists pull requests that edit each file or folder in the Godot source tree.
This can be used to avoid duplicate work, or to find related pull requests
when working on a specific engine subsystem.

Team reports
------------

- **Link:** `godotengine.github.io/godot-team-reports <https://godotengine.github.io/godot-team-reports/>`__
- `Source code <https://github.com/godotengine/godot-team-reports>`__
  (maintained by `akien-mga <https://github.com/akien-mga>`__)

Lists pull requests in a way that helps monitor stale and old PRs and
helps clean up the review backlog.

Pull requests are grouped by the teams assigned to review them, so that maintainers
have a good overview of their area of the engine.
