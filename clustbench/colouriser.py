#!/usr/bin/env python3

"""
Interactive Planar Data Editor

See <https://clustering-benchmarks.gagolewski.com> for more details.
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2018-2022, Marek Gagolewski <https://www.gagolewski.com>      #
#                                                                              #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU Affero General Public License                #
#   Version 3, 19 November 2007, published by the Free Software Foundation.    #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the               #
#   GNU Affero General Public License Version 3 for more details.              #
#   You should have received a copy of the License along with this program.    #
#   If this is not the case, refer to <https://www.gnu.org/licenses/>.         #
#                                                                              #
# ############################################################################ #


# TODO: redraw only locally
# TODO: MSTs for each cluster, computed on-state-change only
# TODO: add new points to the dataset interactively


import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial
import genieclust

##############################################################################
class Colouriser:
    """
    Interactive planar data editor


    Parameters
    ----------

    data
        An `n`-by-2 real matrix giving the coordinates of `n` planar points.

    labels
        Either a vector of `n` corresponding integer labels or ``None``.


    Attributes
    ----------

    data
        The data matrix.

    labels
        A vector of `n` integer labels;
        0 denotes the noise cluster



    Examples
    --------

    >>> import clustbench
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> benchmark = clustbench.load_dataset("wut", "x2", data_path)
    >>> clr = clustbench.Colouriser(benchmark.data, benchmark.labels[0])
    >>> clr.print_help()
    >>> clr.show()  # starts the interactive mode
    >>> new_data = clr.get_data()
    >>> new_labels = clr.get_labels()
    """

    def __init__(self, data, labels=None):
        self.data = data
        self._n = self.data.shape[0]
        if self._n <= 1 or self.data.shape[1] != 2:
            raise ValueError(
                "Wrong data shape. An n-by-2 matrix should be provided."
            )

        # read labels or set them as missing/noise (represented by 0)
        if labels is None:
            self.labels = np.repeat(0, self._n)
        else:
            self.labels = labels

        if len(self.labels) != self._n:
            raise ValueError("Wrong number of labels in the input vector.")


    def _recolour_labels(self, q):
        """
        Changes the state of labels at indices in q to current_colour
        """
        num_q = len(q)
        num_q_new = np.sum(self.labels[q] != self._current_colour)
        self.labels[q] = self._current_colour
        #print(
        #    "%6d selected, %6d changed; "
        #    "colour distribution = %s." % (
        #        num_q, num_q_new,
        #        np.bincount(self.labels.tolist())
        #    ))


    def _key_press(self, event):
        """
        Keyboard event handler (via matplotlib)
        """
        try:
            self._current_colour = int(event.key, 16)   # {0,1,...,e} (and f) - set colour
            #print("Current colour: %2d" % self._current_colour)
        except: pass

        if event.key in ["+", "=", "-"]: # set radius
            # why bother with the SHIFT key? → = is +
            if event.key in ["=", "+"]: self.r *= 1.25
            if event.key == "-":        self.r /= 1.25
            #print("Current radius: %5g." % self.r)

        if event.key == "n":             # normalise labels
            self._normalise_labels()

        if event.key == "z":             # undo last paint
            self.labels, self._undo_labels = self._undo_labels, self.labels
            #print("Last brush stroke undone, %6d changed; "
            #"colour distribution = %s." % (
            #    np.sum(self.labels != self._undo_labels),
            #    np.bincount(self.labels.tolist())
            #    ))

        #if event.key == "m":             # toggle the MSTs view
            #self._show_msts = not self._show_msts

        #sys.stdout.flush()
        self._redraw()


    def _mouse_motion(self, event):
        """
        Mouse event handler (via matplotlib)
        """
        if event.button is None and self._undo_started:
            self._undo_started = False
        elif event.button == 1 and not self._undo_started:
            self._undo_labels = self.labels.copy()
            self._undo_started = True

        if event.inaxes is None:
            self.xy = None
            self._redraw()
            return
        self.xy = np.r_[event.xdata, event.ydata]

        if event.button == 1:
            q = self.tree.query_ball_point(self.xy, self.r)
            self._recolour_labels(q)

        self._redraw()


    def _redraw(self):
        """
        The plotting routine
        """
        self._ax.clear()

        #if self._show_msts:
            #pass

        # scatter plots:
        for i in np.unique(self.labels):
            self._ax.scatter(
                self.data[self.labels==i, 0],
                self.data[self.labels==i, 1],
                c=self._col[(i-1) % len(self._col)],
                marker=self._mrk[(i-1) % len(self._mrk)],
                alpha=0.5 if i>0 else 1.0)

        if self.xy is not None:
            # draw the "cursor"
            self._ax.add_artist(plt.Circle(self.xy, self.r,
                color=self._col[(self._current_colour-1)], alpha=0.4))
        self._fig.canvas.draw()

        self._fig.suptitle(
            "Current radius: %5g; Colour: %d\nCluster size distribution: %s" % (
                self.r,
                self._current_colour,
                np.bincount(self.labels.tolist())
        ))


    def normalise_labels(self):
        """
        Translate the current label vector
        (ignoring colour 0, which denotes the noise cluster)
        so that labels are assigned in decreasing order of occurrence.
        """
        self._undo_labels = self.labels.copy()
        self._undo_started = False

        # order labels>0 w.r.t. decreasing counts; merge=stable sort
        srt = -np.bincount(self.labels[self.labels>0])[1:]  # decreasing
        srt = np.argsort(srt, kind="mergesort")  # the ordering permutation
        srt = np.argsort(srt, kind="mergesort")  # the inverse permutation
        for i in range(self._n):
            if self.labels[i] > 0:
                self.labels[i] = srt[self.labels[i]-1]+1

        #print("New colour distribution = %r." % (
        #    np.bincount(self.labels.tolist()),
        #))


    def show(self):
        """
        Start the interactive colouriser app.
        """

        self.tree = scipy.spatial.KDTree(self.data) # spatial search data struct
        self.xy = None                     # last mouse position; in plot coords

        self.r = (self.data.max()-self.data.min())*0.1

        self._current_colour = 0

        self._show_msts = False  # TODO: future feature

        self._undo_labels = self.labels.copy()
        self._undo_started = False

        self._fig, self._ax = plt.subplots()
        self._ax.axis("equal")

        #xmin = self.data[:,0].min()
        #xmax = self.data[:,0].max()
        #ymin = self.data[:,1].min()
        #ymax = self.data[:,1].max()
        #self._ax.set_xlim(xmin, xmax)
        #self._ax.set_ylim(ymin, ymax)

        plt.get_current_fig_manager().set_window_title(
            "Colouriser: Interactive Planar Data Editor"
        )

        self._col = genieclust.plots.col
        self._mrk = genieclust.plots.mrk
        self._fig.canvas.mpl_connect("key_press_event", self._key_press)
        self._fig.canvas.mpl_connect("motion_notify_event", self._mouse_motion)
        self._fig.canvas.mpl_connect("button_press_event", self._mouse_motion)

        self._redraw()

        plt.show()


    def get_labels(self):
        """
        Get the current labels.


        Returns
        -------

        labels
        """
        return self.labels


    def get_data(self):
        """
        Get the current data matrix.


        Returns
        -------

        data
        """
        return self.data


    def print_help(self):
        """
        List the keyboard shortcuts available.
        """
        print("Press {n} to normalise the cluster labels/size distribution")
        print("    (only affects the non-noise points, i.e., those with ID>0).")
        #print("Press {m} to toggle the MST (minimum spanning trees) view.")
        print("Press {z} to undo/redo the last brush stroke or label normalisation.")
        print("Press {0,1,...,9,a,...,e} to change the current colour.")
        print("Press {+,-} to change the radius.")
