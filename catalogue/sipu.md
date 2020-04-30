**[Benchmark Suite for Clustering Algorithms -- Version 1](https://github.com/gagolews/clustering_benchmarks_v1)
is maintained by [Marek Gagolewski](http://www.gagolewski.com)**


--------------------------------------------------------------------------------

**Datasets**

* [sipu/a1](#sipu_a1)
* [sipu/a2](#sipu_a2)
* [sipu/a3](#sipu_a3)
* [sipu/aggregation](#sipu_aggregation)
* [sipu/birch1](#sipu_birch1)
* [sipu/birch2](#sipu_birch2)
* [sipu/compound](#sipu_compound)
* [sipu/d31](#sipu_d31)
* [sipu/flame](#sipu_flame)
* [sipu/jain](#sipu_jain)
* [sipu/pathbased](#sipu_pathbased)
* [sipu/r15](#sipu_r15)
* [sipu/s1](#sipu_s1)
* [sipu/s2](#sipu_s2)
* [sipu/s3](#sipu_s3)
* [sipu/s4](#sipu_s4)
* [sipu/spiral](#sipu_spiral)
* [sipu/unbalance](#sipu_unbalance)
* [sipu/worms_2](#sipu_worms_2)
* [sipu/worms_64](#sipu_worms_64)

--------------------------------------------------------------------------------

## sipu/a1 (n=3000, d=2) <a name="sipu_a1"></a>

    Source: I. Kärkkäinen, P. Fränti, Dynamic local search algorithm
    for the clustering problem, Research Report A-2002-6.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with varying number of vectors and clusters.
    There are 150 vectors per cluster.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=20, noise=    0, true_g=0.000

label_counts=[150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]

![](sipu/a1.labels0.png)




## sipu/a2 (n=5250, d=2) <a name="sipu_a2"></a>

    Source: I. Kärkkäinen, P. Fränti, Dynamic local search algorithm
    for the clustering problem, Research Report A-2002-6.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with varying number of vectors and clusters.
    There are 150 vectors per cluster.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=35, noise=    0, true_g=0.000

label_counts=[150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]

![](sipu/a2.labels0.png)




## sipu/a3 (n=7500, d=2) <a name="sipu_a3"></a>

    Source: I. Kärkkäinen, P. Fränti, Dynamic local search algorithm
    for the clustering problem, Research Report A-2002-6.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with varying number of vectors and clusters.
    There are 150 vectors per cluster.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=50, noise=    0, true_g=0.000

label_counts=[150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]

![](sipu/a3.labels0.png)




## sipu/aggregation (n=788, d=2) <a name="sipu_aggregation"></a>

    Source: A. Gionis, H. Mannila, P. Tsaparas, Clustering aggregation,
    ACM Transactions on Knowledge Discovery from Data (TKDD), 2007, pp. 1-30.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 7, noise=    0, true_g=0.454

label_counts=[273, 170, 130, 102, 45, 34, 34]

![](sipu/aggregation.labels0.png)




## sipu/birch1 (n=100000, d=2) <a name="sipu_birch1"></a>

    Source: Zhang et al., BIRCH: A new data clustering algorithm and its applications,
    Data Mining and Knowledge Discovery, 1 (2), 141-182, 1997.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=100, noise=    0, true_g=0.008

label_counts=[1011, 982, 998, 1013, 1002, 982, 1023, 999, 999, 992, 1001, 1007, 980, 997, 998, 1007, 990, 989, 1028, 989, 993, 1002, 998, 1034, 1016, 979, 1005, 994, 992, 1019, 998, 991, 1007, 973, 996, 999, 994, 988, 1002, 981, 1022, 993, 991, 1019, 996, 1021, 991, 1009, 1009, 998, 995, 1000, 1017, 981, 1012, 998, 1001, 1002, 987, 1005, 1005, 975, 1024, 992, 992, 996, 1013, 972, 1016, 993, 1018, 993, 980, 999, 1011, 1007, 983, 998, 1017, 1001, 986, 1017, 1003, 1022, 1012, 1004, 1018, 1025, 1002, 988, 993, 1003, 996, 991, 995, 983, 1003, 975, 1014, 990]

![](sipu/birch1.labels0.png)




## sipu/birch2 (n=100000, d=2) <a name="sipu_birch2"></a>

    Source: Zhang et al., BIRCH: A new data clustering algorithm and its applications,
    Data Mining and Knowledge Discovery, 1 (2), 141-182, 1997.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=100, noise=    0, true_g=0.000

label_counts=[1000, 1000, 1000, 1000, 1002, 997, 999, 1002, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 999, 1000, 1000, 1000, 1001, 999, 1001, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1001, 999, 999, 1001, 1000, 1000, 1000, 1000, 1000, 1000, 1001, 1000, 998, 1002, 1001, 998, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1001, 998, 1001, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 999, 999, 1004, 999, 1000, 999, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1001, 997, 1002, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1001, 997, 1002, 1000, 1000, 1000, 1000, 1000, 1000]

![](sipu/birch2.labels0.png)




## sipu/compound (n=399, d=2) <a name="sipu_compound"></a>

    Source: C.T. Zahn, Graph-theoretical methods for detecting and describing
    gestalt clusters, IEEE Transactions on Computers C-20(1), 1971, pp. 68-86.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    `labels1`--`labels4` generated by A. Cena and M. Gagolewski.
    `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 6, noise=    0, true_g=0.440

label_counts=[158, 92, 50, 45, 38, 16]

![](sipu/compound.labels0.png)

#### `labels1`

true_k= 4, noise=    0, true_g=0.405

label_counts=[158, 142, 83, 16]

![](sipu/compound.labels1.png)

#### `labels2`

true_k= 5, noise=   50, true_g=0.483

label_counts=[158, 92, 44, 39, 16]

![](sipu/compound.labels2.png)

#### `labels3`

true_k= 4, noise=   50, true_g=0.415

label_counts=[158, 92, 83, 16]

![](sipu/compound.labels3.png)

#### `labels4`

true_k= 5, noise=    0, true_g=0.485

label_counts=[158, 142, 44, 39, 16]

![](sipu/compound.labels4.png)




## sipu/d31 (n=3100, d=2) <a name="sipu_d31"></a>

    Source: C.J. Veenman, M.J.T. Reinders, E. Backer, A maximum variance cluster
    algorithm, IEEE Transactions on Pattern Analysis and Machine Intelligence 24(9),
    2002, pp. 1273-1280.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    


#### `labels0`

true_k=31, noise=    0, true_g=0.000

label_counts=[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

![](sipu/d31.labels0.png)




## sipu/flame (n=240, d=2) <a name="sipu_flame"></a>

    Source: L. Fu, E. Medico, FLAME, a novel fuzzy clustering method for
    the analysis of DNA microarray data, BMC Bioinformatics 8, 2007, p. 3.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    `labels1` generated by A. Cena and M. Gagolewski.
    `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 2, noise=    0, true_g=0.275

label_counts=[153, 87]

![](sipu/flame.labels0.png)

#### `labels1`

true_k= 2, noise=   12, true_g=0.272

label_counts=[145, 83]

![](sipu/flame.labels1.png)




## sipu/jain (n=373, d=2) <a name="sipu_jain"></a>

    Source: A. Jain, M. Law, Data clustering: A user’s dilemma,
    Lecture Notes in Computer Science 3776, 2005, pp. 1-10.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 2, noise=    0, true_g=0.480

label_counts=[276, 97]

![](sipu/jain.labels0.png)




## sipu/pathbased (n=300, d=2) <a name="sipu_pathbased"></a>

    Source: H. Chang, D.Y. Yeung, Robust path-based spectral clustering,
    Pattern Recognition 41(1), 2008, pp. 191-203.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    `labels1` generated by M. Gagolewski.
    `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 3, noise=    0, true_g=0.057

label_counts=[110, 97, 93]

![](sipu/pathbased.labels0.png)

#### `labels1`

true_k= 4, noise=    0, true_g=0.196

label_counts=[98, 94, 56, 52]

![](sipu/pathbased.labels1.png)




## sipu/r15 (n=600, d=2) <a name="sipu_r15"></a>

    Source: C.J. Veenman, M.J.T. Reinders, E. Backer, A maximum variance cluster
    algorithm, IEEE Transactions on Pattern Analysis and Machine Intelligence 24(9),
    2002, pp. 1273-1280.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    `labels1`, `labels2` generated by A. Cena and M. Gagolewski.
    `0` denotes the noise class (if present).
    


#### `labels0`

true_k=15, noise=    0, true_g=0.000

label_counts=[40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]

![](sipu/r15.labels0.png)

#### `labels1`

true_k= 9, noise=    0, true_g=0.400

label_counts=[280, 40, 40, 40, 40, 40, 40, 40, 40]

![](sipu/r15.labels1.png)

#### `labels2`

true_k= 8, noise=    0, true_g=0.467

label_counts=[320, 40, 40, 40, 40, 40, 40, 40]

![](sipu/r15.labels2.png)




## sipu/s1 (n=5000, d=2) <a name="sipu_s1"></a>

    Source: P. Fränti, O. Virmajoki,
    Iterative shrinking method for clustering problems,
    Pattern Recognition, 39(5), 2006, pp. 761-765.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with n=5000 vectors and K=15 Gaussian clusters with different
    degree of cluster overlapping.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=15, noise=    0, true_g=0.028

label_counts=[300, 316, 314, 318, 325, 326, 334, 338, 341, 342, 347, 349, 350, 350, 350]

![](sipu/s1.labels0.png)




## sipu/s2 (n=5000, d=2) <a name="sipu_s2"></a>

    Source: P. Fränti, O. Virmajoki,
    Iterative shrinking method for clustering problems,
    Pattern Recognition, 39(5), 2006, pp. 761-765.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with n=5000 vectors and K=15 Gaussian clusters with different
    degree of cluster overlapping.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=15, noise=    0, true_g=0.027

label_counts=[300, 317, 315, 320, 321, 329, 334, 333, 340, 345, 346, 350, 350, 350, 350]

![](sipu/s2.labels0.png)




## sipu/s3 (n=5000, d=2) <a name="sipu_s3"></a>

    Source: P. Fränti, O. Virmajoki,
    Iterative shrinking method for clustering problems,
    Pattern Recognition, 39(5), 2006, pp. 761-765.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with n=5000 vectors and K=15 Gaussian clusters with different
    degree of cluster overlapping.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=15, noise=    0, true_g=0.026

label_counts=[300, 321, 316, 323, 322, 331, 333, 337, 334, 337, 346, 350, 350, 350, 350]

![](sipu/s3.labels0.png)




## sipu/s4 (n=5000, d=2) <a name="sipu_s4"></a>

    Source: P. Fränti, O. Virmajoki,
    Iterative shrinking method for clustering problems,
    Pattern Recognition, 39(5), 2006, pp. 761-765.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    Synthetic 2D data with n=5000 vectors and K=15 Gaussian clusters with different
    degree of cluster overlapping.
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k=15, noise=    0, true_g=0.026

label_counts=[300, 316, 327, 320, 323, 324, 327, 336, 337, 344, 347, 350, 349, 350, 350]

![](sipu/s4.labels0.png)




## sipu/spiral (n=312, d=2) <a name="sipu_spiral"></a>

    Source: H. Chang, D.Y. Yeung, Robust path-based spectral clustering,
    Pattern Recognition 41(1), 2008, pp. 191-203.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 3, noise=    0, true_g=0.016

label_counts=[101, 105, 106]

![](sipu/spiral.labels0.png)




## sipu/unbalance (n=6500, d=2) <a name="sipu_unbalance"></a>

    Source: M. Rezaei, P. Fränti, Set-matching methods for external cluster
    validity, IEEE Trans. on Knowledge and Data Engineering, 28(8), pp. 2173-2186, 2016.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors. `0` denotes the noise class (if present).
    


#### `labels0`

true_k= 8, noise=    0, true_g=0.626

label_counts=[2000, 2000, 2000, 100, 100, 100, 100, 100]

![](sipu/unbalance.labels0.png)




## sipu/worms_2 (n=105600, d=2) <a name="sipu_worms_2"></a>

    Synthetic 2D data with worm-like shapes
    
    Source: S. Sieranoja and P. Fränti,
    Fast and general density peaks clustering,
    Pattern Recognition Letters, 128, 551-558, 2019.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    


#### `labels0`

true_k=35, noise=    0, true_g=0.283

label_counts=[3120, 4560, 4368, 4008, 3648, 3144, 1992, 1008, 4464, 936, 2904, 1296, 2496, 2328, 4968, 5880, 3696, 4896, 2160, 2160, 3048, 5640, 1752, 1176, 4968, 4920, 768, 2472, 1392, 1752, 3840, 2664, 840, 3336, 3000]

![](sipu/worms_2.labels0.png)




## sipu/worms_64 (n=105000, d=64) <a name="sipu_worms_64"></a>

    Synthetic 64D data with worm-like shapes
    
    Source: S. Sieranoja and P. Fränti,
    Fast and general density peaks clustering,
    Pattern Recognition Letters, 128, 551-558, 2019.
    
    Web: https://cs.joensuu.fi/sipu/datasets/
    
    `labels0` come from the Authors.
    


#### `labels0`

true_k=25, noise=    0, true_g=0.000

label_counts=[4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200]

> **(preview generation suppressed)**





