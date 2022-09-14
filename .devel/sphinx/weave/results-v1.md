





(sec:results-v1)=
# Explore Clustering Results (v1.1.0) 🚧


::::{todo}
This page is under construction. Please come back later.
::::


https://github.com/gagolews/clustering-results-v1/


TODO: https://github.com/gagolews/clustering-results-v1 cleanup

The algorithms operated on the *original* data spaces,
i.e., subject to only some minor preprocessing:

* columns of zero variance have been removed;
* tiny amount of white noise has been added to each datum to make sure the
    distance matrices consist of unique elements (this guarantees that the
    results of hierarchical clustering algorithms are unambiguous);
* all data were translated and scaled proportionally
    to assure that each column is of mean 0 and that the total variance
    of *all* entries is 1 (this is not standardisation).


Note, however, that spectral clustering (results included herein)
can be considered as one that modifies the input data space.




Currently, [genieclust](https://genieclust.gagolewski.com) (Genie)
outperforms (on average) all other algorithms.
You are free to use the results included herein when testing
your own clustering methods.
As a courtesy, please cite the benchmark battery and
some of the papers included in its
[Bibliography](https://github.com/gagolews/clustering_benchmarks_v1/blob/master/README.md#bibliography) section
as well as the papers introducing the algorithms you are comparing yourself to.




## Algorithms

The outputs of the following algorithms are included
(across a wide range of control parameters; note that we have only considered
the methods which allow for setting the precise number of generated clusters):

* [`genieclust`](https://genieclust.gagolewski.com)
    1.0.0 (Python; R version available too)
    with different `gini_threshold` parameter values

    single linkage (Genie_1.0)

    * M. Gagolewski. genieclust: Fast and robust hierarchical
    clustering. *SoftwareX*, 15:100722, 2021. [doi:10.1016/j.softx.2021.100722](https://dx.doi.org/10.1016/j.softx.2021.100722).

    * M. Gagolewski, M. Bartoszuk, and A. Cena. Genie: A new, fast,
    and outlier-resistant hierarchical clustering algorithm.
    *Information Sciences*, 363:8–23, 2016. [doi:10.1016/j.ins.2016.05.003](https://dx.doi.org/10.1016/j.ins.2016.05.003).



* [`ITM`](https://github.com/amueller/information-theoretic-mst)
    git commit 178fd43 (Python)

        The outputs of the ITM ("information-theoretic") algorithm based on
minimum spanning trees.


    * A.C. Müller, S. Nowozin, and C.H. Lampert.
    *Information theoretic clustering using minimum spanning trees*.
    In *Proc. German Conference on Pattern Recognition*. 2012.
    URL: https://github.com/amueller/information-theoretic-mst.



* [`sklearn`](https://scikit-learn.org/stable/modules/clustering.html)
    0.23.1 (Python) — k-means, spectral, Gaussian mixtures, Birch

    * F. Pedregosa and others. Scikit-learn: Machine learning in Python.
    *Journal of Machine Learning Research*, 12(85):2825–2830, 2011.
    URL: http://jmlr.org/papers/v12/pedregosa11a.html.

    * L. Buitinck and others. *API design for machine learning software:
    Experiences from the scikit-learn project*. In *ECML PKDD Workshop:
    Languages for Data Mining and Machine Learning*, 108–122. 2013.


* [`fastcluster`](http://www.danifold.net/fastcluster.html) 1.1.26
    (Python; R version available too) — average, centroid, complete,
    median, Ward, weighted/McQuitty linkage

    * D. Müllner. fastcluster: Fast hierarchical, agglomerative clustering
    routines for R and Python. *Journal of Statistical Software*,
    53(9):1–18, 2013. [doi:10.18637/jss.v053.i09](https://dx.doi.org/10.18637/jss.v053.i09).


* [`optim_cvi`](https://github.com/gagolews/optim_cvi) —
    local maxima (great effort was made to maximise the probability of their
    being high-quality ones) of many internal cluster validity measures,
    including the Caliński–Harabasz, Dunn, or Silhouette index.

    * M. Gagolewski, M. Bartoszuk, A. Cena,
    Are cluster validity measures (in)valid?,
    *Information Sciences*, 581:620–636, 2021.
    [doi:10.1016/j.ins.2021.10.004](https://dx.doi.org/10.1016/j.ins.2021.10.004).


