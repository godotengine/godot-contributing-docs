.. _doc_release_translation_workflow:

Translation workflow
====================

.. TODO

Editor Strings
--------------

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

* Clone the Weblate git repository used for these components locally: `https://hosted.weblate.org/git/godot-engine/godot-properties/`_

  * It's named ``godot-properties`` for historical reasons, but includes all three components. Name your local clone ``weblate-editor-l10n``.

* Clone the main repository where we sync the translations manually: `https://github.com/godotengine/godot-editor-l10n`_

  * Initialize the godot submodule with ``git submodule update --init``.

* Go to the ``#repository`` tab on each of the three Weblate components (Editor, Properties, Class Reference).

* Press "Commit" on any of them to commit pending changes (this commits for all three components that share the same repository).

* Press "Lock" on all three components to prevent translators pushing more changes while you're doing a sync.

* Pull the newly committed translations in your local ``weblate-editor-l10n`` clone.

* Copy Weblate translations to ``godot-editor-l10n``. Assuming both clones are next to each other, go to ``godot-editor-l10n`` and do:

  ::

    for component in classes editor extractable properties; do
      cp ../weblate-editor-l10n/$component/*.po $component/
    done

* Check the ``git diff`` to make sure it looks as expected. In general, remember to check ``git diff`` after each stage as any mishap in these sync steps
  can lead to losing translators' work.

* Check ``git status`` to see if new languages were added. If yes, check on Weblate that they aren't empty.
  Users will sometimes just add languages on Weblate if they are missing, without actually being motivated enough to do the work.
  0% complete translations that churn every time we update the POT files just makes the Git repo bigger for no reason.
  Sometimes, people also add regional language variants which may or may not be warranted, e.g. ``fr_FR`` vs ``fr``.
  French doesn't have big enough regional variants to warrant making region-specific branches for hundreds of thousands of strings
  (at least not restarting from 0%).
  So you can simply delete the new PO files in that case instead of committing them.
  Check with `#translation <https://chat.godotengine.org/channel/translation>`__ if in doubt.

* Commit changes with the message: ``Sync translations with Weblate``.

* Update the ``godot`` submodule to the latest commit.

  * We keep the ``godot`` submodule on the latest stable branch during the early stages of development for the next feature branch,
    this way we can provide updated translations in maintenance releases.

  * Around beta time we switch back to ``master`` to add all the new and updated strings that translators should work on for the next feature release.

* Update all POT files for each translation component with:

  ::

    for component in classes editor extractable properties; do
      make -C $component update
    done

* Merge the POT files update into their respective PO files with:

  ::

    for component in classes editor extractable properties; do
      make -C $component merge
    done

* Once it's done, export all updated translations to the ``godot`` submodule:

  ::

    for component in classes editor extractable properties; do
      make -C $component export
    done

* *Optional:* At this stage, it can be good to validate that the class reference translations aren't malformed and can be converted with ``doc/tools/make_rst.py``.
  See :ref:`below <doc_release_translation_workflow_validating_class_reference_translations>` for details.

* In the ``godot`` submodule, commit the modified translations as ``Sync translations with Weblate``. Push this commit directly upstream.

* In ``godot-editor-l10n``, stage and commit everything as ``Merge and export translations for \<version\> branch``.

* Push commits.

* On Weblate, on one of the three components, hit "Reset and discard".

  * This is a slow process, you can check the update progress at `https://hosted.weblate.org/progress/godot-engine/godot-properties/?info=1`_

  * Once the update is done, unlock all three components, and notify that a sync was done in `#translation <https://chat.godotengine.org/channel/translation>`_.

.. _doc_release_translation_workflow_validating_class_reference_translations:

Validating class reference translations for ``make_rst.py``
-----------------------------------------------------------

Translators often make mistakes in the class reference translations around BBCode markup, e.g., translating things like ``[constant ...]`` or ``[ClassName]``.
This can be validated before pushing the changes upstream by running ``make_rst.py``, but it's a bit convoluted. Here is the process:

* After running ``make export`` to have the updated PO files in the ``godot`` submodule of ``godot-editor-l10n``,
  build the engine from source in that submodule.

* Clone `godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`_ alongside ``godot-editor-l10n``.

  * This is where we include the RST versions of the class reference for a selection of languages, as well as the Weblate translations for the docs
    (see update process :ref:`below <doc_release_translation_workflow_documentation>`).

* From the ``godot`` submodule of ``godot-editor-l10n``, with a compiled binary, run ``../../godot-docs-l10n/classref_export.sh``.

* Check the output of that script to see if ``make_rst.py`` reports any errors for any of the languages.
  ``ru`` and ``uk`` are known to have a lot of errors currently, but others can be kept error free.

* Either report the errors to translators in `#translation <https://chat.godotengine.org/channel/translation>`_,
  or fix them yourself in the main ``.po`` files in ``godot-editor-l10n``, then re-run ``make update`` and ``make export``.
  You can then redo the above steps (including compiling Godot to get the fixed translations) until it's error free.

* If you decide to fix them yourself, make sure to do all this work before pushing upstream and resetting the Weblate repo.

.. _doc_release_translation_workflow_documentation:

Documentation
-------------

.. TODO
