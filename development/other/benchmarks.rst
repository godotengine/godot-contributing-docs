.. _doc_contributing_benchmarks:

Contributing benchmarks
=======================

To keep track of Godot performance across commits,
we have a `benchmarks repository <https://github.com/godotengine/godot-benchmarks>`__
that is run on a dedicated server every day. You can look at the results on
`benchmarks.godotengine.org <https://benchmarks.godotengine.org>`__.

While we have a set of benchmarks that we run on a daily basis, we are always
looking for new benchmarks to add to the repository. If you have an idea for a
new benchmark, please submit a pull request for it on the
`Godot benchmarks <https://github.com/godotengine/godot-benchmarks>`__ repository.

This page describes the process of adding a new benchmark to the repository.
It's recommended to open one pull request per set of benchmarks. If you create
multiple benchmarks in unrelated categories, please open separate pull requests
for each.

If you are serious about helping out, or have anything else to discuss, come join us in the
`#benchmarks <https://chat.godotengine.org/channel/benchmarks>`__ channel!

Adding new benchmarks
---------------------

You can add new benchmarks by following these steps:

Create new benchmark
^^^^^^^^^^^^^^^^^^^^

Create a new script with ``snake_case`` naming that
``extends Benchmark``, then save it in one of the existing folders
depending on its category. If your benchmark does not suit any existing
category or subcategory, you can also create a new folder in the
repository's root folder.

Configure the benchmark
^^^^^^^^^^^^^^^^^^^^^^^

In the ``_init()`` function of your script, configure your benchmark by
initializing any desired ``Benchmark`` variables to true:

- ``test_render_cpu``: Enable this for rendering benchmarks. Leave it
  disabled for other benchmarks.
- ``test_render_gpu``: Enable this for rendering benchmarks. Leave it
  disabled for other benchmarks.
- ``test_idle``: Enable this for non-rendering CPU-intensive
  benchmarks. Leave it disabled for other benchmarks.
- ``test_physics``: Enable this for physics benchmarks. Leave it
  disabled for other benchmarks.
- Leaving all of these disabled will only time the initial call to your
  ``benchmark_`` function (see below).

Implement the benchmark
^^^^^^^^^^^^^^^^^^^^^^^

The runtime will scan your script for functions beginning with
``benchmark_``. For basic benchmarks, writing your code inside such a
function is sufficient for it to be automatically registered and become
available for benchmarking by the user. The runtime will end the
benchmark once your function returns and report the amount of time spent
running inside it.

For more advanced benchmarks, the runtime expects the function to return
a ``Node``. Return the appropriate node for your benchmark to
signal to the runtime that it should continue measuring system resource
usage even after your function returns. The node type you should return
depends on what kind of benchmark it is:

- For 3D rendering benchmarks, the root node should be Node3D.
- For 2D rendering benchmarks, the root node should be Node2D.
- For UI benchmarks, the root node should be Control.
- For scripting or miscellaneous benchmarks, the root node should be Node.

The runtime will add your node to the scene as a root node, leave it running
for a fixed amount of time (5 seconds), and then end the benchmark and
report the various metrics configured above.

Remember to follow the
`GDScript style guide <https://docs.godotengine.org/en/latest/tutorials/scripting/gdscript/gdscript_styleguide.html>`__
when writing new scripts. Adding type hints is recommended whenever
possible, unless you are specifically benchmarking non-typed scripts.

.. note::

   C# benchmark functions must begin with ``Benchmark``, instead of
   ``benchmark_``. For C# benchmarks to be available, you must use the
   .NET version of the engine.

Test the benchmark
^^^^^^^^^^^^^^^^^^

1. Run the project in the editor.
2. Check the checkbox next to your newly added benchmark and click
   **Run** in the bottom-right corner.
3. Wait for the benchmark to complete.
4. If all goes well, the benchmark completion time should appear in the
   table for all enabled benchmarks (and all relevant metrics). Metrics
   that were disabled on a specific benchmarks will not display any
   result.

If the benchmark works as expected, congratulations! You can now open a
pull request for it on the
`Godot benchmarks <https://github.com/godotengine/godot-benchmarks>`__
repository.
