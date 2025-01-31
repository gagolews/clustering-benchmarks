#!/usr/bin/env -S python3 -W ignore::FutureWarning


"""
Compute external cluster validity measures on the benchmark datasets
described in: Gagolewski M., A framework for benchmarking clustering algorithms,
SoftwareX 20, 2022, 101270, https://clustering-benchmarks.gagolewski.com,
DOI: 10.1016/j.softx.2022.101270.


Copyright (C) 2023-2025, Marek Gagolewski <https://www.gagolewski.com>

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

import clustbench  # https://pypi.org/project/clustering-benchmarks/
import os.path
import numpy as np
import pandas as pd
import sys
#import matplotlib.pyplot as plt
import os.path, glob, re, csv
import genieclust




np.set_printoptions(precision=5, threshold=10, edgeitems=10)
pd.set_option("min_rows", 20)
#plt.style.use("seaborn-whitegrid")
#plt.rcParams["figure.figsize"] = (8,4)




## TODO: change me: -------------------------------------------------------

# see <https://github.com/gagolews/clustering-data-v1>:
data_path = "/home/gagolews/Projects/clustering-data-v1"

results_path_base = "/home/gagolews/Projects/clustering-results-v1/original"
results_subdirs = [
    "Genie",
    "ITM",
    #"IcA",
    #"GenieIc",
    #"Test_Genie_ForcedMerge",
    #"Test_GIc",
    #"lukaszbrzozowski_msts",
    #"optim_cvi_mst_divisive",
    #"optim_cvi_mst_exact",
    #"optim_cvi",
    "fastcluster_average",
    "fastcluster_centroid",
    "fastcluster_complete",
    "fastcluster_median",
    "fastcluster_ward",
    "fastcluster_weighted",
    "sklearn_birch",
    "sklearn_gm",
    "sklearn_kmeans",
    "sklearn_spectral",
]

max_n = 10_000

skip_batteries = ["h2mg", "g2mg"] #, "mnist"]

skip_methods = [
    'Dunn',   # == GDunn_d1_D1
    'Gamma',  # slow!
    'WCSS',   # the same as Calinski-Harabasz
    'GDunn_d6_D1',
    'GDunn_d6_D2',
    'GDunn_d6_D3',
    #'GIc',
    #'IcA',
    #'fastcluster_centroid',
    #'fastcluster_weighted',
    #'fastcluster_median',

    #"Test_Genie_ForcedMerge_G0.1",
    #"Test_Genie_ForcedMerge_G0.3",
    #"Test_Genie_ForcedMerge_G0.5",
    #"Test_Genie_ForcedMerge_G0.7",
    #"Test_Genie_ForcedMerge_G1.0",

    #"Test_GIc_Addcl10_Thresnum4",
    #"Test_GIc_Addcl10_Thresnum11",
    #"Test_GIc_Addcl5_Thresnum4",
    #"Test_GIc_Addcl5_Thresnum11",
    #"Test_GIc_Addcl1_Thresnum4",
    #"Test_GIc_Addcl1_Thresnum11",
    #"Test_GIc_Addcl0_Thresnum4",
    #"Test_GIc_Addcl0_Thresnum11",

    'labels0',
    'labels1',
    'labels2',
    'labels3',
    'labels4',
    'labels5',
    'labels6',
    'labels7',
    'labels8',
    'labels9',
    #'sklearn_birch_T0.005_BF10',
    #'sklearn_birch_T0.005_BF100',
    #'sklearn_birch_T0.005_BF50',
    #'sklearn_birch_T0.01_BF10',
    #'sklearn_birch_T0.01_BF100',
    ##'sklearn_birch_T0.01_BF50',
    #'sklearn_birch_T0.025_BF10',
    #'sklearn_birch_T0.025_BF100',
    #'sklearn_birch_T0.025_BF50',
    #'sklearn_birch_T0.05_BF10',
    #'sklearn_birch_T0.05_BF100',
    #'sklearn_birch_T0.05_BF50',
    #'sklearn_birch_T0.1_BF10',
    #'sklearn_birch_T0.1_BF100',
    #'sklearn_birch_T0.1_BF50',
    #'sklearn_birch_T0.25_BF10',
    #'sklearn_birch_T0.25_BF100',
    #'sklearn_birch_T0.25_BF50',
    #'sklearn_birch_T0.5_BF10',
    #'sklearn_birch_T0.5_BF100',
    #'sklearn_birch_T0.5_BF50',
    #'sklearn_birch_T1_BF10',
    #'sklearn_birch_T1_BF100',
    #'sklearn_birch_T1_BF50',
    #'sklearn_spectral_Alaplacian_G0.25',
    #'sklearn_spectral_Alaplacian_G0.5',
    #'sklearn_spectral_Alaplacian_G1',
    #'sklearn_spectral_Alaplacian_G2.5',
    #'sklearn_spectral_Alaplacian_G5',
    #'sklearn_spectral_Apoly_G0.25',
    #'sklearn_spectral_Apoly_G0.5',
    #'sklearn_spectral_Apoly_G1',
    #'sklearn_spectral_Apoly_G2.5',
    #'sklearn_spectral_Apoly_G5',
    #'sklearn_spectral_Arbf_G0.25',
    #'sklearn_spectral_Arbf_G0.5',
    ##'sklearn_spectral_Arbf_G1',
    #'sklearn_spectral_Arbf_G2.5',
    #'sklearn_spectral_Arbf_G5',
    #'sklearn_spectral_Asigmoid_G0.25',
    #'sklearn_spectral_Asigmoid_G0.5',
    #'sklearn_spectral_Asigmoid_G1',
    #'sklearn_spectral_Asigmoid_G2.5',
    #'sklearn_spectral_Asigmoid_G5',
]

## ------------------------------------------------------------------------

def get_metrics(y_pred, y_true):
    # disregard noise points from counting
    # noise cluster == 0
    y_pred = y_pred[y_true>0]
    y_true = y_true[y_true>0]

    C = genieclust.compare_partitions.confusion_matrix(y_true, y_pred)
    # after the removal of the noise points,
    # C might have more columns than rows!

    while C.shape[0] > C.shape[1]:
        C = np.c_[C, [0]*C.shape[0]]

    #if np.any(C.sum(axis=1) == 0):
        #raise Exception

    res = genieclust.compare_partitions.compare_partitions(C)
    if not res["nca"] >= 0.0:
        raise Exception("NOT: NCA >= 0.0")
    return res

## ------------------------------------------------------------------------

batteries = clustbench.get_battery_names(path=data_path)
batteries = sorted(set(batteries) - set(skip_batteries))

res = []
for battery in batteries:
    datasets = clustbench.get_dataset_names(battery, path=data_path)

    for dataset in datasets:
        b = clustbench.load_dataset(battery, dataset, path=data_path)

        print("%s/%s [n=%d, d=%d]: " % (
            b.battery, b.dataset, b.data.shape[0], b.data.shape[1]
        ), end="", file=sys.stderr, flush=True)

        if b.data.shape[0] > max_n:
            print("**skipping (n>max_n)**", file=sys.stderr, flush=True)
            continue

        ks = np.unique(b.n_clusters)

        labels_pred = dict()
        for subdir in results_subdirs:
            results_path = os.path.join(results_path_base, subdir)
            labels_pred = {**labels_pred, **clustbench.load_results(
                results_path, battery, dataset, ks
            )}

        for skip in skip_methods:
            if skip in labels_pred: del labels_pred[skip]

        #labels_pred = clustbench.transpose_results(labels_pred)
        labels_true = b.labels
        labels_true_Ks = b.n_clusters
        labels_true_names = ["labels%d" % i for i in range(len(labels_true))]

        for method in labels_pred:
            for i in range(len(labels_true)):
                try:
                    y_true = labels_true[i]
                    y_pred = labels_pred[method][labels_true_Ks[i]]
                    #assert max(y_true) == max(y_pred)
                    counts = np.bincount(y_pred)[1:]
                    res.append(dict(
                        battery=battery,
                        dataset=dataset,
                        n=b.data.shape[0],
                        d=b.data.shape[1],
                        labels=labels_true_names[i],
                        n_clusters=labels_true_Ks[i],
                        method=method,
                        **get_metrics(y_pred, y_true)
                    ))
                except Exception as e:
                    print("    method=%s, K=%d (%s: %s)" %
                        (method, labels_true_Ks[i], e.__class__.__name__, str(e)),
                        file=sys.stderr, flush=True)

        print("", file=sys.stderr, flush=True)


res_df = pd.DataFrame(res).sort_values(["battery", "dataset", "labels"])
res_df.to_csv("v1-scores.csv.gz", index=False, quoting=csv.QUOTE_NONNUMERIC)

print("Done.", file=sys.stderr, flush=True)

print(res_df)
