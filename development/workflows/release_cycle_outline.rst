.. _doc_release_cycle_outline:

.. note::

  This is a more general outline of the release cycle for general contributors.
  For an in-depth maintainer description of the release cycle, as well as critical checkpoints,
  see :ref:`doc_release_cycle_checklists`.

Release cycle outline
=====================

This page outlines the process of Godot development, which includes things like:

- When a PR can (or should) be merged, and when it must not be merged.

- What to consider when reviewing or creating PRs, what to look out for, and what
  to expect or not to expect from maintainers.

- What contributors should focus on at different points in the cycle, what you can
  do to help, and what is the most helpful use of your time.

Note that these rules are, generally, not hard rules, but following them helps make the release
progress smoother and reduces unnecessary work and risks.

This page is meant to serve as a guideline for maintainers when reviewing PRs, as well as a reference
to understand how this process works and what to expect for specific contributions,
for example why it might not be possible to merge it right now and when you might expect it to be considered for merger.

Testing and fixing bugs
-----------------------

Testing bugs is important at all points of the release cycle, but during the feature freeze period it becomes
the main focus of work. While some bug fixes can be off-limits during the late stages of the release cycle, for example
if they are too risky, bug fixes are always wanted and should always get some maintainer and contributor attention.
The release candidate (rc) phase of development is the only real exception to this, during this phase only critical bugs are
considered.

It is important however what bugs are prioritized as we approach release. Later in the release cycle we focus more on
:ref:`release priorities and regressions <doc_bug_triage_release_priorities>`.

Outline of Feature Freeze restrictions
--------------------------------------

This is a rough outline of what should be considered off limits post feature freeze. These are not
hard and fast rules but should *generally* be followed. This is in addition to the general restriction on
new features.

- Breaking changes in general.

- Bug fixes that include major new features, or that significantly change existing features, or that are otherwise
  considered risky.

In general the following can be used to evaluate if something should be considered appropriate post feature freeze:

- Does this change require significant testing or feedback, including if it is risky, potentially controversial, or difficult to
  properly test in isolation (i.e., as an unmerged PR, meaning it can only be properly evaluated by testing it after merging)?

- Does it significantly alter the editor UI in a way that might cause confusion, or that requires adjustments to documentation
  or promotional material (for example screenshots used in the release page blog)?

- Does it significantly alter translated strings that might risk translations not being updated in time for release?

- Does it depend on changes to other parts of the ecosystem, for example godot-cpp, or in external tools or plugins.
  Would it require follow-up PRs elsewhere to function properly?

- Does it require major work to document the feature or to add demo projects to cover this new content?

In the end the main goal of the feature freeze is giving ourselves enough time to make sure the release is ready,
to avoid as many surprises as possible, and to focus effort away from new features and towards fixing bugs.

