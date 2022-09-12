







(sec:suite-v1)=
# Benchmark Suite (v1.0.9991)

We have compiled **a large suite of benchmark datasets**.
For reproducibility, the datasets and label vectors are **versioned**.


Version 1.0.9991 of the
[*Benchmark Suite for Clustering Algorithms*](https://github.com/gagolews/clustering-data-v1)
consists of **nine benchmark batteries**:

1. {ref}`sec:battery-sipu`,
2. {ref}`sec:battery-fcps`,
3. {ref}`sec:battery-graves`,
4. {ref}`sec:battery-uci`,
5. {ref}`sec:battery-wut`,
6. {ref}`sec:battery-mnist`,
7. {ref}`sec:battery-other`,
8. {ref}`sec:battery-g2mg`,
9. {ref}`sec:battery-h2mg`.

Each battery consists of **several datasets of different origins**.
When referring to particular datasets, we use the convention
`battery/dataset`, e.g, `wut/x2`.
Each dataset represents *n* points in $\mathbb{R}^d$
and is accompanied by at least one reference partition of cardinality *k*
(see below for a listing).


::::{important}
The versioned **snapshots of the suite** are available for download at:
<https://github.com/gagolews/clustering-data-v1/releases/tag/v1.0.9991>.

All files can be browsed at:
<https://github.com/gagolews/clustering-data-v1/tree/v1.0.9991>.

The **datasets** and the corresponding ground truth labels
can be browsed in the {ref}`sec:data-v1` section.

**Results** of different clustering algorithms can be investigated in the
{ref}`sec:results-v1` section.
::::




The datasets are provided **solely for research purposes**,
unless stated otherwise.
As mentioned in the {ref}`sec:file-format` section,
each dataset is accompanied by a text file specifying more details thereon
(e.g., the literature references that we are asked to cite).

Moreover, as courtesy, **please cite** the current project
{cite}`clustering_benchmarks` as well as mention {cite}`clustering_data_v1`
which gives the exact version and URL of the dataset suite. Thank you.



## Data Sources

There is some inherent overlap between the original databases.
We have tried to resolve any conflicts in the *best* possible manner.

Some datasets are equipped with
{ref}`additional reference labellings <sec:many-partitions>`
that did not appear in the original setting.





(sec:battery-sipu)=
## `sipu`

An excellent battery of 20 diverse datasets created or compiled
by P. Fränti and his colleagues and research students
from the University of Eastern Finland.
Available for download from <https://cs.joensuu.fi/sipu/datasets/>;
see {cite}`kmsix` for discussion:

* `a1`, `a2`, `a3`       {cite}`KarkkainenFranti2002:asets`,
* `aggregation`          {cite}`GionisETAL2007:clustagg`,
* `birch1`, `birch2`     {cite}`ZhangETAL1997:birch`,
* `compound`             {cite}`Zahn1971:gestalt`,
* `d31`, `r15`           {cite}`VeenmanETAL2002:maxvar`,
* `flame`                {cite}`FuMedico2005:flame`,
* `jain`                 {cite}`JainLaw2005:dilemma`,
* `pathbased`, `spiral`  {cite}`ChangYeung2008:pathbased`,
* `s1`, `s2`, `s3`, `s4` {cite}`FrantiVirmajoki2006:ssets`,
* `unbalance`            {cite}`psi`,
* `worms_2`, `worms_64`  {cite}`SieranojaFranti2019:densitypeaks`.


We have not included the `G2` sets as we suggest
the cluster variances should be corrected for space dimensionality;
see {ref}`sec:battery-g2mg` for an alternative.
`Birch3` is not included as no ground-truth labels were provided.
We excluded the `DIM`-sets as they are too easy for most algorithms.


| dataset              | *n*    | *d*   | reference labels   |   *k* |   noise points |
|:---------------------|:-------|:------|:-------------------|------:|---------------:|
| **sipu/a1**          | 3000   | 2     | labels0            |    20 |              0 |
| **sipu/a2**          | 5250   | 2     | labels0            |    35 |              0 |
| **sipu/a3**          | 7500   | 2     | labels0            |    50 |              0 |
| **sipu/aggregation** | 788    | 2     | labels0            |     7 |              0 |
| **sipu/birch1**      | 100000 | 2     | labels0            |   100 |              0 |
| **sipu/birch2**      | 100000 | 2     | labels0            |   100 |              0 |
| **sipu/compound**    | 399    | 2     | labels0            |     6 |              0 |
|                      |        |       | labels1            |     4 |              0 |
|                      |        |       | labels2            |     5 |             50 |
|                      |        |       | labels3            |     4 |             50 |
|                      |        |       | labels4            |     5 |              0 |
| **sipu/d31**         | 3100   | 2     | labels0            |    31 |              0 |
| **sipu/flame**       | 240    | 2     | labels0            |     2 |              0 |
|                      |        |       | labels1            |     2 |             12 |
| **sipu/jain**        | 373    | 2     | labels0            |     2 |              0 |
| **sipu/pathbased**   | 300    | 2     | labels0            |     3 |              0 |
|                      |        |       | labels1            |     4 |              0 |
| **sipu/r15**         | 600    | 2     | labels0            |    15 |              0 |
|                      |        |       | labels1            |     9 |              0 |
|                      |        |       | labels2            |     8 |              0 |
| **sipu/s1**          | 5000   | 2     | labels0            |    15 |              0 |
| **sipu/s2**          | 5000   | 2     | labels0            |    15 |              0 |
| **sipu/s3**          | 5000   | 2     | labels0            |    15 |              0 |
| **sipu/s4**          | 5000   | 2     | labels0            |    15 |              0 |
| **sipu/spiral**      | 312    | 2     | labels0            |     3 |              0 |
| **sipu/unbalance**   | 6500   | 2     | labels0            |     8 |              0 |
| **sipu/worms_2**     | 105600 | 2     | labels0            |    35 |              0 |
| **sipu/worms_64**    | 105000 | 64    | labels0            |    25 |              0 |


(sec:battery-fcps)=
## `fcps`

9 datasets from the *Fundamental Clustering Problem Suite*
proposed by A. Ultsch {cite}`fcps` from the Marburg University,
Germany.

Each dataset consists of 212–4096 observations in 2–3 dimensions.
The `GolfBall` dataset is not included as it has no cluster structure.
`Tetragonula` and `Leukemia` are also not part of our suite
as they are given as distance matrices.

Data were originally available from elsewhere, but now
can be accessed, e.g., via the R package
[*FCPS*](https://CRAN.R-project.org/package=FCPS);
see also {cite}`ThrunUltsch2020:fcps`.


(sec:battery-graves)=
## `graves`

10 *synthetic data sets* discussed by D. Graves and W. Pedrycz
in {cite}`graves`.

Each dataset consists of 200–1050 observations in 2 dimensions.
Originally, they come with no reference labels.




(sec:battery-uci)=
## `uci`

A selection of 8 datasets available at UCI
(University of California, Irvine)
[Machine Learning Repository](http://archive.ics.uci.edu/ml/)
{cite}`uci`.

Some of these datasets were considered for benchmark purposes
in, amongst others, {cite}`graves`.
They are also listed in the {ref}`sec:battery-sipu` battery.



(sec:battery-wut)=
## `wut`

22 datasets in $\mathbb{R}^2$ or $\mathbb{R}^3$
authored by the fantastic students of Marek's 2016/2017
R and Python for Data Analysis courses at the
[Faculty of Mathematics and Information Science](https://www.pw.edu.pl/engpw/Academics/Faculties/Faculty-of-Mathematics-and-Information-Science), Warsaw University of Technology:
Anna Gierlak,
Eliza Kaczorek,
Mateusz Kobyłka,
Przemysław Kosewski,
Jędrzej Krauze,
Michał Maciąg,
Aleksander Truszczyński,
and
Adam Wawrzeńczyk.
Thanks!



(sec:battery-mnist)=
## `mnist`

This battery features two large, high-dimensional datasets:

1. [MNIST](https://en.wikipedia.org/wiki/MNIST_database) –
    a database of handwritten digits (a preprocessed remix of
    [NIST](https://www.nist.gov/srd/nist-special-database-19) data
    made by Y. LeCun, C. Cortes, and C.J.C. Burges),

2. [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) –
    a similarly-structured dataset of Zalando articles
    compiled by H. Xiao, K. Rasul, and R. Vollgraf;
    see {cite}`fashion_mnist`.

Both datasets consist of 70,000 flattened 28x28 grayscale images
(train and test samples combined).



(sec:battery-other)=
## `other`

Datasets from multiple sources:

*   `chameleon_t4_8k`, `chameleon_t5_8k`, `chameleon_t7_10k`,
    `chameleon_t8_8k` – datasets supposedly related to the
    CHAMELEON algorithm by G. Karypis et al. {cite}`chameleon`.

    Source: <http://glaros.dtc.umn.edu/gkhome/cluto/cluto/download>

    In fact, in {cite}`chameleon` only two of the above
    (and some other ones) datasets are studied:
    `chameleon_t7_10k` is referred to as `DS3`,
    whilst `chameleon_t8_8k` is nicknamed `DS4`.
    The `DS2` set mentioned therein looks like a more noisy version
    of `fcps/twodiamonds`.

    
*   `hdbscan` – a dataset used for demonstrating the outputs of the
    [*hdbscan*](https://github.com/scikit-learn-contrib/hdbscan)
    package for Python {cite}`hdbscanpkg`;

* `iris`, `iris5` - "the" (see {cite}`bezdek_iris` for discussion)
    famous Iris {cite}`Fisher1936:iris` dataset
    and its imbalanced version considered in {cite}`genieins`;

* `square` – a dataset of unknown/unconfirmed origin (TODO: help needed).



(sec:battery-g2mg)=
## `g2mg`

Each dataset consists of 2,048 observations from
two equisized Gaussian clusters in $d=1, 2, \dots, 128$ dimensions
(the components are sampled independently from a normal distribution).

They can be considered a modified version of Gaussian `G2`-sets from
<https://cs.joensuu.fi/sipu/datasets/>, but with variances
dependent on datasets' dimensionalities, i.e., $s\sqrt{d/2}$
for different $s$. This makes these new problems more difficult than
their original counterparts.

It is well-known that such a data distribution
(multivariate normal with independent components)
is subject to the so-called curse of dimensionality,
leading to some weird behaviour for high $d$;
see, e.g., the Gaussian Annulus Theorem mentioned in {cite}`foundds`.

Generator: <https://github.com/gagolews/clustering-data-v1/blob/master/.devel/generate_gKmg.py>

We suggest that these datasets should be studied separately
from other batteries, because they are too plentiful.
Also, *parametric* algorithms that *specialise* in detecting
Gaussian blobs (*k*-means, expectation-maximisation (EM)
for Gaussian mixtures) will naturally perform better thereon than
the non-parametric approaches.


(sec:battery-h2mg)=
## `h2mg`

Two Gaussian-like hubs of equal sizes,
with spread dependent on datasets' dimensionalities.
Each dataset consists of 2,048 observations in 1, 2, ..., 128 dimensions.
Each point is sampled from a sphere centred at its own cluster's centre,
of radius that follows the Gaussian distribution
with a predefined scaling parameter.

Generator: <https://github.com/gagolews/clustering-data-v1/blob/master/.devel/generate_hKmg.py>

Just like in the case of {ref}`sec:battery-g2mg`, we suggest
these datasets should be studied separately from other batteries.
