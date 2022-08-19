



# Partition Similarity Scores


Let `x` and `y` represent two partitions of the same set with :math:`n`
elements into, respectively, :math:`K` and :math:`L`
nonempty and pairwise disjoint subsets.
For instance, these can be two clusterings of a dataset with :math:`n`
observations specified as vectors of labels. Moreover, let `C` be the
confusion matrix (with :math:`K` rows and :math:`L` columns, :math:`K \\leq L`)
corresponding to `x` and `y`, see also
`genieclust.compare_partitions.confusion_matrix`.

This function implements a few scores that aim to quantify
the similarity between `x` and `y`.
Partition similarity scores can be used as external cluster validity
measures — for comparing the outputs of clustering algorithms
with reference (ground truth) labels, see, e.g., [5]_
for a suite of benchmark datasets.

Every index except `mi_score` (which computes the mutual
information score) outputs the value of 1.0 if two identical partitions
are given.
Note that partitions are always defined up to a bijection of the set of
possible labels, e.g., (1, 1, 2, 1) and (4, 4, 2, 4)
represent the same 2-partition.

Their implementation is included
in the [*genieclust*](https://genieclust.gagolewski.com/) package for Python.

https://genieclust.gagolewski.com/genieclust_compare_partitions.html

...
