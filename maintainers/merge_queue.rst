Pull request merge queue
========================

Guidelines for release coordinators to use the PRs merge queue project
to track, review, and merge PRs during development phases.

-  Target users: **Release coordinators**, and to some extent **team
   leaders / area maintainers**.
-  Relevant reading for: **All engine contributors**, to understand how
   merges are scheduled.
-  Other relevant docs: `PR review process `__.

   -  Note: This page currently says that either team leaders or
      production team members (here “release coordinators”) can merge
      PRs. This is slightly outdated and the current process has only
      release coordinators doing merges (with exceptions for
      e.g. critical CI or build fixes).

Rationale
---------

Godot’s development currently requires that PRs are first approved by
maintainers, and then merged by release coordinators. This is for
multiple reasons:

-  Release coordinators are in charge of making engine builds (dev
   snapshots, beta, RC, stable), and need to control the timing of
   merges in the ``master`` branch, to ensure the snapshots they build
   are suitable for end user testing.
-  The PR review process has a number of requirements for both technical
   assessment by competent maintainers, and stylistic or organization
   considerations. Release coordinators are trained to assess whenever
   all relevant reviews have been done, and can sign off on merging the
   PR.
-  Godot’s CI process is heavy, and to avoid wasting resources and CI
   congestion, PRs are merged in batches. This is currently a manual
   process done by release coordinators.
-  Adding some delay between a “ready to merge” maintainer approval and
   the actual merge gives time to other maintainers to voice concerns
   they may have.

Process
-------

The internal process for merging a PR is:

-  A PR is opened, ``CODEOWNERS`` assigns relevant reviewers, and
   reviews are done. An unreviewed PR should *not* be added to the merge
   queue project.

   -  An exception to this is if the PR is a must-have for the next dev
      snapshot (e.g. regression fix, or very important to merge timely
      to fit the roadmap for that release), in which case it can be
      added to the merge queue even before approval.
   -  TODO: Should we add a “Priority review” state for this?

-  At least one engine maintainer approves the PR, i.e. it becomes an
   “approved PR”. This is the cue to add the PR to the merge queue
   project, to hand it over to release coordinators.
-  Release coordinators ensure that all approved PRs get tracked in the
   merge queue project. See below for how to do this.
-  Approved (or priority) PRs can have the following statuses in the
   merge queue project:

   -  To Review: Despite having one approval, more approvals are still
      needed for it to be ready. This should be reflected in the review
      requests, and clarified to other release coordinators with the
      comment field.
   -  Needs Work or Consensus: These PRs have been approved at least by
      one maintainer, but more work is needed, or a consensus still
      needs to be formed. The reason for being shelved here needs to be
      written in the comment field.
   -  Approved: These PRs are approved and a priori ready to merge.
      Release coordinators do a second review and write in the comment
      field whether it’s indeed ready to merge (with their name), or
      still needs some action (e.g. rebase or squashing). During that
      second review, PRs can be sent back to “To Review” (if more
      maintainers need to approve) or “Needs Work or Consensus”.
   -  TODO: The state of “approved by maintainers AND approved for merge
      by release coordinators” could warrant its own status instead of
      relying on a comment. But we still need to know *who* approved for
      merge.

-  At least once per day, release coordinators do a merge batch with all
   the approved PRs queued for the “Next Wave” and where a release
   coordinator has confirmed that they’re ready to go.

Keeping track of all approved PRs
---------------------------------

As a goal, all PRs which have been approved by a maintainer should be
tracked in the merge queue project, and be assessed by release
coordinators in a timely manner.

This implies:

-  Making sure that PRs that get approved by maintainers get added to
   the merge queue project. Approved PRs that haven’t yet been added to
   the merge queue can be found with this search:
   https://github.com/godotengine/godot/issues?q=is%3Apr%20state%3Aopen%20sort%3Aupdated-desc%20review%3Aapproved%20-project%3Agodotengine%2F90%20(milestone%3A4.4%20OR%20milestone%3A4.x%20OR%20no%3Amilestone)

   -  Release coordinators should make it a habit of reviewing this list
      daily to find newly approved PRs.
   -  TODO: The above list is specific to 4.4 (project “90”) but can be
      adjusted if/when we switch to a new project for future releases.

-  Assessing PRs added to the merge queue by other maintainers, which
   may not have been seen yet by release management. Currently, a lot
   can be found in the “Mislabeled” tab as some maintainers don’t set
   the wave or status when adding to the merge queue. Likewise, some
   maintainers add unapproved PRs to the merge queue (typically their
   own, which they want reviewed), and that’s a misuse of the project
   that we need to clarify.
-  Reviewing PRs ourselves as part of our daily routine, and adding them
   right away to the merge queue project with the right wave and status.
-  (Re)-Assessing the items in all statuses in the “Next Wave” tab
   regularly, to ensure that we don’t miss when a PR that was close to
   ready is now fully ready. PRs that were put in “To Review” or “Needs
   Work or Consensus” which get a new maintainer review should
   automatically be moved to “Approved”, which helps put them back in
   the “hot” queue.

Merging a PR batch
------------------

One purpose of the merge queue, aside from doing all the review
validations described above, is to be able to merge batches of multiple
PRs all at once. This helps reduce the strain on CI resources by
starting only one CI workflow for a whole batch being merged.

The process to make a PR batch is along those lines:

-  Go through the “Approved” PRs with a “Ready to merge” comment from a
   release coordinator, and open them all in tabs. Keep those tabs open
   through the process.
-  Make sure that those PRs are actually ready to merge (there might
   have been new comments/reviews made after a release coordinator
   approval, or new merge conflicts, etc.).
-  Make sure that each PR has the proper milestone (e.g. ``4.4`` if
   merged during the 4.4 release cycle), properly references the issues
   it closes with a closing keyword, and that those issues also have the
   corresponding milestone.
-  Copy the PR numbers of all PRs meant for a merge batch in some file.
-  Merge them all locally with ``git merge --no-ff`` and a merge commit
   message matching what GitHub would generate (see the script below).
   **DO NOT REBASE** after this, as it would flatten the merge commits
   and lose the association to the original PRs.
-  Build once and run the editor to make sure no obvious bug is being
   introduced.
-  Push to the ``master`` branch.
-  Go through the now merged open tabs for each PR and thank the
   contributor(s) for their work.

..

   [!NOTE] To merge PRs locally in the same way that GitHub would do it,
   we use this
   ```git-local-merge.py`` `__
   Python script. Make it executable and place it in the ``PATH``, so
   that a batch of PRs can be merged with:

   .. code:: bash

      git-local-merge.py 100001 100002 100003 ...

Future work
-----------

The above procedure is based on the current workflow with the merge
queue project, and the various usage that different maintainers make of
it.

It’s meant to clarify for release coordinators how they should use it,
and in that process we should keep re-evaluating how to improve both the
merge queue project and the guidelines further, so that things are
clearer for both maintainers and new release coordinators.
