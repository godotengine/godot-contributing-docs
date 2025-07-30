Introduction to engine contributions
====================================

The possibility to study, use, modify and redistribute modifications of the
engine's source code are the fundamental rights that
Godot's `MIT <https://tldrlegal.com/license/mit-license>`_ license grants you,
making it `free and open source software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_.

As such, everyone is entitled to modify
`Godot's source code <https://github.com/godotengine/godot>`_, and send those
modifications back to the upstream project in the form of a patch (a text file
describing the changes in a ready-to-apply manner) or - in the modern workflow
that we use - via a so-called "pull request" (PR), i.e. a proposal to directly
merge one or more Git commits (patches) into the main development branch.

Contributing code changes upstream has two big advantages:

-  Your own code will be reviewed and improved by other developers, and will be
   further maintained directly in the upstream project, so you won't have to
   reapply your own changes every time you move to a newer version. On the
   other hand it comes with a responsibility, as your changes have to be
   generic enough to be beneficial to all users, and not just your project; so
   in some cases it might still be relevant to keep your changes only for your
   own project, if they are too specific.

-  The whole community will benefit from your work, and other contributors will
   behave the same way, contributing code that will be beneficial to you. At
   the time of this writing, over 2,000 developers have contributed code
   changes to the engine!

To ensure good collaboration and overall quality, the Godot developers
enforce some rules for code contributions, for example regarding the style to
use in the C++ code (indentation, brackets, etc.) or the Git and PR workflow.

A good place to start is by searching for issues tagged as
`good first issue <https://github.com/godotengine/godot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`_
on GitHub.

.. seealso:: Technical details about the PR workflow are outlined in a
             specific section, :ref:`doc_pr_workflow`.

             Details about the code style guidelines and the ``clang-format``
             tool used to enforce them are outlined in
             :ref:`doc_code_style_guidelines`.

All pull requests must go through a review process before being accepted.
Depending on the scope of the changes, it may take some time for a maintainer
responsible for the modified part of the engine to provide their review.
We value all of our contributors and ask them to be patient in the meantime,
as it is expected that in an open source project like Godot, there is going to be
way more contributions than people validating them.

To make sure that your time and efforts aren't wasted, it is recommended to vet the idea
first before implementing it and putting it for a review as a PR. To that end, Godot
has a `proposal system <https://github.com/godotengine/godot-proposals>`_. Its
usage is encouraged to plan changes and discuss them with the community. Implementation
details can also be discussed with other contributors on the `Godot Contributors Chat <https://chat.godotengine.org/>`_.

.. note:: Proposals are only required when working on an enhancement or a new feature.
          Bug reports are sufficient for fixing issues.
