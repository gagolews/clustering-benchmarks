



(sec:internal-validity-measures)=
# Side Note: Internal *(In)Validity* Measures




Internal cluster *validity* measures (see, e.g.,
{cite}`Milligan1985:psycho,Maulik2002:cvi_comp,Halkidi2001:cluster_validity,
ArbelaitzEtAl2013:extensive_CVI,XU2020:external_synthetic`)
might aid in selecting the number of clusters a dataset should
be partitioned to. They do not require the presence of expert labels.
Instead, their aim is to quantify different aspects of the obtained
partitions, e.g., the average degree of cluster compactness or point
separability.

Sometimes, internal measures are also used to compare
the outputs of different clustering algorithms on the same dataset
with the intention to determine which one is more *valid*.

However, in {cite}`cvi` (also see the {ref}`sec:results-v1` section),
we have pointed out that **many measures promote some rather random
groupings whilst other ones seem more suitable for...
detecting outliers**.
We should therefore not uncritically deem a high value of, say,
the Silhouette or Davies–Bouldin index *better* than a lower one.


## Notation

For the sake of completeness, let us recall the definitions
of some popular indices. Their implementation is included
in the [*genieclust*](https://genieclust.gagolewski.com/)
package for Python and R {cite}`genieclust`.
Note that this section contains excerpts from {cite}`cvi`.


Let $\mathbf{X}\in\mathbb{R}^{n\times d}$ denote the input dataset
comprised of $n$ points in a $d$-dimensional Euclidean space, with
$\mathbf{x}_i = (x_{i,1},\dots,x_{i,d})$ giving the coordinates of
the $i$-th point, $i\in\{1,2,\dots,n\}$.

A $k$-partition $\{X_1,\dots,X_k\}$ of a set
$\{\mathbf{x}_1, \dots, \mathbf{x}_n\}$
can be encoded by means of a *label vector* $\mathbf{y}$, where
$y_i\in\{1,\dots,k\}$ gives the cluster ID of the $i$-th point.


The measures listed below are based on Euclidean distances between all pairs
of points, $\|\mathbf{x}_i-\mathbf{x}_j\|$, or the input points and some
other pivots, such as their corresponding *cluster centroids*,
$\|\mathbf{x}_i-\boldsymbol\mu_j\|,$ where for $j\in\{1,\dots,k\}$ and $l\in\{1,\dots,d\}$:

$$
\mu_{j,l} = \frac{1}{|X_j|} \sum_{\mathbf{x}_i\in X_j} x_{i,l}.
$$






## Indices Based on Cluster Centroids

### Ball–Hall


The Ball--Hall index {cite}`BallHall1965:isodata` is the within-cluster
sum of squares weighted by the cluster cardinality:

$$\mathrm{BallHall}(\mathbf{y}) = -\sum_{i=1}^n \frac{1}{|X_{y_i}|}
\| \mathbf{x}_i - \boldsymbol\mu_{y_i} \|^2.
$$


Note the minus sign that accounts for the fact that we would rather
have the index maximised.

*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.negated_ball_hall_index`*.



### Caliński–Harabasz


The Caliński–Harabasz index (Eq. (3) in {cite}`CalinskiHarabasz1974:index`;
"variance ratio criterion") is given by:

$$
\mathrm{CalińskiHarabasz}(\mathbf{y}) =
\frac{n-k}{k-1}
\frac{
\sum_{i=1}^n   \| \boldsymbol\mu - \boldsymbol\mu_{y_i} \|^2
}{
\sum_{i=1}^n   \| \mathbf{x}_i - \boldsymbol\mu_{y_i} \|^2
},
$$

where $\boldsymbol\mu$ denotes the centroid of the whole dataset $\mathbf{X}$,
i.e., a vector such that
$\mu_{l} = \frac{1}{n} \sum_{x=1}^n x_{i,l}$ for $l\in\{1,\dots,d\}$.

It may be shown that the task of minimising the (unweighted) within-cluster
sum of squares is equivalent to maximising the Caliński--Harabasz index.
Hence, this index is precisely the objective function in the $k$-means method
{cite}`lloyd` and the algorithms by Ward, Edwards, and Cavalli–Sforza;
see {cite}`Ward1963:hier,EdwardsSforza1965:divisive,CalinskiHarabasz1974:index`.

*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.calinski_harabasz_index`*.



### Davies–Bouldin

The Davies-Bouldin index (Def. 5 in {cite}`DaviesBouldin1979:index`)
is given as the average similarity between each cluster and its most
similar counterpart (note the minus sign again):

$$
\mathrm{DaviesBouldin}(\mathbf{y}) =
-\frac{1}{k}
\sum_{i=1}^k\left(
\max_{j\neq i}
\frac{s_i+s_j}{m_{i,j}}
\right),
$$

where $s_i$ is the dispersion of the $i$-th cluster: if
$|X_i|>1$, it is given by
$s_i=\frac{1}{|X_i|}\sum_{\mathbf{x}_u\in X_i} \|\mathbf{x}_u-\boldsymbol\mu_i\|$
and otherwise we set $s_i=\infty$. Furthermore, $m_{i,j}$ is the
intra-cluster distance, $m_{i,j}=\|\boldsymbol\mu_i-\boldsymbol\mu_j\|$.

On a side note, in {cite}`DaviesBouldin1979:index`, other choices of $s_i$
and $m_{i,j}$ are also suggested. We have recalled only the most popular setting
here (used, e.g., in {cite}`ArbelaitzEtAl2013:extensive_CVI`).

*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.negated_davies_bouldin_index`*.



## Silhouettes

### Silhouette

In Sec. 2 of {cite}`Rousseeuw1987:silhouettes`, Rousseeuw proposed the notion of
a silhouette as a graphical aid in cluster analysis.

Denote the average dissimilarity between the $i$-th point and all other
points in its own cluster by:

$$
a_i = \frac{1}{|X_{y_i}|-1} \sum_{\mathbf{x}_u\in X_{y_i}} \| \mathbf{x}_i-\mathbf{x}_u \|,
$$

and the average dissimilarity between the $i$-th point and all other
entities in the "closest" cluster with:

$$
b_i = \min_{j\neq y_i} \left(
\frac{1}{|X_j|} \sum_{\mathbf{x}_v\in X_{j}} \| \mathbf{x}_i-\mathbf{x}_v \|
\right).
$$

Then the *Silhouette* index is defined as the average
silhouette score:

$$
\mathrm{Silhouette}(\mathbf{y}) = \frac{1}{n}\sum_{i=1}^n \frac{b_i-a_i}{\max\{ a_i, b_i \}},
$$

with convention $\pm\infty/\infty=0$.

*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.silhouette_index`*.


### SilhouetteW


The paper {cite}`Rousseeuw1987:silhouettes` also defines
what we call here the *SilhouetteW* index,
being the mean of the cluster average silhouette widths:

$$
\mathrm{SilhouetteW}(\mathbf{y}) = \frac{1}{k-s}
\sum_{i=1}^n
\frac{1}{|X_{y_i}|}
\frac{b_i-a_i}{\max\{ a_i, b_i \}},
$$

where $s$ is the number of singletons, i.e., clusters of size 1.
Note that *SilhouetteW*, just like *BallHall*, employs
weighting by cluster cardinalities.


*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.silhouette_w_index`*.


## Generalised Dunn Indices

In {cite}`Dunn1974:index` (see Eq. (3) therein),
Dunn proposed an index defined as the
ratio between the smallest between-cluster distance and the largest
cluster diameter.

This index has been generalised by Bezdek and Pal in
{cite}`BezdekPal1998:gdunn` as:

$$
\mathrm{GDunn}(\mathbf{y})=
\frac{
\min_{i\neq j} d\left( X_i, X_j \right)
}{
\max_{i} D\left( X_i \right)
}.
$$

The numerator measures the between-cluster separation whilst the
denominator quantifies the cluster compactness.

The function $d$ can be assumed one of:

-   $d_1(X_i, X_j)=\mathrm{Min}\left(
    \left\{ \|\mathbf{x}_{u}-\mathbf{x}_{v}\|: \mathbf{x}_{u}\in X_i, \mathbf{x}_{v}\in X_j\right\}
    \right)$,

-   $d_2(X_i, X_j)=\mathrm{Max}\left(
    \left\{ \|\mathbf{x}_{u}-\mathbf{x}_{v}\|: \mathbf{x}_{u}\in X_i, \mathbf{x}_{v}\in X_j \right\}
    \right)$,

-   $d_3(X_i, X_j)=\mathrm{Mean}\left(
    \left\{ \|\mathbf{x}_{u}-\mathbf{x}_{v}\|: \mathbf{x}_{u}\in X_i, \mathbf{x}_{v}\in X_j \right\}
    \right)$,

-   $d_4(X_i, X_j)= \|\boldsymbol\mu_i-\boldsymbol\mu_j\|$,

-   $d_5(X_i, X_j)=
    \frac{
    |X_i|\,\mathrm{Mean}\left(
    \left\{ \|\mathbf{x}_{u}-\boldsymbol\mu_i \|: \mathbf{x}_{u}\in X_i\right\}
    \right)
    +
    |X_j|\,\mathrm{Mean}\left(
    \left\{ \|\mathbf{x}_{v}-\boldsymbol\mu_j \|: \mathbf{x}_{v}\in X_j\right\}
    \right)
    }{
    |X_i|+|X_j|
    }$.

Bezdek and Pal in {cite}`Dunn1974:index` also considered a function
based on the Hausdorff metric, but it is overall quite slow to compute.

On the other hand, $D$ can be, for example:

-   $D_1(X_i)=\mathrm{Max}\left(
    \left\{ \|\mathbf{x}_{u}-\mathbf{x}_{v}\|: \mathbf{x}_{u},\mathbf{x}_{v}\in X_i\right\}
    \right)$,

-   $D_2(X_i)=\mathrm{Mean}\left(
    \left\{ \|\mathbf{x}_{u}-\mathbf{x}_{v}\|: \mathbf{x}_{u},\mathbf{x}_{v}\in X_i\right\}
    \right)$,

-   $D_3(X_i)=\mathrm{Mean}\left(
    \left\{ \|\mathbf{x}_{u}-\boldsymbol\mu_i\|: \mathbf{x}_{u}\in X_i\right\}
    \right)$.

There are thus 15 different combinations of the possible numerators and
denominators, hence 15 different indices, which we may denote
by *GDunn_dX_DY*. In particular, *GDunn_d1_D1* gives the original Dunn
{cite}`Dunn1974:index` index.


*Implementation: [`genieclust`](https://genieclust.gagolewski.com/)`.cluster_validity.generalised_dunn_index`*.

