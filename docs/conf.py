# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

for path in sys.path:
    if path == '' or path == '.':
        print(f"Current directory: {os.getcwd()}")
    elif 'site-packages' in path or 'lib' in path or 'Frameworks' in path:
        print(f"Standard library or site-packages: {path}")
    elif path == '/usr/bin' or path.startswith('/usr/lib'):
        print(f"System directory: {path}")
    else:
        print(f"Custom or user-defined path: {path}")

# -- Project information -----------------------------------------------------

project = u"wordle_dk3481"
copyright = u"2025, Daegeun Kim"
author = u"Daegeun Kim"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
