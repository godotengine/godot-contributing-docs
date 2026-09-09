Participate in Godot's development
==================================

The engine development is coordinated by :ref:`teams <doc_areas>` and discussed on the `Godot Contributors Chat <https://chat.godotengine.org/>`__.
If you are serious about getting involved, you should join us there!

- **Engine code (mainly C++)**:
  If you are a programmer, you can contribute to Godot by :ref:`working on its source code <doc_ways_to_contribute_engine_code>`, or the source code of any :ref:`other repository <doc_development_other>`.
- **Documentation**:
  :ref:`Contribute documentation <doc_ways_to_contribute_documentation>` to improve the Godot Engine with your technical writing skills.
- **Translations (spoken languages other than English)**:
  Are you interested in making the Godot Engine more accessible to non-English speakers?
  Contribute to our :ref:`community translations <doc_editor_and_docs_localization>` on
  `Weblate <https://hosted.weblate.org/projects/godot-engine/godot/>`__.
- **Test and discuss pull requests**:
  Every change to Godot starts with a pull request, and all pull requests need feedback.
  Even without knowing how to program, you can help by :ref:`testing whether pull requests work as intended <doc_testing_pull_requests>`,
  by discussing whether new features are useful and appropriate, and giving feedback on how to improve fixes or new features.
- **Bugsquad & triage**:
  With so many bug reports and pull requests being opened each day, the :team:`Triage` — also called bugsquad — is
  invaluable to keep things organized.
  If you'd like to get involved, please visit :ref:`doc_bug_triage_intro`!

.. _doc_ways_to_contribute_engine_code:

Contribute engine code
~~~~~~~~~~~~~~~~~~~~~~

You can theoretically propose and implement any kind of change to Godot. The community will discuss whether the change
is needed and appropriate, and will make suggestions for how to improve it. :ref:`Area maintainers <doc_areas>`
consider community demand, priority, and complexity, and make a decision about whether to accept it.

Even if you already have some specific change in mind, in many cases you should :ref:`report a bug <doc_reporting_issues>`
or :ref:`propose the change <doc_contributing_ideas>` first. These are useful for maintainers to understand the change,
and proposals especially are used to gauge community interest and challenge your solution idea.

If you would like to contribute, but don't have anything specific in mind, look for simple, relevant,
and uncontroversial changes to contribute, especially at first. Here are some ideas:

- **Fix bugs.** A great place to start is by fixing bugs. Feel free to `browse issues <https://github.com/godotengine/godot/issues>`__ on the Godot repository, choose one, and just get started!
    - Issues labeled as `good first issue <https://github.com/godotengine/godot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__ are issues that maintainers think should be good for newcomers. However, these issues are claimed pretty quickly, so it's likely you won't find anything actionable here.
- **Add unit tests.** Many engine areas are not covered by unit tests. Feel free to `look yourself <https://github.com/godotengine/godot/tree/master/tests>`__ or browse the `unit test tracker <https://github.com/godotengine/godot/issues/43440>`__. Find a guide to add unit tests in the `engine docs <https://docs.godotengine.org/en/stable/engine_details/architecture/unit_testing.html>`__.
- **Contribute to an area.** If you are knowledgeable or interested in a specific :ref:`area <doc_areas>`, you can browse its `bug reports <https://github.com/godotengine/godot/issues>`__ using the associated labels or by looking through `trackers <https://github.com/orgs/godotengine/projects/58>`__. Some teams also maintain a :ref:`triage project <doc_triage_projects>`. This can be an especially effective way to make meaningful contributions. Find triage projects linked in :ref:`doc_areas`.
- **Contribute improvements or new features.** You can find popular `open proposals <https://godot-proposals-viewer.github.io>`__ or `propose your own <https://github.com/godotengine/godot-proposals>`__. The :ref:`bar for adding new features <doc_best_practices_for_engine_contributors>` is high, so is is usually better to engage with proposal discussions before starting work to implement something. Please note that we :ref:`do not accept feature PRs from new contributors <doc_new_contributor_rules>`.
- **Review pull requests.** Godot's development is bottlenecked by :ref:`reviews <doc_pr_review_guidelines>`. You can find pull requests to review by browsing each :ref:`team's <doc_areas>` review requests and :ref:`triage projects <doc_triage_projects>`, by browsing `pull requests <https://github.com/godotengine/godot/pulls>`__ and filtering by label, or by exploring the `Godot team reports <https://godotengine.github.io/godot-team-reports>`__ and `PRs by file <https://godotengine.github.io/godot-prs-by-file/>`__ websites.

.. _doc_ways_to_contribute_documentation:

Contribute documentation
~~~~~~~~~~~~~~~~~~~~~~~~

Start contributing in the :ref:`areas <doc_areas>` that you are most familiar with.
This ensures that the added description will be based on experience and the
necessary know-how, not just the name of a method or a property. We advise not to
add low effort descriptions, no matter how appealing it may look. Such descriptions
obscure the need for documentation and are hard to identify automatically.

.. seealso::

    Following this principle is important and allows us to create tools for contributors.
    Such as the class reference's `completion status tracker <https://godotengine.github.io/doc-status/>`_.
    You can use it to quickly find documentation pages missing descriptions.

If you decide to document a class, but don't know what a particular method does, don't
worry. Leave it for now, and list the methods you skipped when you open a pull request
with your changes. Another writer will take care of it.

You can still look at the method's implementation in Godot's source code on GitHub.
If you have doubts, feel free to ask on the `Godot Forum <https://forum.godotengine.org/>`_
and `Godot Contributors Chat <https://chat.godotengine.org/>`_.

.. warning::

    Unless you make minor changes, like fixing a typo, we do not recommend using the
    GitHub web editor to edit the class reference's XML files. It lacks features to edit
    XML well, like keeping indentations consistent, and it does not allow amending commits
    based on reviews.

    It also doesn't allow you to test your changes in the engine or with validation
    scripts as described in the `class reference documentation <https://docs.godotengine.org/en/latest/engine_details/class_reference/index.html>`__.
