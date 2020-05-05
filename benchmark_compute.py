#%%silent
#%%restart
#%%cd @

# Copyright (C) 2020, Marek Gagolewski, https://www.gagolewski.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



##############################################################################

# "https://github.com/gagolews/clustering_benchmarks_v1"
benchmarks_path = "."
save_csv = False
preprocess = ["none", "std", "robuststd"][1]
folders = ["wut", "sipu", "other", "fcps", "graves", "mnist", "uci", "g2mg", "h2mg"][-2:]
method = ["genieclust"][0]

##############################################################################

import sys
sys.path.append(benchmarks_path)
from load_dataset import load_dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path, glob, re, csv
from natsort import natsorted
import genieclust
import sklearn.metrics
import seaborn as sns
np.set_printoptions(precision=5, threshold=10, edgeitems=10)
pd.set_option("min_rows", 20)
plt.style.use("seaborn-whitegrid")
#plt.rcParams["figure.figsize"] = (8,4)





def get_metrics(labels_true, labels_pred):
    # disregard noise points from counting
    # noise cluster == 0
    labels_pred = labels_pred[labels_true>0]
    labels_true = labels_true[labels_true>0]
    return {**genieclust.compare_partitions.compare_partitions2(labels_true, labels_pred)}




def do_benchmark_genie(res, genie, X, labels_true, K, params):
    for M in sorted([1, 3, 5, 9, 15, 25])[::-1]: # decreasing M => NNs are reused
        for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
            genie.set_params(n_clusters=K,
                gini_threshold=g, M=M, postprocess="all")
            labels_pred = genie.fit_predict(X)
            res.append({
                **params,
                "method": "Genie_g%.1f:M%d"%(g,M),
                **get_metrics(labels_true, labels_pred)
            })
            print(".", end="")
    print(" ")



def do_benchmark_gic(res, gic, X, labels_true, K, params):
    for M in sorted([1, 3, 5, 9, 15, 25])[::-1]: # decreasing M => NNs are reused
        for add in [5, 1, 0]:
            for g in [np.r_[0.3, 0.5, 0.7], np.linspace(0.0, 1.0, 11), []]:
                if len(g) == 0 and add > 0: continue

                gic.set_params(n_clusters=K,
                    gini_thresholds=g, add_clusters=add, M=M, postprocess="all")
                labels_pred = gic.fit_predict(X)
                res.append({
                    **params,
                    "method": "GIc_A%d_TC%d:M%d"%(add,len(g),M),
                    **get_metrics(labels_true, labels_pred)
                })
                print(".", end="")
    print(" ")


def benchmark(dataset, benchmarks_path, method, preprocess="none"):
    """
    Processes a single benchmark dataset.

    preprocess is one of "none", "std", "robuststd",
    where the latter is (x-median(x))/mad(x)
    """
    np.random.seed(123)
    X = np.loadtxt(os.path.join(benchmarks_path, dataset+".data.gz"), ndmin=2)

    X = X[:, X.var(axis=0) > 0] # remove all columns of 0 variance

    if preprocess == "std": # mean/sd
        s = X.std(axis=0, ddof=1)
        X = (X-X.mean(axis=0))/s
    elif preprocess == "robuststd": # median/MAD
        s = np.median(np.abs(X-np.median(X, axis=0)), axis=0)
        s[s<1e-12] = 1.0 # don't scale columns of zero MAD
        X = (X-np.median(X, axis=0))
    else:
        s = X.std(axis=None, ddof=1) # scale all axes proportionally
        X = (X-X.mean(axis=0))


    X += np.random.normal(0.0, 1e-9, size=X.shape)  # add a tiny bit of noise
    X = X.astype(np.float32, order="C", copy=False) # work with float32


    print("## %s preprocess=%s (n=%d, d=%d)" %
          (dataset, preprocess, X.shape[0], X.shape[1]))

    label_names = sorted([re.search(r"\.(labels[0-9]+)\.gz", name).group(1)
        for name
        in glob.glob(os.path.join(benchmarks_path, dataset+".labels*.gz"))])
    label_fnames = [os.path.join(benchmarks_path, "%s.%s.gz" % (dataset,name))
        for name in label_names]
    labels = [np.loadtxt(fname, dtype="int") for fname in label_fnames]

    res = []

    if method == "genieclust":
        genie = genieclust.Genie(compute_full_tree=False)
        gic = genieclust.GIc(compute_full_tree=False)


    for i in range(len(label_names)):
        params = dict(
            dataset=dataset,
            preprocess=preprocess,
            labels=label_names[i]
        )

        labels_true = labels[i]
        labels_true_counts = np.bincount(labels_true)[1:] # noise cluster == 0
        K = len(labels_true_counts)

        # 1. find a K-partition of X -->  labels_pred
        # 2. res.append({
        #        **params,
        #        "method": "METHOD_NAME:param1:param2:etc.",
        #        **get_metrics(labels_true, labels_pred)
        #    })

        if method == "genieclust":
            do_benchmark_genie(res, genie, X, labels_true, K, params)
            do_benchmark_gic(res, gic, X, labels_true, K, params)


    return res


for folder in folders:
    fnames = glob.glob(os.path.join(benchmarks_path, folder, "*.data.gz"))
    datasets = natsorted([re.search(r"([^/]*/[^/]*)\.data\.gz", name)[1]
                          for name in fnames])

    res = []
    for dataset in datasets:
        res += benchmark(dataset, benchmarks_path,
            method=method, preprocess=preprocess)

    res_df = pd.DataFrame(res)

    if save_csv:
        res_df.to_csv("results/v1_%s_%s_%s.csv"%(folder,preprocess,method),
            index=False, quoting=csv.QUOTE_NONNUMERIC)

