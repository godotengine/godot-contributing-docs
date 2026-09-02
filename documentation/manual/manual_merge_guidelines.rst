:allow_comments: False

.. _doc_manual_merge_guidelines:

Manual merge guidelines
=======================

.. note::

    This section is targeted at maintainers. Regular contributors to Godot
    cannot merge pull requests.

There are no rules on which maintainers are or are not allowed to merge changes to
the manual. You do not need to be part of the :team:`Documentation` to do so.

The following are guidelines on when a PR can be merged. These are not hard rules
that you must adhere to. If you're a maintainer then that means we already trust
your judgement. This page exists to help guide your thought process on whether or
not something should be merged.

Like the engine, you should not be doing self-merges unless it's an emergency. As an
example, another maintainer's account was hacked and vandalism and spam were merged.

Even when there are enough approvals, give other maintainers some time to add their
review (a few days is usually fine). This especially applies if a specific person's
review was requested. If more than a month or so passes without that review coming
in, use your judgement to decide whether to poke the person or skip that review.

Broadly speaking all PRs can be put into three categories: **objective fixes**,
**content changes**, and **backend changes**.

Trivial fixes
-------------

Trivial fixes are, as the name implies, any change small change where the PR is an
unarguable fix for a problem with the documentation, where the type of fix can't be
debated. For PRs like these you can merge them with only your own approval. The
following would be considered trivial fixes:

- Removing a duplicated word. For example, a page says the following: "this and and
  that node."
- Fixing a typo.
- Fixing grammar. For example, changing "it's" to "its".
- Fixing a link that no longer works because content was moved.
- Removing a dead link that doesn't need to be replaced. For example, a link to a
  removed community tutorial. Links need to be replaced if any text relies on them.
  For example, "Download Tool ABC here and then do this with it." In situations like
  that a replacement needs to be found, or if the workflow is different, more
  substantial changes need to be done.
- Replacing an image that does not show what is described in the text.
- Replacing an outdated image with no major text changes. Minor text changes like a
  rename are fine, for example, changing ``Node`` to ``Node3D``.

There are two important things to keep in mind. First, updating a page for engine
changes is **not** automatically a trivial fix in this context. If there's a
substantial amount of text that's changed, that would be considered a content
change.

Second, even though these are relatively minor changes, you are still responsible
for ensuring all changes are correct and adhere to the :ref:`image guidelines <docs_image_guidelines>`
if applicable.

Content changes
---------------

Content changes are any change that change where the PR is not considered a
trivial fix. This includes new pages, updated paragraphs, reworded sections, and
added sections.

When these PRs should be merged will vary from situation to situation, but you may
use the following sections as a starting point to decide.

Small changes
~~~~~~~~~~~~~

Small edits, such as one paragraph and a screenshot are generally fine with only one
approval. However, you should be leaving the PR open for about a week before merging
in case anyone else wants to chime in and review.

Large changes
~~~~~~~~~~~~~

For larger changes, such as an entirely new page with a substantial amount of
content, or an extensive overhaul of an existing one, you should be waiting longer
and for more approvals.

Generally 2 weeks and 3 PR approvals is the minimum for situations like this.

Backend changes
---------------

Backend changes are anything that changes dependencies, or the website
itself such as its layout or design.

Dependency updates
~~~~~~~~~~~~~~~~~~

Typically, GitHub's Dependabot will open a PR to update dependencies on GitHub.
These can be merged with just your own approval, provided that you've built the
branch of that PR locally and confirmed that nothing has broken. You don't need to
check every page. As an example, if Dependabot submits a PR to update ``sphinx-tabs``
then you should check about 3 pages that have code tabs of different types and make
sure everything still looks normal.

Other changes
~~~~~~~~~~~~~

For any other change, such as adjusting website style or functionality, you should
typically wait at least two weeks, and it should have at least 3 PR approvals
including your own.

This is also the one situation where approval from the documentation team is
required. It doesn't have to be everyone on the team, but it should be approved by 2
people on the team at minimum.
