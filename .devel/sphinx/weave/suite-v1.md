







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
"`battery/dataset`", e.g, "{ref}`sec:battery-wut``/x2`".
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


|    | dataset              | *n*    | *d*   | reference labels   |   *k* |   noise points |
|:---|:---------------------|:-------|:------|:-------------------|------:|---------------:|
| 1  | **sipu/a1**          | 3000   | 2     | labels0            |    20 |              0 |
| 2  | **sipu/a2**          | 5250   | 2     | labels0            |    35 |              0 |
| 3  | **sipu/a3**          | 7500   | 2     | labels0            |    50 |              0 |
| 4  | **sipu/aggregation** | 788    | 2     | labels0            |     7 |              0 |
| 5  | **sipu/birch1**      | 100000 | 2     | labels0            |   100 |              0 |
| 6  | **sipu/birch2**      | 100000 | 2     | labels0            |   100 |              0 |
| 7  | **sipu/compound**    | 399    | 2     | labels0            |     6 |              0 |
|    |                      |        |       | labels1            |     4 |              0 |
|    |                      |        |       | labels2            |     5 |             50 |
|    |                      |        |       | labels3            |     4 |             50 |
|    |                      |        |       | labels4            |     5 |              0 |
| 8  | **sipu/d31**         | 3100   | 2     | labels0            |    31 |              0 |
| 9  | **sipu/flame**       | 240    | 2     | labels0            |     2 |              0 |
|    |                      |        |       | labels1            |     2 |             12 |
| 10 | **sipu/jain**        | 373    | 2     | labels0            |     2 |              0 |
| 11 | **sipu/pathbased**   | 300    | 2     | labels0            |     3 |              0 |
|    |                      |        |       | labels1            |     4 |              0 |
| 12 | **sipu/r15**         | 600    | 2     | labels0            |    15 |              0 |
|    |                      |        |       | labels1            |     9 |              0 |
|    |                      |        |       | labels2            |     8 |              0 |
| 13 | **sipu/s1**          | 5000   | 2     | labels0            |    15 |              0 |
| 14 | **sipu/s2**          | 5000   | 2     | labels0            |    15 |              0 |
| 15 | **sipu/s3**          | 5000   | 2     | labels0            |    15 |              0 |
| 16 | **sipu/s4**          | 5000   | 2     | labels0            |    15 |              0 |
| 17 | **sipu/spiral**      | 312    | 2     | labels0            |     3 |              0 |
| 18 | **sipu/unbalance**   | 6500   | 2     | labels0            |     8 |              0 |
| 19 | **sipu/worms_2**     | 105600 | 2     | labels0            |    35 |              0 |
| 20 | **sipu/worms_64**    | 105000 | 64    | labels0            |    25 |              0 |


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

|    | dataset              | *n*   | *d*   | reference labels   |   *k* |   noise points |
|:---|:---------------------|:------|:------|:-------------------|------:|---------------:|
| 1  | **fcps/atom**        | 800   | 3     | labels0            |     2 |              0 |
| 2  | **fcps/chainlink**   | 1000  | 3     | labels0            |     2 |              0 |
| 3  | **fcps/engytime**    | 4096  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 4  | **fcps/hepta**       | 212   | 3     | labels0            |     7 |              0 |
| 5  | **fcps/lsun**        | 400   | 2     | labels0            |     3 |              0 |
| 6  | **fcps/target**      | 770   | 2     | labels0            |     6 |              0 |
|    |                      |       |       | labels1            |     2 |             12 |
| 7  | **fcps/tetra**       | 400   | 3     | labels0            |     4 |              0 |
| 8  | **fcps/twodiamonds** | 800   | 2     | labels0            |     2 |              0 |
| 9  | **fcps/wingnut**     | 1016  | 2     | labels0            |     2 |              0 |





(sec:battery-graves)=
## `graves`

10 *synthetic data sets* discussed by D. Graves and W. Pedrycz
in {cite}`graves`.

Each dataset consists of 200–1050 observations in 2 dimensions.
Originally, they come with no reference labels.

