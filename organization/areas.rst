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
* **Triage project**: links to the :ref:`team triage project <doc_triage_projects>` for the team. You are welcome to
  help the team out by implementing or reviewing something from this list.
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
   :maintainers: Hugo Locurcio (@Calinou)

Animation
---------

Nodes and features for 2D and 3D animation and IK workflows.

.. gdareatable::
   :communication: #animation
   :github_reviews: @godotengine/animation
   :github_labels: <gh-label>topic:animation</gh-label>
   :triage_project: <gh-triage project=74>Animation issue triage</gh-triage>
   :maintainers: Juan Linietsky (@reduz), K. S. Ernest Lee (@fire), @Lyuma, @SaracenOne, <lead>Silc 'Tokage' Renew (@TokageItLab)</lead>

Asset pipeline
--------------

Asset import pipeline for 2D (textures) and 3D (scenes, models, animations, etc.).

.. gdareatable::
   :communication: #asset-pipeline
   :github_reviews: @godotengine/asset-pipeline
   :github_labels: <gh-label>topic:import</gh-label>
   :triage_project: <gh-triage project=72>Asset pipeline issue triage</gh-triage>
   :maintainers: Aaron Franke (@aaronfranke), @BlueCube3310, Hugo Locurcio (@Calinou), K. S. Ernest Lee (@fire), @Lyuma, Rémi Verschelde (@akien-mga)

Audio
-----

All audio-related features, from low-level AudioServer and drivers to high-level nodes and effects.

.. gdareatable::
   :communication: #audio
   :github_reviews: @godotengine/audio
   :github_labels: <gh-label>topic:audio</gh-label>
   :triage_project: <gh-triage project=101>Audio issue triage</gh-triage>
   :maintainers: Adam Scott (@adamscott), Lukas Tenbrink (@Ivorius/@Ivorforce), Juan Linietsky (@reduz)

Core
----

Low-level Core API: Object, Variant, templates, base nodes like Node, Viewport, etc. (everything under ``core`` and ``scene/main``).

.. gdareatable::
   :communication: #core
   :github_reviews: @godotengine/core
   :github_labels: <gh-label>topic:core</gh-label>
   :triage_project: <gh-triage project=95>Core issue triage</gh-triage>
   :maintainers: HP van Braam (@hpvb), <lead>Juan Linietsky (@reduz)</lead>, @lawnjelly, Lukas Tenbrink (@Ivorius/@Ivorforce), Rémi Verschelde (@akien-mga)

.. _team_demos:

Demos
-----

.. gdareatable::
   :communication: #demo-content
   :github_reviews: @godotengine/demos
   :maintainers: <lead>Aaron Franke (@aaronfranke)</lead>, Gilles Roudière (@groud), <lead>Hugo Locurcio (@Calinou)</lead>, K. S. Ernest Lee (@fire)

.. _team_documentation:

Documentation
-------------

Documentation for the engine and its systems. You can find documentation for this team in the :ref:`documentation section <doc_documentation_overview>`.

Note that, while there is a dedicated documentation team, all other teams are expected to contribute to the documentation
for their area.

.. gdareatable::
   :communication: #documentation
   :github_reviews: @godotengine/documentation
   :github_labels: <gh-label>documentation</gh-label>
   :maintainers: A Thousand Ships (@AThousandShips), Hana - Piralein (@Piralein), Hugo Locurcio (@Calinou), <lead>Max Hilbrunner (@mhilbrunner)</lead>, Matthew (@skyace65), Micky (@Mickeon)

Editor
------

All things related to the editor.

.. gdareatable::
   :communication: #editor
   :github_reviews: @godotengine/editor
   :github_labels: <gh-label>topic:editor</gh-label>, <gh-label>topic:export</gh-label>, <gh-label>topic:plugin</gh-label>
   :triage_project: <gh-triage project=111>Editor issue triage</gh-triage>
   :maintainers: Gilles Roudière (@groud), Hugo Locurcio (@Calinou), Kit Bishop (@kitbdev), Michael Alexsander (@YeldhamDev), Pāvels Nadtočajevs (@bruvzg), Robert Yevdokimov (@ryevdokimov), Tomasz Chabora (@KoBeWi)

Debugger
~~~~~~~~

