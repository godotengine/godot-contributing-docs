.. _doc_contributing_to_release_pages:

Contributing to release pages
=============================

Every minor (4.x) release of Godot has a release page dedicated to explaining the
version's improvements and changes.

See the following pages for examples of previous 4.x release pages:

- `Godot 4.3 <https://godotengine.org/releases/4.3/>`__
- `Godot 4.4 <https://godotengine.org/releases/4.4/>`__
- `Godot 4.5 <https://godotengine.org/releases/4.5/>`__
- `Godot 4.6 <https://godotengine.org/releases/4.6/>`__
- `Godot 4.7 <https://godotengine.org/releases/4.7/>`__

Structure guidelines
--------------------

For copywriters and copyeditors, cards on a release page consist of three major components:

- The **title** provides a fragment-sentence description of the improvement.
- The **subtitle** provides a short motto or quip related to the improvement, and is often a reference to something else.
- The **text** provides a few paragraphs discussing the improvement in detail and how it improves on previous Godot behavior.

The problem comes first
~~~~~~~~~~~~~~~~~~~~~~~

As per the :ref:`best practices for engine contributions themselves <doc_best_practices_problem_always_comes_first>`,
we often start the section describing an enhancement with a recap of the previous/existing behavior.
By highlighting what was previously problematic, we help the reader understand why they should be excited for this new feature or fix.

**Bad:**

    The new **Time Travel** feature lets you freely move through the temporal dimension,
    allowing you to get more time to work on your project or see what genres of game
    are going to be popular in the next few years.

**Good:**

    Previously, finding time to work on your game could be difficult, with lots of
    other responsibilities and things going on around you. And even when you did have
    time to work on it, there was no telling if people would be interested in it by
    the time it came out.

    That’s now going to be a thing of the past. We've added **Time Travel** mode,
    which lets you freely move through the temporal dimension so you can ensure your
    game is what people will be interested in by the time it releases, and you can
    take as much time as you need to develop it.

Spelling, grammar, and formatting
---------------------------------

In general, the :ref:`documentation writing guidelines <doc_docs_writing_guidelines>`
are applicable when writing or editing content for release pages.
Notably, however, the words listed in the section “Ban these 8 words” are acceptable to use on
release pages.

Title and subtitle formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Card titles and subtitles should not have periods at the ends of sentences.
Exclamation or question marks at the ends of sentences in a subtitle are allowed,
if the sentence needs them.

Tense
~~~~~

Use the present tense when referring to features or fixes in the current version
of Godot, and the past tense when referring to previous versions of Godot.

**Bad:**

    Currently in Godot, there’s no way to get an ice cream sundae. If you want a
    sweet treat while working on your game, you have to get up and get it yourself.
    
    In the next version, you’ll be able to click the **Ice Cream** button to have
    a bowl full of ice cream appear in your hands instantly!

**Good:**

    Previously, there was no way to get an ice cream sundae. If you wanted a sweet
    treat while working on your game, you had to get up and get it yourself.

    Now, you can click the **Ice Cream** button to have a bowl full of ice cream
    appear in your hands instantly!

Referring to authors
~~~~~~~~~~~~~~~~~~~~

Within the body text of a block, avoid naming specific PR authors by name.
Instead, refer to the Godot contributors as a collective “we”.
(Don't worry about the PR authors; they get credited in the space at the bottom of the feature card!)
Likewise, refer to the reader (and potential user of the new Godot version) as “you”.

**Bad:**

    TODO

**Good:**

    TODO

..
    TODO: good and bad examples here, perhaps using a popular historical person or fictional character's name


Quotation marks
~~~~~~~~~~~~~~~

Use the correct quotation mark and apostrophe symbols:

* Apostrophe: `’` 
* Opening quote: `“`
* Closing quote: `”`

..
    TODO: explain how to quickly type these on various platforms
