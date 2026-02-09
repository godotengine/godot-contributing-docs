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

- **Patch releases** (e.g. 4.3.1 to 4.3.2) must not break compatibility at all.
  Existing projects, scripts, and GDExtensions should continue to work without
  any changes.
- **Minor releases** (e.g. 4.3 to 4.4) aim to preserve compatibility, but small,
  targeted breakages may occur in specific areas when necessary to fix
  high-priority issues. The vast majority of projects should not be affected.
- **Major releases** (e.g. 4.x to 5.0) may introduce significant compatibility
  breakages that require porting work.

When contributing changes to the engine, two types of compatibility matter:

- **Binary compatibility**: Existing compiled binaries (including GDExtensions)
  load and execute correctly without recompilation, and their runtime behavior
  does not change.
- **Source compatibility**: Existing source code (scripts, scenes, and
  GDExtension source) compiles and runs without modification after upgrading
  Godot.

If your change modifies a method signature in any way (even adding an optional
parameter with a default value), you must implement a **GDExtension compatibility
method**. Most language bindings use raw method pointers and handle
default parameters in the binding itself, so even seemingly backward-compatible
signature changes break existing binaries.

The CI validation system checks for these breakages automatically. If a function
has changed and no compatibility method exists, the pull request cannot be merged.

.. note::

   Reviewers and area maintainers examine PRs with the ``breaks compat`` label
   more closely, checking whether the breakage is justified and whether the
   compatibility methods are correctly implemented.

For the full technical details on implementing compatibility methods, handling
removed or renamed methods, and the GDExtension compatibility promise, see the
`current documentation for compatibility breakages <https://docs.godotengine.org/en/stable/engine_details/development/handling_compatibility_breakages.html>`_.
