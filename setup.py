"""
clustering-benchmarks Package
"""

# ############################################################################ #
#                                                                              #
#   Copyleft (C) 2015-2022, Marek Gagolewski <https://www.gagolewski.com>      #
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


import setuptools
import os.path
import glob
import os
import sys


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clustering-benchmarks",
    packages=["clustbench"],
    #packages=setuptools.find_packages(),
    version="1.1.0",  # see also clustbench/__init__.py; e.g., 1.0.0.9001
    description="A Framework for Benchmarking Clustering Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marek Gagolewski",
    author_email="marek@gagolewski.com",
    maintainer="Marek Gagolewski",
    license="GNU Affero General Public License v3",
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pandas",
        "genieclust",
      ],
    download_url="https://github.com/gagolews/clustering-benchmarks",
    url="https://clustering-benchmarks.gagolewski.com/",
    project_urls={
        "Bug Tracker":   "https://github.com/gagolews/clustering-benchmarks/issues",
        "Documentation": "https://clustering-benchmarks.gagolewski.com/",
        "Source Code":   "https://github.com/gagolews/clustering-benchmarks",
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering",
    ],
)
