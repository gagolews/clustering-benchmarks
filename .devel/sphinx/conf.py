# Copyleft (C) 2020-2022, Marek Gagolewski <https://www.gagolewski.com>
# Configuration file for the Sphinx documentation builder.

#import sys
#import os
#import sphinx
#import matplotlib.sphinxext
#import IPython.sphinxext
import sphinx_rtd_theme
import clustbench

# -- Project information -----------------------------------------------------

copyright_year = '2020–2022'
author = 'Marek Gagolewski'

pkg_name = "clustbench"
pkg_title = 'Clustering Benchmarks'
pkg_version = clustbench.__version__

print("This is %s %s by %s.\n" % (pkg_title, pkg_version, author))


github_url = "https://github.com/gagolews/clustering-benchmarks/"
html_baseurl = "https://clustering-benchmarks.gagolewski.com/"
github_star_repo = "gagolews/clustering-benchmarks"  # or None to disable
analytics_id = None  # "d2cambjfe3"  # https://clarity.microsoft.com
copyright = f"{copyright_year}"
html_title = f"{pkg_title} by {author}"
html_short_title = f"{pkg_title}"

pygments_style = 'default'  #'trac' - 'default' is more readable for some
project = f'{pkg_title} [{pkg_version}]'
version = f'by {author}'
release = f'[{pkg_version}]'

nitpicky = True
smartquotes = True
today_fmt = "%Y-%m-%dT%H:%M:%S%Z"
highlight_language = "python"
html_last_updated_fmt = today_fmt


extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    #'sphinxcontrib.proof',
    'sphinx_multitoc_numbering',
    'sphinx_rtd_theme',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'numpydoc'
    #'sphinx.ext.viewcode',
    #'sphinx.ext.imgmath',
    # 'sphinx.ext.napoleon',
]

myst_enable_extensions = [
    "deflist",
    "colon_fence",
    "dollarmath",
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

todo_include_todos = True

source_suffix = ['.md', '.rst']

numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s'
}
numfig_secnum_depth = 1


plot_include_source = True
plot_html_show_source_link = False
plot_pre_code = """
import numpy as np
import clustbench
np.random.seed(123)
"""

doctest_global_setup = plot_pre_code

numpydoc_use_plots = True



# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
autosummary_imported_members = True
autosummary_generate = True


html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'prev_next_buttons_location': 'both',
    'sticky_navigation': True,
    'display_version': True,
    'style_external_links': True,
    'vcs_pageview_mode': github_star_repo,
    'analytics_id': analytics_id,
    #'display_github': "blob",
    #'style_nav_header_background': '#ff704d',
}

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sourcelink = False

html_static_path = ['_static']
html_css_files = ['css/custom.css']



bibtex_bibfiles = ['bibliography.bib']
bibtex_default_style = 'alpha'