|    | dataset                    | *n*   | *d*   | reference labels   |   *k* |   noise points |
|:---|:---------------------------|:------|:------|:-------------------|------:|---------------:|
| 1  | **graves/dense**           | 200   | 2     | labels0            |     2 |              0 |
| 2  | **graves/fuzzyx**          | 1000  | 2     | labels0            |     5 |              0 |
|    |                            |       |       | labels1            |     2 |              0 |
|    |                            |       |       | labels2            |     2 |              0 |
|    |                            |       |       | labels3            |     2 |              0 |
|    |                            |       |       | labels4            |     2 |              0 |
|    |                            |       |       | labels5            |     4 |              0 |
| 3  | **graves/line**            | 250   | 2     | labels0            |     2 |              0 |
| 4  | **graves/parabolic**       | 1000  | 2     | labels0            |     2 |              0 |
|    |                            |       |       | labels1            |     4 |              0 |
| 5  | **graves/ring**            | 1000  | 2     | labels0            |     2 |              0 |
| 6  | **graves/ring_noisy**      | 1050  | 2     | labels0            |     2 |             43 |
| 7  | **graves/ring_outliers**   | 1030  | 2     | labels0            |     5 |              0 |
|    |                            |       |       | labels1            |     2 |             30 |
| 8  | **graves/zigzag**          | 250   | 2     | labels0            |     3 |              0 |
|    |                            |       |       | labels1            |     5 |              0 |
| 9  | **graves/zigzag_noisy**    | 300   | 2     | labels0            |     3 |             38 |
|    |                            |       |       | labels1            |     5 |             38 |
| 10 | **graves/zigzag_outliers** | 280   | 2     | labels0            |     3 |             30 |
|    |                            |       |       | labels1            |     5 |             30 |



(sec:battery-uci)=
## `uci`

