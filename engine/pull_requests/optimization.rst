.. _doc_optimization:

Optimization
============

Introduction
------------

In general, the project prefers clear, simple code over highly optimized code,
except in bottlenecks.

However, optimization PRs are welcome providing they follow the guidelines below.

.. note::

    The project doesn't automatically accept all optimization PRs, even if they
    improve performance.


Background
----------

When assessing optimization we need to take into account:

Benefits
~~~~~~~~

Is optimization worth doing in this case?

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


If code is relatively slow but is only called rarely (for instance once on level load),
then there is less potential benefit to speeding it up.

Choosing what to optimize
-------------------------

Most optimizations do have some costs, so instead of randomly picking part of
the engine to optimize, we recommend that you use a profiler to identify bottlenecks
**before** making any changes.

If an area of the engine is not appearing in a profile, no matter how inefficient the
code, then a PR is unlikely to be approved and merged.

*(There are some exceptions, but this is generally the pattern.)*

PR Requirements
---------------

For this reason, when making an optimization PR you should:

- Include profiling and benchmarking before / after
- Test on multiple platforms where appropriate, especially mobile
- Show assembly before / after (for CPU PRs) to confirm how the optimization is working

In particular you should be aware that for micro-optimizations, c++ compilers will often
be aware of basic tricks and be performing them already in optimized builds. This is why
showing before / after assembly can be important in these cases.

Optimizing for best / worst cases
---------------------------------

Often in optimization there can be situations where optimizing for a rare case slows a
common case, or vice versa. Be aware that surprisingly often in games, optimizing for
the worst case can be more important than optimizing for the best case, as worst cases
can cause dropped frames.

In situations like this trading off speed for different paths, reviewers may have to
decide whether a change is worth making.

GPU Optimization
----------------
GPU optimization can be even more fraught with difficulty than CPU optimization,
primarily because of the vast range of hardware the engine must run on, and differences
in drivers and behaviour.

Even more so than for CPU work, it is essential to test GPU changes on mobile as well as
desktop, and the more platforms, the better.

In particular you should be aware that changes which increase performance on one platform
can often reduce performance on another.

