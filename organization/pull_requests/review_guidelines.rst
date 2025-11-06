.. _doc_pr_review_guidelines:

Review guidelines
=================

Code review and testing
-----------------------

The following is a list of things that contributors and engine maintainers can
do to conduct a substantive code review of a pull request.

.. note::
  If you want to conduct a code review, but can't do everything on this list,
  say that in your review comment. For example, it is still very helpful to
  provide comments on code, even if you can't build the pull request locally to
  test the pull request (or vice versa). Feel free to review the code, just
  remember to make a note at the end of your review that you have reviewed the
  code only and have not tested the changes locally.

1. Confirm that the problem exists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PRs need to solve problems and problems need to be documented. Make sure that
the pull request links and closes (or at least addresses) a bug or a proposal.
If it doesn't, consider asking the contributor to update the opening message of
the PR to explain the problem that the PR aims to solve in more detail.

.. note::
  It should be clear _why_ a pull request is needed before it is merged. This
  assists reviewers in determining whether a PR does what it says it does and it
  helps contributors in the future understand why the code is the way it is.

2. Test the PR and look for regressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While strict code review and CI help to ensure that all pull requests work as
intended, mistakes happen and sometimes contributors push code that creates a
problem in addition to solving a problem. Maintainers will avoid merging code
that contains a regression even if it solves the problem as intended.

When reviewing a pull request, ensure that the PR does what it says it does
(i.e. fixes the linked bug or implements the new feature) and nothing outside of
the PR target area is broken by the change. You can do this by running the
editor and trying out some common functions of the editor (adding objects to a
scene, running GDScript, opening and closing menus etc.). Also, while reviewing
the code, look for suspicious changes in other parts of the engine. Sometimes
during rebasing changes slip through that contributors are not aware of.

3. Do a code review
~~~~~~~~~~~~~~~~~~~

Code reviews are usually done by people who are already experienced in a given
area. They may be able to provide ideas to make code faster, more organized, or
more idiomatic. But, even if you are not very experienced, you may want to
conduct a code review to provide feedback within the scope of what you are
comfortable reviewing. Doing so is valuable for the area maintainer (as a second
set of eyes on a problem is always helpful) and it is also helpful for you as it
will help you get more familiar with that area of code and will expose you to
how other people solve problems. In fact, reviewing the code of experienced
engine maintainers is a great way to get to know the codebase.

Here are some things to think about and look out for as you review the code:

* **Code only touches the areas announced in the PR (and the commit
  message).**

  It can be tempting to fix random things in the code, as you see them. However,
  this can quickly make a pull request difficult to review and can make it hard
  to dig through in the commit history. Small touch-ups next to the related area
  are alright, but often bugs that you can find along the way are better fixed
  in their own PRs.

* **Code properly uses Godot's own APIs and patterns.**

  Consistency is very important, and a solution that already exists in the
  codebase is preferable to an ad-hoc solution.

* **Are core areas affected by the change?**

  Sometimes a PR that is supposed to solve a local problem can have a
  far-reaching effect way outside of its scope. Usually it is best to keep code
  changes local to where the problem arises. If you think that the solution
  requires changes outside the scope of the problem, it is usually best to seek
  the opinion of a team leader who may have another idea for how to solve the
  problem.

4. Iterate with the contributor and improve the PR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Maintainers should provide feedback and suggestions for improvement if they spot
things in the code that they would like changed. Preferably, suggestions should
come in order of importance: first, address overall code design and the approach
to solving the problem, then make sure the code is complying with the engine's
best practices, and lastly, do the :ref:`code style review <doc_code_style_review>`.

.. note::

    **Communicate barriers to merging early in the review process.**

    If the PR has clear blockers or will likely not get merged for whatever other
    reason, that fact should be communicated as early and clearly as possible. We
    want to avoid stringing people along because it feels bad to say "sorry, no".

As you review pull requests, keep the Godot `Code of Conduct
<https://godotengine.org/code-of-conduct>`_ in mind. Especially the following:

* Politeness is expected at all times. Be kind and courteous.

* Always assume positive intent from others.

* Feedback is always welcome, but keep your criticism constructive.

Here are some things to avoid as you iterate on a pull request with a
contributor:

* **Needless double reviews.**

  In other words, review the full PR at once and avoid coming back endless times
  to point out issues that you could have noted in the first review. Of course,
  this can't always be avoided, but we should try to catch everything at once.

* **Being overly nitpicky.**

  Code quality can be flexible depending on the area of the engine you are
  working in. In general, our standard for code quality is much higher in core
  areas and in performance-sensitive areas than it is in editor code for
  example.

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

5. Approve the pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After reviewing the code, if you think that the code is ready to be merged into
the engine, then go ahead and "approve" it. Make sure to also comment and
specify the nature of your review (i.e. say whether you ran the code locally,
whether you reviewed for style as well as correctness, etc.). Even if you are
not an engine maintainer, approving a pull request signals to others that the
code is good and likely solves the problem the PR says it does. Approving a pull
request as a non-engine maintainer does not guarantee that the code will be
merged, other people will still review it, so don't be shy.

.. _doc_code_style_review:

Code style review
-----------------

Generally speaking, we aim to conduct a code review before a style/clarity
review as contributors typically want to know if their general approach is
acceptable before putting in the effort to make nitpicky changes to style. In
other words, maintainers shouldn't ask contributors to change the style of code
that may need to be rewritten in subsequent reviews. Similarly, maintainers
should avoid asking for contributors to rebase PRs if the PR has not been
reviewed.

That being said, not everyone feels confident enough to provide a review on code
correctness, in that case, providing comments on code style and clarity ahead of
a more substantive code review is totally appropriate and more than welcome.

In practice the code style review can be done as part of the substantive code
review. The important thing is that both the substantive code and the code style
need to be reviewed and considered before a pull request is merged.

When reviewing code style pay particular attention to ensuring that the pull
request follows the :ref:`doc_code_style_guidelines`. While ``clang-format`` and
various CI checks can catch a lot of inconsistencies, they are far from perfect
and are unable to detect some issues. For example, you should check that:

  * The style of header includes is respected.
  * Identifiers use ``snake_case`` and follow our naming conventions.
  * Method parameters start with ``p_*`` or ``r_*`` (if they are used to return
    a value).
  * Braces are used appropriately, even for one-liner conditionals.
  * Code is properly spaced (exactly one empty line between methods, no
    unnecessary empty lines inside of method bodies).

.. note::

    This list is not complete and doesn't aim to be complete. Refer to
    the linked style guide document for a complete set of rules. Keep
    in mind that ``clang-format`` may not catch things you hope it would,
    so pay attention and try to build a sense of what exactly it can and
    cannot detect.
