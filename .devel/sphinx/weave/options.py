# import key packages – required:
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# further settings – optional:
pd.set_option("display.notebook_repr_html", False)  # disable "rich" output

import os
os.environ["COLUMNS"] = "74"  # output width, in characters
np.set_printoptions(linewidth=74)
pd.set_option("display.width", 74)

import sklearn
sklearn.set_config(display="text")

plt.style.use("seaborn-v0_8")  # overall plot style


_colours = [  # the "R4" palette
    "#000000", "#DF536B", "#61D04F", "#2297E6",
    "#28E2E5", "#CD0BBC", "#F5C710", "#999999"
]

_linestyles = [
    "solid", "dashed", "dashdot", "dotted"
]

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    # each plotted line will have a different plotting style
    color=_colours, linestyle=_linestyles*2
)
plt.rcParams["patch.facecolor"] = _colours[0]

np.random.seed(123)  # initialise the pseudorandom number generator

plt.rcParams.update({  # further graphical parameters
    "font.size":         13,
    "font.family":       "sans-serif",
    "font.sans-serif":   ["Alegreya Sans", "Alegreya"],
    "figure.autolayout": True,
    "figure.dpi":        240,
    "figure.figsize":    (5.9375, 3.4635),
})
