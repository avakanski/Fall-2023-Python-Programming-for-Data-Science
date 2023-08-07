# Configuration file for the Sphinx documentation builder.

import sphinx_rtd_theme

# -- Project information
project = 'Fall 2023 Python Programming for Data Science'
copyright = '2023, Alex Vakanski'
author = 'Alex Vakanski'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'nbsphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_gallery.load_style',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Add any paths that contain templates here, relative to this directory.
# The template links to a custom style css to increase the width of displayed content
templates_path = ['_templates']

# -- Options for HTML output
# -- The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# -- Path to static files
html_static_path = ['_static']

master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
