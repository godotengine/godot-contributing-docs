.. _doc_areas:

Areas and teams
===============

Godot is organized into areas, most of which has a designated team working on them.
This page lists these areas and explains their goals and how they're organized.

For each team or area there is a list of links and resources associated with them:
* *Triage project*: links to the team triage project for the team.
* *RocketChat channel*: links to the `RocketChat <https://chat.godotengine.org/>`__ channel for the team,
  joining this channel is the best way to get involved with the team.
* *GitHub review*: opens a GitHub search for PRs that have a review request for the team.
  Note that this *doesn’t* show PRs that have already been reviewed by that team,
  any review comments at all, from any member of a specific team, will remove the request, so this is not always helpful.
* *GitHub label*: lists any labels relevant to the team, and links to issues and PRs tagged with those tags.
  For more information about the different GitHub labels, please see the :ref:`doc_bug_triage_guidelines`.
  Note that some GitHub labels aren’t neatly covered by trackers.

You can find information about the teams on the `godot website <https://godotengine.org/teams/>`_, as well
as their `current priorities <https://godotengine.org/priorities/>`_.

2D
--

* RocketChat channel: `#2d <https://chat.godotengine.org/channel/2d>`__
* GitHub review: `godotengine/2d-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-nodes>`__
* GitHub label: ``topic:2d`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3A2d>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3A2d>`__

3D
--

* GitHub review: `godotengine/3d-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-nodes>`__
* GitHub label: ``topic:3d`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3A3d>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3A3d>`__

Animation
---------

Nodes and features for 2D and 3D animation and IK workflows.

* Triage project: `Animation team Issue Triage <https://github.com/orgs/godotengine/projects/74>`__
* RocketChat channel: `#animation <https://chat.godotengine.org/channel/animation>`__
* GitHub review: `godotengine/animation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fanimation>`__
* GitHub label: ``topic:animation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aanimation>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aanimation>`__

Audio
-----

All audio-related features, from low-level AudioServer and drivers to high-level nodes and effects.

* Triage project: `Audio issue triage <https://github.com/orgs/godotengine/projects/101>`__
* RocketChat channel: `#audio <https://chat.godotengine.org/channel/audio>`__
* GitHub review: `godotengine/audio <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Faudio>`__
* GitHub label: ``topic:audio`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aaudio>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aaudio>`__

Buildsystem
-----------

Tools and scripts that we use to compile and maintain Godot, both for development purpose (SCons, CI) and releases (official build containers).

* Triage project: `Buildsystem issue triage <https://github.com/orgs/godotengine/projects/53>`__
* RocketChat channel: `#buildsystem <https://chat.godotengine.org/channel/buildsystem>`__
* GitHub review: `godotengine/buildsystem <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fbuildsystem>`__
* GitHub label: ``topic:buildsystem`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Abuildsystem>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Abuildsystem>`__

Core
----

Low-level Core API: Object, Variant, templates, base nodes like Node, Viewport, etc. (everything under ``core`` and ``scene/main``).

* Triage project: `Core issue triage <https://github.com/orgs/godotengine/projects/95>`__
* RocketChat channel: `#core <https://chat.godotengine.org/channel/core>`__
* GitHub review: `godotengine/core <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fcore>`__
* GitHub label: ``topic:core`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Acore>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Acore>`__

Input
~~~~~

* RocketChat channel: `#input <https://chat.godotengine.org/channel/input>`__
* GitHub review: `godotengine/input <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Finput>`__
* GitHub label: ``topic:input`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ainput>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ainput>`__

Demos
-----

* RocketChat channel: `#demo-content <https://chat.godotengine.org/channel/demo-content>`__

Documentation
-------------

Documentation for the engine and its systems.
Note that, while there is a dedicated documentation team, all other teams are expected to contribute to the documentation
for their area.

* RocketChat channels
    * `#documentation <https://chat.godotengine.org/channel/documentation>`__
    * `#translation <https://chat.godotengine.org/channel/translation>`__
        * `#translation-de <https://chat.godotengine.org/channel/translation-de>`__
        * `#translation-es <https://chat.godotengine.org/channel/translation-es>`__
        * `#translation-fr <https://chat.godotengine.org/channel/translation-fr>`__
        * `#translation-it <https://chat.godotengine.org/channel/translation-it>`__