.. gdareatable::
   :communication: #gui
   :github_reviews: @godotengine/debugger
   :github_labels: <gh-label>topic:gui</gh-label>
   :triage_project: <gh-triage project=111>Editor issue triage</gh-triage>
   :maintainers: Fabio Alessandrelli (@Faless), George Marques (@vnen)

Script Editor
~~~~~~~~~~~~~

.. gdareatable::
   :communication: #gui
   :github_reviews: @godotengine/script-editor
   :github_labels: <gh-label>topic:gui</gh-label>
   :triage_project: <gh-triage project=111>Editor issue triage</gh-triage>
   :maintainers: Kit Bishop (@kitbdev), Michael Alexsander (@YeldhamDev), Paul Batty (@Paulb23)

Usability
~~~~~~~~~

The usability team represents a user-oriented view of the engine, and plans and reviews functionality, workflows,
and accessibility.

Feel free to approach the usability team for guidance and support in planning an engine feature, especially if it
involves GUI or user experience (UX).

.. gdareatable::
   :communication: #usability
   :github_reviews: @godotengine/usability
   :github_labels: <gh-label>usability</gh-label>
   :maintainers: Adriaan de Jongh (@AdriaandeJongh), Gilles Roudière (@groud), Hendrik Brucker (@Geometror), Hugo Locurcio (@Calinou), K. S. Ernest Lee (@fire), Michael Alexsander (@YeldhamDev), Micky (@Mickeon), @passivestar, Paul Batty (@Paulb23), Timothé Bonhoure (@ajreckof)

GUI
---

Everything that inherits Control (everything under ``scene/gui``) and can be used to build Graphical User Interfaces (both game UI and editor tools).

.. gdareatable::
   :communication: #gui
   :github_reviews: @godotengine/gui-nodes
   :github_labels: <gh-label>topic:gui</gh-label>
   :triage_project: <gh-triage project=100>GUI issue triage</gh-triage>
   :maintainers: Gilles Roudière (@groud), Hendrik Brucker (@Geometror), Kit Bishop (@kitbdev), Michael Alexsander (@YeldhamDev), Paul Batty (@Paulb23), Pāvels Nadtočajevs (@bruvzg), Rémi Verschelde (@akien-mga), Tomasz Chabora (@KoBeWi)

Input
-----

.. gdareatable::
   :communication: #input
   :github_reviews: @godotengine/input
   :github_labels: <gh-label>topic:input</gh-label>
   :maintainers: Alexander Hartmann (@Alex2782), Rémi Verschelde (@akien-mga), Gilles Roudière (@groud), @Nintorch

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
   :github_reviews: @godotengine/physics, @godotengine/jolt-physics
   :github_labels: <gh-label>topic:physics</gh-label>
   :triage_project: <gh-triage project=102>Physics issue triage</gh-triage>
   :maintainers: Jorrit Rouwe (@jrouwe), Juan Linietsky (@reduz), @lawnjelly, Mikael Hermansson (@mihe), Ricardo Buring (@rburing)

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
   :maintainers: Alexander Hartmann (@Alex2782), Anish (@syntaxerror247), <lead>Fredia Huya-Kouadio (@m4gr3d)</lead>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Apple
~~~~~

.. gdareatable::
   :communication: #apple
   :github_reviews: @godotengine/ios, @godotengine/macos
   :github_labels: <gh-label>platform:ios</gh-label>, <gh-label>platform:macos</gh-label>, <gh-label>platform:visionos</gh-label>
   :maintainers: Bastiaan Olij (@BastiaanOlij), <lead>Pāvels Nadtočajevs (@bruvzg)</lead>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Buildsystem
~~~~~~~~~~~

Tools and scripts that we use to compile and maintain Godot, both for development purpose (SCons, CI) and releases (official build containers).

.. gdareatable::
   :communication: #buildsystem
   :github_reviews: @godotengine/buildsystem
   :github_labels: <gh-label>topic:buildsystem</gh-label>
   :triage_project: <gh-triage project=53>Buildsystem issue triage</gh-triage>
   :maintainers: Fabio Alessandrelli (@Faless), HP van Braam (@hpvb), Hugo Locurcio (@Calinou), Pāvels Nadtočajevs (@bruvzg), <lead>Rémi Verschelde (@akien-mga)</lead>, Thaddeus Crews (@Repiteo)

