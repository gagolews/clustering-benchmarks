





(sec:results-v1)=
# Clustering Results Repository (v1.1.0)

We have prepared a repository of
[clustering results](https://github.com/gagolews/clustering-results-v1/)
for problems from our {ref}`sec:suite-v1`.

A non-interactive results catalogue is available
[here](https://github.com/gagolews/clustering-results-v1/tree/master/.catalogue/original).



## Methods

Currently, the outputs of the following methods are included.
Where applicable, we considered a wide range of control parameters.

* k-means, Gaussian mixtures, spectral, and Birch available in
    [`sklearn`](https://scikit-learn.org/stable/modules/clustering.html)
    0.23.1 (Python) {cite}`sklearn,sklearn_api`;

* hierarchical agglomerative methods with the average, centroid, complete,
    median, Ward, and weighted/McQuitty linkages implemented
    in [`fastcluster`](http://www.danifold.net/fastcluster.html) 1.1.26
    (Python/R) {cite}`fastclusterpkg`

* [`genieclust`](https://genieclust.gagolewski.com) 1.0.0 (Python/R)
    {cite}`genieclust,genieins`
    (note that *Genie* with *g=1.0* is equivalent to the single linkage algorithm);

* `Genie+Ic` – Genie+Information Criterion, see {cite}`cvimst`,
    as implemented in [`genieclust`](https://genieclust.gagolewski.com) 1.0.0 (Python/R).

* `fcps_nonproj` – many algorithms, see {cite}`ThrunStier2021:fcas`, available via the
    [`FCPS`](https://cran.r-project.org/package=FCPS) 1.3.4 package for R,
    which provides a consistent interface to many other
    R packages (versions current as of 2023-10-21).
    We selected all which return an a priori-given number of clusters,
    and do not rely on heavy feature engineering/fancy data projections,
    as such methods should be evaluated separately.
    We did not include the algorithms that are available in other packages and
    are already part of this results repository,
    e.g., `fastcluster`, `genieclust`, and `scikit-learn`.

* [`ITM`](https://github.com/amueller/information-theoretic-mst)
    git commit 178fd43 (Python) {cite}`itm` –
    an "information-theoretic" algorithm based on
    minimum spanning trees;

* [`optim_cvi`](https://github.com/gagolews/optim_cvi) —
    local maxima (great effort was made to maximise the probability of their
    being high-quality ones) of many
    {ref}`internal cluster validity measures <sec:external-validity-measures>`,
    including the Caliński–Harabasz, Dunn, or Silhouette index;
    see {cite}`cvi`;

* `optim_cvi_mst_divisive` – maximising internal cluster validity measures
    over Euclidean minimum spanning trees using a divisive strategy;
    see {cite}`cvimst`.

New results will be added in the future (note that we can only consider
methods that allow for setting the precise number of generated clusters).
New quality contributions are {ref}`welcome <sec:contributing>`.


## Feature Engineering

The algorithms operated on the *original* data spaces,
i.e., subject to only some mild preprocessing:

* columns of zero variance have been removed;
* a tiny amount of white noise has been added to each datum to make sure the
    distance matrices consist of unique elements (this guarantees that the
    results of hierarchical clustering algorithms are unambiguous);
* all data were translated and scaled proportionally
    to assure that each column is of mean 0 and that the total variance
    of *all* entries is 1 (this is not standardisation).

Note, however, that spectral clustering and Gaussian mixtures
can be considered as ones that modify the input data space.

Overall, comparisons between distance-based methods that apply automated
feature engineering/selection and those that only operate on raw inputs
are not exactly fair.
In such settings, the classical methods should be run on the transformed
data spaces as well.
This is left for further research (stay tuned).





