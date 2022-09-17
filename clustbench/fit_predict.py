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


import numpy as np


def fit_predict_many(model, data, n_clusters):
    """
    Determine many clusterings of the same dataset.

    Ideally, for hierarchical methods, it would be best
    if ``model`` was be implemented smartly enough
    that for the same ``X`` and different ``n_clusters``
    it does not recompute the whole hierarchy from scratch.


    Parameters
    ----------

    model
        An object equipped with ``fit_predict``
        and ``set_param`` methods (e.g., a `scikit-learn`-like class)

    data : array-like
        Data matrix.

    n_clusters : int or list of ints
        Number of clusters.


    Returns
    -------

    results
        A dictionary of label vectors,
        where ``results[K]`` gives the discovered ``K``-partition.
    """
    n_clusters = np.unique(np.r_[n_clusters])

    results = dict()
    for k in n_clusters:
        k = int(k)
        model.set_params(n_clusters=k)
        results[k] = model.fit_predict(data) + 1

    return results