Web
~~~

.. gdareatable::
   :communication: #web
   :github_reviews: @godotengine/web
   :github_labels: <gh-label>platform:web</gh-label>
   :maintainers: <lead>Adam Scott (@adamscott)</lead>, Fabio Alessandrelli (@Faless)
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Windows
~~~~~~~

.. gdareatable::
   :communication: #platforms
   :github_reviews: @godotengine/windows
   :github_labels: <gh-label>platform:windows</gh-label>
   :maintainers: Max Hilbrunner (@mhilbrunner), <lead>Pāvels Nadtočajevs (@bruvzg)</lead>
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Linux / BSD
~~~~~~~~~~~

.. gdareatable::
   :communication: #platforms
   :github_reviews: @godotengine/linux-bsd
   :github_labels: <gh-label>platform:linuxbsd</gh-label>
   :maintainers: Dery Almas (@deralmas), Fabio Alessandrelli (@Faless), <lead>HP van Braam (@hpvb)</lead>, Pāvels Nadtočajevs (@bruvzg), Rémi Verschelde (@akien-mga)
   :triage_project: <gh-triage project=84>Platforms issue triage</gh-triage>

Quality Assurance
-----------------

All things QA: unit/integration tests, static analysis, benchmarks, code style/quality, builds testing.

.. gdareatable::
   :communication: #quality-assurance, #benchmarks

Tests
~~~~~

Tests for the engine and its systems.
Note that, while there is a dedicated tests team, every team is expected to contribute to the tests
for their area.

.. gdareatable::
   :communication: #quality-assurance
   :github_reviews: @godotengine/tests
   :github_labels: <gh-label>topic:tests</gh-label>
   :maintainers: Hugo Locurcio (@Calinou), Hendrik Brucker (@Geometror), Thaddeus Crews (@Repiteo)

.. _team_triage:

Bugsquad / Issue triage
~~~~~~~~~~~~~~~~~~~~~~~

You can find documentation for this team in the :ref:`triage section <doc_triage>`.

.. gdareatable::
   :communication: #bugsquad, #bugsquad-sprints
   :github_reviews: @godotengine/bugsquad
   :maintainers: <lead>A Thousand Ships (@AThousandShips)</lead>, K. S. Ernest Lee (@fire), @lawnjelly, Rémi Verschelde (@akien-mga), Ricardo Subtil (@rsubtil), Rudolph Bester (@Rudolph-B), Sébastien Dunne Fulmer (@CreatedBySeb)

Rendering
---------

Rendering server and RenderingDevice implementations (Vulkan, OpenGL), as well as the actual rendering techniques implemented using those graphics APIs.

.. gdareatable::
   :communication: #rendering
   :github_reviews: @godotengine/rendering
   :github_labels: <gh-label>topic:rendering</gh-label>
   :triage_project: <gh-triage project=78>Rendering issue triage</gh-triage>
   :maintainers: Bastiaan Olij (@BastiaanOlij), @BlueCube3310, <lead>Clay John (@clayjohn)</lead>, Darío Banini (@DarioSamo), Hugo Locurcio (@Calinou), Juan Linietsky (@reduz), @lawnjelly, Skyth (Asilkan) (@blueskythlikesclouds), Stuart Carnie (@stuartcarnie)

Shaders
~~~~~~~

.. gdareatable::
   :communication: #rendering
   :github_reviews: @godotengine/shaders
   :github_labels: <gh-label>topic:shaders</gh-label>
   :triage_project: <gh-triage project=78>Rendering issue triage</gh-triage>
   :maintainers: <lead>Clay John (@clayjohn)</lead>, Hendrik Brucker (@Geometror), <lead>Ilaria Cislaghi (@QbieShay)</lead>, Patrick Exner (@paddy-exe), Skyth (Asilkan) (@blueskythlikesclouds), <lead>Yuri Rubinsky (@Chaosus)</lead>

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

.. _team_gdextension:

GDExtension
~~~~~~~~~~~

GDExtension and godot-cpp.

