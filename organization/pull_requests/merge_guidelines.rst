.. _doc_pr_review_guidelines:

Merge guidelines
================

.. note::

    This section is targeted at maintainers. Regular contributors to Godot
    cannot merge pull requests.

In general, pull requests should only be merged by members of the production
team or team leaders for pull requests in their area of the engine. For example,
the networking team leader could merge a networking pull request that doesn't
substantially change non-networking sections of code.

In practice it is best to wait for a member of the production team to merge the
pull request as they keep a close eye on the entire codebase and will likely
have a better sense of what other recent/upcoming changes this pull request may
conflict with (or any other reason that it may make sense to delay the pull
request). Feel free to leave a comment saying that the PR should be ready to
merge.

The following are the steps to take before merging a pull request. The degree to
which you adhere to these steps can be flexible for simple/straightforward pull
requests, but they should be carefully taken for complex or risky pull requests.

As a contributor you can help move a pull request forward by doing some of these
steps yourself.

1. Get feedback from the right people/teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Production team members should ensure that the right people look at a pull
request before it is merged. In some cases this may require multiple people to
weigh in. In other cases, only one substantive approval is needed before the
code can be merged.

In general, try not to merge things based on one review alone, especially if it
is your own. Get a second opinion from another maintainer, and make sure all the
teams that may be impacted have been reasonably represented by the reviewers.
For example, if a pull request adds to the documentation, it's often useful to
let the area maintainers check it for factual correctness and let documentation
maintainers check it for formatting, style, and grammar.

A good rule of thumb is that at least one subject matter expert should have
approved the pull request for correctness, and at least one other maintainer
should have approved the pull request for code style. Either of those people
could be the person merging the pull request.

Make sure that the reviews and approvals were left by people competent in that
specific engine area. It is possible that even a long-standing member of the
Godot organization left a review without having the relevant expertise.

.. note::

    An easy way to find PRs that may be ready for merging is filtering by
    approved PRs and sorting by recently updated. For example, in the main Godot
    repository, you can use `this link
    <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+review%3Aapproved+sort%3Aupdated-desc>`_.

2. Get feedback from the community
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a pull request is having trouble attracting reviewers, you may need to reach
out more broadly to ask for help reviewing. Consider asking:

* the person who reported the bug if the pull request fixes the bug for them,
* contributors who have recently edited that file if they could take a look, or
* a more experienced maintainer from another area if they could provide feedback.

3. Git checklist
~~~~~~~~~~~~~~~~

* **Make sure that the PR comes in one commit.**

  When each commit is self-contained and could be used to build a clean and
  working version of the engine, it may be okay to merge a pull request with
  multiple commits, but in general, we require that all pull requests only have
  one commit. This helps us keep the Git history clean.

* **Fixes made during the review process must be squashed into
  the main commit.**

  For multi-commit PRs check that those fixes are amended in the relevant
  commits, and are not just applied on top of everything.

* **Make sure that the PR has no merge conflicts.**

  Contributors may need to rebase their changes on top of the relevant branch
  (e.g. ``master`` or ``3.x``) and manually fix merge conflicts. Even if there
  are no merge conflicts, contributors may need to rebase especially old PRs as
  the GitHub conflict checker may not catch all conflicts, or the CI may have
  changed since it was originally run.

* **Check for proper commit attribution.**

  If a contributor uses an author signature that is not listed in their GitHub
  account, GitHub won't link the merged pull request to their account. This
  keeps them from getting proper credit in the GitHub history and makes them
  appear like a new contributor on the GitHub UI even after several
  contributions.

  Ultimately, it's up to the user if they want to fix it, but they can do so by
  authoring the Git commit with the same email they use for their GitHub
  account, or by adding the email they used for the Git commit to their GitHub
  profile.

* **Check for proper commit messages.**

  While we don't have a very strict ruleset for commit messages, we still
  require them to be short yet descriptive and use proper English. As a
  maintainer you've probably written them enough times to know how to make one,
  but for a general template think about *"Fix <issue> in <part of codebase>"*.
  For a more detailed recommendation see the `contributing.md
  <https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md#format-your-commit-messages-with-readability-in-mind>`_
  page in the main Godot repository.

4. GitHub checklist
~~~~~~~~~~~~~~~~~~~

* **Validate the target branch of the PR.**

  Most Godot development happens around in the ``master`` branch. Therefore most
  pull requests must be made against it. From there pull requests can then be
  backported to other branches. Be wary of people making PRs on the version they
  are using (e.g, ``3.3``) and guide them to make a change against a
  higher-order branch (e.g. ``3.x``). If the change is not applicable for the
  ``master`` branch, the initial PR can be made against the current maintenance
  branch, such as ``3.x``. It's okay for people to make multiple PRs for each
  target branch, especially if the changes cannot be easily backported.
  Cherry-picking is also an option, if possible. Use the appropriate labels if
  the PR can be cherrypicked (e.g. ``cherrypick:3.x``).

.. note::

    It is possible to change the target branch of the PR, that has already been
    submitted, but be aware of the consequences. As it cannot be synchronized
    with the push, the target branch change will inevitable tag the entire list
    of maintainers for review. It may also render the CI incapable of running
    properly. A push should help with that, but if nothing else, recommend
    opening a new, fresh PR.

* **Make sure that the appropriate milestone is assigned.**

  This will make it more obvious which version would include the submitted
  changes, should the pull request be merged now. Note, that the milestone is
  not a binding contract and does not guarantee that this version is definitely
  going to include the PR. If the pull request is not merged before the version
  is released, the milestone will be moved (and the PR itself may require a
  target branch change).

  Similarly, when merging a PR with a higher milestone than the current version,
  or a "wildcard" milestone (e.g. "4.x"), ensure to update the milestone to the
  current version.

* **Make sure that the opening message of the PR contains the
  magic words "Closes #..." or "Fixes #...".**

  These link the PR and the referenced issue together and allow GitHub to
  auto-close the latter when you merge the changes. Note, that this only works
  for the PRs that target the ``master`` branch. For others you need to pay
  attention and close the related issues manually. Do it with *"Fixed by #..."*
  or *"Resolved by #..."* comment to clearly indicate the act for future
  contributors.

* **For the issues that get closed by the PR add the closest
  relevant milestone.**

  In other words, if the PR is targeting the ``master`` branch, but is then also
  cherrypicked for ``3.x``, the next ``3.x`` release would be the appropriate
  milestone for the closed issue.

5. Merge the pull request
~~~~~~~~~~~~~~~~~~~~~~~~~

If it is appropriate for you to be merging a pull request (i.e. you are on the
production team or you are the team leader for that area), you are confident
that the pull request has been sufficiently reviewed, and once you carry out
these steps you can go ahead and merge the pull request.
