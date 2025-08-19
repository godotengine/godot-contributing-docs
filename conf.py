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
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    'flyout_display': 'hidden',
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Remove version and language picker beneath the title
    "version_selector": False,
    "language_selector": False,
    'display_version': False,
}

html_context = {
    "display_github": True,
    "github_user": "godotengine",
    "github_repo": "godot-contributing-docs",
    "github_version": "main",
    "conf_py_path": "/",
}

html_logo = "img/docs_logo.svg"

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    "css/custom.css",
]

html_js_files = [
    "js/custom.js",
#     ('https://plausible.godot.foundation/js/script.file-downloads.outbound-links.js',
#      {'defer': 'defer', 'data-domain': 'godotengine.org'}),
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
