"""
clustering-benchmarks Package
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2020-2023, Marek Gagolewski <https://www.gagolewski.com>      #
#                                                                              #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU Affero General Public License                #
#   Version 3, 19 November 2007, published by the Free Software Foundation.    #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the               #
#   GNU Affero General Public License Version 3 for more details.              #
#   You should have received a copy of the License along with this program.    #
#   If this is not the case, refer to <https://www.gnu.org/licenses/>.         #
#                                                                              #
# ############################################################################ #


import os.path
import numpy as np
import pandas as pd
import os
import glob
from natsort import natsorted


def load_results(
    method_group, battery, dataset, n_clusters, path=None,
    expanduser=True, expandvars=True
):
    """
    Load benchmark results

    Reads the datasets named like `method_group/battery/dataset.resultK.gz`
    (relative to the directory `path`), for each `K` in
    ``n_clusters``. `method_group` can be a wildcard like ``"*"``
    if a look up in multiple directories is required.


    Parameters
    ----------

    method_group
        Name of the method group, e.g., ``"Genie"``, ``"."``, or ``"*"``.

    battery
        Name of the battery (dataset collection), e.g., ``"wut"`` or ``"other"``.

    dataset
        Dataset name, e.g., ``"x2"`` or ``"iris"``.

    n_clusters : int or list of ints
        Number of clusters.

    path
        Path to the directory containing the downloaded benchmark datasets
        suite. Defaults to the current working directory.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Returns
    -------

    results
        A dictionary of dictionaries of label vectors
        that can be accessed like ``results[method_name][n_clusters]``.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> # load from a local library (a manually downloaded repository)
    >>> results_path = os.path.join("~", "Projects", "clustering-results-v1", "original")
    >>> res = clustbench.load_results("*", "wut", "x2", 3, path=results_path)
    >>> print(res.keys())
    """
    if path is None: path = "."
    if expanduser: path = os.path.expanduser(path)
    if expandvars: path = os.path.expandvars(path)

    fname_pat = os.path.join(path, method_group, battery, dataset)

    n_clusters = np.unique(np.r_[n_clusters])

    results = dict()
    for k in n_clusters:
        k = int(k)
        for fname in natsorted(glob.glob(fname_pat + ".result%d.gz" % k)):
            labels = pd.read_csv(fname)
            for i in range(labels.shape[1]):
                if labels.columns[i] not in results:
                    results[labels.columns[i]] = dict()

                results[labels.columns[i]][k] = np.array(labels.iloc[:, i])
                if np.max(results[labels.columns[i]][k]) != k:
                    raise ValueError("max(labels) does not match n_clusters")

    return results


def labels_list_to_dict(labels):
    """
    Convert a list of labels to a dictionary indexed by ``n_clusters``

    If ``labels`` is a single label vector, it will be wrapped inside
    a list.


    Parameters
    ----------

    labels
        A vector-like object or a list thereof.


    Returns
    -------

    ret : dict
        ``ret[max(ll)] = ll`` for each ``ll`` in ``labels``.

    """

    labels = list(np.array(labels, ndmin=2))

    ret = dict()
    for ll in labels:
        k = int(np.max(ll))
        if k in ret:
            raise ValueError("duplicate max(labels[i])")
        ret[k] = ll

    return ret


def transpose_results(results):
    """
    "Transpose" a results dictionary

    Parameters
    ----------

    results : dict
        A dictionary of dictionaries or lists
        of objects.


    Returns
    -------

    ret : dict
        A dictionary such that ``ret[b][a]``
        is taken from ``results[a][b]``.
        If ``results[a]`` is not a dictionary,
        `labels_list_to_dict` will be called first.

    """
    if type(results) is not dict:
        raise ValueError("`results` is not a dict")

    ret = dict()
    for a in results:
        cur = results[a]
        if type(cur) is not dict:
            cur = labels_list_to_dict(cur)

        for b in cur:
            if b not in ret: ret[b] = dict()
            ret[b][a] = cur[b]

    return ret


def save_results(filename, results, expanduser=True, expandvars=True):
    """
    Write results of many clustering algorithms

    Parameters
    ----------

    filename : string or file handle
        For example, `method_group/battery/dataset.resultK.gz`.

    results : dict
        A dictionary where each ``results[method_name]``
        is a label vector.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> # load from a local library (a manually downloaded repository)
    >>> results_path = os.path.join("~", "Projects", "clustering-results-v1", "original")
    >>> res = clustbench.load_results("*", "wut", "x2", 3, path=results_path)
    >>> print(res.keys())
    >>> clustbench.save_results("x1.result3.gz", clustbench.transpose_results(res)[3])
    """
    if type(results) is not dict:
        raise ValueError("`results` is not a dict")

    res = pd.DataFrame(results)

    if not np.all(res.min().isin([0, 1])):
        raise ValueError("Minimal label neither 0 nor 1.")

    mx = res.max()
    if not mx[0] >= 1:
        raise ValueError("At least 1 cluster is necessary.")

    if not np.all(mx == mx[0]):
        raise ValueError("All partitions should be of the same cardinality.")

    if not np.all(res.apply(np.bincount).iloc[1:, :] > 0):
        raise ValueError("Denormalised label vector: Cluster IDs should be consecutive integers.")

    if expanduser: filename = os.path.expanduser(filename)
    if expandvars: filename = os.path.expandvars(filename)

    res.to_csv(filename, index=False, sep=",", header=True)
