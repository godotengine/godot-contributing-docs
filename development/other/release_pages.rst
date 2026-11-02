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


.. note::
    
    To keep them from becoming too long, some examples may omit guidelines
    specified in another part of this document.

Structure overview
--------------------

For copywriters and copyeditors, cards on a release page consist of three major components:

- The **title** provides a fragment-sentence description of the improvement.
- The **subtitle** provides a short motto or quip related to the improvement, and is often a reference to something else.
- The **text** provides a few paragraphs discussing the improvement in detail and how it improves on previous Godot behavior.

Spelling, grammar, and formatting
---------------------------------

In general, the :ref:`documentation writing guidelines <doc_docs_writing_guidelines>`
are applicable when writing or editing content for release pages.

.. note::

    The words listed in the section "Ban these 8 words" are (more) acceptable to use,
    as the release pages have a relatively informal tone and are intended to "sell"
    the new version of Godot more than documentation pages.
    
    Still, take care to avoid writing text such that a reader/user may feel
    belittled or bad for not understanding something.


Sentence formatting for titles and subtitles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Card titles and subtitles should not have periods at the ends of sentences.
Exclamation or question marks at the ends of sentences in a subtitle are allowed,
if the sentence needs them.

Formatting card text
~~~~~~~~~~~~~~~~~~~~

Make text ``**bold**`` when it is the name of the feature being described by the card.
A card's text does not necessarily need to name the feature, and if it doesn't, then
nothing needs to be bolded.

Text should be ````monospaced```` when it is a node or class name. For the first instance
of the name, link it to the relevant page in the Godot Docs as well.

If some text refers to a lengthy or notable discussion, link the text to the discussion.

**Bad:**

    The new Smell node type can be placed in a Viewport when using 3D graphics
    to send a scent from your game directly to the player. Note that this will not work
    if the Viewport is rendering a 2D scene.

**Good:**

    The new **Smell** node type can be placed in a ``Viewport``
    when using 3D graphics to send a scent from your game directly to the player.
    Note that this will not work if the ``Viewport`` is rendering a 2D scene.

..
    TODO: Get the first `Viewport` to link to https://docs.godotengine.org/en/stable/classes/class_viewport.html
    I couldn't figure out how to get that to work with RST.
    In the YML files for release pages, it looks like it uses markdown syntax (like [Link text](https://link.com))
    but that does not appear to work here.

Tense
~~~~~

Use the present tense when referring to features or fixes in the new version
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

Referring to contributors and readers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within the body text of a block, avoid naming specific PR authors by name.
Instead, refer to the Godot contributors as a collective "we".
The authors will be credited in the space at the bottom of the feature card.

Likewise, refer to the reader (and potential user of the new Godot version) as "you".

**Bad:**

    Our contributor Sherlock Holmes has added the new **Error Deduction** feature, which
    will allow the user to figure out what’s causing their game to crash.

**Good:**

    We’ve added the new **Error Deduction** feature, which will allow you to figure out
    what’s causing your game to crash.


Quotation marks and apostrophes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the correct quotation mark and apostrophe symbols:

* Apostrophe: ``’`` (``U+2019``)
* Opening quote: ``“`` (``U+201C``)
* Closing quote: ``”`` (``U+201D``)

.. warning::

    If you are using a code-focused text editor, it may not use these symbols by default,
    but instead symbols that look very much like them. Pay close attention to the direction
    that the symbols "lean" in!

**Bad:**

    We're putting the "woah" in Godot!

**Good:**

    We’re putting the “woah” in Godot!

You can enter these characters with the following methods:

* **Windows:** Hold :kbd:`Alt`, then type the Unicode codepont number (such as ``2019`` for the apostrophe).
* **macOS:** Press :kbd:`Ctrl + Cmd + Space`, then type the Unicode codepoint (such as ``U+2019`` for the apostrophe).

If these methods don't work, you can also copy and paste the characters from this page.

Card content
------------

Coming up with good subtitles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subtitles should be only a line or two long.
They may reference a common English idiom or saying, or reference a relatively universal
piece of pop culture.
Emoji are acceptable, but should be used very sparingly.

.. note::

    Creating subtitles is not an exact science. If you have an idea for one, propose it to
    others working on the page who come from different backgrounds (e.g., countries, cultures)
    and see how frequently they understand the joke/reference.


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

    That’s now going to be a thing of the past. We’ve added **Time Travel** mode,
    which lets you freely move through the temporal dimension so you can ensure your
    game is what people will be interested in by the time it releases, and you can
    take as much time as you need to develop it.