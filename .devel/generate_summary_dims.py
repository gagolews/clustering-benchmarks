#!/usr/bin/env python3


"""
Compute intrinsic dimensionality (di) of each dataset, see estimate_dimension.py

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


# ``````````````````````````````````````````````````````````````````````````````
# `````` USER SETTINGS                                                   ```````
# ``````````````````````````````````````````````````````````````````````````````

# TODO: download the clustering benchmarks repository from
# https://github.com/gagolews/clustering_benchmarks_v1
benchmarks_path = "/home/gagolews/Projects/clustering_benchmarks_v1"


# TODO: select one or more processing methods  (must be a list)
preprocessors = ["original", "scale_standard", "scale_robust"][:1]

# TODO: skip datasets with > 10000 rows?
small_only = False

# TODO: select one or more test batteries (must be a list)
batteries = ["wut", "graves", "uci", "other", "fcps",
             "sipu", "mnist", "g2mg", "h2mg"]

save_csv = False




# ``````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````


import sys
import numpy as np
import pandas as pd
import scipy.stats
import os.path, glob, re, csv, os
from natsort import natsorted
import sklearn.metrics
import time
from benchmark_load import *
from estimate_dimension import *


def benchmark(battery, dataset, benchmarks_path,
              preprocess="original", small_only=False):

    input_fname_base = os.path.join(benchmarks_path, battery, dataset)

    np.random.seed(123)
    X = load_data(input_fname_base+".data.gz", preprocess)




    n = X.shape[0]
    d = X.shape[1]
    if small_only and X.shape[0] > 10_000:
        di = np.nan
    else:
        di = estimate_dimension(X)
    s = "%s/%s/%s"%(preprocess, battery, dataset)

    print("## %-45s %6d %4d %5.2f" %
        (s, n, d, di))

    return [dict(battery=battery, dataset=dataset, n=n, d=d, di=di)]


if __name__ == "__main__":
    assert os.path.exists(benchmarks_path)
    assert type(preprocessors) is list
    assert type(batteries) is list

    res = []
    # for every preprocessing scheme
    for preprocess in preprocessors:
        # for every battery of benchmark tests:
        for battery in batteries:
            fnames = glob.glob(os.path.join(benchmarks_path, battery, "*.data.gz"))
            datasets = natsorted([re.search(r"([^/]*)\.data\.gz", name)[1]
                                for name in fnames])

            # for every dataset in the benchmark battery:
            for dataset in datasets:
                try:
                    res += benchmark(battery, dataset, benchmarks_path,
                        preprocess, small_only)
                except Exception as e:
                    print("%s: %s" % (e.__class__.__name__, format(e)))

    res_df = pd.DataFrame(res)
    print(res_df)
    if save_csv:
        res_df.to_csv("%s/v1-dims.csv"%(preprocess),
            index=False, quoting=csv.QUOTE_NONNUMERIC)
    print("Done.")
