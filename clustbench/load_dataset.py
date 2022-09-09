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


import sys, os.path
import numpy as np
import glob
import re
from collections import namedtuple


def load_dataset(
    battery, dataset, path=None,
    url=None, expanduser=True, expandvars=True
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
        Can be an empty string or ``"."`` if all files are
        in a single directory as specified by `path`.

    dataset
        Dataset name, e.g., ``"x2"`` or ``"iris"``.

    path
        Mutually exclusive with `url`.
        Path to the directory containing the downloaded benchmark datasets
        suite.

    url
        Mutually exclusive with `path`. For example,
        ``"https://github.com/gagolews/clustering-data-v1/raw/master"``
        to get access to <https://github.com/gagolews/clustering-data-v1>,

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Returns
    -------

    dataset
        A named tuple with the following elements:

        data
            Data matrix.

        labels
            A list consisting of the label vectors.

        name
            A string of the form `battery/name`.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> # load from a local library (e.g., a manually downloaded battery)
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> wut_x2 = clustbench.load_dataset("wut", "x2", path=data_path)
    >>> print(wut_x2.data, wut_x2.labels, wut_x2.name)
    >>> # load from GitHub:
    >>> data_url = "https://github.com/gagolews/clustering-data-v1/raw/master"
    >>> wut_smile = clustbench.load_dataset("wut", "smile", url=data_url)
    >>> print(wut_smile.data, wut_smile.labels, wut_smile.name)
    """
    if url is not None and path is not None:
        raise ValueError("`url` and `path` are mutually exclusive.")

    if path is not None:
        base_name = os.path.join(path, battery, dataset)
        if expanduser: base_name = os.path.expanduser(base_name)
        if expandvars: base_name = os.path.expandvars(base_name)
    else:
        base_name = url + "/" + battery + "/" + dataset

    data_file = base_name + ".data.gz"
    data = np.loadtxt(data_file, ndmin=2)

    if data.ndim != 2:
        raise ValueError("Not a matrix.")

    labels = []
    i = 0
    while True:
        try:
            f = base_name + ".labels%d.gz" % i
            l = np.loadtxt(f, dtype="int")
            if l.ndim != 1 or l.shape[0] != data.shape[0]:
                raise ValueError("Incorrect number of labels in '%s'." % f)

            labels.append(l)
            i += 1
        except FileNotFoundError:
            # this could be done better with glob.glob for local files,
            # but not for remote URLs
            break

    RetClass = namedtuple("ClusteringBenchmark", ["data", "labels", "name"])
    return RetClass(data=data, labels=labels, name=battery+"/"+dataset)
