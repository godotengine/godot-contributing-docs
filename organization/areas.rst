.. _doc_areas:

Areas and teams
===============

Godot is organized into areas, most of which has a designated team working on them.
This page lists these areas and explains their goals and how they're organized.

For each team or area there is a list of links and resources associated with them:

* **Communication**: links to the `RocketChat <https://chat.godotengine.org/>`__ channels for the team,
  joining this channel is the best way get involved with a team.
* **GitHub reviews**: opens a GitHub search for PRs that have a review request for the team.
  Note that this *doesn’t* show PRs that have already been reviewed by that team,
  any review comments at all, from any member of a specific team, will remove the request, so this is not always helpful.
* **GitHub labels**: lists any labels relevant to the team, and links to issues and PRs tagged with those tags.
  For more information about the different GitHub labels, please see the :ref:`doc_bug_triage_guidelines`.
  Note that some GitHub labels aren’t neatly covered by trackers.
* **Triage project**: links to the team triage project for the team.
* **Maintainers**: lists the members of each team. The area maintainers take ownership of the area, and will steer its
  development by creating and reviewing pull requests and improvement proposals. Maintainers are listed alphabetically.
  Maintainers written as ⭐ **Member** (with a star and in bold) are team leads.

You can find information about the teams' `current priorities <https://godotengine.org/priorities/>`__ on the Godot website.

.. As a guideline, a team is anything that:
   - People refer to as a team.
   - An area that has multiple facets, like a RocketChat channel and a GitHub team.

.. Regarding maintainers:
   - Generally, the maintainers should correspond to the respective GitHub teams.
   - "Members" are maintainers here, and "Maintainers" are team leads.
   - Before adding a maintainer, ask them if they want to be mentioned here.
   - In particular, ask them how they'd like to be referred to.
   - If you are a maintainer, you can also open a PR to add yourself, if you are on the respective GitHub team.

.. Html hyperlink targets cannot start with numbers. We're using a trick to override the default generated target: https://stackoverflow.com/a/65284203/503822
.. _2d:
.. _team-2d:

2D
--

.. gdareatable::
   :communication: #2d
   :github_reviews: @godotengine/2d-nodes
   :github_labels: <gh-label>topic:2d</gh-label>
   :maintainers: Gilles Roudière (@groud), Tomasz Chabora (@KoBeWi)

.. _3d:
.. _team-3d:

3D
--

.. gdareatable::
   :communication: #devel
   :github_reviews: @godotengine/3d-nodes
   :github_labels: <gh-label>topic:3d</gh-label>
   :maintainers: Hugo Locurcio (@Calinou), Joan Fons Sanchez (@JFonS)

Animation
---------

Nodes and features for 2D and 3D animation and IK workflows.

.. gdareatable::
   :communication: #animation
   :github_reviews: @godotengine/animation
   :github_labels: <gh-label>topic:animation</gh-label>
   :triage_project: <gh-triage project=74>Animation issue triage</gh-triage>
   :maintainers: <lead>Juan Linietsky (@reduz)</lead>, K. S. Ernest Lee (@fire), @Lyuma, @SaracenOne, Silc 'Tokage' Renew (@TokageItLab)

Audio
-----

All audio-related features, from low-level AudioServer and drivers to high-level nodes and effects.

.. gdareatable::
   :communication: #audio
   :github_reviews: @godotengine/audio
   :github_labels: <gh-label>topic:audio</gh-label>
   :triage_project: <gh-triage project=101>Audio issue triage</gh-triage>
   :maintainers: Adam Scott (@adamscott), Ellen Poe (@ellenhp), Juan Linietsky (@reduz)

Buildsystem
-----------

Tools and scripts that we use to compile and maintain Godot, both for development purpose (SCons, CI) and releases (official build containers).

.. gdareatable::
   :communication: #buildsystem
   :github_reviews: @godotengine/buildsystem
   :github_labels: <gh-label>topic:buildsystem</gh-label>
   :triage_project: <gh-triage project=53>Buildsystem issue triage</gh-triage>
   :maintainers: Fabio Alessandrelli (@Faless), HP van Braam (@hpvb), Hugo Locurcio (@Calinou), <lead>Rémi Verschelde (@akien-mga)</lead>, Thaddeus Crews (@Repiteo)

Core
----

Low-level Core API: Object, Variant, templates, base nodes like Node, Viewport, etc. (everything under ``core`` and ``scene/main``).

