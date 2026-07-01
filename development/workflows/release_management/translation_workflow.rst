.. _doc_release_translation_workflow:

Translation workflow
====================

Godot translations are managed on Weblate as four different components with two source repositories:

- `godot-editor-l10n <https://github.com/godotengine/godot-editor-l10n>`_

  - Editor: `godot-engine/godot/ <https://hosted.weblate.org/projects/godot-engine/godot/>`_
  - Properties: `godot-engine/godot-properties/ <https://hosted.weblate.org/projects/godot-engine/godot-properties/>`_
  - Class Reference: `godot-engine/godot-class-reference/ <https://hosted.weblate.org/projects/godot-engine/godot-class-reference/>`_

- `godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`_

  - Documentation: `godot-engine/godot-docs/ <https://hosted.weblate.org/projects/godot-engine/godot-docs/>`_

.. _doc_release_translation_workflow_editor::

Editor / Properties / Class Reference
-------------------------------------

The source repository for these is `godot-editor-l10n <https://github.com/godotengine/godot-editor-l10n>`_.
It serves as an intermediate place to keep all translations done via Weblate.
After syncing updated strings from Weblate and new strings from Godot,
we run ``make export`` to copy only the PO files with a high enough completion ratio to the main Godot repo.
This export process also strips fuzzy strings or comments to keep the file size minimal.

Update process
~~~~~~~~~~~~~~

The steps on Weblate need to be done by someone with admin permissions.
The steps on ``godot-editor-l10n`` need to be done by the same person,
who should have write permissions on that repo and on ``godotengine/godot``.

The goal is to retrieve the latest translations from Weblate, commit them in ``godot-editor-l10n``,
update the POT files with the latest Godot changes, export the translations to Godot, and commit all this again.
Then the Weblate git repository is hard reset on ``godot-editor-l10n`` to get the new strings and cleaned up history.
Weblate uses an intermediate repository where translators' work is committed directly,
and to reduce churn we do this manual update process every once in a while.

.. important::

  The reset on Weblate is a destructive operation, so make sure to follow the steps below thoroughly
  so all newly translated strings since the last sync are properly committed in ``godot-editor-l10n``.

- Clone the Weblate git repository used for these components locally: `godot-engine/godot-properties/ <https://hosted.weblate.org/git/godot-engine/godot-properties/>`_

  - It's named ``godot-properties`` for historical reasons, but includes all three components. Name your local clone ``weblate-editor-l10n``.

- Alongside it, clone the main repository where we sync the translations manually: `godotengine/godot-editor-l10n <https://github.com/godotengine/godot-editor-l10n>`_

  - Initialize the ``godot`` submodule with ``git submodule update --init``.

- Go to the ``#repository`` tab on each of the three Weblate components
  (`Editor <https://hosted.weblate.org/projects/godot-engine/godot/#repository>`_,
  `Properties <https://hosted.weblate.org/projects/godot-engine/godot-properties/#repository>`_, and
  `Class Reference <https://hosted.weblate.org/projects/godot-engine/godot-class-reference/#repository>`_).

- Press "Commit" on any of them to commit the pending changes (it commits for all three components that share the same repository).

- Press "Lock" on all three components to prevent translators pushing more changes while you're doing a sync.

- Pull the newly committed translations in your local ``weblate-editor-l10n`` clone.

