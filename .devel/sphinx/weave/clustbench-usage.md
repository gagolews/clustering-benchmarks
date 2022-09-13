



(sec:clustbench-usage)=
# Using *clustbench*

::::{epigraph}
*To learn more about Python,
check out Marek's recent open-access (free!) textbook*
[Minimalist Data Wrangling in Python](https://datawranglingpy.gagolewski.com/)
{cite}`datawranglingpy`.
::::

TO DO...

install..



```python
import clustbench
# load from a local library (download the suite manually)
import os.path
data_path = os.path.join("~", "Projects", "clustering-data-v1")
print(clustbench.get_battery_names(path=data_path))
## ['fcps', 'g2mg', 'graves', 'h2mg', 'mnist', 'other', 'sipu', 'uci', 'wut']
battery = "wut"
clustbench.get_dataset_names(battery, path=data_path)
## ['circles', 'cross', 'graph', 'isolation', 'labirynth', 'mk1', 'mk2', 'mk3', 'mk4', 'olympic', 'smile', 'stripes', 'trajectories', 'trapped_lovers', 'twosplashes', 'windows', 'x1', 'x2', 'x3', 'z1', 'z2', 'z3']
dataset = "x2"
b = clustbench.load_dataset(battery, dataset, path=data_path)
print(b.battery, b.dataset, sep="/")
## wut/x2
print(b.description)
## Author: Eliza Kaczorek (Warsaw University of Technology)
## 
## `labels0` come from the Author herself.
## `0` denotes the noise class (if present).
print(b.data.shape, len(b.labels), [max(l) for l in b.labels])
## (120, 2) 1 [3]
import genieclust
genieclust.plots.plot_scatter(b.data, labels=b.labels[0], axis="equal")
plt.show()
```

(fig:using-clustbench-example1)=
```{figure} clustbench-usage-figures/using-clustbench-example1-1.*
An example benchmark dataset and the corresponding ground truth labels.
```

