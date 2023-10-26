"""
clustering-benchmarks Package
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2020-2023, Marek Gagolewski <https://www.gagolewski.com>      #
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
import warnings
import genieclust
from .load_results import labels_list_to_dict


def get_score(
    labels,
    results,
    metric=genieclust.compare_partitions.normalized_clustering_accuracy,
    compute_max=True,
    warn_if_missing=True
):
    """
    Computes a similarity score between the reference and the predicted partitions

    Takes into account that there can be more than one ground truth partition
    and ignores the noise points (as explained in the Methodology section
    of the clustering benchmark framework's website).

    If ``labels`` is a single label vector, it will be wrapped inside
    a list. If ``results`` is not a dictionary,
    `labels_list_to_dict` will be called first.


    Parameters
    ----------

    labels
        A vector-like object or a list thereof.

    results
        A dictionary of clustering results, where
        ``results[K]`` gives a K-partition.

    metric : function
        An external cluster validity measure; defaults to
        ``genieclust.compare_partitions.normalized_clustering_accuracy``.
        It will be called like ``metric(y_true, y_pred)``.

    compute_max : bool
        Whether to apply ``max`` on the particular similarity scores.

    warn_if_missing : bool
        Warn if some ``results[K]`` is required, but missing.

    Returns
    -------

    score : float or array thereof
        The computed similarity scores. Ultimately, it is a vector of
        ``metric(y_true[y_true>0], results[max(y_true)][y_true>0])``
        over all ``y_true`` in ``labels``
        or the maximum thereof if ``compute_max`` is ``True``.
    """

    labels = list(np.array(labels, ndmin=2))

    if type(results) is not dict:
        results = labels_list_to_dict(results)

    scores = []
    for y_true in labels:
        k = int(max(y_true))

        if k not in results:
            if warn_if_missing:
                warnings.warn("`results[%d]` is not available." % k)
            scores.append(np.nan)
            continue

        y_pred = results[k]
        if np.min(y_pred) < 1 or np.max(y_pred) > k:
            raise ValueError("`results[k]` is not between 1 and k=%d." % k)

        scores.append(metric(y_true[y_true > 0], y_pred[y_true > 0]))

    if compute_max and len(scores) > 0:
        return np.nanmax(scores)
    else:
        return np.array(scores)
