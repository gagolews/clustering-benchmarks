



(sec:partition-similarity-scores)=
# Partition Similarity Scores

In this section we review the partition similarity scores that are defined
in the [*genieclust*](https://genieclust.gagolewski.com/) package for Python
and R.

Let $\mathbf{y}$ be a label vector representing one of the reference
$k$-partitions[^footpart] $\{X_1,\dots,X_k\}$ of a benchmark dataset $X$,
where $y_i\in[1:k]$ gives the true cluster number (ID) of the $i$-th object.

Furthermore, let $\hat{\mathbf{y}}$ be a label vector
encoding another partition, $\{\hat{X}_1,\dots,\hat{X}_l\}$,
which we would like to *relate* to the reference one, $\mathbf{y}$.
In our context, we assume that $\hat{\mathbf{y}}$ has been output by some
clustering algorithm.

::::{note}
Below we assume $k \le l$, i.e., the true clustering
might theoretically be more coarse-grained than the reference one.
Also, any noise points in $X$ have been removed.
::::




Let $\mathbf{C}$ be the confusion matrix with $k$ rows and $l$ columns,
i.e., $c_{u,v}$ gives the number point indices $i$ for which $y_i=u$
and $\hat{y}_v$. In other words, $c_{u,v}$ gives the number of points
from the $u$-th reference cluster that the clustering algorithm
classified as belonging to the $v$-th group.




```python
# (C := genieclust.compare_partitions.confusion_matrix(y_true, y_pred))
```

pivoting...

say that this is different than accuracy in classification





genieclust:: bibliography, compare_partitions.pyx

some axioms

Every index except `mi_score` (which computes the mutual
information score) outputs the value of 1.0 if two identical partitions
are given.
Note that partitions are always defined up to a bijection of the set of
possible labels, e.g., (1, 1, 2, 1) and (4, 4, 2, 4)
represent the same 2-partition.

