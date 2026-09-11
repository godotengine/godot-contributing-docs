.. _doc_release_cycle_checklists:

Release cycle checklists
========================

.. note::

    This section is targeted at maintainers. For a general outline of the release
    cycle, please see :ref:`doc_release_cycle_outline`.

Required steps
--------------

This is a list of specific steps or checkpoints during the release cycle and what needs to be done
at each step.

Feature Freeze
~~~~~~~~~~~~~~

After feature freeze the following processes should start if they have not already been started:

* Writing a "Migrating from X to Y" page.
* Updating the list of features in the documentation.
* Drafting the release blog, including gathering assets to use on the page such as images and videos.
* Ensuring that new features or major changes have the necessary documentation either merged, in progress,
  or planned to ensure documentation is available for release.

Release Candidates
~~~~~~~~~~~~~~~~~~

.. TODO

Release
~~~~~~~

* In the `godot-headers <https://github.com/godotengine/godot-headers>`_ repo.

  * Update the ``master`` branch to include the latest ``extension_api.json`` and ``gdextension_interface.h`` output.
  * Create a new branch for the new release.

* In the ``godot`` repository:

  * :ref:`Sync translations <doc_release_translation_workflow>`
    .. TODO: Align link to workflow

  * Update ``CHANGELOG.md`` with the contents of the interactive changelog.
    .. TODO: Add further details on this

  * Bump ``version.py`` in a *dedicated commit*, changing ``status = "stable"`` and ``docs = "4.x"`` (matching the current release),
    with a commit message on the form:

    ::

      Bump version to 4.x-stable \o/

      <maintainer writeup from the release page's blogpost for major/minor releases>

      See the release page for details: https://godotengine.org/releases/4.x/

  * Create a **lightweight** Git tag pointing to the SHA and push it.
    There should be no existing branch with the same name as the tag (taken from the 4.7 release):

    ::

      git tag -f 4.7-stable 5b4e0cb0fd279832bbdd69fed5354d4e5ad26f88
      git push upstream 4.7-stable

  * Bump the development version again to ``status = "dev"`` and ``docs = "4.x"``
    (matching the *new* development version, so if releasing ``4.7`` it should be ``4.8`` here).

.. TODO: Add more details here

* In the ``godot-docs`` repository:

  * :ref:`Documentation workflow <doc_release_documentation_workflow>`

* In the ``godot-website`` repository:

  * Publish the blog post.

.. TODO:

    Steps to be clarified:

    * Steam release

    * Update priority projects

    * Update merge queue logic

.. _doc_release_cycle_translations:

Translations
------------

In order for the editor to be translated properly there needs to be time for translators to work.
Translations shouldn't be uploaded unnecessarily but if there are major changes or more critical changes after
feature freeze the source strings should be updated to make sure that there is time to translate them before release.

.. TODO: Any need to update the source strings more often, i.e. at intervals during the dev phase?

.. TODO: Add details on the actual process here.
