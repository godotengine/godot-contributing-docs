.. _doc_bug_triage_sprint_organization:

Organizing triage sprints
=========================

.. note::

   This section is for the bugsquad team. Regular Godot contributors are not
   expected to organize triage sprints.

   For instructions on participating in triage sprints, see :ref:`doc_bug_triage_sprint_instructions`.

These are instructions for organizing triage sprints.

Before starting
---------------

Before starting a sprint it is good to evaluate the timing, leave at least a month between sprints, two if
the most recent sprint had low attendance. Sprints should be held during the ``dev`` phase. To evaluate the
need for a sprint, use the search query below to assess how many issues are available for the sprint.

If you feel it is a good time for a sprint and you are interested in organizing one,
feel free to ask in the internal bugsquad maintainer channel.

Gauge interest
--------------

Before deciding to organize a triage sprint, make sure to gauge interest from the community.
Do this by posting a message in the |#bugsquad| channel, something like this:

.. code-block:: text

    @all considering doing a new sprint but wanting to gauge the interest, so if you're interested in joining please react to this comment.
    It's not binding but please only react if you feel like you will be able to join!

    If you're interested in updates about sprints, please join #bugsquad-sprints if you haven't already!

Post a shorter message in |#devel| and |#general| pointing to |#bugsquad| and asking anyone who is interested to look there.

Wait for a week or two or until there are at least 8-10 reactions to the comment. If there's no significant interest
after over two weeks you can make a follow-up comment in a thread under that comment that due to lack of interest there
won't be a sprint at this time.

Prepare the sprint
------------------

If there's been enough interest in a sprint, you can begin gathering issues for it.

Gather issues from GitHub's issue tracker, excluding platform and language specific labels
to reduce the risk of hard-to-evaluate issues. You can use this example from previous sprints:

.. code-block:: text

    updated:>@today-1m label:"needs testing" -label:confirmed -label:platform:ios -label:platform:android -label:platform:uwp -label:platform:visionos -label:platform:web -label:platform:windows -label:platform:linuxbsd -label:platform:macos -label:topic:dotnet

Use the ``updated`` range to filter out recently updated issues and focus on issues that need to be picked up.
Collect ten batches of ten issues each by copying individual issues from the search to make sure they aren't lost before starting the sprint.
If there are unclaimed batches from previous sprints you can use them here.

Decide on a funny alliterative name for the sprint (the most important step!), like "Frivolous Frog" or "External Emu".
Check the |#bugsquad-sprints| channel for the last letter to continue from.

When you have a name, create a new **discussion** in the |#bugsquad-sprints| channel named ``Triage Sprint #{number} ({Name})``,
counting up from the most recent sprint. When the discussion has been created, change it to read-only by clicking the info icon (an "i" in a circle),
clicking the "Edit" button, scrolling down to the section named "Advanced Settings", and checking the "Read Only" option. You can also add a fitting
image based on the name.

In the discussion, add an introduction linking to the sprint instructions (``contributing.godotengine.org/en/latest/triage/sprint_instructions.html``),
make sure to exclude the ``https://`` portion of the link to prevent previews being generated. Add a line of ``-`` characters as a separator and then add
a message for each batch, ``Batch 1``, ``Batch 2``, etc., and make a thread for each. Put the list of issues as a message in this thread and add
``"Comment here to claim this batch."`` at the end.

After the batches add another separator and then a questions thread and another one for feedback, followed by another separator.
Finally, if the sprint is not starting immediately, put in a note about when the sprint is expected to start,
and for anyone interested in participating to join the thread for updates.

For an example of how to format and structure these messages, please see previous sprint threads.

Announce that a sprint is being prepared, link to the sprint discussion, and ask anyone that is interested to join the discussion for updates.

Start the sprint
----------------

Start the sprint by removing the read-only status of the discussion and announcing the sprint in the |#bugsquad|, |#devel|, and |#general| channels.
Then announce the start of the sprint in the discussion, asking people to read the first message with instructions and to claim batches.

Track and follow up the sprint
------------------------------

While the sprint is running keep an eye on the discussion and the individual threads, as well as in the issue tracker. Make sure to check any questions or
feedback in the respective threads. Follow the general :ref:`triage guidelines <doc_bug_triage_overview>` as the issues are checked by participants.

If more than half the batches are unclaimed or things are generally slow after a week, make a new announcement like the one starting the sprint calling for participants.
If there are participants that have finished a single batch and there are batches remaining, remind everyone that they can claim a second batch if they have completed their first.

Finalize the sprint
-------------------

If a week has passed since the last change, or all claimed batches are completed, announce in the channel at the start of the week that if no one has any new updates that the sprint will be finished at the end of the week.
Ask for feedback in the relevant thread and remind participants that if they have not claimed a second batch and are done with their first they can claim a second one.
Remember to thank participants at this point as well, and make a reminder in the same channels as the initial announcement if there are unclaimed batches left.

At the end of that week, if all batches are finished, or no one has claimed any new batches, and there have been no objections, announce that the sprint is finished
and no batches can be claimed. Thank everyone once again and ask for feedback.

Final steps
-----------

When the discussion has been inactive for more than a week after finishing the sprint, mark it as read-only, thank everyone a final time, and ask people to stay tuned for the next sprint.

Discuss any relevant feedback in the bugsquad maintainer channel and check how it went with the rest of the bugsquad that participated on the triage side.

Finally, gather any unclaimed batches for future sprints, and save any issues that participants couldn't test for future triage, then archive the discussion.

.. |#devel| replace:: `#devel <https://chat.godotengine.org/channel/devel>`__
.. |#general| replace:: `#general <https://chat.godotengine.org/channel/general>`__
.. |#bugsquad| replace:: `#bugsquad <https://chat.godotengine.org/channel/bugsquad>`__
.. |#bugsquad-sprints| replace:: `#bugsquad-sprints <https://chat.godotengine.org/channel/bugsquad-sprints>`__
