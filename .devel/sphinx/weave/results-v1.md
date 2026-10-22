





(sec:results-v1)=
# Clustering Results Repository (v1.2.0)

We have prepared a repository of
[clustering results](https://github.com/gagolews/clustering-results-v1/)
for problems from our {ref}`sec:suite-v1`.

A non-interactive results catalogue is available
[here](https://github.com/gagolews/clustering-results-v1/tree/master/.catalogue/original).




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


