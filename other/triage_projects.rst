.. _doc_triage_projects:

Helping out teams (using triage projects)
=========================================

Godot is organized into :ref:`teams <doc_areas>`, and some teams actively maintain a **triage project**.

Triage projects can be seen as the teams' public to-do lists: It is where they keep track of bugs and proposals,
and organize them by importance and complexity.

There are several ways to contribute, even if you are not a maintainer! Feel free to browse the issues
and help the team out by :ref:`implementing fixes <doc_creating_pull_requests>` or :ref:`reviewing pull requests <doc_pr_review_guidelines>`.

Keep reading to learn how to do this effectively.

How to use triage projects
--------------------------

Triage projects use GitHub's "Projects" feature, which you can learn more about in `GitHub's documentation <https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects>`__.

They are organized into tabs, each of which represents some view of the underlying data. Tabs may differ from team to
team; try several tabs to see which one is most useful to you.

Below the tabs you will find a large table. Each **row** represents an **issue** (bug report or proposal), while
**columns** show different **aspects** of said issue. The following columns are of particular importance:

- **Priority**: How important the issue is to the team (from ``low`` to ``critical``).
- **Complexity**: How difficult the solution may turn out to be. This is not a guarantee; just an educated guess by knowledgeable maintainers.
- **Status**: The latest evaluation of the issue by the team, with the following values:
    - **For team assessment**: The team has not discussed or triaged the issue yet.
    - **Up for grabs**: Any contributor is free to work on the issue.
    - **Needs further info**: The team is waiting for more information on the issue.
    - **Needs Proposal**: Resolving the issue requires adding new features, which should be :ref:`formally proposed <doc_contributing_ideas>` and discussed.
    - **In progress / assigned**: A maintainer is working on the issue.
    - **Fix pending review**: A potential solution has been submitted and needs reviews.
    - **Done**: The issue is closed and the problem solved. Huzzah!
- **Category**: Identifies the area of code the issue affects.
- **Assignees**: When maintainers work on an issue, they will link themselves here. Regular contributors cannot be linked as assignees.

Keep in mind that values may be outdated, as there are a lot of issues to triage. You can bring issues to the
attention of maintainers in the `contributor chat <https://chat.godotengine.org/>`__.

If you start working on an issue, but aren't a maintainer, please comment on the issue that you are doing so.

Triage guidelines
-----------------

.. note::

    Only maintainers and members of the :team:`Bugsquad <triage>` can edit triage projects, regular contributors
    can only view them. To participate, get involved with the :ref:`teams <doc_areas>` or the :ref:`Bugsquad <doc_triage>`!

Generally, each team is free to use the triage projects as they see fit. Always consult with your
team about how to use the triage project effectively.

That being said, here are some things to keep in mind:

- **Respect our code of conduct.** Please keep in mind that triage projects are public. Use the "Comments" column respectfully.
- **Only triage what you know.** For example, if you don't know how complex a solution is going to be, it is better not to fill this value in than to guess.
- **Use triage projects to your advantage.** If you were hoping to implement a feature or track down a bug,
  but can't get around to it, make an issue or proposal and link it in the triage project. Community members may come and help you out!
- **Be selective about "Up for grabs".** Contributors see this tag as a signal to start working on issues.
  For proposals especially, please only use it if you actually want to see implementations for this proposal posted by the community.
- **Remember to work as a team.** If you disagree with the triage of an issue, please discuss it with the team before making changes.
