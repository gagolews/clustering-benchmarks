#!/usr/bin/env python3

"""Unit tests for the Clustering Datasets and their Catalogue

Copyleft (C) 2018-2021 Marek Gagolewski <https://www.gagolewski.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import sys, os.path
import numpy as np
import glob
import re
from natsort import natsorted

def test(base_name):
    print("%-32s"%base_name, end="")

    if not re.match(r"^.+/[a-z0-9_]+$", base_name):
        raise Exception("data set name not like [a-z0-9_]+.")

    data_file = base_name+".data.gz"
    if not os.path.isfile(data_file):
        raise Exception("data file not found.")

    readme_file = base_name+".txt"
    if not os.path.isfile(readme_file):
        raise Exception("README not found.")

    data = np.loadtxt(data_file, ndmin=2)
    if data.ndim != 2:
        raise Exception("not a matrix")

    if data.shape[0] <= 1:
        raise Exception("too few rows.")

    # labels files are named 0,1,2,...
    labels_files = sorted(glob.glob(base_name+".labels?.gz"))
    if len(labels_files) == 0:
        raise Exception("no labels found.")

    for i in range(len(labels_files)):
        labels_file = base_name+".labels%d.gz"%i
        if labels_file not in labels_files:
            raise Exception("the i-the labels set is missing"%i)

        labels = np.loadtxt(labels_file, dtype='int')
        if len(labels) != data.shape[0]:
            raise Exception("labels count mismatch")
        counts = np.bincount(labels)
        if not all(counts[1:])>0:
            raise Exception("denormalised labels")
        if max(labels) < 2:
            raise Exception("too few classes")

        # check for the corresponding image file in the catalog
        image_file = "catalogue/"+base_name+".labels%d.png"%i
        if data.shape[1] <= 3 and not os.path.isfile(image_file):
            raise Exception(image_file+" not found")

    print("OK.")


data_files = natsorted([f for f in glob.glob("*/*.data.gz")
                                   if not f.startswith("todo_")])
for f in data_files:
    base_name = f[:-8]
    test(base_name) # raises an exception
