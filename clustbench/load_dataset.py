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


def load_dataset(battery, dataset, path=".", expanduser=True, expandvars=True):
    """
    Load a benchmark dataset

    Reads a dataset named `battery/dataset.data.gz`
    relative to the directory `path` as well as all the corresponding labels
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
        Path to the downloaded benchmark datasets suite.
        Defaults to the current working directory.

    expanduser
        Whether to call ``os.path.expanduser``.

    expandvars
        Whether to call ``os.path.expandvars``.


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
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> benchmark = clustbench.load_dataset("wut", "x2", data_path)
    >>> print(benchmark.data, benchmark.labels, benchmark.name)

    """
    base_name = os.path.join(path, battery, dataset)

    if expanduser:
        base_name = os.path.expanduser(base_name)

    if expandvars:
        base_name = os.path.expandvars(base_name)

    data_file = base_name + ".data.gz"
    data = np.loadtxt(data_file, ndmin=2)

    labels_files = sorted(glob.glob(base_name+".labels*.gz"))

    #if len(labels_files) <= 0:
    #    raise ValueError("No label files found.")

    labels = [
        np.loadtxt(labels_file, dtype='int')
        for labels_file in labels_files
    ]

    RetClass = namedtuple("ClusteringBenchmark", ["data", "labels", "name"])
    return RetClass(data=data, labels=labels, name=battery+"/"+dataset)
