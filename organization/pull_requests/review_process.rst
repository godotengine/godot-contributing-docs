Review and merge process
========================

.. note::

    This page is intended to provide insight into the pull request (PR) review
    process that we aspire to. As such, it is primarily targeted at engine
    maintainers who are responsible for reviewing and approving pull requests.
    That being said, much of the content is useful for prospective contributors
    wanting to know how to ensure that their PR is merged.

From a high level, the ideal life cycle of a pull request looks like the
following:

  1. A contributor opens a PR that fixes a specific problem (optimally closing
     a GitHub `issue <https://github.com/godotengine/godot>`_ or implementing
     a `proposal <https://github.com/godotengine/godot-proposals>`_).

  2. Other contributors provide feedback on the PR (including reviewing and/or
     approving the PR, as appropriate).

  3. An engine maintainer reviews the code and provides feedback, requests
     changes, or approves the pull request, as appropriate.

  4. Another maintainer reviews the code with a focus on code style/clarity and
     approves it once satisfied.

  5. A team leader or a member of the `production team
     <https://godotengine.org/teams#production>`_ merges the pull request if
     satisfied that it has been sufficiently reviewed.

This document will explain steps 2, 3, 4, and 5 in more detail. For a more
detailed explanation of the pull request workflow please see the :ref:`pull
request workflow document <doc_pr_workflow>`.

.. note::
  In practice these steps may blend together. Oftentimes maintainers will
  provide comments on code style and code quality at the same time and will
  approve a pull request for both.

Typically the first interaction on a pull request will be an engine maintainer
assigning tags to the pull request and flagging it for review by someone
familiar with that area of code.

Engine maintainers are folks who are "members" of the Godot project repository
on GitHub and/or are listed on the `Teams page <https://godotengine.org/teams>`_
on the Godot website. Maintainers are responsible for a given area of the
engine. Typically this means they are the people who are given more trust to
approve and recommend pull requests for merging.

Even if you are not a maintainer, you can still help by reviewing code,
providing feedback on PRs and testing PRs locally on your machine to confirm
that they work as intended. Many of the currently active maintainers started out
doing this before they became maintainers.
