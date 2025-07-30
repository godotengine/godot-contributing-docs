.. _doc_areas:

Areas and teams
===============

Godot is organized into areas, most of which has a designated team working on them.
This page lists these areas and explains their goals and how they're organized.

You can find information about the teams on the `godot website <https://godotengine.org/teams/>`_, as well
as their `current priorities <https://godotengine.org/priorities/>`_.

For more information about the different GitHub labels, please see the
:ref:`doc_bug_triage_guidelines`.

Core
----

Low-level Core API: Object, Variant, templates, base nodes like Node, Viewport, etc. (everything under core and scene/main).

* Triage: `Core issue triage <https://github.com/orgs/godotengine/projects/95>`_
* RC channel: `#core <https://chat.godotengine.org/channel/core>`_
* GitHub team: `godotengine/core <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fcore>`_
* GitHub label: ``topic:core`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Acore>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Acore>`_

Input
~~~~~

* GitHub team: `godotengine/input <https://github.com/orgs/godotengine/teams/input>`_
* RC channel: `#input <https://chat.godotengine.org/channel/input>`_
* GitHub label: ``topic:input`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ainput>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ainput>`_

GUI
---

Everything that inherits Control (everything under scene/gui) and can be used to build Graphical User Interfaces (both game UI and editor tools).

* Triage: `GUI issue triage <https://github.com/orgs/godotengine/projects/100>`_
* RC channel: `#gui <https://chat.godotengine.org/channel/gui>`_
* GitHub team: `godotengine/gui-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgui-nodes>`_
* GitHub label: ``topic:gui`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agui>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agui>`_

2D
--

* RC channel: `#2d <https://chat.godotengine.org/channel/2d>`__
* GitHub team: `godotengine/2d-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-nodes>`_
* GitHub label: ``topic:2d`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3A2d>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3A2d>`_

3D
--

* GitHub team: `godotengine/3d-nodes <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-nodes>`_
* GitHub label: ``topic:3d`` · issues · PRs

Editor
------

All things related to the editor, both tools and usability (editor).

* Triage: `Editor issue triage <https://github.com/orgs/godotengine/projects/111>`_
* RC channels
    * `godotengine/editor <https://chat.godotengine.org/channel/editor>`_
    * `godotengine/editor-design <https://chat.godotengine.org/channel/editor-design>`_
* GitHub labels
    * ``topic:editor`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aeditor>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aeditor>`_
    * ``topic:export`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aexport>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aexport>`_
    * ``topic:i18n`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ai18n>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ai18n>`_
    * ``topic:plugin`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aplugin>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aplugin>`_
* GitHub teams
    * `godotengine/2d-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-editor>`_
    * `godotengine/3d-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-editor>`_
    * `godotengine/debugger <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdebugger>`_
    * `godotengine/docs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocks>`_
    * `godotengine/script-editor <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fscript-editor>`_
    * `godotengine/usability <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fusability>`_

Scripting
---------

Umbrella team for all the scripting languages usable with Godot.
Encompasses some shared core components (Object, ClassDB, MethodBind, ScriptLanguage, etc.) and language specific implementations in dedicated subteams.

GDExtension
~~~~~~~~~~~

GDExtension and godot-cpp.

* Triage: `GDExtension issue triage <https://github.com/orgs/godotengine/projects/81/views/1>`_
* RC Channel: `#gdextension <https://chat.godotengine.org/channel/gdextension>`_
* GitHub team: `godotengine/gdextension <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdextension>`_
* GitHub label: ``topic:gdextension`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdextension>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdextension>`_

GDScript
~~~~~~~~

GDScript language implementation.

* Triage: `GDScript issue triage <https://github.com/orgs/godotengine/projects/79>`_
* RC channel: `#gdscript <https://chat.godotengine.org/channel/gdscript>`_
* GitHub team: `godotengine/gdscript <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdscript>`_
* GitHub label: ``topic:gdscript`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdscript>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdscript>`_

C# / .NET / Mono
~~~~~~~~~~~~~~~~

