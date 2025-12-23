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

We try our best to avoid unnecessary delays and to get to PRs as soon as possible we cannot make any guarantees about when
a PR will get reviewed or merged, even if it is a is a very simple fix or change. An issue can seem simple at first but can
end up being a far more complicated issue after maintainers have evaluated a proposed fix. If you are not able to continue
working on a fix if this happens, or are not interested in doing so, you do not have to do so, and you can just close your
PR explaining this. We understand that it might be frustrating to feel that you did a lot of work for nothing,
but we cannot merge an incorrect or temporary fix in most cases. If the final fix contains significant parts of your original
PR you will be added as a co-author to that PR.

Please be aware that PRs are prioritized based on how critical the issue it solves is, and the needs of the engine, and we cannot
speed up the process based on other time constraints (for example if you open a PR as part of an assignment in school).
You can still ask maintainers if they can take a look at your PR quicker based on this, but we cannot make exceptions for these reasons,
not to our priorities nor our review process.

We understand that this can cause stress when a PR being merged or not can affect your grade in a class, but if this is causing
problems for you please talk to your teacher or professor about this and ask them to take the way open source projects into
account when creating assignments, to avoid causing stress or friction.

How quickly a PR gets reviewed or merged also depends on where in the release cycle we are currently in. During the development (dev)
phase both bug fixes and new features or enhancements are merged, we then enter "feature freeze" in the beta phase, and we stop merging
(most) new features and focus on bug fixes only. Then we finally enter the release candidate (rc) phase where we only consider critical
fixes. What kind of changes (new features *and* bug fixes) also depends on when in each phase we are in. Some big or risky features
will only be merged during the early part of the dev phase, to give us as much time as possible to find potential regressions or
issues before release.

If you think your pull request has been overlooked, or you have any questions about the review process,
feel free to ask about it in the `Contributors' chat <https://chat.godotengine.org>`__.
You can ask in `#new-contributors <https://chat.godotengine.org/channel/new-contributors>`__, `#devel <https://chat.godotengine.org/channel/devel>`__,
or the channel of the :ref:`area <doc_areas>` you're expecting reviews from.
