



(sec:file-format)=
# File Format Specification

The files in our benchmark dataset suite
(<https://github.com/gagolews/clustering-data-v1>)
and the corresponding clustering results repository
(<https://github.com/gagolews/clustering-results-v1>)
follow the following convention.

::::{important}
Future versions of benchmark batteries
will adhere to these guidelines as well,
with any possible extensions being all backward compatible.
::::




## Benchmark Datasets

For each `battery/dataset` (e.g., `wut/labirynth`),
we have the following corresponding files:

* `dataset.txt` – gives the dataset description, comments,
    copyright information, license, how to cite, etc.

* `dataset.data.gz` – defines an *n*-by-*d* data matrix
    representing a dataset with *n* points in $\mathbb{R}^d$:

    * a gzipped text file storing data in tabular format
    (many environments can decompress `.gz` inputs on the fly;
    see {ref}`sec:how-to-access`);
    * columns are whitespace-delimited;
    * there are exactly *n* file lines
        (no column names, no headers, no comments);
    * values might be in either decimal or scientific notation
        (e.g., 1.0, 1.23e-8).

* `dataset.labels0.gz`, `dataset.labels1.gz`, `dataset.labels2.gz`, ... –
    ground truth partitions (as
    {ref}`there can be many <sec:many-partitions>` equally valid
    ways to cluster a dataset)
    identified by consecutive  integers starting at 0.

    Each file stores a separate label vector:

    * a gzipped text file with exactly *n* integers, one per line;
    * the *i*-th label (line) corresponds to the *i*-th data point
    * `0` denotes the {ref}`noise class <sec:noise-points>` (if present),
        the first meaningful cluster is denoted with `1`;
    * class labels are consecutive integers:
        `0`, `1`, `2`, ..., `K`, where `K = max(labels)` is the total
        number of clusters (noise not included in the counting);
    * `labels0` usually denotes the original label vector as defined by
        the dataset's creator (if one was provided).





## Clustering Results

As far as the storing of clustering results is concerned,
the files are named like `method-group/battery/datasetK.gz`,
where `K` is the number of identified clusters, e.g.,
`Genie/wut/labirynth4.gz`.

Each results file is a gzipped CSV where columns are label vectors
with elements in `1`, `2`, ..., `K`.


Each column represents the output of a different clustering method
or the same algorithm with different parameter settings
(e.g., `Genie_0.1`, `Genie_0.3`, etc.).
The first row gives in the CSV gives the method (column) names.


For example:


```python
"Genie_G0.1","Genie_G0.3","Genie_G0.5","Genie_G0.7","Genie_G1.0"  # <--- names
1,1,1,1,1
2,2,2,2,2
3,3,3,3,3
4,1,1,1,1
2,2,2,2,2
3,3,3,3,3
4,1,1,1,1  # <--- Genie_G0.1 claims the 7th data point belongs to the 4th cluster
2,2,2,2,2
3,3,3,3,3
...        # <--- As many rows as data points in total (plus names in the 1st row)
```
