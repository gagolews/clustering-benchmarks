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


import scipy.stats


def preprocess_data(data, noise_factor=1e-6, random_state=None):
    """
    Normalise a data matrix

    Removes all columns of zero variance (constant). Centres the data
    around the centroid (so that each column mean is 0).
    Scales all columns proportionally (so that the total variance is 1;
    note that this is not the same as standardisation: standard
    deviations in each column might still be different).
    Adds a tiny amount of noise to minimise the risk of having
    duplicate points.


    Parameters
    ----------

    data
        Data matrix.

    noise_factor
        Standard deviation of the white noise added.

    random_state
        Seed of the random number generator; see ``scipy.stats.norm.rvs``.


    Returns
    -------

    data
        A modified data matrix.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> data_url = "https://github.com/gagolews/clustering-data-v1/raw/v1.1.0"
    >>> wut_smile = clustbench.load_dataset(
    ...     "wut", "smile", url=data_url, preprocess=False)
    >>> np.random.seed(123)  # assure reprodicibility
    >>> X = clustbench.preprocess_data(wut_smile.data)
    """
    if data.ndim != 2:
        raise ValueError("Not a matrix.")

    # remove all columns of 0 variance:
    data = data[:, data.var(axis=0) > 0]

    # centre + scale all columns proportionally (not: standardise)
    data = (data-data.mean(axis=0))/data.std(axis=None, ddof=1)

    # add a tiny bit of white noise:
    data += scipy.stats.norm.rvs(
        loc=0.0, scale=data.std(ddof=1)*noise_factor, size=data.shape,
        random_state=random_state
    )

    # data = data.astype(np.float32, order="C", copy=False) # work with float32

    return data
