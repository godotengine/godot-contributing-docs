Review and merge process
========================

From a high level, the ideal life cycle of a pull request looks like the
following:

  1. A contributor :ref:`opens a pull request <doc_pr_workflow>` that fixes a
     specific problem (ideally closing a GitHub `issue <https://github.com/godotengine/godot>`_
     or implementing a `proposal <https://github.com/godotengine/godot-proposals>`_).

  2. The :ref:`bugsquad and triage team <doc_areas>` **categorize** the pull request,
     adding appropriate tags and requesting reviews from :ref:`area maintainers <doc_areas>`.

  3. Contributors discuss **whether the approach of the PR is appropriate** to fix the problem
     at hand, and leave feedback.

  4. Contributors **review the code**, and iterate improvements with the pull request author.
     When they are satisfied, they will approve the pull request.

  5. A release manager merges the pull request when there are sufficient approvals. A pull request
     always needs approvals from the respective :ref:`area maintainers <doc_areas>`, but reviews
     from other contributors help.

.. note::
  In practice, the above steps may often blend together.

Even if you are not a maintainer, you can still help by :ref:`reviewing <doc_pr_review_guidelines>`,
providing feedback, and :ref:`testing PRs <doc_testing_pull_requests>` locally on your machine
to confirm that they work as intended. Many of the currently active maintainers started out doing
this before they became maintainers.

When will a pull request get reviewed?
--------------------------------------

When you open a new pull request, :ref:`Area maintainers <doc_areas>` are notified immediately.

However, a lot of pull requests are opened every day, so reviews can take a while to come in. Going by historical data,
you can expect the following review timelines:

- 80% of **regression fixes** are merged (or rejected) within **a week**.
- 80% of **bug fixes** are merged (or rejected) within **two weeks**.
- 80% of **enhancements** are merged (or rejected) within **two months**.

As you can imagine, simple pull requests will usually be reviewed more quickly than large and complicated pull requests.

If you think your pull request has been overlooked, feel free to ask about it in the `Contributors' chat <https://chat.godotengine.org>`__.
You can ask in `#new-contributors <https://chat.godotengine.org/channel/new-contributors>`__, `#devel <https://chat.godotengine.org/channel/devel>`__,
or the channel of the :ref:`area <doc_areas>` you're expecting reviews from.
