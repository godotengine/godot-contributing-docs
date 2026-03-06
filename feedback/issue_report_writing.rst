.. _doc_issue_report_writing:

How to write a good issue report
================================

Before opening an issue
-----------------------

Please make sure you have done the following before opening an issue, to avoid unnecessary work.

- Double check that the issue is not caused by any add-on or plugin in your project, unless the issue is specifically
  about a bug in how add-ons or plugins work. Generally, issues caused by add-ons or plugins should be reported to the
  creator of the add-on or plugin first. Only if the issue is a problem in Godot should a report be made for Godot.
- Check the documentation. Some issues are caused by a misunderstanding about how a feature works,
  or involve known limitations that are documented.
- Search for existing issues, `open *and* closed <https://github.com/godotengine/godot/issues?q=is%3Aissue>`__,
  to reduce the risk of creating a duplicate issue.
- Consider if the issue you are facing is actually a bug and not a missing feature. If it is a missing feature,
  please :ref:`propose an improvement <doc_contributing_ideas>` instead.

If you are unsure if something is a bug, and not a missing feature or a documented limitation, please don't hesitate
to ask in the `is-this-a-godot-bug discord channel <https://discord.com/channels/1235157165589794909/1334482804863406101>`__
or the other `community channels <https://godotengine.org/community/>`__.

The anatomy of an issue report
------------------------------

The basics
~~~~~~~~~~

If in doubt, list things like system details in case it might be relevant.

Please make a clear note on the issue report for issues that might cause any of the following:

- Harmful effects to anyone testing it, like rapidly flashing images.
- Damage to the project the bug happens in, like corrupting or deleting files.
- Damage to the device the bug happens on, like deleting files outside the project or the device running very hot.
- Disruption or other problems, like crashing or locking up the device, slowing down the device until restarted, etc.

The critical parts
~~~~~~~~~~~~~~~~~~

There are a few parts of an issue report that are critical, without which an issue is
unlikely to be solved (or even tested as triagers are unlikely to spend time testing a report
with these details missing).

The tested versions
^^^^^^^^^^^^^^^^^^^

List *all* versions you have tested if you have tested multiple versions, this helps make it
clear if an issue is a regression or not. If the issue is for a feature that was different or
unavailable in previous versions to the ones tested, please mention this in the tested versions
for ease of testing. Please group tested versions to make it easier to evaluate, like so:

.. code-block:: text

  Reproducible in: 4.6.1, 4.5.1, 4.5
  Not reproducible in: 4.4.1 and earlier

If a bug has been present for the last few minor versions there's usually no need to test it further back.

If you are testing a pre-release version, like ``4.7.dev``, please also test the latest stable version to
help confirm if this is a new regression.

The issue description
^^^^^^^^^^^^^^^^^^^^^

The most important part of an issue report is the description of the issue. While clear steps
to reproduce the issue, or even a :ref:`minimal reproduction project (MRP) <doc_reporting_minimal_reproduction_project>`,
are great *additions* to a report they are not replacements for a clear and detailed description of the issue.

When writing the description of your issue, it's important that you cover the following:

- **What is happening.** Try to get as much detail as possible to avoid confusion, and please keep in mind
  that what might be obvious to you might not be to everyone else. This should be described in text form
  if possible (see :ref:`below <doc_reporting_video_and_screenshots>` for a note about video and screenshots).
- **How you expect, or want, it to behave and work.** It is important that we understand what you expect to happen
  and how you expect the engine to work, as this might not be obvious to maintainers. Even if your assumptions were incorrect,
  this might indicate a failure of how the engine communicates, and might indicate that the documentation needs to be improved,
  or that the design of the editor could be improved to make it more obvious.
- **How the way it behaves conflicts with that expectation.** Even with a clear description of what happens,
  and how you expect it to behave, it might not always be clear exactly in what way the two don't align.

Having a clear description of the issue, and not relying on people replicating the issue to see what is going on,
helps in many ways. Many contributors can find the time to look through an issue and try to understand what is
going on, even when they aren't able to dedicate the time to run an MRP or try to reproduce a bug. Many bugs are
solved without even running the editor by contributors figuring out what is happening from just the description.
This includes, when appropriate, :ref:`adding snippets of code <doc_reporting_code_snippets>` to the report description
even if they are already in the MRP.

