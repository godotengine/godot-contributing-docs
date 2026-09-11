.. _doc_release_cycle_outline:

Release cycle outline
=====================

This page outlines the process of Godot development, which includes things like:

* When a PR can (or should) be merged, and when it must not be merged.
* What needs to be done at what points in the release cycle.
* What to consider when reviewing or creating PRs, and what to look out for.
* What needs to be tracked and where.

Note that these rules are, generally, not hard rules, but following them helps make the release
progress smoother and reduces unnecessary work and risks.

This page is meant to serve as a guideline for maintainers when reviewing PRs, as well as a reference
to understand how this process works and what to expect for specific contributions,
for example why it might not be possible to merge it right now and when you might expect it to be considered for merger.

Outline of Feature Freeze restrictions
--------------------------------------

This is a rough outline of what should be considered off limits post feature freeze. These are not
hard and fast rules but should *generally* be followed. This is in addition to the general restriction on
new features.

* Breaking changes in general.
* Bug fixes that include major new features, or that significantly change existing features, or that otherwise
  are considered risky.

In general the following can be used to evaluate if something should be considered appropriate post feature freeze:

* Does this change require significant testing or feedback, including is it risky, potentially controversial, or difficult to
  properly test in isolation?
* Does it significantly alter the editor UI in a way that might cause confusion, or that requires adjustments to documentation
  or promotional material (for example screenshots used in the release page blog)?
* Does it significantly alter translated strings that might risk translations not being updated in time for release?
* Does it depend on changes to other parts of the organization or in external tools or plugins, would it require follow-up PRs elsewhere
  to function properly?
* Does it require major work to document the feature or to add demo projects to cover this new content?

In the end the main concern with feature freeze is giving ourselves enough time to make sure the release is ready, to avoid as many surprises
as possible, and to focus effort away from new features and towards fixing bugs.

.. TODO