* Triage: `Dotnet issue triage <https://github.com/orgs/godotengine/projects/83>`_
* RC channel: `#dotnet <https://chat.godotengine.org/channel/dotnet>`_
* GitHub team: `godotengine/dotnet <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdotnet>`_
* GitHub label: ``topic:dotnet`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Adotnet>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Adotnet>`_

Buildsystem
-----------

Tools and scripts that we use to compile and maintain Godot, both for development purpose (SCons, CI) and releases (official build containers).

* Triage: `Buildsystem issue triage <https://github.com/orgs/godotengine/projects/53>`_
* RC channel: `#buildsystem <https://chat.godotengine.org/channel/buildsystem>`_
* GitHub team: `godotengine/buildsystem <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fbuildsystem>`_
* GitHub label: ``topic:buildsystem`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Abuildsystem>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Abuildsystem>`_

Platforms
---------

Platform specific layers that reside in platform, with shared components (Unix, Win32, Apple, etc.) in drivers.

* Triage: `Platforms issue triage <https://github.com/orgs/godotengine/projects/84>`_
* RC channels
    * `#platforms <https://chat.godotengine.org/channel/platforms>`_
    * `#apple <https://chat.godotengine.org/channel/apple>`_
    * `#android <https://chat.godotengine.org/channel/android>`_
    * `#web <https://chat.godotengine.org/channel/web>`_
* GitHub teams
    * `godotengine/android <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fandroid>`_
    * `godotengine/ios <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fios>`_
    * `godotengine/linux-bsd <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Flinux-bsd>`_
    * `godotengine/macos <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fmacos>`_
    * `godotengine/uwp <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fuwp>`_
    * `godotengine/web <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fweb>`_
    * `godotengine/windows <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fwindows>`_
* GitHub labels
    * ``topic:porting`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aporting>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aporting>`_
    * ``topic:android`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aandroid>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aandroid>`_
    * ``topic:ios`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aios>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aios>`_
    * ``topic:linuxbsd`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Alinuxbsd>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Alinuxbsd>`_
    * ``topic:macos`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Amacos>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Amacos>`_
    * ``topic:uwp`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Auwp>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Auwp>`_
    * ``topic:web`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aweb>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aweb>`_
    * ``topic:windows`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Awindows>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Awindows>`_

Animation
---------

Nodes and features for 2D and 3D animation and IK workflows.

* Triage: `Animation team Issue Triage <https://github.com/orgs/godotengine/projects/74>`__
* RC channel: `#animation <https://chat.godotengine.org/channel/animation>`__
* GitHub team: `godotengine/animation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fanimation>`__
* GitHub label: ``topic:animation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aanimation>`__ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aanimation>`__

Audio
-----

All audio-related features, from low-level AudioServer and drivers to high-level nodes and effects.

* Triage: `Audio issue triage <https://github.com/orgs/godotengine/projects/101>`__
* RC channel: `#audio <https://chat.godotengine.org/channel/audio>`__
* GitHub team: `godotengine/audio <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Faudio>`_
* GitHub label: ``topic:audio`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aaudio>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aaudio>`_

Import
------

Asset import pipeline for 2D (textures) and 3D (scenes, models, animations, etc.).

* Triage: `Asset pipeline issue triage <https://github.com/orgs/godotengine/projects/72>`__
* RC channel: `#asset-pipeline <https://chat.godotengine.org/channel/asset-pipeline>`__
* GitHub team: `godotengine/import <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fimport>`_
* GitHub label: ``topic:import`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aimport>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aimport>`_

Networking
----------

Networked multiplayer, RPCs and replication, HTTP/TCP/UDP/DNS, WebSockets, ENet, encryption.

* Triage: `Network issue triage <https://github.com/orgs/godotengine/projects/96>`_
* RC channels
    * `#networking <https://chat.godotengine.org/channel/networking>`_
    * `#voip <https://chat.godotengine.org/channel/voip>`_
* GitHub team: `godotengine/network <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnetwork>`_
* GitHub labels
    * ``topic:network`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anetwork>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anetwork>`_
    * ``topic:multiplayer`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Amultiplayer>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Amultiplayer>`_

Physics
-------

Physics servers and their implementation in 2D and 3D.

