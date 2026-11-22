.. _doc_handling_compatibility_breakages:

Handling compatibility breakages
================================

Godot's developers are committed to ensure backwards compatibility as best as feasible in ``patch``
and ``minor`` releases. For an overview in expectations, please see `Godot release policy <https://docs.godotengine.org/en/stable/about/release_policy.html>`__.

This article describes how best to achieve this.

How to approach a change that needs a compatibility break
---------------------------------------------------------

First, establish a consensus for the change: propose it on `godot-proposals <https://github.com/godotengine/godot-proposals>`__,
engage in the discussion, and see that you find a version that the community and maintainers
agree is better than the status quo.

Once consensus is established, make the change as soon as feasible. If possible, target the
next ``minor`` version, but implement it in a way that doesn't break projects which rely on
the old behavior.

This can be difficult, but consider the following guidelines:

- **Replace a feature or a system:** Add the feature under a new name, and deprecate the old
  feature. The old feature will be removed on the next ``major`` release.
- **Remove a feature with no replacement:** Deprecate the feature now, but don't remove it.
  It will be removed on the next ``major`` release.
- **Change behavior of a function:** If no backwards compatibility can be guaranteed, add the
  new version as a new function, and deprecate the existing function.
- **Change the signature of an exposed method:** Avoid removing parameters
  or changing their respective meanings. If you add parameters, provide a default value that
  doesn't change behavior. In all cases, you need to add a `GDExtension compatibility method <https://docs.godotengine.org/en/stable/engine_details/development/handling_compatibility_breakages.html>`_.

- **When no feasible backwards compatibility path can be provided:** First establish that the
  change is necessary. Consider providing adding a *project setting* that flips the behavior
  (defaulting to the old for existing projects, and to the new for new projects by modifying ``EditorNode::get_initial_settings()`` in ``editor/editor_node.cpp``),
  or a hook in the ``ProjectUpgradeTool`` which makes the update easier.

    - For import options and export options, changing the default value can be done
      without breaking compatibility, as ``.import`` files and ``export_presets.cfg``
      always store default values. This means changing the default value will keep
      values in existing projects unchanged.

.. note::

    Forwards compatibility (for example, opening a Godot 4.4 project in Godot 4.3) is not a
    priority, and is supported only on a best-effort basis.

Examples of compatibility breaking changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``patch`` releases, we generally avoid any kind of backwards compatibility
breakage unless absolutely necessary. Beyond that, most low-risk bug fixes
are eligible.

For ``minor`` versions, the following examples of minor compatibility breaks are
acceptable:

- Renaming a method parameter. In C#, method parameters can be passed by name
  (but not in GDScript). As a result, this can break some projects that use C#.
- Deprecating a method, member variable, or class.
- Bug fixes which substantially change the behavior or the output, with the aim
  to meet user expectations better. This is only acceptable if the change unblocks
  substantially more projects than it breaks.
- Improvements or optimizations that result in observable behavior changes, as long
  as this does not plausibly break many projects and the improvement is worth that
  risk.
- Inserting a class to an Object's inheritance tree.
- Changes to the `module APIs <https://docs.godotengine.org/en/stable/engine_details/engine_api/custom_modules_in_cpp.html>`__.

The following changes are considered **compatibility-breaking** and must wait
for a ``major`` release:

- Renaming or removing a method, member variable, or class. Deprecate it instead,
  and it will be removed in the next ``major`` release.
- Remove a class from an Object's inheritance tree.
- Change the binary size of a ``Variant`` type.

Adding features that plausibly need to change in the future
-----------------------------------------------------------

If a feature is needed but there is no consensus on finalizing the API or behavior for it,
mark the feature as ``experimental``. ``experimental`` features can change version-by-version,
so using this flag allows Godot developers to put out a feature for wide testing and feedback
without setting its behavior into stone as usually required by our compatibility guarantees.

Once there is decent confidence about the feature's behavior and design, the ``experimental``
flag should be removed.
