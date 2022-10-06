"""
clustering-benchmarks Package
"""


# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2020-2022, Marek Gagolewski <https://www.gagolewski.com>      #
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


import os.path
import os
import glob
from natsort import natsorted


def get_dataset_names(battery, path=None, expanduser=True, expandvars=True):
    """
    Get the names of datasets in a given benchmark battery


    Parameters
    ----------

    battery
        Name of the battery, e.g., ``"wut"`` or ``"other"``.
        Can be an empty string or ``"."`` if all files are
        in a single directory as specified by `path`.

    path
        Path to the directory containing the downloaded benchmark dataset
        suite. Defaults to the current working directory.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Returns
    -------

    datasets
        A list of strings.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> print(clustbench.get_battery_names(data_path))
    >>> print(clustbench.get_dataset_names("wut", data_path))
    """
    if path is None: path = "."

    if expanduser: path = os.path.expanduser(path)
    if expandvars: path = os.path.expandvars(path)

    if not os.path.isdir(os.path.join(path, battery)):
        raise ValueError("battery does not exist")

    # (#3): root_dir in glob.glob is Python >= 3.10
    # was: glob.glob("*.data.gz", root_dir=os.path.join(path, battery)
    datasets = natsorted([
        os.path.basename(f)[:-len(".data.gz")]
        for f in glob.glob(os.path.join(path, battery, "*.data.gz"))
    ])

    datasets = [dataset for dataset in datasets if not dataset.startswith(".")]

    return datasets


def get_battery_names(path=None, expanduser=True, expandvars=True):
    """
    Get the names of benchmark batteries in a given directory


    Parameters
    ----------

    path
        Path to the directory containing the downloaded benchmark dataset
        suite. Defaults to the current working directory.

    expanduser
        Whether to call ``os.path.expanduser`` on the file path.

    expandvars
        Whether to call ``os.path.expandvars`` on the file path.


    Returns
    -------

    batteries
        A list of strings.


    Examples
    --------

    >>> import os.path
    >>> import clustbench
    >>> data_path = os.path.join("~", "Projects", "clustering-data-v1")  # up to you
    >>> print(clustbench.get_battery_names(data_path))
    >>> print(clustbench.get_dataset_names("wut", data_path))
    """
    if path is None: path = "."

    if expanduser: path = os.path.expanduser(path)
    if expandvars: path = os.path.expandvars(path)


    # (#3): root_dir in glob.glob is Python >= 3.10
    # was: glob.glob(os.path.join("*", "README.txt"), root_dir=path)
    batteries = natsorted([
        os.path.basename(os.path.dirname(f))
        for f in glob.glob(os.path.join(path, "*", "README.txt"))
    ])

    batteries = [battery for battery in batteries if not battery.startswith(".")]

    return batteries
