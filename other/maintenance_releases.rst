.. _doc_maintenance_release_process:

Maintenance release process
===========================

.. note::

   This section is for the release team. Regular contributors to Godot are not
   expected to make maintenance releases.

Maintenance releases are made to provide safe upgrades to users for a stable branch,
suitable for use in production (including updating a published game without much
risk of potential regressions).

Stable branches are **feature and release frozen**, so the same criteria that are used
during release candidate (RC) phases apply to changes for stable branches:
no new features (unless necessary to enable platform support),
and no risky bugfixes unless absolutely critical.

Stable branches are usually kept at the RC stage: when ``4.6.stable`` is released,
we bump the version to ``4.6.1.rc``. So the kind of changes that can be included in a
maintenance release are the kind we’d consider for inclusion in RC 1 of a feature branch.

Changes suitable for maintenance releases
-----------------------------------------

The types of changes that should be considered for cherry-picking to a maintenance
release are the ones that fit the :ref:`release priority tracking criteria <doc_identifying_release_priorities>`.

As a rule of thumb, if an issue is a release priority for the next feature branch,
and also affects supported stable branches, the PR fixing it should be considered
for cherry-picking and get the relevant label(s).

This includes:

- Regression fixes.
- Crashes which potentially affect a lot of users.
- Critical bugs with evidence of affecting a lot of users.
- Bugs that significantly disrupt a new feature added in that stable release.
- Security fixes (both in Godot code and in third-party libraries).
- New platform requirements which will roll out to users soon.

Additionally, we can occasionally cherry-pick changes which aren’t release priorities per se,
but would provide a significant improvement to the user experience.
These would typically only be considered for the latest stable branch and not older branches
with “critical fixes only” support policy.

This includes:

- Safe bug fixes that add a lot of value to users.

    - By “safe”, we imply that these changes have a very low risk of introducing regressions
      or disrupting workflows. They should be ready for production use.
    - This should be assessed by area maintainers and/or the release management team.
    - They should not expose any new API or significantly change the behavior of existing APIs.

- Documentation fixes or enhancements that won’t impact translations (see below).

PRs which should **not** be cherry-picked, or need to be further assessed by area owners to
make sure the risk is well understood:

- Risky changes: Changes to core, rendering, scripting, or some nodes for which we’re not confident
  that we have good enough testing to ensure there is no regression (e.g. changes to threading,
  resource loading, or base Control nodes can often cause regressions).

    - Those changes should be vetted by area maintainers on how safe they are for the stable release.

- Any compatibility breaking change, including changes that modify the behavior of an API in a way
  that may affect user projects negatively.
- Documentation enhancements: These break localizations, so we should only add to the documentation,
  or fix obvious bugs, but not tweak language/fix typos, etc.
- Likewise, changes which modify localized strings significantly should be assessed on a case by case
  basis to see if the translation breakage is worth it.

Cherry-picking process
----------------------

Triage process for cherry-pickable PRs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PRs which fulfill the above criteria should be:

- Given the ``cherrypick`` label for the versions where it’s relevant.

    - Can be added by triagers, maintainers, or the release team.
    - Area maintainers are encouraged to re-assess this label during PR review and remove it if they consider
      it’s not suitable for a stable branch (e.g., too risky, or not critical enough).
    - Release managers will also check that the criteria are fulfilled before actually cherry-picking a PR,
      and may occasionally remove the label.

- Added to the merge queue for the relevant stable branch, with the “Wave” set to the relevant maintenance
  release (can be the next, or the following one if a PR needs some time for testing in ``master`` before being
  considered ready for cherry-picking).

    - Use the “Comment” field to provide relevant insights about how important or risky the cherry-pick may be.

These two steps are partially redundant, but for now we apply both. The merge queue projects provide
more information about when and why a PR was cherry-picked, but the labels are easier to add while triaging
and are more visible to end users (who may be asking for a bugfix PR to be cherry-picked).

Release manager process to cherry-pick
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cherry-picking process (assuming ``4.6`` branch and ``4.6.1`` maintenance release):

- Open the `list of merged PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+label%3Acherrypick%3A4.6+is%3Aclosed>`_
  with the ``cherrypick:4.6`` label.
- Open the ones that seem relevant to cherry-pick in priority.

    - First priority are PRs that fix issues fulfilling the :ref:`criteria for release priorities <doc_identifying_release_priorities>`
      (regressions, crashes, security issues, new platform requirements, etc.).
    - Other PRs such as non-critical bugfixes and documentation fixes are second priority.
    - Sometimes a PR that’s meant to be cherry-picked has follow-ups linked in the GH thread.
      Make sure to read the thread and cherry-pick all of them if relevant.
      If the follow-ups are regression fixes to that PR, and show that it turned out trickier than expected,
      re-evaluate whether the whole batch should be cherry-picked or skipped.
    - If they are not already in it, add them to the merge queue for that stable branch (here “4.6 Merge Queue”),
      with the “wave” set to the maintenance release we expect to cherry-pick them in.
      This merge queue can be used to prioritize what are must-haves for the next patch release,
      and document in a convenient interface which PRs were cherry-picked for a given maintenance release.

- Cherry-pick them one by one in a local branch (e.g. named ``4.6-cherrypicks``) with ``git cherry-pick -x <hash>``.

    - The ``-x`` is important to add a reference to the original commit in the commit message.
    - If this is a cherry-pick of another cherry-pick, then don’t use ``-x``,
      only the reference to the commit merged in the newest branch is necessary.

- Comment “Cherry-picked for 4.6.1.”, remove the ``cherrypick:4.6`` label, and set it to “Merged” in the 4.6 Merge Queue project on each PR.
- Once done, open a PR targeting the ``4.6`` branch named “[4.6] Cherry-picks for the 4.6 branch (future 4.6.1) - nth batch”.

    - It’s fine to have multiple batches of cherry-picks for a given maintenance release.
      If it’s useful, you can also group them by area and have for example a rendering batch
      or a regression fixes batch if you’d like reviews from relevant maintainers.