* GitHub review: `godotengine/documentation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocumentation>`__
* GitHub label: ``documentation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Adocumentation>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Adocumentation>`__

Editor
------

All things related to the editor, both tools and usability (editor).

* Triage project: `Editor issue triage <https://github.com/orgs/godotengine/projects/111>`__
* RocketChat channels
    * `#editor <https://chat.godotengine.org/channel/editor>`__
    * `#editor-design <https://chat.godotengine.org/channel/editor-design>`__
* GitHub review
    * `godotengine/2d-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-editor>`__
    * `godotengine/3d-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-editor>`__
    * `godotengine/debugger <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdebugger>`__
    * `godotengine/docs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocks>`__
    * `godotengine/script-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fscript-editor>`__
    * `godotengine/usability <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fusability>`__
* GitHub labels
    * ``topic:editor`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aeditor>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aeditor>`__
    * ``topic:export`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aexport>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aexport>`__
    * ``topic:i18n`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ai18n>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ai18n>`__
    * ``topic:plugin`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aplugin>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aplugin>`__

GUI
---

Everything that inherits Control (everything under ``scene/gui``) and can be used to build Graphical User Interfaces (both game UI and editor tools).

* Triage project: `GUI issue triage <https://github.com/orgs/godotengine/projects/100>`__
* RocketChat channel: `#gui <https://chat.godotengine.org/channel/gui>`__
* GitHub review: `godotengine/gui-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgui-nodes>`__
* GitHub label: ``topic:gui`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agui>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agui>`__

Import
------

Asset import pipeline for 2D (textures) and 3D (scenes, models, animations, etc.).

* Triage project: `Asset pipeline issue triage <https://github.com/orgs/godotengine/projects/72>`__
* RocketChat channel: `#asset-pipeline <https://chat.godotengine.org/channel/asset-pipeline>`__
* GitHub review: `godotengine/import <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fimport>`__
* GitHub label: ``topic:import`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aimport>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aimport>`__

Navigation
----------

* Triage project: `Navigation issue triage <https://github.com/orgs/godotengine/projects/103>`__
* RocketChat channel: `#navigation <https://chat.godotengine.org/channel/navigation>`__
* GitHub review: `godotengine/navigation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnavigation>`__
* GitHub label: ``topic:navigation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anavigation>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anavigation>`__

Networking
----------

Networked multiplayer, RPCs and replication, HTTP/TCP/UDP/DNS, WebSockets, ENet, encryption.

* Triage project: `Network issue triage <https://github.com/orgs/godotengine/projects/96>`__
* RocketChat channels
    * `#networking <https://chat.godotengine.org/channel/networking>`__
    * `#voip <https://chat.godotengine.org/channel/voip>`__
* GitHub review: `godotengine/network <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnetwork>`__
* GitHub labels
    * ``topic:network`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anetwork>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anetwork>`__
    * ``topic:multiplayer`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Amultiplayer>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Amultiplayer>`__

Physics
-------

Physics servers and their implementation in 2D and 3D.

* Triage project: `Physics issue triage <https://github.com/orgs/godotengine/projects/102>`__
* RocketChat channel: `#physics <https://chat.godotengine.org/channel/physics>`__
* GitHub review: `godotengine/physics <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fphysics>`__
* GitHub label: ``topic:physics`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aphysics>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aphysics>`__

Platforms
---------

Platform specific layers that reside in ``platform``, with shared components (Unix, Win32, Apple, etc.) in ``drivers``.

* Triage project: `Platforms issue triage <https://github.com/orgs/godotengine/projects/84>`__
* RocketChat channels
    * `#platforms <https://chat.godotengine.org/channel/platforms>`__
    * `#apple <https://chat.godotengine.org/channel/apple>`__
    * `#android <https://chat.godotengine.org/channel/android>`__
    * `#web <https://chat.godotengine.org/channel/web>`__
* GitHub review
    * `godotengine/android <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fandroid>`__
    * `godotengine/ios <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fios>`__
    * `godotengine/linux-bsd <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Flinux-bsd>`__
    * `godotengine/macos <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fmacos>`__
    * `godotengine/uwp <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fuwp>`__
    * `godotengine/web <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fweb>`__
    * `godotengine/windows <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fwindows>`__
