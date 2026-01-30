.. _doc_godot_cpp:

Contributing to godot-cpp
=========================

.. seealso::

    You may also be interested in visiting godot-cpp's official documentation:
    `C++ (godot-cpp) on the Godot docs <https://docs.godotengine.org/en/latest/tutorials/scripting/cpp/index.html>`__

Thank you for your interest in contributing to `godot-cpp <https://github.com/godotengine/godot-cpp>`__,
the official C++ GDExtension bindings maintained as part of the Godot project!
We greatly appreciate help in maintaining and extending this project.

If you wish to help out, ensure you have an account on GitHub and create a "fork" of the
`godot-cpp repository <https://github.com/godotengine/godot-cpp>`__.
To contribute, please use our regular :ref:`PR workflow <doc_pr_workflow>`.
The code should adhere to the same :ref:`code guidelines <doc_engine_guidelines>` as the engine itself.

Please install clang-format and the `pre-commit <https://pre-commit.com/>`__ Python framework so formatting is done
before your changes are submitted. See the :ref:`code style guidelines <doc_code_style_guidelines>` for instructions.

Feature guidelines
------------------

godot-cpp's API is modeled after Godot's API. We want writing godot-cpp code to be as similar as possible
to writing a
`module <https://docs.godotengine.org/en/stable/engine_details/engine_api/custom_modules_in_cpp.html#doc-custom-modules-in-cpp>`__.
This means:

* The frameworks (templates, helper methods, etc.) are synchronized to Godot's frameworks regularly.
* We will not add features that are not already present in Godot. If you want to add new features
  to godot-cpp's API, please consider proposing the feature to Godot itself first.

If you want to make changes to Godot's API, you can use one of two systems:

* `Core features <https://docs.godotengine.org/en/latest/tutorials/scripting/index.html#core-features>`__: You can add
  new methods and classes to Godot's core features. This exposes the new functionality on godot-cpp as well.
  To get started, please see :ref:`doc_intro_to_engine_contributions`.
* `GDExtension API <https://docs.godotengine.org/en/latest/tutorials/scripting/gdextension/index.html>`__: You can add
  GDExtension lifecycle methods to the GDExtension API itself. We do not have an article for this kind of change as of
  yet.
