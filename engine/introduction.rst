.. _doc_intro_to_engine_contributions:

Introduction to engine contributions
====================================

The possibility to study, use, modify and redistribute modifications of the
engine's source code are the fundamental rights that
Godot's `MIT <https://tldrlegal.com/license/mit-license>`_ license grants you,
making it `free and open source software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_.
As such, everyone is entitled to modify `Godot's source code <https://github.com/godotengine/godot>`_.

Contributing changes upstream has two big advantages:

-  Your code will be reviewed and improved by other developers. It will be
   further maintained in the upstream project, so you won't have to reapply
   your own changes every time you move to a newer version. On the
   other hand it comes with a responsibility, as your changes should be
   beneficial to all users; so in some cases it might still be better to
   keep your changes only for your own project by maintaining a fork.

-  The whole community will benefit from your work. Other contributors will
   behave the same way, contributing code that will be beneficial to you. At
   the time of this writing, over 2,000 developers have contributed code
   changes to the engine!


To ensure good collaboration and overall quality, the Godot developers document
rules and guidelines for the contribution process. You can find these in the
:ref:`doc_pull_request_guidelines` and :ref:`doc_engine_guidelines`.

You can contribute changes using the :ref:`PR workflow <doc_pr_workflow>`.
We value all contributions; however please note that PRs may :ref:`take a while <doc_when_will_a_pull_request_get_reviewed>`
to be reviewed. Critical bug fixes, as well as simple, relevant changes are reviewed with priority.
Read the :ref:`section below <doc_how_to_make_engine_contributions>` to find meaningful
changes to contribute.

.. _doc_how_to_make_engine_contributions:

What can I contribute?
----------------------

.. seealso::

    | This section explains how to make contributions to the engine as a C++ programmer.
    | See :ref:`How to contribute <doc_ways_to_contribute>` to find other ways to contribute to Godot.

You can theoretically propose and implement any kind of change to Godot. The community will discuss whether the change
is needed and appropriate, and will make suggestions for how to improve it. :ref:`Area maintainers <doc_areas>`
consider community demand, priority, and complexity, and make a decision about whether to accept it.

Even if you already have some specific change in mind, in many cases you should :ref:`report a bug <doc_reporting_issues>`
or :ref:`propose the change <doc_contributing_ideas>` first. These are useful for maintainers to understand the change,
and proposals especially are used to gauge community interest and challenge your solution idea.

If you would like to contribute, but don't have anything specific in mind, we recommend looking for simple, relevant,
and uncontroversial changes to contribute, especially at first.

A great place to start is by fixing bugs. Issues labeled as
`good first issue <https://github.com/godotengine/godot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__
are issues that maintainers think should be good for newcomers.

If you are knowledgeable or interested in a specific :ref:`area <doc_areas>`, you can browse its `bug reports <https://github.com/godotengine/godot/issues>`__
using the associated labels or by looking through `trackers <https://github.com/orgs/godotengine/projects/58>`__.
Some teams also maintain a :ref:`triage project <doc_triage_projects>`. This can be an especially effective way to make
meaningful contributions. Find triage projects linked in :ref:`doc_areas`.

Many contributors are interested in contributing :ref:`improvements or new features <doc_contributing_ideas>`. This
kind of contribution can be more difficult than fixing bugs, because changes need to be evaluated for priority and
complexity, and because they need to receive a healthy amount of discussion before they can be considered for merge.
You can learn more about our guidelines for new features in :ref:`doc_best_practices_for_engine_contributors`. New
features also have a lower priority than bug fixes, so they can take :ref:`longer to review <doc_when_will_a_pull_request_get_reviewed>`.
To find meaningful improvements to contribute, you can look for accepted improvements in the :ref:`teams <doc_areas>`'
:ref:`triage projects <doc_triage_projects>`, or you can browse the `proposal viewer <https://godot-proposals-viewer.github.io>`__
to find proposals with community interest. Keep in mind that, until a proposal is accepted, your pull request might not
be reviewed. It can often be better to engage with the proposal discussion before starting work to implement something.

Once you start gaining more experience, you can help with the :ref:`review process <doc_pr_review_guidelines>`. You
can find pull requests to review by browsing each :ref:`team's <doc_areas>` review requests and :ref:`triage projects <doc_triage_projects>`,
by browsing `pull requests <https://github.com/godotengine/godot/pulls>`__ and filtering by label,
or by exploring the `Godot team reports <https://godotengine.github.io/godot-team-reports>`__ and
`PRs by file <https://godotengine.github.io/godot-prs-by-file/>`__ websites.
