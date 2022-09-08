#!/usr/bin/env python3

"""
Interactive Planar Data Editor

A standalone console app using clustbench.Colouriser

Be careful: input files will be overwritten!

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

import sys, os.path
import numpy as np
import clustbench


###############################################################################
# the app

if __name__ == "__main__":
    ###########################################################################
    # read input data

    print("""\
Colouriser: Interactive Planar Data Editor
Copyright (C) 2018-2022 Marek Gagolewski <https://www.gagolewski.com>
This program is free software licensed under the GNU GPL v3 or later.
See <https://clustering-benchmarks.gagolewski.com> for more details.

Be careful: input files will be overwritten!
    """)

    if len(sys.argv) != 3:
        sys.exit("Usage: %s data_file labels_file" % sys.argv[0])

    data_file = sys.argv[1]
    if not os.path.isfile(data_file):
        sys.exit("File %s does not exist." % data_file)

    # read data matrix
    data = np.loadtxt(data_file, ndmin=2)

    labels_file = sys.argv[2]
    if not os.path.isfile(labels_file):
        labels = None
    else:
        labels = np.loadtxt(labels_file, dtype='int')

    # --------------------------------------------------------------------------
    clr = clustbench.Colouriser(data, labels)
    clr.print_help()
    clr.show()
    # --------------------------------------------------------------------------

    np.savetxt(data_file, clr.get_data(), fmt="%g")
    print("File %s saved." % data_file)

    np.savetxt(labels_file, clr.get_labels(), fmt="%d")
    print("File %s saved." % labels_file)

