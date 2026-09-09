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

Checklist for new contributors
------------------------------

By reading this list, you can make a great first impression as a new contributor:

- **Test your pull request.** The code you submit might be used by tens of
  thousands of users. At the very least, please test it to avoid any surprises.
- **Disclose the use of AI.** If you use AI, you :ref:`need to tell us <doc_ai_assisted_contributions>`.
  AI-written code and descriptions have risks, so if you care about the
  long-term health of Godot, please be transparent about how you created your
  contribution.
- **Set up local style checks.** The tests will fail on your pull request if
  it does not pass a style check. Save yourself some time and
  :ref:`set up local style checks <doc_prek>`.
- **Keep it simple.** We :ref:`intentionally avoid <doc_cpp_disallowed_features>`
  using complex C++ features unless necessary. In most cases, avoid using
  clever solutions if a simple solution does the trick.
- **Adapt to the style of surrounding code.** Observe the code you are
  changing, and avoid changing it to suit your own personal preferences unless
  there is a tangible benefit.

For everything else, we have the :ref:`pull request rules <doc_pull_request_guidelines>`
and the :ref:`engine contribution guidelines <doc_engine_guidelines>`.
To become a proficient contributor, continue reading at your own leisure.

.. _doc_prek:

Setting up a dev environment
----------------------------

You can learn how to work with our source code using the `Engine development section <https://docs.godotengine.org/en/stable/engine_details/development/index.html>`__.

Additionally, we recommend you set up style checks locally.
For example, we use `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`__ and `clang-tidy <https://clang.llvm.org/extra/clang-tidy/>`__
to format our C++ code.
The easiest way to set them up is via `prek <https://prek.j178.dev/>`__.

You can install prek in your local Python installation using pip using the shell code below.
Depending on your system, there may be other ways to install it which you may prefer.

.. code-block:: shell

    pip install prek
    prek install

IDE integration
^^^^^^^^^^^^^^^

Learn how to configure an IDE in `respective Godot docs section <https://docs.godotengine.org/en/stable/engine_details/development/configuring_an_ide/index.html>`__.

You may also want to set up style checks with your IDE.
Most IDEs or code editors have beautifier plugins that can be configured to run
clang-format automatically, for example, each time you save a file.

Here is a non-exhaustive list of beautifier plugins for some IDEs:

- Qt Creator: Starting from version ``10.0``, the ClangFormat plugin is enabled by default.
  Follow the `Qt Creator configuration guide for Godot <https://docs.godotengine.org/en/stable/engine_details/development/configuring_an_ide/qt_creator.html#code-style-configuration>`__
  to set it up
- Visual Studio Code: `Clang-Format <https://marketplace.visualstudio.com/items?itemName=xaver.clang-format>`__
- Visual Studio: `Clang Power Tools 2022 <https://marketplace.visualstudio.com/items?itemName=caphyon.ClangPowerTools2022>`__
- vim: `vim-clang-format <https://github.com/rhysd/vim-clang-format>`__
- CLion: Starting from version ``2019.1``, no plugin is required. Instead, enable
  `ClangFormat <https://www.jetbrains.com/help/clion/clangformat-as-alternative-formatter.html#clion-support>`__

(Pull requests are welcome to extend this list with tested plugins.)