A clear description also makes it easier for triagers to work out what is happening, even when they can't test the bug
themselves; for example, if it is a bug happening on a platform you don't have access to. Even when a bug requires actively
reproducing it yourself to solve it, a clear description helps to get you on the right path. More importantly, it
helps you confirm that what you are seeing when testing the issue is the same as what the author of the report is facing.

If you are adding large blocks of text, like crash information, to your report, please use the ``<details>`` tag to hide it by default,
like so:

.. code-block::

  <details><summary>Details</summary>
  <p>

  Put your long crash trace here.

  </p>
  </details>

In the end, it's *impossible* for contributors to fix an issue without a clear description.

The reproduction steps
^^^^^^^^^^^^^^^^^^^^^^

Almost all bugs require clear steps to reproduce the issue. They are a *complement* to the issue description above,
and should help triagers to test and confirm the bug. Try to make the reproduction steps as detailed as possible, without
getting too long or difficult to follow. Long descriptions or explanations should be in the description section. You can
direct readers to the description section if you need to explain something, but try to keep the reproduction steps simple.

Make sure to go through the steps yourself to confirm that they are correct. It can be easy to misremember the details, and if
contributors cannot reproduce the issue with your description, they cannot fix the bug.

.. _doc_reporting_minimal_reproduction_project:

The Minimal Reproduction Project (MRP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A common misconception about the MRP is that its main goal is to "prove" that a bug is happening.

It actually provides a way for contributors to reproduce the bug.
Fixing a bug often requires being able to reproduce it, an MRP provides a reliable way to do exactly that.

This is important both because knowing how to make a bug happen easily is critical to finding what is causing the issue;
for example, by being able to slightly adjust the MRP and see if it stops happening, or running on
a different platform to see if it still happens. Once you have figured out what is causing the bug, the MRP once again
comes in handy to help you make sure the bug *stops* happening after you've created a fix. The hardest kind of bug to fix is
a bug that you can't be sure if it stops happening because you fixed it, or because you just can't make it happen reliably.

An MRP, as the name implies, should be minimal. It should be the least amount of content necessary to replicate the bug, no more,
no less. Please make the MRP as easy to navigate as possible, it shouldn't require extra changes to make it work. If the bug
involves behavior in a running scene it should just require opening the editor and pressing run, if it involves editor behavior
it should just require starting the editor and looking in the main scene, etc.

Full game projects or exported games (executable files) are *not* valid MRPs. If you are running into a bug in your project
and are unable to recreate it in a new project, please create a copy of your project and remove components from it until you
reach a point where the bug happens and nothing unnecessary is left.

If the bug requires any third-party content, like an add-on, please include it in the MRP.

.. _doc_reporting_video_and_screenshots:

Video and screenshots in reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding screenshots or video of what is happening is a great way to add more detail to this, but behavior should,
if possible, be described in text as well to make sure everyone understands and that everyone can access the information.
It can also be hard to judge if something is obvious from a video when you already know what it looks like.
Not only is this important for accessibility reasons, but some video formats are unavailable on some platforms,
especially in mobile browsers. The links to video files or screenshots can also become dead over time meaning
the information gets lost, this cannot happen to text descriptions. It is also not possible to search for information
in images or videos making it much harder to discover existing issues when reporting.

Code should *always* be posted as text (using the code formatting tags [add details]), unless the issue is not about the
code itself, for example if it is about syntax highlighting. Error messages should also always be provided in text form
rather than image or video, this is for multiple reasons, including the ones listed in the previous paragraph.

Having clear details of an error message can be enough to solve an issue. Especially if the error message is very specific.
It is, after all, the very reason error messages even exist, to give clear information that users and maintainers can use
to work out what is wrong.

Make sure to put an empty line before *and* after the link to any content, images or screenshots posted to GitHub will not work
otherwise.

.. note::

    Make sure to take screenshots or video on the actual device used, *not* using another device or camera to record the
    screen (for example with your phone). On Windows you can use the Snipping Tool, on macOS you can use the Screenshot App.
    Please only record the screen with a camera if you need to record something that doesn't turn up in a screenshot or screencapture.

.. _doc_reporting_code_snippets:

Code snippets in reports
^^^^^^^^^^^^^^^^^^^^^^^^

Adding short and specific code snippets to a report can be very helpful in testing the issue. Please make sure to format the code correctly,
use a single backtick (\`) for short snippets of code inside other text, ``\`# Like this!\```. For longer pieces of code or other text,
use triple backticks, and if appropriate add syntax highlighting hints, like this:

.. code-block:: text

  \`\`\`gdscript
  var foo
  \`\`\`