.. gdareatable::
   :communication: #core
   :github_reviews: @godotengine/core
   :github_labels: <gh-label>topic:core</gh-label>
   :triage_project: <gh-triage project=95>Core issue triage</gh-triage>
   :maintainers: George Marques (@vnen), HP van Braam (@hpvb), <lead>Juan Linietsky (@reduz)</lead>, @lawnjelly, Lukas Tenbrink (@Ivorius/@Ivorforce), Rémi Verschelde (@akien-mga)

Input
~~~~~

.. gdareatable::
   :communication: #input
   :github_reviews: @godotengine/input
   :github_labels: <gh-label>topic:input</gh-label>
   :maintainers: Rémi Verschelde (@akien-mga), Gilles Roudière (@groud)

Demos
-----

.. gdareatable::
   :communication: #demo-content
   :github_reviews: @godotengine/demos
   :maintainers: <lead>Aaron Franke (@aaronfranke)</lead>, Ilaria Cislaghi (@QbieShay), K. S. Ernest Lee (@fire), Rémi Verschelde (@akien-mga)

Documentation
-------------

Documentation for the engine and its systems.
Note that, while there is a dedicated documentation team, all other teams are expected to contribute to the documentation
for their area.

.. gdareatable::
   :communication: #documentation
   :github_reviews: @godotengine/documentation
   :github_labels: <gh-label>documentation</gh-label>
   :maintainers: A Thousand Ships (@AThousandShips), Clay John (@clayjohn), Hana - Piralein (@Piralein), Hugo Locurcio (@Calinou), Julian Murgia (@StraToN), <lead>Max Hilbrunner (@mhilbrunner)</lead>, Matthew (@skyace65), Micky (@Mickeon), Raul Santos (@raulsntos)

Editor
------

All things related to the editor, both tools and usability (editor).

.. gdareatable::
   :communication: #editor, #editor-design
   :github_reviews: @godotengine/2d-editor, @godotengine/3d-editor, @godotengine/debugger, @godotengine/docks, @godotengine/script-editor, @godotengine/usability
   :github_labels: <gh-label>topic:editor</gh-label>, <gh-label>topic:export</gh-label>, <gh-label>topic:plugin</gh-label>
   :triage_project: <gh-triage project=111>Editor issue triage</gh-triage>
   :maintainers: Fabio Alessandrelli (@Faless), George Marques (@vnen), Gilles Roudière (@groud), Hendrik Brucker (@Geometror), Hugo Locurcio (@Calinou), Joan Fons Sanchez (@JFonS), K. S. Ernest Lee (@fire), Kit Bishop (@kitbdev), Michael Alexsander (@YeldhamDev), Paul Batty (@Paulb23), Tomasz Chabora (@KoBeWi)

GUI
---

Everything that inherits Control (everything under ``scene/gui``) and can be used to build Graphical User Interfaces (both game UI and editor tools).

.. gdareatable::
   :communication: #gui
   :github_reviews: @godotengine/gui-nodes
   :github_labels: <gh-label>topic:gui</gh-label>
   :triage_project: <gh-triage project=100>GUI issue triage</gh-triage>
   :maintainers: Gilles Roudière (@groud), Hendrik Brucker (@Geometror), Kit Bishop (@kitbdev), Michael Alexsander (@YeldhamDev), Paul Batty (@Paulb23), Pāvels Nadtočajevs (@bruvzg), Rémi Verschelde (@akien-mga), Tomasz Chabora (@KoBeWi)

Import
------

Asset import pipeline for 2D (textures) and 3D (scenes, models, animations, etc.).

.. gdareatable::
   :communication: #asset-pipeline
   :github_reviews: @godotengine/import
   :github_labels: <gh-label>topic:import</gh-label>
   :triage_project: <gh-triage project=72>Asset pipeline issue triage</gh-triage>
   :maintainers: Aaron Franke (@aaronfranke), @BlueCube3310, Gordon MacPherson (@RevoluPowered), Hugo Locurcio (@Calinou), Joan Fons Sanchez (@JFonS), K. S. Ernest Lee (@fire), @Lyuma, Rémi Verschelde (@akien-mga)

Navigation
----------

.. gdareatable::
   :communication: #navigation
   :github_reviews: @godotengine/navigation
   :github_labels: <gh-label>topic:navigation</gh-label>
   :triage_project: <gh-triage project=103>Navigation issue triage</gh-triage>

Networking
----------

Networked multiplayer, RPCs and replication, HTTP/TCP/UDP/DNS, WebSockets, ENet, encryption.

.. gdareatable::
   :communication: #networking, #voip
   :github_reviews: @godotengine/network
   :github_labels: <gh-label>topic:network</gh-label>, <gh-label>topic:multiplayer</gh-label>
   :triage_project: <gh-triage project=96>Network issue triage</gh-triage>
   :maintainers: <lead>Fabio Alessandrelli (@Faless)</lead>, Max Hilbrunner (@mhilbrunner)

