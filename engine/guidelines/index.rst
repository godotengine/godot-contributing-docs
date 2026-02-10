.. _doc_engine_guidelines:

Engine contribution guidelines
==============================

This section explains guidelines for contributing to the engine.

.. toctree::
   :maxdepth: 1
   :name: sec-engine-contribution-guidelines

   best_practices
   optimization
   cpp_usage_guidelines
   code_style
   editor_style_guide
   gdscript_language_guidelines

.. _doc_handling_compatibility_breakages:

Handling compatibility breakages
--------------------------------

Godot follows a **major.minor.patch** versioning scheme, and each level carries
different expectations around compatibility:

Maintainers generally control what kind of feature is merged at which part of the dev cycle. That being said, you can expect the following kinds of changes to be merged per version:

- **Patch releases** (e.g. 4.3.1 to 4.3.2) should not break compatibility at all.
- **Minor releases** (e.g. 4.3 to 4.4) should generally not break compatibility, except to fix bugs. New features are added in backwards-compatible ways.
- **Major releases** (e.g. 4.x to 5.0) are rare and can include major changes that break compatibility.

When contributing changes to the engine, two types of compatibility matter:

- **Binary compatibility**: Existing compiled binaries (including GDExtensions)
  load and execute correctly without recompilation, and their runtime behavior
  does not change.
- **Source compatibility**: Existing source code (scripts, scenes, and
  GDExtension source) compiles and runs without modification after upgrading
  Godot.

If your change adds a parameter to a method, changes a return type, changes the
type of a parameter, or alters a default value, you need to implement a
`GDExtension compatibility method <https://docs.godotengine.org/en/stable/engine_details/development/handling_compatibility_breakages.html>`_.
The CI validation system checks for this automatically, and the pull request
cannot be merged until it passes.

.. note::

   Reviewers and area maintainers examine PRs with the ``breaks compat`` label
   more closely, checking whether the breakage is justified and whether the
   compatibility methods are correctly implemented.
