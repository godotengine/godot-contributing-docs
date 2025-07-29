Bug triage overview
===================

This is page is meant to outline in more detail the process of triaging
bugs. For a basic introduction, please see the `introduction to
triage `__ page. If you have any questions,
or if there’s anything missing, please don’t hesitate to ask in the
`#bugsquad `__ channel.

Triage checklist
----------------

-  Make sure the issue is `valid <#check-issue-validity>`__:

   -  If the issue is not filled in properly, i.e. ignores the template,
      ask the author to do so.
   -  If the issue is in the wrong place, direct the author to the
      correct place.
   -  If the issue is spam, close it.

-  Make sure the issue has all the required information, if not ask the
   author to add the missing information.
-  `Check for duplicates <#check-for-duplicates>`__.
-  Check if the issue is a recent regression. If it is, add it to the
   `release blocker tracker `__ and
   mark it as a “regression”.
-  Add initial labels.
-  `Assign a milestone <#assigning-milestones>`__ if relevant.
-  Test the issue if you are able, or ask others to test it.

   -  If you cannot replicate the issue, and it has been fixed, close
      the issue.
   -  If you need more details after testing it, ask the author. And add
      the “needs testing” and “needs work” labels as needed.
   -  If you can replicate the issue, mark it as “confirmed”.

-  Finalize the assessment, updating any labels or milestone if needed
   and adding it to the appropriate `team
   trackers `__.

Check Issue Validity
--------------------

The first step of triage is to confirm that the issue is valid and
filled in properly. This means that: \* It is a bug report, for the
engine, and not a: - Feature proposal, belonging in `Godot
Proposals `__ - Online
documentation issue, belonging in `Godot
Docs `__ (this should
generally be transferred) - A support question, these should be directed
to other `community channels `__ \*
Has all the required information: - The engine version tested with (with
a specific version hash if not using an official release) - System
information in most cases - Clear and detailed reproduction steps - A
valid MRP if the steps are not trivial, or if the issue depends on scene
setup or requires data, such as animations, meshes, etc., where getting
the required setup to test are not trivial.

If the report is missing this information, ask for this information
before proceeding. If the issue lacks critical information, or is
written in a way that makes it difficult to classify the issue, it
should be tagged with “needs work”. Otherwise you can proceed and add
some basic tags to the issue and add the “needs testing” tag.

Issues that are clearly spam should be closed and tagged as “spam” and
marked as archived.

Initial Assessment
------------------

Once the basic details of the issue have been verified the issue should
be tagged with the appropriate tags. See `bug triage
guidelines `__
for details on these tags.

If the bug is reported on the current development version (i.e. the
``master`` branch, and any pre-releases such as ``4.4.beta1``) it is
important to verify if it also occurs on a past stable release. If this
information is missing from the report (i.e. the author only reports
having tested development versions) please either ask the author to test
with a stable version or test the bug yourself. If it *doesn’t* occur on
a past release it is considered a regression and should be tagged with
the “regression” label, and should also be added to the “4.x Release
Blockers” project. See `release blocker
tracking `__ for details.

Try to tag an issue as specifically as possible, adding “needs testing”
and “needs work” if necessary. Don’t worry about misidentifying issues,
for example classifying something as a “bug” when it’s actually an issue
in the documentation or a missing feature. Maintainers for each area
will double checks reports when investigating, and will change tags as
necessary. It’s more important to get an issue tagged correctly than
getting it right from the start.

Check for Duplicates
--------------------

.. raw:: html



.. raw:: html



If the same bug, with the same fix, is reported in multiple versions, it
is a duplicate. For example a bug reported for and fixed in ``4.5``,
which is marked for cherry-picking for ``4.4`` (i.e. the PR has the
“cherrypick:4.4” label), should not be tracked separately for ``4.4``.

Assigning Milestones
--------------------

Note that this is for assigning milestones to *open* issues, please see
`closing an issue <#closing-an-issue>`__ for details on closed issues
and milestones.

Below is an outline of the different milestones we use, but as a general
rule you can assume that issues that aren’t release blockers, or
specific to ``3.x``, shouldn’t have milestones assigned.

