.. _doc_code_style_guidelines:

Other language guidelines
=========================

Not all code in the Godot engine source code is written in C++. Find rules and guidelines for other
languages listed here.

GDScript
--------

We expect that, where possible, GDScript follows our
`GDScript style guide <https://docs.godotengine.org/en/4.4/tutorials/scripting/gdscript/gdscript_styleguide.html>`__.

Objective-C
-----------

Our Objective-c and Objective-c++ code should follow our :ref:`C++ guidelines <doc_cpp_usage_guidelines>`.

Some styles are also automatically enforced using our :ref:`pre-commit hooks <doc_pre_commit>`.

Java
----

Godot's Java code (mostly in ``platform/android``) is enforced via ``clang-format``.
It is automatically enforced using our :ref:`pre-commit hooks <doc_pre_commit>`.

Keep in mind that our style guide only applies to code written and maintained by Godot,
not third-party code such as the ``java/src/com/google`` subfolder.

Python
------

Godot's SCons buildsystem is written in Python, and various scripts included
in the source tree are also using Python. We use the
`Ruff linter and code formatter <https://docs.astral.sh/ruff/>`__ to format it.

We recommend you run ruff using our :ref:`pre-commit hooks <doc_pre_commit>`.

Alternatively, you can install and run Ruff separately.
