



# Side Note: Cluster *(In)Validity* Measures




Cluster *validity* measures (see, e.g.,
{cite}`Milligan1985:psycho,Maulik2002:cvi_comp,Halkidi2001:cluster_validity,
ArbelaitzEtAl2013:extensive_CVI,XU2020:external_synthetic`)
are sometimes used to compare the outputs of different clustering algorithms
on the same dataset.

However, in {cite}`cvi`
(see [preprint](https://github.com/gagolews/bibliography/raw/master/preprints/2021cvi.pdf))
we have pointed out that **many measures
promote rather random groupings while other ones work better
as... outlier detectors**.

We should therefore not deem a high value of, say,
the Silhouette or Davies–Bouldin index *better* than a lower one,
at least not uncritically.

Overall, **we do not recommend relying on cluster *validity* measures
to judge whether a partition is meaningful or not**.



## Notation

Still, for the sake of completeness, let us recall the definitions
of some of the more popular indices. Their implementation is included
in the [*genieclust*](https://genieclust.gagolewski.com/) package for Python
and R {cite}`genieclust`.
Note that this section contains excerpts from our paper {cite}`cvi`.


Let $\mathbf{X}\in\mathbb{R}^{n\times d}$ denote the input dataset
comprised of $n$ points in a $d$-dimensional Euclidean space, with
$\mathbf{x}_i = (x_{i,1},\dots,x_{i,d})$ giving the coordinates of
the $i$-th point, $i\in[1:n]=\{1,2,\dots,n\}$.

A $k$-partition $\{X_1,\dots,X_k\}$ of a set
$\{\mathbf{x}_1, \dots, \mathbf{x}_n\}$
can be encoded by means of a *label vector*[^footsurj] $\mathbf{y}$, where
$y_i\in[1:k]$ gives the cluster number of the $i$-th point.

[^footsurj]: More precisely, a surjection $[1:n]\stackrel{\text{onto}}{\to}[1:k]$.


The measures listed below are based on Euclidean distances between all pairs
of points, $\|\mathbf{x}_i-\mathbf{x}_j\|$, or the input points and some
other pivots, such as their corresponding *cluster centroids*,
$\|\mathbf{x}_i-\boldsymbol\mu_j\|,$ where for $j\in[1:k]$ and $l\in[1:d]$:

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

*Implementation: [`genieclust.cluster_validity.negated_ball_hall_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*



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
$\mu_{l} = \frac{1}{n} \sum_{x=1}^n x_{i,l}$ for $l\in[1:d]$.

It may be shown that the task of minimising the (unweighted) within-cluster
sum of squares is equivalent to maximising the Caliński--Harabasz index.
Hence, this index is precisely the objective function in the $k$-means method
{cite}`lloyd` and the algorithms by Ward, Edwards, and Cavalli–Sforza;
see {cite}`Ward1963:hier,EdwardsSforza1965:divisive,CalinskiHarabasz1974:index`.

*Implementation: [`genieclust.cluster_validity.calinski_harabasz_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*



### Davies–Bouldin

The Davies-Bouldin (Def. 5 in {cite}`DaviesBouldin1979:index`)
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

*Implementation: [`genieclust.cluster_validity.negated_davies_bouldin_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*



## Silhouettes

### Silhouette

In Sec. 2 of {cite}`Rousseeuw1987:silhouettes`, Rousseeuw proposes the notion of
a silhouette as a graphical aid in cluster analysis.

Denote the average dissimilarity between the $i$-th point and all other
points in its own cluster with:

$$
a_i = \frac{1}{|X_{y_i}|-1} \sum_{\mathbf{x}_u\in X_{y_i}} \| \mathbf{x}_i-\mathbf{x}_u \|
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

*Implementation: [`genieclust.cluster_validity.silhouette_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*


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


*Implementation: [`genieclust.cluster_validity.silhouette_w_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*


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

Function $d$ can be assumed one of:

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
as *GDunn_dX_DY*. In particular, *GDunn_d1_D1* gives the original Dunn
{cite}`Dunn1974:index` index.


*Implementation: [`genieclust.cluster_validity.generalised_dunn_index`](https://genieclust.gagolewski.com/genieclust_cluster_validity.html)*