Physics
-------

Physics servers and their implementation in 2D and 3D.

.. gdareatable::
   :communication: #physics
   :github_reviews: @godotengine/physics
   :github_labels: <gh-label>topic:physics</gh-label>
   :triage_project: <gh-triage project=102>Physics issue triage</gh-triage>
   :maintainers: Fabrice Cipolla (@fabriceci), Juan Linietsky (@reduz), @lawnjelly, Mikael Hermansson (@mihe), Ricardo Buring (@rburing)

Platforms
---------

Platform specific layers that reside in ``platform``, with shared components (Unix, Win32, Apple, etc.) in ``drivers``.

.. gdareatable::
   :communication: #platforms
   :github_labels: <gh-label>topic:platforms</gh-label>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Android
~~~~~~~

.. gdareatable::
   :communication: #android
   :github_reviews: @godotengine/android
   :github_labels: <gh-label>platform:android</gh-label>
   :maintainers: Alexander Hartmann (@Alex2782), Anish (@syntaxerror247), <lead>Fredia Huya-Kouadio (@m4gr3d)</lead>, Rémi Verschelde (@akien-mga)
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Apple
~~~~~

.. gdareatable::
   :communication: #apple
   :github_reviews: @godotengine/ios, @godotengine/macos
   :github_labels: <gh-label>platform:ios</gh-label>, <gh-label>platform:macos</gh-label>, <gh-label>platform:visionos</gh-label>
   :maintainers: Bastiaan Olij (@BastiaanOlij), <lead>Pāvels Nadtočajevs (@bruvzg)</lead>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Web
~~~

.. gdareatable::
   :communication: #web
   :github_reviews: @godotengine/web
   :github_labels: <gh-label>platform:web</gh-label>
   :maintainers: <lead>Adam Scott (@adamscott)</lead>, Fabio Alessandrelli (@Faless)
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Windows / UWP
~~~~~~~~~~~~~

.. gdareatable::
   :communication: #platforms
   :github_reviews: @godotengine/uwp, @godotengine/windows
   :github_labels: <gh-label>platform:uwp</gh-label>, <gh-label>platform:windows</gh-label>
   :maintainers: <lead>George Marques (@vnen)</lead>, Max Hilbrunner (@mhilbrunner), <lead>Pāvels Nadtočajevs (@bruvzg)</lead>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Linux / BSD
~~~~~~~~~~~

.. gdareatable::
   :communication: #platforms
   :github_reviews: @godotengine/linux-bsd
   :github_labels: <gh-label>platform:linuxbsd</gh-label>
   :maintainers: Dery Almas (@deralmas), Fabio Alessandrelli (@Faless), HP van Braam (@hpvb), Rémi Verschelde (@akien-mga)
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Quality Assurance
-----------------

All things QA: unit/integration tests, static analysis, benchmarks, code style/quality, builds testing.

.. gdareatable::
   :communication: #quality-assurance, #benchmarks

Tests
~~~~~

Tests for the engine and its systems.
Note that, while there is a dedicated tests team, all other teams are expected to contribute to the tests
for their area.

.. gdareatable::
   :communication: #quality-assurance
   :github_reviews: @godotengine/tests
   :github_labels: <gh-label>topic:tests</gh-label>
   :maintainers: Hugo Locurcio (@Calinou), Gordon MacPherson (@RevoluPowered), Hendrik Brucker (@Geometror), Rémi Verschelde (@akien-mga)

Bugsquad / Issue triage
~~~~~~~~~~~~~~~~~~~~~~~

.. gdareatable::
   :communication: #bugsquad, #bugsquad-sprints
   :github_reviews: @godotengine/bugsquad
   :maintainers: <lead>A Thousand Ships (@AThousandShips)</lead>, K. S. Ernest Lee (@fire), @lawnjelly, Rémi Verschelde (@akien-mga)

Rendering
---------

Rendering server and RenderingDevice implementations (Vulkan, OpenGL), as well as the actual rendering techniques implemented using those graphics APIs.

.. gdareatable::
   :communication: #rendering
   :github_reviews: @godotengine/rendering
   :github_labels: <gh-label>topic:rendering</gh-label>
   :triage_project: <gh-triage project=78>Rendering issue triage</gh-triage>
   :maintainers: Bastiaan Olij (@BastiaanOlij), @BlueCube3310, <lead>Clay John (@clayjohn)</lead>, Hugo Locurcio (@Calinou), Joan Fons Sanchez (@JFonS), Juan Linietsky (@reduz), @lawnjelly, Skyth (Asilkan) (@blueskythlikesclouds), Stuart Carnie (@stuartcarnie)

