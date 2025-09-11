.. _doc_updating_the_contributing_docs:

Contributing to the contributing docs
=====================================

The contributing documentation documents how people can best contribute
to Godot. It is the website you are looking at right now!

Because Godot is driven by public contributions, we'd like to see this
documentation evolve and improve by contributions of its own. Community
involvement is just as welcome on this site as in the rest of Godot's
documentation!

If you'd like to submit an idea for a change of guidelines or operations,
please consider proposing it as an :ref:`idea <doc_contributing_ideas>`
instead of attempting to change the docs directly.

Making changes to the contributing docs
---------------------------------------

The information on this site are managed in a GitHub repository
(`github.com/godotengine/godot-contributing-docs <https://github.com/godotengine/godot-contributing-docs>`__).
You can contribute to this repository using our regular
:ref:`PR workflow <doc_pr_workflow>`. Please adhere to our
:ref:`documentation guidelines <doc_documentation_guidelines>` when making
changes.

To get started quickly, visit any article on this site and click the "Edit
on GitHub" button in the top right of the page.

What kinds of information are documented here?
----------------------------------------------

This page is intended for people who are interested in contributing to
Godot. They should be able to quickly find out how they can contribute,
be guided to confidently make their first contributions, and be able to
find all the relevant guidelines to become proficient contributors.

It can be difficult to determine if any piece of information should be
documented here or elsewhere. Consider reading the following examples
to get an idea.

The following kinds of information **should** be documented here:

* The expected workflow for contributing to any area of Godot (engine, documentation, etc.).
* The guidelines for contributing to any project.
* Organizational structures (tools and teams) of Godot contributors.

The following kinds of information **should not** be documented here:

* Information that is relevant to regular users of Godot (not just potential contributors).
    * Please document this in `docs.godotengine.org <https://docs.godotengine.org>`__
* Information that changes across different versions of Godot.
    * Please document this in `docs.godotengine.org <https://docs.godotengine.org>`__
* Technical information about any of Godot's repositories.
    * Please document this in the respective repositories.

How is this page structured?
----------------------------

This page is structured such that it is easy to find the different ways
in which you can contribute to Godot. To accomplish this, every *kind*
of contribution should have a dedicated section in the side bar. If a new
way to contribute emerges, it should get a dedicated section in the side
bar so that it is easy to find.

Building the documentation locally
----------------------------------

You may want to test your changes locally before making a pull request.
To do this, you first need to install `Python <https://www.python.org>`__, if it is not already installed.
We recommend you use a virtual environment to install the required packages:

.. code-block:: shell

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

You can build and serve the documentation by running the following commands:

.. code-block:: shell

    source .venv/bin/activate
    make html
    cd build/html
    python -m http.server
