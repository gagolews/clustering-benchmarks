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

::::{todo}
show some example outputs - plot
::::

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

::::{important}
This project aims to:

* **aggregate, polish, and standardise the existing clustering
    benchmark batteries** referred to across the machine learning
    and data mining literature,
* introduce **new datasets** of different dimensionalities,
    sizes, and cluster types,
* propose a **consistent methodology** for evaluating clustering algorithms.
::::


::::{note}
Here is the proposed methodology at a glance:

* {ref}`Datasets <sec:suite-v1>` of different origin,
    difficulty, dimensionality, and cluster structure (including clusters
    of imbalanced sizes and different shapes) are included.
* A clustering algorithm under scrutiny run so as to split the datasets into
    different number of clusters (e.g., to find all 2-, 3-, 4-... -clusterings).
* Each dataset is equipped with at least one ground truth partition
    provided by experts. Clustering is an unsupervised data mining problem, so
    {ref}`there can be many equally valid partitions <sec:many-partitions>`.
* {ref}`External cluster validity scores <sec:external-validity-measures>`
    are used to relate the outputs to all the possible reference sets.
* {ref}`Noise points <sec:noise-points>` can be included in the dataset
    to make the clustering harder. The way they are classified
    is ignored when computing the final similarity score.
* The best result is reported (has or has not the algorithm
    reproduced at least one of the ground-truth partitions well?)

Details follow in the sections below.
::::



**Author/Editor/Maintainer**: [Marek Gagolewski](https://www.gagolewski.com)

**How to Cite**:
Gagolewski M., *A Framework for Benchmarking Clustering Algorithms*, 2022, <https://clustering-benchmarks.gagolewski.com>, submitted for publication.


Data are provided solely for research purposes, unless stated otherwise.
Please cite the literature references mentioned in the description files
corresponding to each dataset if you use them in your publications.


::::{toctree}
:maxdepth: 2
:caption: Methodology

Introduction <self>
weave/true-vs-predicted
weave/noise-points
weave/many-partitions
::::


::::{toctree}
:maxdepth: 2
:caption: Benchmark Batteries

weave/suite-v1
weave/data-v1
weave/results-v1
weave/file-format
weave/how-to-access
weave/contributing
::::

::::{toctree}
:maxdepth: 1
:caption: Python API

weave/clustbench-usage
clustbench-documentation
Source Code (GitHub) <https://github.com/gagolews/clustering-benchmarks>
PyPI Entry <https://pypi.org/project/clustering-benchmarks/>
::::


::::{toctree}
:maxdepth: 1
:caption: See Also

Author's Homepage <https://www.gagolewski.com/>
Data Wrangling in Python <https://datawranglingpy.gagolewski.com/>
genieclust Package <https://genieclust.gagolewski.com/>
::::


::::{toctree}
:maxdepth: 1
:caption: Appendix

weave/colouriser
weave/external-validity-measures
weave/internal-validity-measures
news
z_bibliography
::::
