# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Contributing to Godot'
copyright = '2025, Godot Engine Contributors'
author = 'Godot Engine Contributors'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'flyout_display': 'hidden',
    'version_selector': False,
    'language_selector': False,
    'display_version': False,
}

html_context = {
    "display_github": True,
    "github_user": "Ivorforce",
    "github_repo": "godot-contributing-docs",
    "github_version": "main",
    "conf_py_path": "/",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
