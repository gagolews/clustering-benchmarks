A Framework for Benchmarking Clustering Algorithms
==================================================

<!--
::::{epigraph}
**Genie finds meaningful clusters and is fast even on large data sets.**
::::
-->

::::{image} _static/img/x2-banner.png
:class: img-right-align-always
:alt: wut_x2_labels0
:width: 128px
::::

There is no, nor will there ever be, single best clustering algorithm.
Still, we would like to be able to separate the wheat from the chaff:
to **pinpoint grouping methods that are well-performing on certain task
types as well as filter out the systematically disappointing ones**.

A common approach is to run the algorithms on a variety of
benchmark datasets and **compare their outputs to the reference,
ground truth groupings that are provided by experts**.



<!--
::::{todo}
TODO: Show some example outputs - plot
::::
-->

However, it is not rare for research papers/graduate theses to **consider
only a small number of datasets**. We regularly come across the same 5–10
test problems from the UCI database. This is obviously too few to
make any evaluation rigorous enough.

Other authors propose their own datasets, but do not test their methods
against other benchmark suites. This might lead to biased conclusions.

Some researchers who share their data (thanks!) might not make
the interaction with their batteries particularly smooth
(**different file formats**, different ways to access, etc.,
even across a single repository).

Existing repositories do not reflect the idea that **there might be many equally
valid/plausible/useful partitions of the same dataset**;
see {cite}`sdmc,LuxburgETAL2012:clustscienceart` for discussion.

On the other hand,
some well-agreed-upon approaches for testing the quality of the algorithms
in other machine learning domains
(e.g., classification and regression problems included in the said UCI
{cite}`uci`; but also:
[optimisation](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
{cite}`optimisation-benchmarks1,optimisation-benchmarks2`)
have been developed a long time ago.

This is why:

::::{important}
This project aims to:

* propose a **consistent methodology** for evaluating clustering
    algorithms,
* **aggregate, polish, and standardise the existing clustering
    benchmark batteries** (collections) referred to across the machine learning
    and data mining literature,
* introduce **new datasets** of different dimensionalities,
    sizes, and cluster types.
::::


::::{note}
The proposed approach at a glance:

*   {ref}`Datasets <sec:suite-v1>` of different origins,
    difficulty, dimensionality, and cluster structure (including clusters
    of imbalanced sizes and different shapes) are provided.
*   Each clustering algorithm under scrutiny should be run so as
    to split the datasets into a desired number of subsets
    (e.g., to find all 2-, 3-, 4-... -clusterings).
*   Each dataset is equipped with at least one ground truth partition
    provided by experts. Clustering is an unsupervised data mining
    problem, so there can be
    {ref}`many equally valid partitions <sec:many-partitions>`.
*   {ref}`External cluster validity scores <sec:external-validity-measures>`
    are computed to quantify the similarity of the outputs to all the
    possible reference sets.
*   {ref}`Noise points <sec:noise-points>` can be included in the dataset
    to make the clustering harder. However, the way they are classified
    is ignored when computing the final similarity score.
*   The best score is reported (has or has not the algorithm
    reproduced at least one of the ground-truth partitions well?)

See the subsequent sections for more details.
::::



**Author/Editor/Maintainer**:
[Marek Gagolewski](https://www.gagolewski.com)

**How to Cite**:
Gagolewski M., *A framework for benchmarking clustering algorithms*,
2022, <https://clustering-benchmarks.gagolewski.com>,
DOI: [10.48550/arXiv.2209.09493](https://doi.org/10.48550/arXiv.2209.09493),
under review (preprint).

Data are provided solely for research purposes, unless stated otherwise.
If you use them in your publications, please cite the literature
references mentioned in the description files corresponding
to each dataset.


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
PyPI Entry <https://pypi.org/project/clustering-benchmarks>
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
