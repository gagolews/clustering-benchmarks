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


def load_dataset(name, path="."):
    """
    Loads a dataset named `name` relative to the directory `path`.

    Parameters
    ----------

    name
        dataset name

    path
        path to the downloaded suite, defaults to the current working dir


    Returns
    -------

    dataset
        A named tuple with the following elements:

        data
            data matrix

        labels
            a list with at least one label vectors

        name
            same as the `name` argument


    Examples
    --------

    >>> import os.path
    >>> #data, labels, name = load_dataset(os.path.join("wut", "smile"), "/usr/share/clustering_benchmarks_v1")
    >>> #ret = load_dataset("smile", "/usr/share/clustering_benchmarks_v1/wut")
    >>> # print(ret.data, ret.labels, ret.name)

    """
    base_name = os.path.join(path, name)

    data_file = base_name+".data.gz"
    data = np.loadtxt(data_file, ndmin=2)
    labels_files = sorted(glob.glob(base_name+".labels?.gz"))
    assert len(labels_files) > 0

    labels = [
        np.loadtxt(labels_file, dtype='int')
        for labels_file in labels_files
    ]

    RetClass = namedtuple("ClusteringBenchmark", ["data", "labels", "name"])
    return RetClass(data=data, labels=labels, name=name)
