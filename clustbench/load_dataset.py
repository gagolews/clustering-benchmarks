"""
clustering-benchmarks Package
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2020-2022, Marek Gagolewski <https://www.gagolewski.com>      #
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
from collections import namedtuple
from .preprocess_data import preprocess_data


def load_dataset(
    battery, dataset, path=None,
    url=None, expanduser=True, expandvars=True,
    preprocess=True, random_state=None
):
    """
    Load a benchmark dataset

    Reads a dataset named `battery/dataset.data.gz`
    (relative to `url` or the directory `path`)
    as well as all the corresponding labels
    (`battery/dataset.labels0.gz`, `battery/dataset.labels1.gz`, ...).

    Parameters
    ----------

    battery
        Name of the battery, e.g., ``"wut"`` or ``"other"``.

    dataset
        Dataset name, e.g., ``"x2"`` or ``"iris"``.

    path
        Mutually exclusive with `url`.
        Path to the directory containing the downloaded benchmark datasets
        suite. Defaults to the current working directory.

    url
        Mutually exclusive with `path`. For example,
        ``"https://github.com/gagolews/clustering-data-v1/raw/v1.1.0"``
        to get access to <https://github.com/gagolews/clustering-data-v1>,

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.

    preprocess
        Whether to call :any:`preprocess_data` on the data matrix.

    random_state
        Seed of the random number generator; passed to :any:`preprocess_data`.


    Returns
    -------

    benchmark
        A named tuple with the following elements:

        battery
            Same as the `battery` argument.

        dataset
            Same as the `dataset` argument.

        description
            Contents of the description file.

        data : ndarray
            Data matrix.

        labels : list
            A list consisting of the label vectors.

        n_clusters : ndarray
            The corresponding cluster counts:
            ``n_clusters[i]`` is equal to ``max(n_clusters[i])``.

    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> # load from a local library (a manually downloaded suite)
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> wut_x2 = clustbench.load_dataset("wut", "x2", path=data_path)
    >>> print(wut_x2.battery, wut_x2.dataset)
    >>> print(wut_x2.description)
    >>> print(wut_x2.data, wut_x2.labels)
    >>> # load from GitHub (slow...):
    >>> data_url = "https://github.com/gagolews/clustering-data-v1/raw/v1.1.0"
    >>> wut_smile = clustbench.load_dataset("wut", "smile", url=data_url)
    >>> print(wut_smile.data, wut_smile.labels)
    """
    if url is not None and path is not None:
        raise ValueError("`url` and `path` are mutually exclusive.")

    if url is not None:
        base_name = url + "/" + battery + "/" + dataset
    else:
        if path is None: path = "."
        base_name = os.path.join(path, battery, dataset)
        if expanduser: base_name = os.path.expanduser(base_name)
        if expandvars: base_name = os.path.expandvars(base_name)

    data_file = base_name + ".data.gz"
    data = np.loadtxt(data_file, ndmin=2)

    if data.ndim != 2:
        raise ValueError("Not a matrix.")

    if preprocess:
        data = preprocess_data(data, random_state=random_state)

    labels = []
    i = 0
    while True:
        try:
            f = base_name + ".labels%d.gz" % i
            ll = np.loadtxt(f, dtype="int")
            if ll.ndim != 1 or ll.shape[0] != data.shape[0]:
                raise ValueError("Incorrect number of labels in '%s'." % f)

            labels.append(ll)
            i += 1
        except FileNotFoundError:
            # this could be done better with glob.glob for local files,
            # but not for remote URLs
            break

    n_clusters = np.array([np.max(ll) for ll in labels])

    with np.DataSource().open(base_name + ".txt", "r") as readme_file:
        description = readme_file.read()

    RetClass = namedtuple(
        "ClusteringBenchmark",
        ["battery", "dataset", "description", "data", "labels", "n_clusters"]
    )
    return RetClass(
        battery=battery,
        dataset=dataset,
        description=description,
        data=data,
        labels=labels,
        n_clusters=n_clusters,
    )


def save_data(filename, data, fmt="%g", expanduser=True, expandvars=True):
    """
    Write a data matrix for inclusion in the clustering benchmark suite


    Parameters
    ----------

    filename : string or file handle
        For example, `path_to_suite/battery/dataset.data.gz`.

    data : 2D array_like
        A matrix-like object

    fmt
        See `numpy.savetxt`.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.

    """
    data = np.array(data)
    if data.ndim != 2:
        raise ValueError("Not a matrix.")

    if expanduser: filename = os.path.expanduser(filename)
    if expandvars: filename = os.path.expandvars(filename)

    np.savetxt(filename, data, fmt=fmt)


def save_labels(filename, labels, expanduser=True, expandvars=True):
    """
    Write a label vector for inclusion in the clustering benchmark suite

    Parameters
    ----------

    filename : string or file handle
        For example, `path_to_suite/battery/dataset.labels0.gz`.

    labels : 1D array_like
        A label vector.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.

    """
    labels = np.array(labels)
    if labels.ndim != 1:
        raise ValueError("Not a vector.")

    if not (0 <= labels.min() <= 1):
        raise ValueError("Minimal label neither 0 nor 1.")

    if not labels.max() >= 1:
        raise ValueError("At least 1 cluster is necessary.")

    if not np.all(np.bincount(labels)[1:] > 0):
        raise ValueError("Denormalised label vector: Cluster IDs should be consecutive integers.")

    if expanduser: filename = os.path.expanduser(filename)
    if expandvars: filename = os.path.expandvars(filename)

    np.savetxt(filename, labels, fmt="%d")
