



(sec:how-to-access)=
# Access from Python, R, MATLAB, etc.


## Python

To facilitate the comparison of clustering algorithms in the
Python environment, we have developed a dedicated package
that is available for download from
[PyPI](https://pypi.org/project/clustering-benchmarks/);
see {ref}`sec:clustbench-usage` for more details.

However, as described in the {ref}`sec:file-format` section,
all data files are neat and tidy. Therefore, we can access them
easily using some more low-level functions from *numpy*
or *pandas*. For example:



```python
import numpy as np
import os.path
# to do: change to your local path
base_name = os.path.join("~", "Projects", "clustering-data-v1", "wut", "smile")
base_name = os.path.expanduser(base_name)
data    = np.loadtxt(base_name + ".data.gz", ndmin=2)
data[:6, :]  # preview
## array([[-1.545826,  2.471133],
##        [-5.001664,  1.066568],
##        [-5.434681,  1.333114],
##        [-4.384334,  1.176669],
##        [-3.950311,  6.94172 ],
##        [-4.23157 ,  7.156661]])
labels  = np.loadtxt(base_name + ".labels0.gz", dtype="int")
labels[:6]  # preview
## array([2, 2, 2, 2, 2, 2])
```


External cluster validity measures
discussed in the {ref}`Appendix <sec:external-validity-measures>`
are implemented in the [*genieclust*](https://genieclust.gagolewski.com)
package.


::::{note}
*To learn more about Python,
check out Marek's recent open-access (free!) textbook*
[Minimalist Data Wrangling in Python](https://datawranglingpy.gagolewski.com/)
{cite}`datawranglingpy`.
::::



## R

Following the {ref}`sec:file-format`,
the datasets can be accessed easily using built-in R functions:



```r
# to do: change to your local path
base_name <- file.path("~", "Projects", "clustering-data-v1", "wut", "smile")
data    <- as.matrix(read.table(paste0(base_name, ".data.gz")))
head(data)  # preview
##           V1     V2
## [1,] -1.5458 2.4711
## [2,] -5.0017 1.0666
## [3,] -5.4347 1.3331
## [4,] -4.3843 1.1767
## [5,] -3.9503 6.9417
## [6,] -4.2316 7.1567
labels  <- scan(paste0(base_name, ".labels0.gz"), integer())
head(labels)  # preview
## [1] 2 2 2 2 2 2
```



The {ref}`external cluster validity measures <sec:external-validity-measures>`
are implemented in the R version of the
[*genieclust*](https://genieclust.gagolewski.com) package.


Algorithms implemented in R
can be called from within Python
using, for example, the [*rpy2*](https://pypi.org/project/rpy2/) package.


::::{note}
*To learn more about R, check out Marek's open-access (free!) textbook*
[Deep R Programming](https://deepr.gagolewski.com/)
{cite}`deepr`.
::::




## MATLAB

Unfortunately, MATLAB does not seem to be able to un*gzip* files
on the fly, but these can be decompressed to a temporary folder
manually.


```matlab
base_name = "~/Projects/clustering-data-v1/wut/smile";
t = tempdir();
data = readmatrix(char(gunzip(base_name + ".data.gz", t)), FileType="text");
labels = readmatrix(char(gunzip(base_name + ".labels0.gz", t)), FileType="text");
```

Note that there is also a MATLAB
[interface](https://au.mathworks.com/products/matlab/matlab-and-python.html)
for Python. This way, algorithms that  have only been implemented in the
former can be called from within the latter.

Unfortunately, MATLAB is not free software.



::::{todo}
Contributions are welcome: Describe how to load
the datasets and benchmark results
in GNU Octave, Scilab, Julia, Mathematica, ...
::::