- Copy the Weblate translations to ``godot-editor-l10n``. Assuming the clones are next to each other, go to ``godot-editor-l10n`` and do:

  .. code-block:: sh

    for component in classes editor extractable properties; do
      cp ../weblate-editor-l10n/$component/*.po $component/
    done

- Check ``git diff``/``git status`` to make sure it looks as expected. In general, remember to check the diff/status after each stage
  as any mishap in these sync steps can lead to losing translators' work.

  - Notably, ``git status`` would show untracked files if new languages have been added to some components on Weblate.
    Try to evaluate whether it's actually meaningful to keep those languages up for translation work,
    especially if they're regional variants for a language which doesn't really warrant duplicating the work for minor differences
    (e.g., ``fr`` or ``es`` variants may not be warranted, but ``pt`` or ``zh`` ones are).
    Deleting ``.po`` files instead of ``add``\ ing them would remove them from Weblate in later stages.
    When in doubt, ask in `#translation <https://chat.godotengine.org/channel/translation>`_.

- Commit the changes with the message: ``Sync translations with Weblate``.

- Update the ``godot`` submodule to the latest commit.

  - During early stages of development of the next feature branch, we keep the ``godot`` submodule on the latest stable branch,
    so we can provide updated translations in maintenance releases.

  - Around beta time, we switch back to ``master`` to add all the new and updated strings that translators should work on for the next feature release.

- Update all POT files for translation components with:

  .. code-block:: sh

    for component in classes editor extractable properties; do
      make -C $component update
    done

- Merge the POT files update into their respective PO files with:

  .. code-block:: sh

    for component in classes editor extractable properties; do
      make -C $component merge
    done

- Once it's done, export all updated translations to the ``godot`` submodule:

  .. code-block:: sh

    for component in classes editor extractable properties; do
      make -C $component export
    done

- *Optional:* At this stage, it can be good to validate that the class reference translations aren't malformed and can be converted with ``doc/tools/make_rst.py``.
  See :ref:`below <doc_release_translation_workflow_validating_class_reference_translations>` for details.

- In the ``godot`` submodule, commit the modified translations as ``Sync translations with Weblate``. Push this commit directly upstream.

- In ``godot-editor-l10n``, stage and commit everything as ``Merge and export translations for \<version\> branch``.

- Push commits.

- On Weblate, on one of the three components, hit "Reset and discard".

  - This is a slow process, you can check the update progress at `https://hosted.weblate.org/progress/godot-engine/godot-properties/?info=1`_.

  - Once the update is done, unlock all three components, and notify that a sync was done in `#translation <https://chat.godotengine.org/channel/translation>`_.


.. _doc_release_translation_workflow_validating_class_reference_translations:

Validating class reference translations for ``make_rst.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Translators often make mistakes in the class reference translations around BBCode markup, e.g., translating things like ``[constant ...]`` or ``[ClassName]``.
This can be validated before pushing the changes upstream by running ``make_rst.py``, but it's a bit convoluted. Here is the process:

- After running ``make export`` to have the updated PO files in the ``godot`` submodule of ``godot-editor-l10n``, build the engine from source in that submodule.

- Clone `godotengine/godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`_ alongside ``godot-editor-l10n``.

  - This is where we include the RST versions of the class reference for a selection of languages, as well as the Weblate translations for the docs
    (see the update process :ref:`below <doc_release_translation_workflow_documentation>`).

- From the ``godot`` submodule of ``godot-editor-l10n``, with a compiled binary, run ``../../godot-docs-l10n/classref-export.sh``.

- Check the output of that script to see if ``make_rst.py`` reports any errors for any of the languages.
  ``ru`` and ``uk`` are known to have a lot of errors currently, but others can be kept error free.

- Either report the errors to translators in `#translation <https://chat.godotengine.org/channel/translation>`_,
  or fix them yourself in the main ``.po`` files in ``godot-editor-l10n``, and re-run ``make update`` and ``make export``.
  You can then re-run the above steps (including compiling Godot to get fixed translations) until it's error free.

- If you decide to fix them yourself, make sure to do all this work *before* pushing upstream and resetting the Weblate repo.

.. _doc_release_translation_workflow_documentation:

Documentation (manual)
----------------------

The source repository for this is `godotengine/godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`_.
It serves as an intermediate place to keep all translations done via Weblate.

The documentation localization setup is a bit more complex than for other resources due to some technical and pipeline constraints:

- The documentation is written in reStructuredText in ``godot-docs`` and compiled as a static website via Sphinx.
  Sphinx supports internationalization via ``sphinx-intl``, generating one ``.pot`` file per page/``.rst`` file.

- For the translation workflow on Weblate, this would mean more than 500 components, each with their own set of languages, etc.
  For convenience, we decided to collate all these ``.pot`` files in a massive, monolithic file, which is the "Documentation" component on Weblate.

- This implies some conversion process to go from Sphinx to Weblate and back. ``godot-docs-l10n`` thus has the monolithic Weblate ``.pot`` and ``.po`` files in ``weblate/``,
  and the per-page Sphinx ``.pot`` and ``.po`` files in ``sphinx/``.
  The former is what users edit on Weblate, and the latter is what ReadTheDocs uses to build the localized instances of the documentation website.
  The Sphinx ``.pot`` files are merged into the monolithic Weblate ``.pot`` file, and the Weblate ``.po`` files need to be de-merged into individual per-page Sphinx ``.po`` files.

- The documentation website also includes the class reference (see :ref:`above <doc_release_translation_workflow_editor>` for its localization process).
  This implies a separate step to export localized ``.rst`` files from ``godot`` to ``godot-docs-l10n``.
  These already localized ``.rst`` files are used as-is for their respective languages, instead of going through the Sphinx localization process
  (which would require ``.po`` files for ``.rst`` content, while we have existing ``.po`` files for the XML source).

Update process
~~~~~~~~~~~~~~

The steps on Weblate need to be done by someone with admin permissions.
The steps on ``godot-docs-l10n`` need to be done by the same person, who should have write permission on that repo.
Ideally, that same person also has maintainer permissions on the ReadTheDocs project for each localized instance of the documentation website.

The goal is to retrieve the latest translations from Weblate, commit them in ``godot-docs-l10n``, update the POT files with the latest ``godot-docs`` changes,
update the localized class reference ``.rst`` files, and commit all this again.
Then the Weblate git repository is hard reset on ``godot-docs-l10n`` to get the new strings and cleaned up history.
Weblate uses an intermediate repository where translators' work is committed directly, and to reduce churn we do this manual update process every once in a while.

.. important::

  The reset on Weblate is a destructive operation, so make sure to follow the steps below thoroughly
  so all newly translated strings since the last sync are properly committed in ``godot-docs-l10n``.

- Clone the Weblate git repository used for these components locally: `godot-engine/godot-docs/ <https://hosted.weblate.org/git/godot-engine/godot-docs/>`_

  - Name your local clone ``weblate-docs-l10n``.

- Alongside it, clone the main repository where we sync the translations manually: `godotengine/godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`_

  - Initialize the ``docs`` (``godot-docs``) submodule with ``git submodule update --init``.

- Go to the ``#repository`` tab on the Weblate components: `Documentation <https://hosted.weblate.org/projects/godot-engine/godot-docs/#repository>`_.

- Press "Commit" to commit the pending changes.

- Press "Lock" to prevent translators pushing more changes while you're doing a sync.

- Pull the newly committed translations in your local ``weblate-docs-l10n`` clone.

- Copy the Weblate translations to ``godot-docs-l10n``. Assuming the clones are next to each other, go to ``godot-docs-l10n`` and do:

  .. code-block:: sh

    cp ../weblate-docs-l10n/weblate/*.po weblate/

- Check ``git diff``/``git status`` to make sure it looks as expected. In general, remember to check the diff/status after each stage
  as any mishap in these sync steps can lead to losing translators' work.

 - See note in the :ref:`editor localization steps <doc_release_translation_workflow_editor>` on how to handle new ``.po`` files.

- Commit the changes with the message: ``Sync translations with Weblate``.

- Update the ``docs`` submodule to the latest commit.

  - During early stages of development of the next feature branch, we keep the ``godot`` submodule on the latest stable branch,
    so we can provide updated translations for the current production documentation.

  - Around beta time, we switch back to ``master`` to add all the new and updated strings that translators should work on for the next feature release.

- Review the ``git`` output after updating the submodule to check if any ``.rst`` files have been added or removed.
  To generate the monolithic ``.pot`` file for Weblate, we use ``templates_list.txt`` to list all Sphinx ``.pot`` files that should be collated
  in the order of the table of contents. This makes the translation flow more naturally as translators are offered strings in the same order they may
  read the docs from start to finish.

  - Occasionally (especially when changing source branches with a lot of new content), it may be necessary to parse a generated ``index.html`` for ``godot-docs``
    to see what the current table of contents is. Copy it into the root of the repository and run ``./update.sh --templates-list``
    (short form: ``./update.sh -tl``) to regenerate ``templates_list.txt`` from an up-to-date ``index.html``.
    Note that the process isn't flawless and some files may be missing after the update (e.g., ``index.pot``, ``404.pot``, or some deeply nested sections).
    Review the ``git diff`` output and, when in doubt, compare with the live instance of the docs to see its table of contents.

- Update the Sphinx and Weblate POT files with:

  .. code-block:: sh

    ./update.sh --sphinx-pot
    ./update.sh --weblate-pot
    # Short form:
    ./update.sh -st
    ./update.sh -wt

- Commit this stage as ``Sync Sphinx and Weblate templates with current docs (<branch>)``.

- Update the Weblate PO files with:

  .. code-block:: sh

    ./update.sh --weblate-po
    # Short form:
    ./update.sh -wo

- Commit this stage as ``Sync Weblate translations with Weblate template``.

- Create the per-page Sphinx PO files by referencing the monolithic Weblate PO files as the source for translated strings with:

  .. code-block:: sh

    ./update.sh --sphinx-po
    # Short form:
    ./update.sh -so

- This step takes a while. Commit the results as ``Merge Sphinx translations with Weblate translations``.

- Finally, generate the localized class reference ``.rst`` files. This uses the :ref:`same workflow <doc_release_translation_workflow_validating_class_reference_translations>`
  used to validate the class reference translations with ``make_rst.py``.

  - Note that which languages have their class reference exported is hardcoded in the ``EXPORT_LANGS`` variable (which can be overridden in the environment).
    We only include class reference translations for languages for which we provide a localized documentation instance,
    and with a high enough completion ratio for their class reference docs.

  - Ensure you have ``godot-editor-l10n`` with its ``godot`` submodule compiled, next to ``godot-docs-l10n``.

  - Run the ``classref-export.sh`` script from ``godot-editor-l10n/godot``.
    Depending on the type of build you made, and the location of your repositories, you may need to adjust the ``GODOT_BIN`` and ``GODOT_DOCS_L10N`` variables
    (they can be overridden in the environment).

- Commit the results as ``Sync classref with <branch> branch``.

- Push the commits. This will trigger builds for all localized instances on ReadTheDocs, so only do this once you're done with the update.

  - ReadTheDocs only gives us two concurrent builds, and builds for each instance take around one hour.
    Other builds get queued but frequently end up timing out and being killed, so we need to restart them manually.

  - Log in to the `dashboard <https://app.readthedocs.org/dashboard/>`_ to see the status of each localized instance.
    If it shows that the build failed, it probably needs to be restarted manually.
    This can take several hours in total but can be done independently from resetting and unlocking the Weblate component.

- On Weblate, hit "Reset and discard".
  - This is a slow process, you can check the update progress at `https://hosted.weblate.org/progress/godot-engine/godot-docs/?info=1`_.

  - Once the update is done, unlock the component, and notify that a sync was done in `#translation <https://chat.godotengine.org/channel/translation>`_.
