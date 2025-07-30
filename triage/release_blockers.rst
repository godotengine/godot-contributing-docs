Release blocker tracking
========================

Release blockers are issues that we aim to fix before we release the
next version. There are a few different things to consider when
determining if an issue is a release blocker or not. Generally any bug
that has appeared during the current cycle should be considered release
blockers (and assigned the “regression” label), if the issue isn’t
considered critical it will marked as not critical, see
`severity <#severity>`__ below.

Issues with new features can also be considered release blockers. This
is because once a feature is part of a released version (and isn’t
considered experimental) it is much harder to change how that feature
works without breaking compatibility (see the `release policy page <https://docs.godotengine.org/en/latest/about/release_policy.html#what-are-the-criteria-for-compatibility-across-engine-versions>`__).
This means that fixing issues, especially minor issues that wouldn’t be
critical otherwise, should be done early to avoid compatibility issues
later.

Release blockers have their own project, `4.x Release Blockers <https://github.com/orgs/godotengine/projects/61>`__.

Severity
--------

Release blockers should also be assigned a severity, this is usually
handled by either the production team or the specific :ref:`area maintainers <doc_areas>`, so this is only a rough
outline to use to assign this if you are able:

* *Not Critical*: For issues that do not have to be fixed before the next release, but would be good if we can to reduce newly introduced issues.
* *Bad*: For issues that should be fixed before the next release, but are less critical.
* *Very bad*: Like *Bad* but worse.
* *Release Blocker*: For issues that we absolutely need to fix before releasing. These include issues that severely hurt engine usability, breaks existing functionality, or are new features that don’t work. In some cases less critical bugs can be considered a release blocker if it involves new API and delaying fixing the problem means restricting the solution due to compatibility issues. \* *Immediate Blocker*: For issues that should be solved as soon as possible, rather than before release. This includes issues that make the engine completely unusable, breaks the buildsystem, or are dangerous or damaging (such as security issues or privacy issues).
