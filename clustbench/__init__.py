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

# version string, e.g., "1.0.0.9001" or "1.1.1"
__version__ = "1.1.1"


from .get_names import get_dataset_names, get_battery_names
from .load_dataset import load_dataset, save_data, save_labels
from .load_results import load_results, save_results
from .load_results import transpose_results, labels_list_to_dict
from .preprocess_data import preprocess_data
from .colouriser import Colouriser
from .fit_predict import fit_predict_many
from .score import get_score