* GitHub labels
    * ``topic:porting`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aporting>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aporting>`__
    * ``topic:android`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aandroid>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aandroid>`__
    * ``topic:ios`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aios>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aios>`__
    * ``topic:linuxbsd`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Alinuxbsd>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Alinuxbsd>`__
    * ``topic:macos`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Amacos>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Amacos>`__
    * ``topic:uwp`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Auwp>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Auwp>`__
    * ``topic:web`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aweb>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aweb>`__
    * ``topic:windows`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Awindows>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Awindows>`__

Quality Assurance
------------------

All things QA: unit/integration tests, static analysis, benchmarks, code style/quality, builds testing.

* RocketChat channels
    * `#quality-assurance <https://chat.godotengine.org/channel/quality-assurance>`__
    * `#benchmarks <https://chat.godotengine.org/channel/benchmarks>`__

Tests
~~~~~

Tests for the engine and its systems.
Note that, while there is a dedicated tests team, all other teams are expected to contribute to the tests
for their area.

* GitHub review: `godotengine/tests <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Ftests>`__
* GitHub label: ``topic:tests`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Atests>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Atests>`__

Bugsquad / Issue triage
~~~~~~~~~~~~~~~~~~~~~~~

* RocketChat channels
    * `#bugsquad <https://chat.godotengine.org/channel/bugsquad>`__
    * `#bugsquad-sprints <https://chat.godotengine.org/channel/bugsquad-sprints>`__

Rendering
---------

Rendering server and RenderingDevice implementations (Vulkan, OpenGL), as well as the actual rendering techniques implemented using those graphics APIs.

* Triage project: `Rendering issue triage <https://github.com/orgs/godotengine/projects/78>`__
* RocketChat channel: `#rendering <https://chat.godotengine.org/channel/rendering>`__
* GitHub review
    * `godotengine/rendering <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Frendering>`__
    * `godotengine/shaders <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fshaders>`__
* GitHub labels
    * ``topic:rendering`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Arendering>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Arendering>`__
    * ``topic:shaders`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ashaders>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ashaders>`__

VFX / Tech Art / Particles
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Triage project: `Particles issue triage <https://github.com/orgs/godotengine/projects/115>`__
* RocketChat channel: `#vfx-tech-art <https://chat.godotengine.org/channel/vfx-tech-art>`__
* GitHub label: ``topic:particles`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aparticles>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aparticles>`__

Scripting
---------

Umbrella team for all the scripting languages usable with Godot.
Encompasses some shared core components (Object, ClassDB, MethodBind, ScriptLanguage, etc.) and language specific implementations in dedicated subteams.

GDExtension
~~~~~~~~~~~

GDExtension and godot-cpp.

* Triage project: `GDExtension issue triage <https://github.com/orgs/godotengine/projects/81/views/1>`__
* RC Channel: `#gdextension <https://chat.godotengine.org/channel/gdextension>`__
* GitHub review: `godotengine/gdextension <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdextension>`__
* GitHub label: ``topic:gdextension`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdextension>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdextension>`__

GDScript
~~~~~~~~

GDScript language implementation.

* Triage project: `GDScript issue triage <https://github.com/orgs/godotengine/projects/79>`__
* RocketChat channel: `#gdscript <https://chat.godotengine.org/channel/gdscript>`__
* GitHub review: `godotengine/gdscript <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdscript>`__
* GitHub label: ``topic:gdscript`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdscript>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdscript>`__

C# / .NET / Mono
~~~~~~~~~~~~~~~~

* Triage project: `Dotnet issue triage <https://github.com/orgs/godotengine/projects/83>`__
* RocketChat channel: `#dotnet <https://chat.godotengine.org/channel/dotnet>`__
* GitHub review: `godotengine/dotnet <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdotnet>`__
* GitHub label: ``topic:dotnet`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Adotnet>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Adotnet>`__

Website
-------

Creating the website `godotengine.org <https://godotengine.org>`__ and `asset library <https://godotengine.org/asset-library>`__ (and upcoming `asset store <https://store-beta.godotengine.org>`_).

* RocketChat channels
    * `#website <https://chat.godotengine.org/channel/website>`__
    * `#asset-store <https://chat.godotengine.org/channel/asset-store>`__

XR
--

Augmented (AR) and virtual reality (VR).

* Triage project: `XR issue triage <https://github.com/orgs/godotengine/projects/104>`__
* RocketChat channel: `#xr <https://chat.godotengine.org/channel/xr>`__
* GitHub review: `godotengine/xr <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fxr>`__
* GitHub label: ``topic:xr`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Axr>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Axr>`__
