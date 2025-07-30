Introduction to issue triage
============================

So you are looking to help with bug triage? First of all, thank you!
Your help means a lot!

Bug triage is a fundamental part of our development, this should not be
surprising, but this process is far more than just confirming that a bug
is happening. The more information we have on a bug, what problems it
causes, when it was introduced, what areas it affects, and so on makes a
lot of difference. A bug being thoroughly triaged bug helps other
contributors a lot. Knowing something was an intentional change means
not wasting time trying to “fix” it, knowing all the details means
solving the complete issue and not just part of it, and it minimizes the
risk of introducing new bugs due to not having the complete picture.

Tasks
-----

Listed below are basic instructions and descriptions of different triage
tasks. When relevant these sections link to more detailed documentation
on these tasks. For more detailed instructions on the triage process in
general, please see `Bug Triage
Overview `__.

Confirming report details
~~~~~~~~~~~~~~~~~~~~~~~~~

The most basic step of triage is to make sure an issue report is filled
in properly. For details on what a report should contain please see
`triage workflow `__.

Identifying duplicates
~~~~~~~~~~~~~~~~~~~~~~

Duplicate reports add a lot of clutter to the tracker, and critical
details reported on one report might not be present on others.
Identifying duplicate issues is very helpful to ensure everything is
tracked in one place. This can be difficult due to different wording,
but using tags can help narrow things down, make sure to also look at
the pinned issues at the top of the issue page in case the author missed
these.

Another tool that can help identifying duplicates are the team trackers,
for a list of these see `Team Triage
Trackers `__.

.. raw:: html

   

Testing bugs
~~~~~~~~~~~~

Testing bugs is a critical part of bug triage. Even just confirming that
a bug occurs is useful. Any information here is helpful, not being able
to reproduce a bug with the provided steps or MRP adds information about
what might be going on.

If you’re unable to reproduce the bug it could mean that the steps are
incomplete, or that the MRP is incorrect. In this case you might need to
ask the author for further details or ask them to create an MRP.

.. raw:: html

   

Creating MRPs
~~~~~~~~~~~~~

If you are able to reproduce a bug, but there is no attached MRP, you
can help by creating one. This is especially important if the steps are
more complex, or if the issue requires specific content, like a 3D model
or a texture. Having an MRP is very useful for the process of solving
issues and testing solutions, and not having to create the conditions
again streamlines this process.

Bisecting regressions
~~~~~~~~~~~~~~~~~~~~~

Figuring out when a particular bug occurred can greatly help fixing the
issue, or at least pointing to what might have caused it. Knowing when a
bug occurred also helps with deciding if a fix for a bug should be
cherry-picked to a previous version. When a bug is reproducible in a
current release but not in a previous one (i.e. a feature broke), we
call it a regression.

Bisecting can be done at multiple levels, the basic level is checking
if, for example, a bug that was confirmed on ``4.4`` is also
reproducible on ``4.3``. Next you can test development releases, such as
``4.4.beta1``, these can be found in the `Godot
archive `__. Once the
specific development release has been identified you can go one step
further and
`bisect `__
the regression.

Make sure to announce the fact that you are bisecting a bug on the issue
report to make sure no one else starts bisecting it as well, as
bisecting can take some time.

Testing confirmed bugs with other environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some bugs may have platform-specific components which may or may not be
apparent in the initial report. Notably issues that relate to areas like
rendering, windowing, input, audio, file I/O, or buildsystem - or
outright crash reports - can often be platform specific. If you have a
different setup from the bug reporter (operating system, GPU, etc.) and
the issue can reasonably be expected to involve platform-specific
components, it can be very useful to test the bug with your setup.
Testing the bug and reporting if you can reproduce it, or if you can’t,
adds important information that can help identifying the cause of the
bug, and making sure that contributors know how to reproduce it. This
applies especially if someone reports that they can’t reproduce the bug
on Windows but you are able to do so on macOS for example.

Here extra details like your graphics driver version, different hardware
like a specific sound card or similar can also be relevant.

Bringing bugs to the attention of maintainers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cases where a report might have gone unnoticed by maintainers, for
example when a report has been confirmed but nothing has happened for a
long time (and you can reproduce it too), linking the issue in the
team’s RC channel can help bringing attention to the issue.

For a list of these see `Team Triage
Trackers `__, as
well as mentioning it in the
`#bugsquad `__ channel if
it needs more attention by triagers. For editor related bugs you can
mention it in the
`#editor `__ channel.

.. raw:: html