A selection of 8 high-dimensional datasets available at UCI
(University of California, Irvine)
[Machine Learning Repository](http://archive.ics.uci.edu/ml/)
{cite}`uci`.
Some of them were considered for benchmark purposes
in, amongst others, {cite}`graves`.
They are also listed in the {ref}`sec:battery-sipu` battery.
However, their original purpose is for testing classification,
not clustering algorithms.

|    | dataset            |   *n* |   *d* | reference labels   |   *k* |   noise points |
|---:|:-------------------|------:|------:|:-------------------|------:|---------------:|
|  1 | **uci/ecoli**      |   336 |     7 | labels0            |     8 |              0 |
|  2 | **uci/glass**      |   214 |     9 | labels0            |     6 |              0 |
|  3 | **uci/ionosphere** |   351 |    34 | labels0            |     2 |              0 |
|  4 | **uci/sonar**      |   208 |    60 | labels0            |     2 |              0 |
|  5 | **uci/statlog**    |  2310 |    19 | labels0            |     7 |              0 |
|  6 | **uci/wdbc**       |   569 |    30 | labels0            |     2 |              0 |
|  7 | **uci/wine**       |   178 |    13 | labels0            |     3 |              0 |
|  8 | **uci/yeast**      |  1484 |     8 | labels0            |    10 |              0 |




(sec:battery-wut)=
## `wut`

22 datasets in $\mathbb{R}^2$ or $\mathbb{R}^3$
authored by the fantastic students of Marek's 2016/2017 courses on Data Analysis
in R and [Python](https://datawranglingpy.gagolewski.com) at the
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

|    | dataset                | *n*   | *d*   | reference labels   |   *k* |   noise points |
|:---|:-----------------------|:------|:------|:-------------------|------:|---------------:|
| 1  | **wut/circles**        | 4000  | 2     | labels0            |     4 |              0 |
| 2  | **wut/cross**          | 2000  | 2     | labels0            |     4 |              0 |
| 3  | **wut/graph**          | 2500  | 2     | labels0            |    10 |              0 |
| 4  | **wut/isolation**      | 9000  | 2     | labels0            |     3 |              0 |
| 5  | **wut/labirynth**      | 3546  | 2     | labels0            |     6 |              0 |
| 6  | **wut/mk1**            | 300   | 2     | labels0            |     3 |              0 |
| 7  | **wut/mk2**            | 1000  | 2     | labels0            |     2 |              0 |
| 8  | **wut/mk3**            | 600   | 3     | labels0            |     3 |              0 |
| 9  | **wut/mk4**            | 1500  | 3     | labels0            |     3 |              0 |
| 10 | **wut/olympic**        | 5000  | 2     | labels0            |     5 |              0 |
| 11 | **wut/smile**          | 1000  | 2     | labels0            |     6 |              0 |
|    |                        |       |       | labels1            |     4 |              0 |
| 12 | **wut/stripes**        | 5000  | 2     | labels0            |     2 |              0 |
| 13 | **wut/trajectories**   | 10000 | 2     | labels0            |     4 |              0 |
| 14 | **wut/trapped_lovers** | 5000  | 3     | labels0            |     3 |              0 |
| 15 | **wut/twosplashes**    | 400   | 2     | labels0            |     2 |              0 |
| 16 | **wut/windows**        | 2977  | 2     | labels0            |     5 |              0 |
| 17 | **wut/x1**             | 120   | 2     | labels0            |     3 |              0 |
| 18 | **wut/x2**             | 120   | 2     | labels0            |     3 |              0 |
| 19 | **wut/x3**             | 185   | 2     | labels0            |     4 |              0 |
| 20 | **wut/z1**             | 192   | 2     | labels0            |     3 |              0 |
| 21 | **wut/z2**             | 900   | 2     | labels0            |     5 |              0 |
| 22 | **wut/z3**             | 1000  | 2     | labels0            |     4 |              0 |




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

|    | dataset           |   *n* |   *d* | reference labels   |   *k* |   noise points |
|---:|:------------------|------:|------:|:-------------------|------:|---------------:|
|  1 | **mnist/digits**  | 70000 |   784 | labels0            |    10 |              0 |
|  2 | **mnist/fashion** | 70000 |   784 | labels0            |    10 |              0 |




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

|    | dataset                    |   *n* |   *d* | reference labels   |   *k* |   noise points |
|---:|:---------------------------|------:|------:|:-------------------|------:|---------------:|
|  1 | **other/chameleon_t4_8k**  |  8000 |     2 | labels0            |     6 |            761 |
|  2 | **other/chameleon_t5_8k**  |  8000 |     2 | labels0            |     6 |           1187 |
|  3 | **other/chameleon_t7_10k** | 10000 |     2 | labels0            |     9 |            926 |
|  4 | **other/chameleon_t8_8k**  |  8000 |     2 | labels0            |     8 |            346 |
|  5 | **other/hdbscan**          |  2309 |     2 | labels0            |     6 |            510 |
|  6 | **other/iris**             |   150 |     4 | labels0            |     3 |              0 |
|  7 | **other/iris5**            |   105 |     4 | labels0            |     3 |              0 |
|  8 | **other/square**           |  1000 |     2 | labels0            |     2 |              0 |





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

|    | dataset              | *n*   | *d*   | reference labels   |   *k* |   noise points |
|:---|:---------------------|:------|:------|:-------------------|------:|---------------:|
| 1  | **g2mg/g2mg_1_10**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 2  | **g2mg/g2mg_1_20**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 3  | **g2mg/g2mg_1_30**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 4  | **g2mg/g2mg_1_40**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 5  | **g2mg/g2mg_1_50**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 6  | **g2mg/g2mg_1_60**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 7  | **g2mg/g2mg_1_70**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 8  | **g2mg/g2mg_1_80**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 9  | **g2mg/g2mg_1_90**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 10 | **g2mg/g2mg_2_10**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 11 | **g2mg/g2mg_2_20**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 12 | **g2mg/g2mg_2_30**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 13 | **g2mg/g2mg_2_40**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 14 | **g2mg/g2mg_2_50**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 15 | **g2mg/g2mg_2_60**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 16 | **g2mg/g2mg_2_70**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 17 | **g2mg/g2mg_2_80**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 18 | **g2mg/g2mg_2_90**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 19 | **g2mg/g2mg_4_10**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 20 | **g2mg/g2mg_4_20**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 21 | **g2mg/g2mg_4_30**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 22 | **g2mg/g2mg_4_40**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 23 | **g2mg/g2mg_4_50**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 24 | **g2mg/g2mg_4_60**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 25 | **g2mg/g2mg_4_70**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 26 | **g2mg/g2mg_4_80**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 27 | **g2mg/g2mg_4_90**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 28 | **g2mg/g2mg_8_10**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 29 | **g2mg/g2mg_8_20**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 30 | **g2mg/g2mg_8_30**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 31 | **g2mg/g2mg_8_40**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 32 | **g2mg/g2mg_8_50**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 33 | **g2mg/g2mg_8_60**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 34 | **g2mg/g2mg_8_70**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 35 | **g2mg/g2mg_8_80**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 36 | **g2mg/g2mg_8_90**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 37 | **g2mg/g2mg_16_10**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 38 | **g2mg/g2mg_16_20**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 39 | **g2mg/g2mg_16_30**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 40 | **g2mg/g2mg_16_40**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 41 | **g2mg/g2mg_16_50**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 42 | **g2mg/g2mg_16_60**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 43 | **g2mg/g2mg_16_70**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 44 | **g2mg/g2mg_16_80**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 45 | **g2mg/g2mg_16_90**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 46 | **g2mg/g2mg_32_10**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 47 | **g2mg/g2mg_32_20**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 48 | **g2mg/g2mg_32_30**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 49 | **g2mg/g2mg_32_40**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 50 | **g2mg/g2mg_32_50**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 51 | **g2mg/g2mg_32_60**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 52 | **g2mg/g2mg_32_70**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 53 | **g2mg/g2mg_32_80**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 54 | **g2mg/g2mg_32_90**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 55 | **g2mg/g2mg_64_10**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 56 | **g2mg/g2mg_64_20**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 57 | **g2mg/g2mg_64_30**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 58 | **g2mg/g2mg_64_40**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 59 | **g2mg/g2mg_64_50**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 60 | **g2mg/g2mg_64_60**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 61 | **g2mg/g2mg_64_70**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 62 | **g2mg/g2mg_64_80**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 63 | **g2mg/g2mg_64_90**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 64 | **g2mg/g2mg_128_10** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 65 | **g2mg/g2mg_128_20** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 66 | **g2mg/g2mg_128_30** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 67 | **g2mg/g2mg_128_40** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 68 | **g2mg/g2mg_128_50** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 69 | **g2mg/g2mg_128_60** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 70 | **g2mg/g2mg_128_70** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 71 | **g2mg/g2mg_128_80** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 72 | **g2mg/g2mg_128_90** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |




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

|    | dataset              | *n*   | *d*   | reference labels   |   *k* |   noise points |
|:---|:---------------------|:------|:------|:-------------------|------:|---------------:|
| 1  | **h2mg/h2mg_1_10**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 2  | **h2mg/h2mg_1_20**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 3  | **h2mg/h2mg_1_30**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 4  | **h2mg/h2mg_1_40**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 5  | **h2mg/h2mg_1_50**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 6  | **h2mg/h2mg_1_60**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 7  | **h2mg/h2mg_1_70**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 8  | **h2mg/h2mg_1_80**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 9  | **h2mg/h2mg_1_90**   | 2048  | 1     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 10 | **h2mg/h2mg_2_10**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 11 | **h2mg/h2mg_2_20**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 12 | **h2mg/h2mg_2_30**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 13 | **h2mg/h2mg_2_40**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 14 | **h2mg/h2mg_2_50**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 15 | **h2mg/h2mg_2_60**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 16 | **h2mg/h2mg_2_70**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 17 | **h2mg/h2mg_2_80**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 18 | **h2mg/h2mg_2_90**   | 2048  | 2     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 19 | **h2mg/h2mg_4_10**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 20 | **h2mg/h2mg_4_20**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 21 | **h2mg/h2mg_4_30**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 22 | **h2mg/h2mg_4_40**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 23 | **h2mg/h2mg_4_50**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 24 | **h2mg/h2mg_4_60**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 25 | **h2mg/h2mg_4_70**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 26 | **h2mg/h2mg_4_80**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 27 | **h2mg/h2mg_4_90**   | 2048  | 4     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 28 | **h2mg/h2mg_8_10**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 29 | **h2mg/h2mg_8_20**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 30 | **h2mg/h2mg_8_30**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 31 | **h2mg/h2mg_8_40**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 32 | **h2mg/h2mg_8_50**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 33 | **h2mg/h2mg_8_60**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 34 | **h2mg/h2mg_8_70**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 35 | **h2mg/h2mg_8_80**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 36 | **h2mg/h2mg_8_90**   | 2048  | 8     | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 37 | **h2mg/h2mg_16_10**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 38 | **h2mg/h2mg_16_20**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 39 | **h2mg/h2mg_16_30**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 40 | **h2mg/h2mg_16_40**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 41 | **h2mg/h2mg_16_50**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 42 | **h2mg/h2mg_16_60**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 43 | **h2mg/h2mg_16_70**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 44 | **h2mg/h2mg_16_80**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 45 | **h2mg/h2mg_16_90**  | 2048  | 16    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 46 | **h2mg/h2mg_32_10**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 47 | **h2mg/h2mg_32_20**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 48 | **h2mg/h2mg_32_30**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 49 | **h2mg/h2mg_32_40**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 50 | **h2mg/h2mg_32_50**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 51 | **h2mg/h2mg_32_60**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 52 | **h2mg/h2mg_32_70**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 53 | **h2mg/h2mg_32_80**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 54 | **h2mg/h2mg_32_90**  | 2048  | 32    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 55 | **h2mg/h2mg_64_10**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 56 | **h2mg/h2mg_64_20**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 57 | **h2mg/h2mg_64_30**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 58 | **h2mg/h2mg_64_40**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 59 | **h2mg/h2mg_64_50**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 60 | **h2mg/h2mg_64_60**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 61 | **h2mg/h2mg_64_70**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 62 | **h2mg/h2mg_64_80**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 63 | **h2mg/h2mg_64_90**  | 2048  | 64    | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 64 | **h2mg/h2mg_128_10** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 65 | **h2mg/h2mg_128_20** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 66 | **h2mg/h2mg_128_30** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 67 | **h2mg/h2mg_128_40** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 68 | **h2mg/h2mg_128_50** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 69 | **h2mg/h2mg_128_60** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 70 | **h2mg/h2mg_128_70** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 71 | **h2mg/h2mg_128_80** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
| 72 | **h2mg/h2mg_128_90** | 2048  | 128   | labels0            |     2 |              0 |
|    |                      |       |       | labels1            |     2 |              0 |
