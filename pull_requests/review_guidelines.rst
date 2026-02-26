.. _doc_pr_review_guidelines:

Reviewing pull requests
=======================

To ensure a bug-free experience for Godot users, we rely on code review and
:ref:`testing <doc_testing_pull_requests>` for pull requests.

While code review is usually done by maintainers, review by other contributors
helps, especially if they are knowledgeable with the subject matter. By helping
to review pull requests, you can improve their chances of being merged.

This article lists things that contributors and engine maintainers can
do to conduct a substantive code review of a pull request.

You don't have to do everything listed here to help with the review process.
Just remember to comment which aspects you have reviewed, and which you haven't.
Commenting a summary of your thoughts is especially helpful, as it shows that
you actually put thought and effort into your review.

.. note::

  During code review, please remember to abide by our `Code of Conduct <https://godotengine.org/code-of-conduct>`__.

Confirm that that pull request is valid
---------------------------------------

Before anything else, please make sure that you are looking at a valid pull
request. Familiarize yourself with our :ref:`pull request rules <doc_pull_request_guidelines>`
and ensure that the author did their best to abide by them.

If you see any invalid PR, it might be best to just ignore it and wait for
maintainers to take action. If you think someone is intentionally
side-stepping rules, for example by using AI without disclosing
it, feel free to let us know in the `Contributors' chat <https://chat.godotengine.org>`__.

Confirm that the problem exists
-------------------------------

PRs need to solve problems and problems need to be documented. Make sure that
the pull request links and closes (or at least addresses) a bug or a proposal.
If it doesn't, consider asking the contributor to update the opening message of
the PR to explain the problem that the PR aims to solve in more detail.

If the pull request isn't sufficiently justified, we recommend you stop your
review here. There is no point in reviewing a PR that will never be merged
because it is not addressing a relevant issue.

Confirm that the approach is appropriate
----------------------------------------

Many reviewers jump right into the code, but this skips one of the most important
steps of the review process: you should ensure that the pull request takes a good
approach to solving the problem at hand.

You should read the pull request description, the linked issue or proposal, and
related discussions, and try to assess whether the pull request is a good way to
approach solving the issue. We have documented some expectations in :ref:`doc_best_practices_for_engine_contributors`.

If the approach of the PR seems inadequate, please comment this on the PR and stop
your review here. The author may revise their PR significantly to improve the
approach, meaning code reviews on the old approach might be wasted effort.

Test the PR and look for regressions
------------------------------------

While the author should test their own pull request, pull request reviewers
are just as responsible for ensuring that pull requests they approve work as
intended.
There is no better way to ensure this than to test the functionality yourself.

Find how to test pull requests in the section :ref:`doc_testing_pull_requests`.

Do a code review
----------------

When you have confirmed that the PR is valid, addresses a real problem, and
takes a valid approach, you can start getting technical and review the code.

Here are some things to think about and look out for as you review:

* **The code follows the area's guidelines.**

  In addition to :ref:`pull request rules <doc_pull_request_guidelines>`,
  each area has a set of guidelines we expect PRs to follow. For example,
  engine contributions should follow the guidelines laid out in
  :ref:`doc_engine_guidelines`, and documentation changes should follow the
  :ref:`doc_documentation_guidelines`.

* **The code will work as intended and is unlikely to introduce risks or regressions.**

  Try to understand what is happening and call out anything that looks like it
  might not work as intended.

* **The code only changes things described and motivated in the PR description.**

  It can be tempting for pull request authors to change nearby code to fix
  bugs or improve style or performance. However, this increases the risk of
  regressions and makes the pull request hard to review. If you see a change
  that is not needed to fix the problem at hand, don't hesitate to call it out.

What to avoid during review
---------------------------

* **Needless double reviews.**

  In other words, review the full PR at once and avoid coming back endless times
  to point out issues that you could have noted in the first review. Of course,
  this can't always be avoided, but we should try to catch everything at once.

* **Being overly nitpicky.**

  Only comment things that will have an actual impact on the quality of the PR.
  Our expectations are flexible depending on the area of the engine you are
  working in. For example, our standard for code quality is much higher in core
  areas and in performance-sensitive areas than it is in editor code.

* **Reviewing by subjective preference.**

  As Godot is a large codebase with many contributors, our style can vary a lot.
  Please keep an open mind and try to differentiate personal preferences versus
  comments that actually improve the quality of the PR.
  We have laid out our stylistic expectations in :ref:`doc_cpp_usage_guidelines`.
  Please avoid commenting too much on style unless it is explicitly described here.

* **Expanding the scope of a pull request.**

  Providing context or related/similar issues or proposals that may be fixed
  similarly can be helpful, but adding a "may as well fix that thing over there
  as well while at it" or "could we add to this as well?" isn't always fair to
  the contributor. Use your judgement when deciding whether additional fixes are
  within scope, but try to keep the scope as close to the original pull request
  as possible.

And ultimately, don't feel pressured to deal with the PR all alone. Feel free to
ask for a helping hand on the `Godot Contributors Chat
<https://chat.godotengine.org>`_, in the appropriate channel or in #general.
Other teams may already be tagged for review, so you can also wait or ask for
their assistance.

Post your review
----------------

When you are done with your review, assess the PRs current state in context:

- If the PR is **not ready** to be merged in its current state, or is **invalid** or **inadequate**, use **"request changes"**.
  If the PR is unlikely to recover, it can be closed.
- If the PR **should be merged** in its current state, or with very minor changes, use **"approve"**.
- If you cannot make a judgement call right now, use **"comment"**.

Use the review comment to summarize your thoughts and specify the nature of your
review. For example, if you reviewed the code but haven't tested the PR, you
should disclose this in your review.

Practically, the approval of :ref:`area maintainers <doc_areas>` is always needed
before the PR can be merged. However, if you conduct useful reviews, maintainers
will take them into account. They will especially take note if you often leave
helpful reviews in their area.
