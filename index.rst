Godot contributing documentation
================================

.. note:: This page documents how to contribute to Godot.
          Looking for the engine documentation instead? Visit
          `docs.godotengine.org <https://docs.godotengine.org/en/stable/>`__!

Learn how to contribute to `Godot Engine <https://godotengine.org>`__,
the free and open source community-driven 2D and 3D game engine!

The table of contents in the sidebar should let you find the documentation
for your topic of interest. You can also use the search function in the top-left corner.

.. _doc_ways_to_contribute:

If you are new, start by selecting the profile that best matches how you'd like to help with Godot.

.. raw:: html

    <style>
        .grid-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 0.375rem;
            grid-auto-flow: row;
            grid-template-areas:
            "new-to-game know-game-learn-godot"
            "know-godot-learn-godot contribute-to-godot";
        }

        .grid-item {
            padding: 1rem;
            border-radius: 0.375rem;
            text-align: center;
        }

        .grid-item,
        .grid-item:visited {
            color: hsla(0, 0%, 100%, 0.9);
        }

        .grid-item:hover,
        .grid-item:focus {
            text-decoration: none;
            filter: brightness(120%);
        }

        .grid-item:active {
            filter: brightness(80%);
        }

        .new-to-game {
            grid-area: new-to-game;
            background-color: #166534;
        }

        .know-game-learn-godot {
            grid-area: know-game-learn-godot;
            background-color: #115e59;
        }

        .know-godot-learn-godot {
            grid-area: know-godot-learn-godot;
            background-color: #1e3a8a;
        }

        .contribute-to-godot {
            grid-area: contribute-to-godot;
            background-color: #831843;
        }
    </style>
    <div class="grid-container">
        <a class="grid-item new-to-game" href="en/latest/ways_to_contribute/fundraising.html">
            <strong>Fundraising</strong><br>
            I'll help to sponsor Godot's development.
        </a>
        <a class="grid-item know-game-learn-godot" href="en/latest/ways_to_contribute/feedback.html">
            <strong>Feedback</strong><br>
            I'll report bugs and discuss ideas.
            </a>
        <a class="grid-item know-godot-learn-godot" href="en/latest/ways_to_contribute/development.html">
            <strong>Development</strong><br>
            I'll participate in Godot's development directly.
        </a>
        <a class="grid-item contribute-to-godot" href="en/latest/ways_to_contribute/ecosystem.html">
            <strong>Ecosystem</strong><br>
            I'll support Godot on my own terms.
        </a>
    </div>
    <br>

.. Below is the main table-of-content tree of the documentation website.
   It is hidden on the page itself, but it makes up the sidebar for navigation.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Ways to contribute
   :name: sec-introduction

   ways_to_contribute/fundraising
   ways_to_contribute/feedback
   ways_to_contribute/development
   ways_to_contribute/ecosystem

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Feedback guidelines
   :name: sec-providing-feedback

   feedback/issues/index
   feedback/ideas

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Development guidelines
   :name: sec-development

   development/contribution_rules
   development/workflows/index
   development/engine/index
   development/documentation/index
   development/translations
   development/other/index
