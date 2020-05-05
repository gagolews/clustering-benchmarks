#%%silent
#%%restart
#%%cd @

# Copyright (C) 2020, Marek Gagolewski, https://www.gagolewski.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



# "https://github.com/gagolews/clustering_benchmarks_v1"
benchmarks_path = "."
import sys
sys.path.append(benchmarks_path)
from load_dataset import load_dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path, glob, re
from natsort import natsorted
import genieclust
import sklearn.metrics
import seaborn as sns
np.set_printoptions(precision=5, threshold=10, edgeitems=10)
pd.set_option("min_rows", 20)
plt.style.use("seaborn-whitegrid")
#plt.rcParams["figure.figsize"] = (8,4)



res = pd.read_csv("results/v1_wut_none_genieclust.csv")


res_max = res.loc[(res.preprocess=="none") & res.method.isin(["GIc_A0_TC3", "Genie_g0.3"]) &
                  (~res.dataset.str.contains("2mg")),:].\
    groupby(["dataset", "method", "preprocess", "M"]).max().\
    reset_index().drop(["k", "g", "noise", "labels"], axis=1)


res_summary_ar = res_max.groupby(["method", "preprocess", "M"]).ar.\
    mean().sort_values(ascending=False).rename("mean").\
    reset_index()
print(res_summary_ar)

res_summary_ar = res_max.groupby(["method", "preprocess", "M"]).ar.\
    median().sort_values(ascending=False).rename("median").\
    reset_index()
print(res_summary_ar)


#plt.rcParams["figure.figsize"] = (12,4)
#plt.subplot("131")
#sns.boxplot(y="method", x="ar", data=res_max.loc[res_max.preprocess=="none",:], orient="h")
#plt.subplot("132")
#sns.boxplot(y="method", x="ar", data=res_max.loc[res_max.preprocess=="standardise",:], orient="h")
#plt.subplot("133")
#sns.boxplot(y="method", x="ar", data=res_max.loc[res_max.preprocess=="standardise_robust",:], orient="h")

plt.rcParams["figure.figsize"] = (12,8)
sns.boxplot(y="method", x="ar", hue="M", data=res_max, orient="h")
plt.show()


plt.rcParams["figure.figsize"] = (8,6)
res_max2 = res.copy()
res_max2["preprocess_M"] = res_max2.preprocess+"_"+res_max2.M.astype(str)
res_max2 = res_max2.loc[(~res.dataset.str.contains("2mg")),:].\
    groupby(["dataset", "method", "preprocess_M"]).max().\
    reset_index().drop(["k", "g", "noise", "labels"], axis=1)
res_summary_ar2 = res_max2.groupby(["method", "preprocess_M"]).ar.\
    mean().sort_values(ascending=False).rename("mean").unstack()
sns.heatmap(res_summary_ar2, annot=True, fmt=".2f", vmin=0.5, vmax=1.0)
plt.title("Mean ARI")
plt.show()
res_max2 = res.copy()
res_max2["preprocess_M"] = res_max2.preprocess+"_"+res_max2.M.astype(str)
res_max2 = res_max2.\
    groupby(["dataset", "method", "preprocess_M"]).max().\
    reset_index().drop(["k", "g", "noise", "labels"], axis=1)
res_summary_ar2 = res_max2.groupby(["method", "preprocess_M"]).ar.\
    median().sort_values(ascending=False).rename("median").unstack()
sns.heatmap(res_summary_ar2, annot=True, fmt=".2f", vmin=0.5, vmax=1.0)
plt.title("Median ARI")
plt.show()
