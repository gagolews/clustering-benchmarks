#!/usr/bin/env python3
#%%silent
#%%restart
#%%cd @

# Copyright (C) 2020-2022, Marek Gagolewski, https://www.gagolewski.com
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

# https://github.com/gagolews/clustering-data-v1
benchmarks_path = "/home/gagolews/Projects/clustering-data-v1"

# select one:
preprocess = ["original", "scale_standard", "scale_robust"][0]

# select a few:
batteries = ["wut", "graves", "uci", "other", "fcps", "sipu", "mnist",
             "g2mg", "h2mg"]

# select a few:
methods = [
    "Genie",   # Genie - thresholds 0.1, 0.3, 0.5, 0.7, 1.0(=single linkage)
    #"GIc",     # GIc - default parameters
    #"GIcTest", # GIc - many parameters (for testing)
    #"GenieNewTest",
    #"GenieApprox",
    #"IcA",     # IcA (via GIc)
    "ITM",     # Andreas Mueller's Information Theoretic Clustering with MSTs
    "sklearn_birch",
    "sklearn_gm",
    "sklearn_kmeans",
    "sklearn_spectral",
    "fastcluster_average",
    "fastcluster_centroid",
    "fastcluster_complete",
    "fastcluster_median",
    "fastcluster_ward",
    "fastcluster_weighted",
    "optim_cvi"
]





##############################################################################

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path, glob, re, csv
from natsort import natsorted
import genieclust
import sklearn.metrics
import seaborn as sns
import scipy.optimize

np.set_printoptions(precision=5, threshold=10, edgeitems=10)
pd.set_option("min_rows", 20)
plt.style.use("seaborn-whitegrid")
#plt.rcParams["figure.figsize"] = (8,4)



def get_metrics(y_true, y_pred):
    # disregard noise points from counting
    # noise cluster == 0
    y_true = y_true[y_true>0]
    y_pred = y_pred[y_true>0]

    C = genieclust.compare_partitions.confusion_matrix(y_true, y_pred)
    # after the removal of the noise points,
    # C might have more columns than rows!

    d = genieclust.compare_partitions.compare_partitions(C)

    return dict(
        **d,
        pa=d["nacc"]*(1-1/C.shape[0])+1/C.shape[0],
    )


# ``````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````


def process_dataset(battery, dataset, benchmarks_path, method, preprocess):
    """
    Reads labels stored in compressed CSV files
    named ./PREPROCESS/METHOD/BATTERY/DATASET.resultK.gz, where
    K is one of possibly many partition cardinalities generated.
    For instance, the path can be ./original/Genie/sipu/aggregation.result7.gz
    for all the 7-partitions obtained.

    Then, compares the labels against the true labels.



    Parameters
    ==========

    battery : str
        Name of the benchmark battery, e.g., 'sipu' or 'wut'.

    dataset : str
        Name of the dataset in the battery, e.g., 'spiral' or 'smile'.

    benchmarks_path : str
        Path to the local copy of the repository
        https://github.com/gagolews/clustering_benchmarks_v1

    method : str
        Name of the method family tested.

    preprocess : one of "original", "scale_standard", "scale_robust"
    """
    labels_true_path_base = os.path.join(benchmarks_path, battery, dataset)
    labels_true_names = sorted([re.search(r"\.(labels[0-9]+)\.gz", name).group(1)
        for name in glob.glob(labels_true_path_base+".labels*.gz")])
    labels_true_fnames = [labels_true_path_base+(".%s.gz" % name)
        for name in labels_true_names]
    labels_true = [np.loadtxt(fname, dtype="int") for fname in labels_true_fnames]
    labels_true_Ks = [len(np.bincount(l)[1:]) for l in labels_true]


    labels_pred_path = os.path.join("results_"+preprocess, method, battery)
    if not os.path.exists(labels_pred_path):
        return []

    labels_pred_path_base = os.path.join(labels_pred_path, dataset)
    labels_pred_Ks = sorted([int(re.search(r"\.result([0-9]+)\.gz", name).group(1))
        for name in glob.glob(labels_pred_path_base+".result*.gz")])

    labels_pred = dict()
    for K in labels_pred_Ks:
        fname = labels_pred_path_base+".result%d.gz"%K
        try:
            l = pd.read_csv(fname)
        except:
            #print("    Missing labels file for method=%s, K=%d" %
            #          (method, K),
            #          file=sys.stderr, flush=True)
            # just don't add any results to labels_pred
            continue

        for i in range(l.shape[1]):
            y_pred = np.array(l.iloc[:,i], dtype="int")
            assert y_pred.shape[0] == labels_true[0].shape[0]
            assert y_pred.max() == K or K == 0
            assert y_pred.min() == 1 or (y_pred.min() == 0 and y_pred.max() == 1)
            assert K == 0 or len(np.unique(y_pred))==K
            if l.columns[i] not in labels_pred:
                labels_pred[l.columns[i]] = dict()
            labels_pred[l.columns[i]][K] = y_pred

    # labels_true -- list of label vectors
    # labels_pred -- dictionary of dictionaries of label vectors, where
    #    labels_pred[M][K] gives the label vector generated by the method M
    #    for n_clusters=K.

    res = []
    for method in labels_pred:
        for i in range(len(labels_true)):
            try:
                y_true = labels_true[i]
                y_pred = labels_pred[method][labels_true_Ks[i]]
                assert max(y_true) == max(y_pred)
                res.append(dict(
                    battery=battery,
                    dataset=dataset,
                    method=method,
                    labels=labels_true_names[i],
                    #K=labels_true_Ks[i],
                    **get_metrics(y_true, y_pred)
                ))
            except Exception as e:
                print("    method=%s, K=%d (%s: %s)" %
                      (method, labels_true_Ks[i], e.__class__.__name__, str(e)),
                      file=sys.stderr, flush=True)
    return res




if __name__ == "__main__":
    assert os.path.exists(benchmarks_path)
    assert type(methods) is list
    assert type(batteries) is list
    assert type(preprocess) is str

    res = []
    for battery in batteries:
        fnames = glob.glob(os.path.join(benchmarks_path, battery, "*.data.gz"))
        datasets = natsorted([re.search(r"([^/]*)\.data\.gz", name)[1]
                            for name in fnames])

        for dataset in datasets:
            print("dataset=%s/%s" % (battery, dataset),
                    file=sys.stderr, flush=True)

            for method in methods:
                res += process_dataset(battery, dataset, benchmarks_path, method, preprocess)

    res_df = pd.DataFrame(res)
    print(res_df)
    res_df.to_csv("results_%s/v1-scores.csv"%(preprocess),
        index=False, quoting=csv.QUOTE_NONNUMERIC)


print("Done.")