Shaders
~~~~~~~

.. gdareatable::
   :communication: #rendering
   :github_reviews: @godotengine/shaders
   :github_labels: <gh-label>topic:shaders</gh-label>
   :triage_project: <gh-triage project=78>Rendering issue triage</gh-triage>
   :maintainers: Clay John (@clayjohn), Hendrik Brucker (@Geometror), Ilaria Cislaghi (@QbieShay), Patrick Exner (@paddy-exe), Skyth (Asilkan) (@blueskythlikesclouds), Yuri Rubinsky (@Chaosus)

VFX / Tech Art / Particles
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gdareatable::
   :communication: #vfx-tech-art
   :github_reviews: @godotengine/rendering, @godotengine/shaders
   :github_labels: <gh-label>topic:particles</gh-label>
   :triage_project: <gh-triage project=115>Particles issue triage</gh-triage>

Scripting
---------

Umbrella team for all the scripting languages usable with Godot.
Encompasses some shared core components (Object, ClassDB, MethodBind, ScriptLanguage, etc.) and language specific implementations in dedicated subteams.

GDExtension
~~~~~~~~~~~

GDExtension and godot-cpp.

.. gdareatable::
   :communication: #gdextension
   :github_reviews: @godotengine/gdextension
   :github_labels: <gh-label>topic:gdextension</gh-label>
   :triage_project: <gh-triage project=81>GDExtension issue triage</gh-triage>
   :maintainers: Bastiaan Olij (@BastiaanOlij), <lead>David Snopek (@dsnopek)</lead>, Fabio Alessandrelli (@Faless), George Marques (@vnen), Gilles Roudière (@groud), Jan Haller (@Bromeon), Juan Linietsky (@reduz), Patrick Exner (@paddy-exe), Pāvels Nadtočajevs (@bruvzg), Rémi Verschelde (@akien-mga)

GDScript
~~~~~~~~

GDScript language implementation.

.. gdareatable::
   :communication: #gdscript
   :github_reviews: @godotengine/gdscript
   :github_labels: <gh-label>topic:gdscript</gh-label>
   :triage_project: <gh-triage project=79>GDScript issue triage</gh-triage>
   :maintainers: Adam Scott (@adamscott), Danil Alexeev (@dalexeev), <lead>George Marques (@vnen)</lead>, @HolonProduction, Yuri Rubinsky (@Chaosus)


C# / .NET / Mono
~~~~~~~~~~~~~~~~

.. gdareatable::
   :communication: #dotnet
   :github_reviews: @godotengine/dotnet
   :github_labels: <gh-label>topic:dotnet</gh-label>
   :triage_project: <gh-triage project=83>Dotnet issue triage</gh-triage>
   :maintainers: Paul Joannon (@paulloz), <lead>Raul Santos (@raulsntos)</lead>

Translation / i18n
------------------

Internationalization and localization team - building the infrastructure to make it possible to translate Godot and its documentation.

If you work on Godot translations and contributors for your language have a dedicated communication channel for coordination, let us know so we can link it here.

.. gdareatable::
   :communication: #translation, #translation-de, #translation-es, #translation-fs, #translation-it
   :github_labels: <gh-label>topic:i18n</gh-label>

Website
-------

Creating the website `godotengine.org <https://godotengine.org>`__ and `asset library <https://godotengine.org/asset-library>`__ (and upcoming `asset store <https://store-beta.godotengine.org>`_).

.. gdareatable::
   :communication: #website, #asset-store
   :github_reviews: @godotengine/website
   :maintainers: Adam Scott (@adamscott), Emilio Coppola (@coppolaemilio), Hugo Locurcio (@Calinou), Iñigo Allende (@InigoAllende/@i.allende), HP van Braam (@hpvb), Max Hilbrunner (@mhilbrunner), Rémi Verschelde (@akien-mga), <lead>Winston (@winston-yallow)</lead>

XR
--

Augmented (AR) and virtual reality (VR).

.. gdareatable::
   :communication: #xr
   :github_reviews: @godotengine/xr
   :github_labels: <gh-label>topic:xr</gh-label>
   :triage_project: <gh-triage project=104>XR issue triage</gh-triage>
   :maintainers: <lead>Bastiaan Olij (@BastiaanOlij)</lead>, David Snopek (@dsnopek), Fredia Huya-Kouadio (@m4gr3d), Logan Lang (@devloglogan)
