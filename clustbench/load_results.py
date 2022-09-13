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


import os.path
import numpy as np
import pandas as pd
import os
import glob
import re
import sys
from natsort import natsorted


def load_results(
    method_group, battery, dataset, n_clusters, path=None,
    expanduser=True, expandvars=True
):
    """
    Load benchmark results

    Reads the datasets named like `method_group/battery/dataset.resultK.gz`
    (relative to the directory `path`), where `K` is equal to
    `n_clusters`.
    `method_group` can be a wildcard like ``"*"`` if a look up in multiple
    directory is required.

    Parameters
    ----------

    method_group
        Name of the method group, e.g., ``"Genie"``, ``"."``, or ``"*"``.

    battery
        Name of the battery, e.g., ``"wut"`` or ``"other"``.

    dataset
        Dataset name, e.g., ``"x2"`` or ``"iris"``.

    n_clusters
        `K` - number of clusters.

    path
        Path to the directory containing the downloaded benchmark datasets
        suite. Defaults to the current working directory.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Returns
    -------

    results
        A dictionary of label vectors.
        Keys correspond to method names.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> # load from a local library (a manually downloaded repository)
    >>> results_path = os.path.join("~", "Projects", "clustering-results-v1", "original")
    >>> res = clustbench.load_results("*", "wut", "x2", 3, path=results_path)
    >>> print(res.keys)
    """
    if path is None: path = "."
    if expanduser: path = os.path.expanduser(path)
    if expandvars: path = os.path.expandvars(path)

    fname_pat = os.path.join(path, method_group, battery, dataset)
    fname_pat += ".result%d.gz" % n_clusters

    results = dict()
    for fname in natsorted(glob.glob(fname_pat)):
        labels = pd.read_csv(fname)
        for i in range(labels.shape[1]):
            results[labels.columns[i]] = np.array(labels.iloc[:, i])

    return results