* Triage: `Physics issue triage <https://github.com/orgs/godotengine/projects/102>`_
* RC channel: `#physics <https://chat.godotengine.org/channel/physics>`_
* GitHub team: `godotengine/physics <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fphysics>`_
* GitHub label: ``topic:physics`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aphysics>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aphysics>`_

Rendering
---------

Rendering server and RenderingDevice implementations (Vulkan, OpenGL), as well as the actual rendering techniques implemented using those graphics APIs.

* Triage: `Rendering issue triage <https://github.com/orgs/godotengine/projects/78>`_
* RC channel: `#rendering <https://chat.godotengine.org/channel/rendering>`_
* GitHub teams
    * `godotengine/rendering <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Frendering>`_
    * `godotengine/shaders <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fshaders>`_
* GitHub labels
    * ``topic:rendering`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Arendering>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Arendering>`_
    * ``topic:shaders`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ashaders>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ashaders>`_

VFX / Tech Art / Particles
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Triage: `Particles issue triage <https://github.com/orgs/godotengine/projects/115>`_
* RC channel: `#vfx-tech-art <https://chat.godotengine.org/channel/vfx-tech-art>`_
* GitHub label: ``topic:particles`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aparticles>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aparticles>`_

XR
--

Augmented (AR) and virtual reality (VR).

* Triage: `XR issue triage <https://github.com/orgs/godotengine/projects/104>`_
* RC channel: `#xr <https://chat.godotengine.org/channel/xr>`_
* GitHub team: `godotengine/xr <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fxr>`_
* GitHub label: ``topic:xr`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Axr>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Axr>`_

Navigation
----------

* Triage: `Navigation issue triage <https://github.com/orgs/godotengine/projects/103>`_
* RC channel: `#navigation <https://chat.godotengine.org/channel/navigation>`_
* GitHub team: `godotengine/navigation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnavigation>`_
* GitHub label: ``topic:navigation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anavigation>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anavigation>`_

Documentation
-------------

Documentation for the engine and its systems.
Note that, while there is a dedicated documentation team, all other teams are expected to contribute to the documentation
for their area.

* RC channels
    * `#documentation <https://chat.godotengine.org/channel/documentation>`_
    * `#translation <https://chat.godotengine.org/channel/translation>`_
        * `#translation-de <https://chat.godotengine.org/channel/translation-de>`_
        * `#translation-es <https://chat.godotengine.org/channel/translation-es>`_
        * `#translation-fr <https://chat.godotengine.org/channel/translation-fr>`_
        * `#translation-it <https://chat.godotengine.org/channel/translation-it>`_
* GitHub team: `godotengine/documentation <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocumentation>`_
* GitHub label: ``documentation`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Adocumentation>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Adocumentation>`_

Quality Assurance
------------------

All things QA: unit/integration tests, static analysis, benchmarks, code style/quality, builds testing.

* RC channels
    * `#quality-assurance <https://chat.godotengine.org/channel/quality-assurance>`_
    * `#benchmarks <https://chat.godotengine.org/channel/benchmarks>`_

Tests
~~~~~

Tests for the engine and its systems.
Note that, while there is a dedicated tests team, all other teams are expected to contribute to the tests
for their area.

* GitHub team: `godotengine/tests <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Ftests>`_
* GitHub label: ``topic:tests`` · `issues <https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Atests>`_ · `PRs <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Atests>`_

See also the `current documentation for unit tests <https://docs.godotengine.org/en/stable/contributing/development/core_and_modules/unit_testing.html>`_.

Bugsquad / Issue triage
~~~~~~~~~~~~~~~~~~~~~~~

* RC channels
    * `#bugsquad <https://chat.godotengine.org/channel/bugsquad>`_
    * `#bugsquad-sprints <https://chat.godotengine.org/channel/bugsquad-sprints>`_

Demos
-----

* RC channel: `#demo-content <https://chat.godotengine.org/channel/demo-content>`_

Website
-------

Creating the website `godotengine.org <https://godotengine.org>`_ and `asset library <https://godotengine.org/asset-library>`_ (and upcoming `asset store <https://store-beta.godotengine.org>`_).

* RC channels
    * `#website <https://chat.godotengine.org/channel/website>`_
    * `#asset-store <https://chat.godotengine.org/channel/asset-store>`_
