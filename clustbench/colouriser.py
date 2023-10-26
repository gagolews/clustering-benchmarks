#!/usr/bin/env python3

"""
Interactive Planar Data Editor

See <https://clustering-benchmarks.gagolewski.com> for more details.
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2018-2023, Marek Gagolewski <https://www.gagolewski.com>      #
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


import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial
import genieclust


##############################################################################
class Colouriser:
    """
    An interactive planar data editor

    See the dedicated section on the package homepage for more details.


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
    >>> data_url = "https://github.com/gagolews/clustering-data-v1/raw/v1.1.0"
    >>> wut_smile = clustbench.load_dataset("wut", "smile", url=data_url)
    >>> clr = clustbench.Colouriser(wut_smile.data, wut_smile.labels[0])
    >>> clr.print_help()
    >>> clr.show()  # starts the interactive mode
    >>> new_data = clr.get_data()
    >>> new_labels = clr.get_labels()
    """

    _modes = ["colourise", "insert", "remove"]


    def __init__(self, data, labels=None):
        self.data = data

        if self.data.ndim != 2 or self.data.shape[1] != 2:
            raise ValueError(
                "Wrong data shape. An n-by-2 matrix should be provided."
            )

        # read labels or set them as missing/noise (represented by 0)
        if labels is None:
            self.labels = np.repeat(0, self.data.shape[0])
        else:
            self.labels = labels

        if len(self.labels) != self.data.shape[0]:
            raise ValueError("Wrong number of labels in the input vector.")


    def _recolour_labels(self, q):
        """
        Changes the state of labels at indices in q to current_colour
        """
        self.labels[q] = self._current_colour


    def _delete_points(self, q):
        """
        Changes the state of labels at indices in q to current_colour
        """
        self.labels = np.delete(self.labels, q, axis=0)
        self.data = np.delete(self.data, q, axis=0)
        self._tree = scipy.spatial.KDTree(self.data)


    def _insert_point(self, xy, r):

        t = np.random.rand()*2*np.pi
        r = np.random.rand()*r
        xy = [[xy[0]+r*np.cos(t), xy[1]+r*np.sin(t)]]
        self.labels = np.append(self.labels, [self._current_colour], axis=0)
        self.data = np.append(self.data, xy, axis=0)
        self._tree = scipy.spatial.KDTree(self.data)


    def _key_press(self, event):
        """
        Keyboard event handler (via matplotlib)
        """
        try:
            # {0,1,...,e} (and f) - set colour
            self._current_colour = int(event.key, 16)
        except: pass

        if event.key in ["+", "=", "-"]:  # set radius
            # why bother with the SHIFT key? → = is +
            if event.key in ["=", "+"]: self._r *= 1.25
            if event.key == "-":        self._r /= 1.25
        elif event.key == "n":             # normalise labels
            self.normalise_labels()
        elif event.key == "z":             # undo last paint
            self.labels, self._undo_labels = self._undo_labels, self.labels
            self.data, self._undo_data = self._undo_data, self.data
            self._tree = scipy.spatial.KDTree(self.data)
        elif event.key == "m":
            self._current_mode = (self._current_mode+1) % len(Colouriser._modes)

        # elif event.key == "t":             # toggle the MSTs view
            # self._show_msts = not self._show_msts

        self._redraw()


    def _mouse_motion(self, event):
        """
        Mouse event handler (via matplotlib)
        """
        if event.button is None and self._undo_started:
            self._undo_started = False
        elif event.button == 1 and not self._undo_started:
            self._undo_labels = self.labels.copy()
            self._undo_data = self.data.copy()
            self._undo_started = True

        if event.inaxes is None:
            self._xy = None
            self._redraw()
            return

        self._xy = np.r_[event.xdata, event.ydata]

        if event.button == 1:
            if self._current_mode == 0:  # colourise
                q = self._tree.query_ball_point(self._xy, self._r)
                self._recolour_labels(q)
            elif self._current_mode == 1:  # insert
                self._insert_point(self._xy, self._r)
            elif self._current_mode == 2:  # delete
                q = self._tree.query_ball_point(self._xy, self._r)
                self._delete_points(q)

        self._redraw()


    def _redraw(self):
        """
        The plotting routine
        """
        if self._xlim is not None: self._xlim = self._ax.get_xlim()
        if self._ylim is not None: self._ylim = self._ax.get_ylim()

        self._ax.clear()

        # if self._show_msts:
        #     pass

        # scatter plots:
        for i in np.unique(self.labels):
            self._ax.scatter(
                self.data[self.labels == i, 0],
                self.data[self.labels == i, 1],
                c=self._col[(i-1) % len(self._col)],
                marker=self._mrk[(i-1) % len(self._mrk)],
                alpha=0.5 if i > 0 else 1.0)

        if self._xlim is None:
            self._xlim = self._ax.get_xlim()
        else:
            self._ax.set_xlim(self._xlim)

        if self._ylim is None:
            self._ylim = self._ax.get_ylim()
        else:
            self._ax.set_ylim(self._ylim)

        self._fig.suptitle(
            "Mode {m}: %s; Radius {+,-}: %5g; Colour {0-9,a-e}: %d\n"
            "Cluster size distribution {n}: %s" % (
                Colouriser._modes[self._current_mode],
                self._r,
                self._current_colour,
                np.bincount(self.labels.tolist())
            )
        )

        if self._xy is not None:
            # draw the "cursor"
            self._ax.add_artist(plt.Circle(
                self._xy, self._r,
                color=self._col[(self._current_colour-1)], alpha=0.4
            ))
        self._fig.canvas.draw()


    def normalise_labels(self):
        """
        Translate the current label vector
        (ignoring colour 0, which denotes the noise cluster)
        so that labels are assigned in decreasing order of occurrence.
        """
        self._undo_labels = self.labels.copy()
        self._undo_started = False

        # order labels>0 w.r.t. decreasing counts; merge=stable sort
        srt = -np.bincount(self.labels[self.labels > 0])[1:]  # decreasing
        srt = np.argsort(srt, kind="mergesort")  # the ordering permutation
        srt = np.argsort(srt, kind="mergesort")  # the inverse permutation
        for i in range(self.data.shape[0]):
            if self.labels[i] > 0:
                self.labels[i] = srt[self.labels[i]-1]+1


    def show(self):
        """
        Start the interactive Colouriser.
        """

        self._tree = scipy.spatial.KDTree(self.data)  # for spatial search
        self._xy = None  # last mouse position; in plot coords

        self._r = max(
            (self.data[:, 0].max()-self.data[:, 0].min()) * 0.1,
            (self.data[:, 1].max()-self.data[:, 1].min()) * 0.1
        )

        self._current_mode = 0

        self._current_colour = 0

        self._show_msts = False  # TODO: future feature

        self._undo_labels = self.labels.copy()
        self._undo_data = self.data.copy()
        self._undo_started = False

        self._fig, self._ax = plt.subplots()
        self._ax.axis("equal")
        self._xlim = None
        self._ylim = None

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
        print("Press {m} to toggle between modes (colourise/insert/delete).")
        print("Press {n} to normalise the cluster labels/size distribution")
        print("    (only affects the non-noise points, i.e., those with ID>0).")
        print("Press {z} to undo/redo the last operation.")
        print("Press {0,1,...,9,a,...,e} to change the current colour.")
        print("Press {+,-} to change the cursor radius.")
