.. _doc_cpp_usage_guidelines:

C++ rules and guidelines
========================

To ensure the quality and coherence of the engine's codebase, the Godot
developers document rules and guidelines for C++ code.

Contributors are not expected to know and understand every detail, but
please try to do your best and familiarize yourself with our expectations,
especially if you make frequent or complex contributions.

.. tip::

    Like many aspects of Godot, our code style is subject to be challenged
    or expanded by the community. If you think it should be changed, please
    :ref:`make proposals <doc_contributing_ideas>` or submit pull requests
    using the :ref:`PR workflow <doc_pr_workflow>`.

.. admonition:: Third-party code

    Godot's code style should *not* be applied to third-party code,
    i.e. code that is included in Godot's source tree, but was not written
    specifically for our project. Such code usually comes from
    different upstream projects with their own style guides (or lack
    thereof), and we don't want to introduce differences that would make
    syncing with upstream repositories harder.

    Most third-party code is in the ``thirdparty/`` folder, where our
    automated style checks are configured not to run.

Automated style checks
----------------------

Most of our code style is automatically enforced with formatters (clang-format
and clang-tidy). If your code does not pass the style checks, the continuous
integration (CI) on your pull request will fail and your pull request cannot
be merged. We recommend you :ref:`set up local checks <doc_pre_commit>` to
save yourself some time.

This article focuses mostly on the parts of our style that are not automatically
enforced.

.. _doc_cpp_disallowed_features:

Disallowed features
-------------------

Since Godot 4.0, the C++ standard used throughout the codebase is a subset of
**C++17**. While modern C++ brings a lot of opportunities to write faster, more
readable code, we choose to restrict our usage of C++ to a subset for a few
reasons:

- **It makes it easier to review code in online editors.** This is because engine
  contributors often don't have access to a full-featured IDE while reviewing
  code.
- **It avoids bugs by keeping the complexity low.** New features might look fancy,
  but if nobody fully understands them, it leads to misuse and buggy code.
- **It makes the code easier to grasp for beginner contributors** (who may not be
  professional C++ programmers). Godot's codebase is known to be easy to learn
  from, and we'd like to keep it that way.

**Any feature not listed below is allowed.** Using features like ``constexpr``
variables and ``nullptr`` is encouraged when possible. Still, try to keep your
use of modern C++ features conservative. Their use needs to serve a real
purpose, such as improving code readability or performance.

- **Standard Template Library**:
  We don't allow using the `STL <https://en.wikipedia.org/wiki/Standard_Template_Library>`__
  as Godot provides its own data types (among other things).
  See `Why does Godot not use STL? <https://docs.godotengine.org/en/stable/about/faq.html#why-does-godot-not-use-stl-standard-template-library>`__ for more information.
  This means that pull requests should **not** use ``std::string``,
  ``std::vector`` and the like. Instead, use Godot's data types as described in
  the `Core types <https://docs.godotengine.org/en/latest/engine_details/architecture/core_types.html>`__ documentation.

- ``auto`` **keyword**:
  We do not allow the use of ``auto`` in the codebase, except in special cases
  where it is impossible to avoid.
  While many IDEs offer ways to inspect the type of ``auto`` variables, we need
  our code to be readable without these inspection features. For example, most
  contributors use GitHub's online code viewer to review code, which does not
  support type inspection.

- **Lambdas**:
  Lambdas should not be used, unless it cannot reasonably be avoided. Prefer using
  named ``inline`` functions.

- ``#ifdef`` **-based include guards**:
  Starting with Godot 4.5, we use ``#pragma once`` instead of ``#ifdef``-based include guards.

- ``try``-``catch`` **blocks**:
  C++ exception handling is disabled in our codebase.
  This makes it impossible to use ``try`` and ``catch`` blocks.
  Use `Common engine methods and macros <https://docs.godotengine.org/en/latest/engine_details/architecture/common_engine_methods_and_macros.html>`__ instead.
  This restriction is in place for several reasons, including performance, binary
  size, and code complexity.

Naming
------

- Types and namespaces use ``PascalCase``, and macros and constants use ``UPPER_SNAKE_CASE``.
  All other identifiers use ``snake_case``.
- Method parameters start with ``p_*``, or ``r_*`` (if they are used to return a value).
- Use full words. Avoid abbreviations except when the full name makes the code hard to read.
- Pointer and reference operators are affixed to the variable identifier, not
  to the type name.

Spacing
-------

- Indentation and alignment are both tab based (respectively one and two tabs).
- One space around math and assignments operators as well as after commas.
- Code is properly spaced (exactly one empty line between methods, no
  unnecessary empty lines inside of method bodies).

Header includes
---------------

- In a ``.cpp`` file (e.g. ``filename.cpp``), the first include should be the
  one where the class is declared (e.g. ``#include "filename.h"``), then the
  compatibility header if there is one (e.g. ``#include "filename.compat.inc``),
  followed by an empty line for separation.
- Then come headers from Godot's own code base, included in alphabetical order
  (enforced by ``clang-format``) with paths relative to the root folder. Those
  includes should be done with quotes, e.g. ``#include "core/object.h"``. The
  block of Godot header includes should then be followed by an empty line for
  separation. Within modules, relative includes are preferred.
- Next come third-party and system includes. Use regular quotes for thirdparty
  headers, but < and > symbols for system includes, e.g. ``#include <png.h>``.
  The block of third-party headers should also be followed by an empty line for separation.
- Godot and third-party headers should be included in the file that requires
  them, i.e. in the ``.h`` header if used in the declarative code or in the ``.cpp``
  if used only in the imperative code.

Comments
--------

This comment style guide applies to all programming languages used within
Godot's codebase.

- Begin comments with a space character to distinguish them from disabled code.
- Use sentence case for comments. Begin comments with an uppercase character and
  always end them with a period.
- Reference variable/function names and values using backticks.
- Wrap comments to ~100 characters.
- You can use ``TODO:``, ``FIXME:``, ``NOTE:``, ``WARNING:``, or ``HACK:`` as admonitions
  when needed.
- You can use Javadoc-style comments above function or macro definitions. Only use
  them for methods which are not exposed to scripting, because exposed methods should
  be documented in the :ref:`class reference XML <doc_updating_the_class_reference>`
  instead.
- For member variables, use single-line comments.
