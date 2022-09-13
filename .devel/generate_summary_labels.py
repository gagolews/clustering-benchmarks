#!/usr/bin/env python3


"""
Generates v1-labels.csv

Copyright (C) 2020, Marek Gagolewski, https://www.gagolewski.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import numpy as np
import pandas as pd
import os.path, glob, re, csv, os
from natsort import natsorted


# ``````````````````````````````````````````````````````````````````````````````
# `````` USER SETTINGS                                                   ```````
# ``````````````````````````````````````````````````````````````````````````````

# TODO: download the clustering benchmarks repository from
# https://github.com/gagolews/clustering_benchmarks_v1
benchmarks_path = "/home/gagolews/Projects/clustering_benchmarks_v1"

output_file = "original/v1-labels.csv"


# ``````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````


if __name__ == "__main__":
    assert os.path.exists(benchmarks_path)
    fnames = glob.glob(os.path.join(benchmarks_path, "catalogue", "*.csv"))

    res = [
        pd.read_csv(f) for f in fnames
    ]

    res_df = pd.concat(res, axis=0)

    res_dataset = res_df["dataset"].str.split("/", n=1, expand=True)
    res_df["battery"] = res_dataset.iloc[:, 0]
    res_df["dataset"] = res_dataset.iloc[:, 1]
    res_df = res_df.set_index(["battery", "dataset"]).reset_index()

    #print(res_df)
    res_df.to_csv(output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
