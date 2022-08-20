A Framework for Benchmarking Clustering Algorithms
==================================================

<!--
::::{epigraph}
**Genie finds meaningful clusters and is fast even on large data sets.**
::::
-->

<!--
.. image:: _static/img/genie_toy_example.png
    :class: img-right-align-always
    :alt: Genie
    :width: 128px
-->

It is not rare for clustering papers/graduate theses to consider only a small
number of datasets, say 5–10 UCI-sourced ones,
which obviously is too few to make any evaluations rigorous enough.
Other authors propose their own datasets, but forget to test their methods
against other benchmarks batteries, risking their evaluations be biased.

Authors who share their data (thanks!) might not necessarily make
the use of their suites particularly smooth (different file formats,
different ways to access, etc., even across a single repository).
On the other hand, other machine learning domains
(but also: [optimisation](https://en.wikipedia.org/wiki/Test_functions_for_optimization))
have had some standardised, well agreed-upon approaches for testing
the quality of the algorithms for quite a long time.

In this project we aim to **aggregate, polish and standardise the existing
clustering benchmark suites** referred to across the machine learning
and data mining literature. Moreover, we introduce **new datasets**
of different dimensionalities, sizes and cluster types.


**How to cite.**
Gagolewski M.,
A Framework for Benchmarking Clustering Algorithms,
2022,
<https://clustering-benchmarks.gagolewski.com>


**Acknowledgements.**
...TO DO...
Anna Cena
datasets: SIPU etc.




::::{toctree}
:maxdepth: 2
:caption: Clustering Benchmarks
:hidden:

About <self>
Author <https://www.gagolewski.com/>
::::


::::{toctree}
:maxdepth: 2
:caption: Introduction

weave/partition-similarity-scores
weave/noise-points
weave/many-partitions
weave/data-v1
weave/file-format
weave/how-to-access
::::


::::{toctree}
:maxdepth: 1
:caption: Python API Documentation

weave/clustbench-usage
clustbench-documentation
::::


::::{toctree}
:maxdepth: 1
:caption: See Also

Source Code (GitHub) <https://github.com/gagolews/clustering-benchmarks>
Bug Tracker and Feature Suggestions <https://github.com/gagolews/clustering-benchmarks/issues>
PyPI Entry <https://pypi.org/project/clustering-benchmarks/>
Data Wrangling in Python <https://datawranglingpy.gagolewski.com/>
genieclust Package <https://genieclust.gagolewski.com/>
::::


::::{toctree}
:maxdepth: 1
:caption: Appendix

weave/cluster-validity-measures
news
z_bibliography
::::
