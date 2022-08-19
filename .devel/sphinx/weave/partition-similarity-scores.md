



# Partition Similarity Scores

Let $X=\{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ be the input dataset
that consists of $n$ objects.

As an illustration, in this section we will be considering
the [`wut/x2`](https://github.com/gagolews/clustering-data-v1) dataset,
which consists of 120 points in $\mathbb{R}^2$.

::::{epigraph}
*To learn more about Python, which we use in this tutorial,
check out Marek's recent open-access (free!) textbook*
[Minimalist Data Wrangling in Python](https://datawranglingpy.gagolewski.com/)
{cite}`datawranglingpy`.
*In a {any}`further section <sec:how-to-access>`, we explain
how to use our benchmark framework from other environments.*
::::



```python
import numpy as np
import pandas as pd
dataset = "https://github.com/gagolews/clustering-data-v1/raw/master/wut/x2"
X = np.loadtxt(dataset + ".data.gz")
X[:5, :]  # preview
## array([[ 0.29087439,  0.27966267],
##        [ 0.24996994, -0.97430785],
##        [ 0.43587577, -0.31895699],
##        [ 0.63048803, -2.15249344],
##        [-1.46511622,  0.36344556]])
```

Assume we are given a $k$-partition[^footpart] $\{X_1,\dots,X_k\}$ of $X$
encoded by means of a *label vector*[^footsurj] $\mathbf{y}$, where
$y_i\in[1:k]$ gives the cluster number (ID) of the $i$-th object.




[^footpart]: We say that $\{X_1,\dots,X_k\}$ is a $k$-partition of $X$,
    whenever $\bigcup_{i=1}^k X_i=X$, each $X_i$ is nonempty,
    and the subsets are pairwise disjoint, i.e., $X_i\cap X_j=\emptyset$
    for $i\neq j$.

[^footsurj]: More precisely, a surjection $[1:n]\stackrel{\text{onto}}{\to}[1:k]$.



In our context, this will be the reference partition
assigned by the experts that comes along this dataset.




```python
(y_true := np.loadtxt(dataset+".labels0.gz", dtype=np.intc))
## array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
##        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
##        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
##        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
##        1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
##        3, 3, 3, 3, 3, 3, 3, 3, 3, 3], dtype=int32)
np.bincount(y_true)
## array([ 0, 50, 40, 30])
```

There are thus 0 noise points (which would be encoded as 0),
50 points in the 1st cluster, 40 points in the 2nd group, and 30 points
in the 3rd set. Hence, $k=3$.

Furthermore, let $\hat{\mathbf{y}}$ be a label vector
encoding another partition, $\{\hat{X}_1,\dots,\hat{X}_l\}$.

For example, let's consider the output of the
[*Genie*](https://genieclust.gagolewski.com) algorithm
with $l=k=3$:



```python
import genieclust
g = genieclust.Genie(n_clusters=3)  # default parameters
(y_genie := g.fit_predict(X) + 1)  # +1 so that cluster IDs are in 1:3, not 0:2
## array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
##        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,
##        2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1,
##        2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2,
##        2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
##        3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
```

The figure below depicts the two partitions side by side.




```python
plt.subplot(1, 2, 1)
genieclust.plots.plot_scatter(X, labels=y_true-1)
plt.axis("equal")
plt.title("y_true")
plt.subplot(1, 2, 2)
genieclust.plots.plot_scatter(X, labels=y_genie-1)
plt.axis("equal")
plt.title("y_genie")
plt.show()
```

(fig:partition-similarity-example)=
```{figure} partition-similarity-scores-figures/partition-similarity-example-1.*
Two example paritions that we would like to compare
```

Partition similarity scores aim to quantify the similarity between
$\mathbf{y}$ and $\hat{\mathbf{y}}$.



can be used as external cluster validity
measures — for comparing the outputs of clustering algorithms
with reference (ground truth) labels








Let $\mathbf{C}$ be the
confusion matrix (with :math:`K` rows and :math:`L` columns, :math:`K \\leq L`)
corresponding to `x` and `y`, see also
`genieclust.compare_partitions.confusion_matrix`.




```python
(C := genieclust.compare_partitions.confusion_matrix(y_true, y_genie))
## array([[12, 37,  1],
##        [40,  0,  0],
##        [ 0,  0, 30]])
```

genieclust:: bibliography, compare_partitions.pyx

some axioms

Every index except `mi_score` (which computes the mutual
information score) outputs the value of 1.0 if two identical partitions
are given.
Note that partitions are always defined up to a bijection of the set of
possible labels, e.g., (1, 1, 2, 1) and (4, 4, 2, 4)
represent the same 2-partition.


...

Their implementation is included
in the [*genieclust*](https://genieclust.gagolewski.com/) package for Python.

https://genieclust.gagolewski.com/genieclust_compare_partitions.html

...
