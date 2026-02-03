.. _doc_bug_triage_release_priorities:

Release priority tracking
=========================

Release priorities are issues that we aim to fix before we release the
next version. There are a few different things to consider when
determining if an issue is a release priority or not.

Release priorities are tracked in a public project, `4.x Release Priorities <https://github.com/orgs/godotengine/projects/61>`__.

See below for an explanation of how to
:ref:`identify release priorities <doc_identifying_release_priorities>`,
and how to assign a :ref:`severity <doc_release_priority_severity>` to them. When in doubt, mark issues as
release priorities. We can always remove issues from the list, but it is critical
that we know about potentially important issues before releasing a version.

.. _doc_identifying_release_priorities:

Identifying release priority issues
-----------------------------------

The following is a checklist to determine if an issue is a release priority or not.

If an issue is old (over 6 months), and hasn't gotten worse, or gotten new duplicate issues
or users that report having encountered the issue, it is likely not a release priority.

If you are unsure if an issue is a priority, prefer to flag it as such, but
add a note in the tracker clarifying this.

Is it a regression?
~~~~~~~~~~~~~~~~~~~

A regression is any feature or part of the engine that used to work but no longer works, for example something
that worked in 4.5.1 but doesn't work in 4.6.dev2. Any regression in the current release cycle is considered a
release priority. Regressions are also assigned the “regression” label.

Regressions from previous cycles can also be considered release priorities depending on when they happened
and how severe they are (for example, a bug that occurs in 4.5 but not 4.4 can be considered a release priority
during the 4.6 dev cycle).

Regressions should be fixed as soon as possible. Regressions from previous cycles should also be backported
where appropriate.

It is important to flag anything that looks like a regression as a priority. Some changes to existing behavior
are intentional, but the relevant maintainers should make this evaluation and will remove the issue if it
isn't a regression. And even if the change in behavior is intentional, there might be missing compatibility code
or documentation for the change which needs to be evaluated.

Is it a crash with significant user impact?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An engine issue that causes crashes or freezes and affects a lot of users is a release priority. This is
mostly determined based on many users reporting the same issue, or issues that remain open over a long period of time.

This often involves graphics issues and can be hard to identify or result in unclear bug reports. Identifying
if the time the issues started line up with recent graphics driver updates can be a good indicator.

Is it a showstopper bug?
~~~~~~~~~~~~~~~~~~~~~~~~

Showstopper bugs are release priorities. A showstopper issue is any issue that prevents users from performing key tasks,
like using certain parts of the engine, or that causes loss of data or work, and that has no workaround or that causes
significant workflow disruption.

Examples of showstopper issues are:
* Parts of the editor or engine that do not work, or are difficult to use, including only on some platforms:
    - Changes to the animation system causing errors when using animation features,
    - Improvements to the way the editor generates previews and thumbnails causing severe performance regressions,
    - Changes to the export process causing C# code to not be exported.
* Errors that cause loss of data or work, for example deleting or corrupting project files.
* Issues using or importing file formats.
* Issues with specific hardware, like controllers not working or rendering being broken on certain graphics hardware.

Is it a bug in a new feature?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Issues in new features should be priorities even if the issue itself isn't critical otherwise.
Fixing issues in new features might require changing significant parts of the feature in ways that break compatibility,
or it might be difficult to fix the issue without breaking compatibility. This means that fixing issues in new features,
and making sure issues in new features are evaluated by maintainers, is especially important.

This also includes issues or enhancements involving code that was already changed in a compatibility-breaking way in the
current release cycle, to avoid breaking compatibility in two separate versions when possible.

Is it a security issue?
~~~~~~~~~~~~~~~~~~~~~~~

Any security issue is a release priority. Security issues include things like vulnerabilities in engine or third-party code,
including remote code execution. They may also include engine issues that cause damage or data loss for the user,
like the editor deleting files outside the project directory.

If something seems like a serious security issue, please contact Godot's security team directly as soon as possible
`security@godotengine.org <mailto:security@godotengine.org>`__. The team will take the appropriate steps to address the issue.

Is it a new platform requirement?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any new platform requirement that will affect users is a release priority. This includes things like Google Play changing
the required target API for Android, or operating system updates or changes that affect users or exported projects on those platforms.

.. _doc_release_priority_severity:

Severity
--------

Release priorities should also be assigned a severity. This is usually
handled by either the production team or the specific :ref:`area maintainers <doc_areas>`, so this is only a rough
outline to use to assign this if you are able:

* *Immediate Blocker*: This must be resolved before the next dev/beta/RC snapshot.
* *Release Blocker*: This must be resolved as soon as possible, and before entering the RC phase or the next RC snapshot.
* *Very Bad*: This is a critical issue which either affects a lot of users, or is a showstopper for a significant part of the userbase.
* *Bad*: This is an annoying issue which may affect a lot of users, but isn’t a showstopper.
* *Not Critical*: This is an overall minor issue, but which may affect a new feature and would be nice to fix before stable.
* *Unassessed*: This issue was added to the tracker but without assessing its severity. This needs to be evaluated by maintainers as it may be a release priority.
