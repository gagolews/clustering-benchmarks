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

There is no, nor will there ever be, single best clustering algorithm.
Still, we would like to be able to separate the wheat from the chaff:
to pinpoint those which are well-performing on certain task types
and filter out the systematically disappointing ones.
To do so, we can run the algorithms on a variety of datasets
and compare their outputs to the reference, ground truth groupings
that are provided by experts.

However, it is not rare for research papers/graduate theses to consider
only a small number of datasets, say 5–10 UCI-sourced ones.
This is obviously too few to make any evaluation rigorous enough.

Other authors propose their own datasets, but forget to test their methods
against other benchmarks batteries. This might lead to biased conclusions.

Also, researchers who share their data (thanks!) might not necessarily make
the use of their suites particularly smooth (different file formats,
different ways to access, etc., even across a single repository).
On the other hand, other machine learning domains
(e.g., classification and regression problems included in the said UCI
{cite}`uci`; but also: [optimisation](https://en.wikipedia.org/wiki/Test_functions_for_optimization))
developed some standardised, well agreed-upon approaches for testing
the quality of the algorithms long time ago.


This project aims to:

* **aggregate, polish, and standardise the existing clustering benchmark suites**
    referred to across the machine learning and data mining literature,
* introduce **new datasets** of different dimensionalities,
    sizes, and cluster types,
* propose a **consistent methodology** for evaluating clustering algorithms.


The proposed methodology at a glance: ***TODO**

* various datasets or different dimensionality, and cluster sizes, including imbalanced problems
* each dataset is equipped with at least one or more ground truth partition provided by experts – as there can be many equally valid partitions
* an algorithm is run to partition the datasets into a desired number of clusters (e.g., to find all 2-, 3-, 4-... -clusterings)
* external cluster validity scores are used to relate the outputs to all the possible reference sets
* noise points can be included in the dataset to make the clustering harder,
but they are ignored when computing the similarity score
* the best result is reported (has or has not the algorithm reproduced at least one of the ground-truth partitions well?)


**Author/Editor/Maintainer**: [Marek Gagolewski](https://www.gagolewski.com)

**How to cite**: Gagolewski M., *A Framework for Benchmarking Clustering Algorithms*,
2022, <https://clustering-benchmarks.gagolewski.com>

**Acknowledgements.**
...TO DO...
Anna Cena
datasets: SIPU etc.

Data are provided solely for research purposes, unless stated otherwise.
Please cite the literature references mentioned in the description files
corresponding to each dataset if you use them in your publications.





::::{toctree}
:maxdepth: 2
:caption: Clustering Benchmarks
:hidden:

About <self>
Author <https://www.gagolewski.com/>
Source Code (GitHub) <https://github.com/gagolews/clustering-benchmarks>
Bug Tracker and Feature Suggestions <https://github.com/gagolews/clustering-benchmarks/issues>
PyPI Entry <https://pypi.org/project/clustering-benchmarks/>
::::


::::{toctree}
:maxdepth: 2
:caption: Introduction

weave/true-vs-predicted
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

Data Wrangling in Python <https://datawranglingpy.gagolewski.com/>
genieclust Package <https://genieclust.gagolewski.com/>
::::


::::{toctree}
:maxdepth: 1
:caption: Appendix

weave/external-validity-measures
weave/internal-validity-measures
news
z_bibliography
::::
