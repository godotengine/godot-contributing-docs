.. _doc_optimization:

Optimization guidelines
=======================

Introduction
------------

In general, the project prefers clear, simple code over highly optimized code,
except in bottlenecks.

However, optimization PRs are welcome provided they follow the guidelines below.

.. note::

    The project doesn't automatically accept all optimization PRs, even if they
    improve performance.

Choosing what to optimize
-------------------------

Predicting which code would benefit from optimization can be difficult without
using performance analysis tools.

Oftentimes code that looks slow has no impact on overall performance, and code
that looks like it should be fast has a huge impact on performance. Further,
reasoning about why a certain chunk of code is slow is often impossible to do
without detailed metrics (e.g. from a profiler). 

Instructions on using some common profilers with Godot can be found `here
<https://docs.godotengine.org/en/stable/engine_details/development/debugging/using_cpp_profilers.html>`_.

As an example, you may optimize a chunk of code by caching intermediate values.
However, if that code was slow due to memory constraints, caching the values and
reading them later may be even slower than calculating them from scratch!

Similarly, if the code is relatively slow but is only called rarely (for
instance once on level load), then there is less potential benefit to speeding
it up (unless you are specifically optimizing load times).

Most optimizations involve making a tradeoff, so instead of randomly picking a
part of the engine to optimize, we recommend that you use a profiler to identify
bottlenecks **before** making any changes to ensure that your optimization will
make a difference.

If an area of the engine is not appearing in a profile, no matter how
inefficient the code, then a PR is unlikely to be approved and merged.

*(There are some exceptions, but this is generally the pattern.)*

When in doubt, look for Github issues tagged with the `performance
<https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aperformance>`_
label to guide your optimization efforts.

When assessing optimization opportunities, we need to take into account:

Benefits
~~~~~~~~

Is the optimization worth doing in this case?

- How often is this code called?
- How much of a bottleneck is it to overall performance?
- Does profiling show it to be a bottleneck?

Costs
~~~~~

What are the downsides?

- Code complexity
- Code readability
- Maintenance burden
- Constraining future changes
- Risk of regressions

Optimization process
--------------------

Once you have decided what you should optimize, you should start by capturing a
baseline profile in your profiler of choice. Ensure you are running Godot's
latest ``master`` branch and that you use an optimized build of Godot, since many
things that run slowly in debug end up disappearing with optimizations enabled.

By default, Godot builds with optimizations enabled. See `the Godot build docs
<https://docs.godotengine.org/en/stable/engine_details/development/compiling/introduction_to_the_buildsystem.html#optimization-level>`_
for more information about build optimization settings.

In some cases using a synthetic benchmark is also acceptable, but remember that
Godot is a game engine. The golden standard is to test the performance of real
games. Benchmarks can be helpful, but they can also be misleading because it is
very difficult to create benchmarks that reflect how performant the code will be
in an actual game.

Once you have your baseline profile/benchmark, make your changes and rebuild the
engine with the exact same build settings you used before. Then profile again
and compare the results.

.. note::

    Results will fluctuate, so you'll need to make your test project or
    benchmark intensive enough to isolate the code you're trying to optimize (ideally,
    go for at least 2 seconds of real-life runtime). Additionally, you should run the
    test multiple times, and observe how much the results fluctuate. Fluctuations of up
    to 10% are common and expected. The fastest run is usually the most accurate number.

Pull request requirements
-------------------------

When making an optimization PR you should:

- Explain why you chose to optimize this code (e.g. include the profiling result, link the issue report, etc.).
- Show that you improved the code either by profiling again, or running systematic benchmarks.
- Test on multiple platforms where appropriate, especially mobile.
- When micro-optimizing, show assembly before / after where appropriate.

In particular, you should be aware that for micro-optimizations, C++ compilers will often
be aware of basic tricks and will already perform them in optimized builds. This is why
showing before / after assembly can be important in these cases.
(`godbolt <https://godbolt.org/>`_ can be particularly useful for this purpose.)

The most important point to get across in your PR is to highlight the source of
the performance issues, and have a clear explanation for how your PR fixes that
performance issue. Your profiling/benchmarking results are proof that your
optimization was successful.

Optimizing for best / worst cases
---------------------------------

Often in optimization there can be situations where optimizing for a rare case slows a
common case, or vice versa. Be aware that surprisingly often in games, optimizing for
the worst case can be more important than optimizing for the best case, as worst cases
can cause dropped frames.

In situations where a PR is trading off speed in different paths, reviewers may have to
decide whether a change is worth making.

GPU optimization
----------------

GPU optimization can be even more fraught with difficulty than CPU optimization,
primarily because of the vast range of hardware the engine must run on, differences in
drivers and behavior, and aggressive power saving modes that downclock the GPU when
not under stress.

Even more so than for CPU work, it is essential to test GPU changes on mobile as well as
desktop, and the more platforms, the better.

In particular, you should be aware that changes which increase performance on one platform
can often reduce performance on another.

