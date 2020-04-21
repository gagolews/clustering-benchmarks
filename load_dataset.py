"""Provides a Python 3 function to load a dataset
from Benchmark Suite for Clustering Algorithms

See: load_dataset()

Copyright (C) 2018-2020 Marek.Gagolewski.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys, os.path
import numpy as np
import glob
import re
from collections import namedtuple


def load_dataset(name, path="."):
    """Loads a dataset named `name` relative to the directory `path`.

    Arguments
    =========

    name
        dataset name
    path
        path to the downloaded suite, defaults to the current working dir


    Returns
    =======

    A named tuple with the following elements:

        data
            data matrix
        labels
            a list with at least one label vectors
        name
            same as the `name` argument


    Examples
    ========

    data, labels, name = load_dataset("wut/wut_smile")

    ret = load_dataset("wut_smile", "wut")
    print(ret.data, ret.labels, ret.name)

    ret = load_dataset("wut/wut_smile", "/usr/share/clustering_benchmarks_v1")
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