For the ``master`` branch: \* *``4.x``*: For Godot 4 in general,
i.e. the ``master`` branch. We do not use the ``4.x`` milestone on
issues, issues with no milestone are assumed to be relevant for the
current development cycle. \* *The current development version*: Should
be assigned to issues that are `release
blockers `__, or otherwise prioritized
for the current version. \* *The next release version*: When we enter
feature freeze we usually create a new milestone used for PRs that are
approved but won’t make it into the current release, this milestone is
not used for issues. \* *Older Godot 4 versions*: This is used for
issues that are only relevant for this specific version (or older
versions), but not any newer version. An example of this would be an
issue that was solved in ``4.5`` as part of an enhancement, but that
enhancement cannot be cherry-picked for ``4.4`` and a separate issue is
necessary to track the specific solution for ``4.4`` (and older, if
relevant). For such issues it can also be relevant to add “[4.4]” at the
beginning of the issue title to help clarify it is specific to this
version.

For Godot 3: \* *``3.x``*: For the ``3.x`` branch in general. Used for
issues that are only relevant for the ``3.x`` version, and occurs on the
current development version of ``3.x``. For these issues it can also
help to add “[3.x]” at the beginning of the issue title to help
identifying the issue. \* Other Godot 3 milestones work the same way as
for the ``master`` branch, except we do not track release blockers for
``3.x``.

Testing an Issue
----------------

A valid MRP is a *minimal* project that reproduces a bug. This means
that it is no larger than it needs to be, it also has to be a project,
not an exported executable. Do *not* run executable projects added to a
bug report, they are not valid MRPs as an MRP needs to be something that
can be evaluated in detail, and be tweaked if needed, and more
importantly they are untrusted files.

.. raw:: html



Some bugs can be hard to verify when testing different versions (for
example when bisecting) due to generated data. In this case, you might
need to delete the ``.godot`` folder or any user data related to the
project. See `data
paths `__
for details on where these files are stored.

.. raw:: html



If you are unable to reproduce the bug, and the author reports using a
different operating system, or using different hardware (for example a
different GPU manufacturer or family), please drop it in the
`#bugsquad `__ channel
and ask for someone to test it.

Finalize Assessment
-------------------

For pre-release versions, it’s critical to identify what change caused a
specific bug. **All** such regressions should be bisected. You can ask
the issue author to follow the instructions in the `Bisecting
regressions `__
documentation. If they are not able to (or the issue is critical and
should be fixed as quickly as possible), then you can look into
bisecting the issue yourself.

Once identified correctly it should be put on the relevant triage
project(s) if appropriate. See `team
trackers `__ for a list of triage
projects. Functional enhancements shouldn’t generally be put on the
trackers (i.e. new features, not enhancements to documentation). Some
teams have dedicated trackers for enhancements, but they aren’t detailed
here.

Closing an issue
----------------

Normally issues that have a linked PR are closed automatically when the
linked PR is merged. [1]_ Note that an issue can still be valid though
it has a linked and merged PR, for example if the issue wasn’t fully
resolved by the PR. So make sure an issue is no longer relevant before
closing.

Issues closed as duplicates should be marked with the archived label,
and the milestone should be removed if it has one. If an issue can no
longer be replicated, it should be assigned to the milestone it was
fixed in. If you can’t pin down when it was fixed (for example if the
report was made long ago), it should be marked as archived as well.

The “needs testing” and “needs work” labels should also be removed when
an issue is closed, regardless of how it was solved.

Team Workflow
-------------

When issues arrive in the triage projects they will have the “For Team
Assessment” status. These issues should be treated as being unverified,
and should be verified before moving the issue to another status. This
can be done as part of regular team meetings, or be handled by
individual maintainers processing these, as long as the assessment made
by triagers is verified.

As part of this verification, other information should be updated if
needed. For example, if the issue was added to multiple trackers because
it was unclear what area it belongs to, it should be removed from the
unrelated tracker(s). This is also a good time to verify any regression
severity or assign one if it is unassessed.

If the report is missing information, please ask the author for more
details. If the task of handling testing updated information can be
handled by the bugsquad, this task can be handed over to them for
verification: for example, testing an updated MRP provided by the
author.

.. [1]
   This is limited to PRs on the ``master`` branch, for other cases
   issues have to be closed manually. This is usually handled by the
   production team.