.. gdareatable::
   :communication: #gdextension
   :github_reviews: @godotengine/gdextension
   :github_labels: <gh-label>topic:gdextension</gh-label>
   :triage_project: <gh-triage project=81>GDExtension issue triage</gh-triage>
   :maintainers: Bastiaan Olij (@BastiaanOlij), <lead>David Snopek (@dsnopek)</lead>, Fabio Alessandrelli (@Faless), George Marques (@vnen), Jan Haller (@Bromeon), Lukas Tenbrink (@Ivorius/@Ivorforce), Patrick Exner (@paddy-exe), Pāvels Nadtočajevs (@bruvzg)

GDScript
~~~~~~~~

GDScript language implementation.

.. gdareatable::
   :communication: #gdscript
   :github_reviews: @godotengine/gdscript
   :github_labels: <gh-label>topic:gdscript</gh-label>
   :triage_project: <gh-triage project=79>GDScript issue triage</gh-triage>
   :maintainers: Adam Scott (@adamscott), Danil Alexeev (@dalexeev), <lead>George Marques (@vnen)</lead>, @HolonProduction

C# / .NET / Mono
~~~~~~~~~~~~~~~~

.. gdareatable::
   :communication: #dotnet
   :github_reviews: @godotengine/dotnet
   :github_labels: <gh-label>topic:dotnet</gh-label>
   :triage_project: <gh-triage project=83>Dotnet issue triage</gh-triage>
   :maintainers: Paul Joannon (@paulloz), <lead>Raul Santos (@raulsntos)</lead>

Server Infrastructure
---------------------

Managing the backend for the website and servers, e.g. `godotengine.org <https://godotengine.org>`__, `asset library <https://godotengine.org/asset-library>`__, and upcoming `asset store <https://store-beta.godotengine.org>`_.

.. gdareatable::
   :communication: #website, #asset-store
   :github_reviews: @godotengine/server-infrastructure
   :maintainers: HP van Braam (@hpvb), Winston (@winston-yallow)

Technical Leadership Committee (TLC)
------------------------------------

The Technical Leadership Committee (TLC) drafts and drives the technical roadmap / development
direction for the engine, supports and assists the project management and release teams, and
provides technical guidance to the Godot Foundation Board. Learn more on the `Governance page <https://godotengine.org/governance/>`__
on the Godot website.

.. gdareatable::
   :github_reviews: @godotengine/tlc
   :maintainers: Bastiaan Olij (@BastiaanOlij), Clay John (@clayjohn), David Snopek (@dsnopek), Fredia Huya-Kouadio (@m4gr3d), George Marques (@vnen), HP van Braam (@hpvb), Juan Linietsky (@reduz), @lawnjelly, Lukas Tenbrink (@Ivorius/@Ivorforce), Pāvels Nadtočajevs (@bruvzg), Rémi Verschelde (@akien-mga), Tomasz Chabora (@KoBeWi)

Translation / i18n
------------------

Internationalization and localization team - building the infrastructure to make it possible to translate Godot and its documentation.

If you work on Godot translations and contributors for your language have a dedicated communication channel for coordination, let us know so we can link it here.

.. gdareatable::
   :github_reviews: @godotengine/i18n
   :communication: #translation, #translation-de, #translation-es, #translation-fs, #translation-it
   :github_labels: <gh-label>topic:i18n</gh-label>
   :maintainers: Rémi Verschelde (@akien-mga)

.. _team_website:

Website
-------

Creating and curating the website `godotengine.org <https://godotengine.org>`__ and `asset library <https://godotengine.org/asset-library>`__ (and upcoming `asset store <https://store-beta.godotengine.org>`_).

.. gdareatable::
   :communication: #website, #asset-store
   :github_reviews: @godotengine/website
   :maintainers: Adam Scott (@adamscott), <lead>Emilio Coppola (@coppolaemilio)</lead>, Hugo Locurcio (@Calinou), Iñigo Allende (@InigoAllende/@i.allende), Winston (@winston-yallow)

XR
--

Augmented (AR) and virtual reality (VR).

.. gdareatable::
   :communication: #xr
   :github_reviews: @godotengine/xr
   :github_labels: <gh-label>topic:xr</gh-label>
   :triage_project: <gh-triage project=104>XR issue triage</gh-triage>
   :maintainers: <lead>Bastiaan Olij (@BastiaanOlij)</lead>, David Snopek (@dsnopek), Fredia Huya-Kouadio (@m4gr3d), Logan Lang (@devloglogan)
