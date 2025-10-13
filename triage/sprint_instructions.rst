.. _doc_bug_triage_sprint_instructions:

.. note::

    This page contains instructions for participants in triage sprints, they are managed in the
    `#bugsquad-sprints <https://chat.godotengine.org/channel/bugsquad-sprints>`__ channel. These
    instructions are only relevant if you are participating in a sprint.

    .. TODO: Add link to instructions for organizing sprints here once written.

Triage sprint instructions
==========================

In the sprint discussion are threads with batches, comment in a thread to claim the batch if it is free.
Please don't work on a batch without claiming it, even if you are unsure if you can finish all the issues in time,
to avoid duplicating work. If you have finished a batch, and are interested in doing more and feel you have the time
to complete one more, you can claim a second batch if there are any open batches. But please claim only one batch at a time.

Please ask any questions or updates about issues relating to a batch in the thread of that batch.

Sprint steps
------------

- Read through the conversation and see if there's some pending request, for example someone asking for an MRP or clarification.

    - If there is, and the information is still missing, please comment with the issue report link in the batch thread and we will close it.

- Confirm that the report is filled in correctly, that all the necessary details are available.

    - If something is missing, please comment on the issue asking for more information, or comment in the batch thread with the issue
      report link and we will do it.

- See if you recognize this issue from somewhere else, it might be a duplicate.

    - If it is a duplicate, please comment on the issue linking to the (possible) duplicate, or comment in the batch thread.

- Test the issue if you are able.

    - If the issue is specific to some platform or hardware you do not have, comment with the issue report link in the sprint
      discussion (and create a thread under it) and someone else can test it if they are able.
    - Otherwise report the result of testing it on the issue itself, including what version(s) you tested it on and other details
      such as OS, hardware, etc. This includes if you are unable to confirm the issue.

If you need help updating any details on the issue, such as fixing the title, any tags or trackers, etc., please tag the person organizing the sprint
or ask in the batch thread.

When you are done with the batch please comment in the batch thread. You can report the result of your triage as you go through them or at the end.

For more details on the general triage workflow, please see :ref:`doc_bug_triage_overview`.
