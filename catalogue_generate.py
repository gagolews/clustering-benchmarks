#!/usr/bin/env python3

"""Generates the Catalogue of Clustering Datasets

Copyleft (C) 2018-2021 Marek Gagolewski <https://www.gagolewski.com>

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


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, matplotlib, matplotlib.image
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import sklearn.metrics, os.path, os, glob, re, sys
import scipy.spatial.distance
import genieclust
import tempfile, base64
from natsort import natsorted

#################################################################################
# Global options

plt.style.use('seaborn-whitegrid')

#################################################################################


def process(f, dataset):
    """
    Processes a single dataset (yup!).
    """
    X = np.loadtxt(dataset+".data.gz", ndmin=2)
    # X = (X-X.mean(axis=0))/X.std(axis=None, ddof=1) # scale all axes proportionally

    print('## %s (n=%d, d=%d) <a name="%s"></a>\n' % (
        dataset, X.shape[0], X.shape[1], str.replace(dataset, os.path.sep, "_")
    ), file=f)

    with open(dataset+".txt", "r") as readme_file:
        for readme_line in readme_file.read().split("\n"):
            print("    "+readme_line, file=f)
    print("\n", file=f)

    label_names = sorted([re.search(r'\.(labels[0-9]+)\.gz', name).group(1) for name in glob.glob(dataset+".labels*.gz")])
    labels = [np.loadtxt("%s.%s.gz" % (dataset, name), dtype='int') for name in label_names]
    label_counts = [np.bincount(l) for l in labels]
    noise_counts = [c[0] for c in label_counts]
    #have_noise = [bool(c[0]) for c in label_counts]
    label_counts = [c[1:] for c in label_counts]
    true_K = [len(c) for c in label_counts]
    true_G = [genieclust.inequity.gini_index(c) for c in label_counts]

    for i in range(len(label_names)):
        print("#### `%s`\n\ntrue_k=%2d, noise=%5d, true_g=%.3f\n\nlabel_counts=%r\n" % (
                label_names[i], true_K[i], noise_counts[i],
                true_G[i], label_counts[i].tolist()
            ),
            file=f
        )

        if X.shape[1] not in [1, 2, 3]:
            print('> **(preview generation suppressed)**\n\n', file=f)
            continue

        plt.figure()
        ax = plt.subplot(111, projection=None if X.shape[1] in [1,2] else '3d')


        if X.shape[1] == 2:
            genieclust.plots.plot_scatter(X, labels=labels[i], alpha=0.25)
            plt.axis("equal")

        elif X.shape[1] == 1:
            X_aug = np.insert(X, 1, np.random.randn(len(X))*(X.max()-X.min())*1e-6, axis=1)
            genieclust.plots.plot_scatter(X_aug, labels=labels[i], alpha=0.25)
            plt.axis("equal")

        elif X.shape[1] == 3:
            ax.scatter(X[:,0], X[:,1],
                       c=np.array(genieclust.plots.col,dtype=np.object)[
                           (labels[i])%len(genieclust.plots.col)
                       ],
                       alpha=0.25)
            #plt.axis("equal")

        plt.title("%s.%s (n=%d, k=%d%s)"%(dataset, label_names[i],
                                                X.shape[0],
                                                true_K[i],
                                                ", noise=%d"%noise_counts[i] if noise_counts[i] else ""))

        _fig_name = "%s.%s.png"%(dataset,label_names[i])
        _fig_path = os.path.join("catalogue", _fig_name)
        plt.savefig(_fig_path, format='png', transparent=True,
                    bbox_inches='tight', dpi=150)
        plt.close()

        print("![](%s)\n"%(_fig_name), file=f)

        # with open(_fig_path, "rb") as img:
            # encoded_string = base64.b64encode(img.read()).decode("US-ASCII")
        #print("<img src='data:image/png;base64,"+encoded_string+"' alt='%s.%s' />\n"%(dataset, label_names[i]), file=f)




    print("\n\n", file=f)

    return [
        dict(
            dataset=dataset,
            n=X.shape[0],
            d=X.shape[1],
            labels=label_names[i],
            k=true_K[i],
            noise=noise_counts[i],
            g=true_G[i]
        )
        for i in range(len(label_names))
    ]




###############################################################################
# Do the job.

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: %s benchmark_folder" % sys.argv[0])

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        raise Exception("`%s` is not a directory")

    fnames = glob.glob(os.path.join(folder, "*.data.gz"))
    datasets = natsorted([re.search(r"(.*)\.data\.gz", name)[1] for name in fnames])

    image_folder = os.path.join("catalogue", folder)
    if not os.path.isdir(image_folder): os.mkdir(image_folder)

    output = os.path.join("catalogue", "%s.md"%folder)
    f = open(output, "w")

    print("**[Benchmark Suite for Clustering Algorithms -- Version 1](https://github.com/gagolews/clustering_benchmarks_v1)", file=f)
    print("is maintained by [Marek Gagolewski](https://www.gagolewski.com)**\n", file=f)
    print("\n"+("-"*80)+"\n", file=f)

    print("**Datasets**\n", file=f)
    for dataset in datasets:
        print("* [%s](#%s)"%(dataset,str.replace(dataset,"/","_")), file=f)
    print("\n"+("-"*80)+"\n", file=f)

    metadata = []
    for dataset in datasets:
        print("Generating %s..."%dataset)
        metadata += process(f, dataset)
    f.close()

    metadata_file = os.path.join("catalogue", "%s.csv"%folder)
    pd.DataFrame(metadata).\
        loc[:,["dataset", "n", "d", "labels", "k", "noise", "g"]].\
        to_csv(metadata_file, header=True, index=False)

    print("Done.")
