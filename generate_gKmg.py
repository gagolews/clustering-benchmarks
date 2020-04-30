#!/usr/bin/env python3

"""Generators for `gKmg` Clustering Datasets

Copyright (C) 2018-2020 Marek.Gagolewski.com

A generalised version of SIPU's G2 sets
(see https://cs.joensuu.fi/sipu/datasets/G2.txt),
but with a correction for dimensionality.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

#%%
import numpy as np
import scipy.spatial.distance

#%%
def generate_gKmg(d, n, mu, s, random_state=None):
    """Generates K=len(n) groups of points in R^d together with their
    corresponding labels.

    The i-th group, i=1,...,K, consists of n[i-1] points
    that are sampled from the Gaussian distribution with mean mu[i-1,:]
    and covariance matrix diag(s[i]).
    """
    assert mu.shape[0] == n.shape[0] == s.shape[0]
    assert mu.shape[1] == d
    assert (s>0).all()
    assert (n>0).all()

    K = mu.shape[0] # number of groups

    if random_state is None:
        random_state = np.random.randint(0, 2**32)

    # Each point group is generated separately,
    # with different (yet predictable) random_state,
    # so that changing n[i] generates the same points

    X = []
    for i in range(K):
        rand = np.random.RandomState((random_state+i) % (2**32))
        X.append(rand.randn(n[i], d)*s[i] + mu[i,:])

    X = np.vstack(X)

    labels0 = np.repeat(np.arange(1, K+1), n) #[1,1,...,1,2,...,2,...,K,...,K]

    labels1 = np.argmax(scipy.spatial.distance.cdist(X, mu), axis=1)+1

    return X, labels0, labels1



#%%
# import matplotlib.pyplot as plt
# import genieclust
# random_state = 666
# mu1 = 500  # cluster1 center
# mu2 = 600  # cluster2 center
# d = 2
# s = 10
# s_cor = s*d

# for n  in [30, 50]:
#     X, labels = generate_gKmg(
#         d,
#         np.r_[n, n],
#         np.array([ [mu1]*d, [mu2]*d ]),
#         np.r_[s_cor, s_cor],
#         random_state)
#     genieclust.plots.plot_scatter(X, labels+n-30, alpha=0.5)

# plt.show()





#%%
if __name__ == "__main__":

    # This is how we generate the (perfectly balanced) g2mg sets
    # included in the Benchmark Suite.

    random_state = 123 # one of few unsuspicious RNG seeds :) [*]
    mu1 = 500  # cluster1 centre
    mu2 = 600  # cluster2 centre
    n   = 1024 # number of points in each cluster
    Ds = [2**k for k in range(0, 8)] # [1, 2, 4, ..., 128]
    Ss = list(range(10, 100, 10))     # [10, 20, ..., 90]


    for d in Ds:
        for s in Ss:
            base_name = "g2mg/g2mg_%d_%s"%(d,s)
            print(base_name)
            s_cor = s*np.sqrt(d/2)
            X, labels0, labels1 = generate_gKmg(
                d,
                np.r_[n, n],
                np.array([ [mu1]*d, [mu2]*d ]),
                np.r_[s_cor, s_cor],
                random_state)

            data_file = base_name+".data.gz"
            # round -> no "." -> reduced file size
            np.savetxt(data_file, np.round(X, 0), fmt="%d")

            labels0_file = base_name+".labels0.gz"
            np.savetxt(labels0_file, labels0, fmt="%d")

            labels1_file = base_name+".labels1.gz"
            np.savetxt(labels1_file, labels1, fmt="%d")

            readme_file = base_name+".txt"
            readme = """\
g2mg clustering benchmark
Two %d-dimensional clusters, each with %d points that have
i.i.d. Gaussian components with standard deviation %d*sqrt(%d/2).


Author: Marek Gagolewski (http://www.gagolewski.com)
Copyleft 2020
Licensed under the Creative Commons Attribution 4.0 International License

`labels0` gives reference labels based on which probability distribution's
mixture component was used to generate the corresponding points.
`labels1` gives reference labels based on the distance to
the true cluster centre (i.e., arg max_ p_i(x)).
There is no noise class.
""" % (d, n, s, d)
            with open(readme_file, "w") as f:
                f.write(readme)

    # [*] the other ones being 42, 666, 1234, 12345, and 123456.
    # EOF.
