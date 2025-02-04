# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

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

# Configuration pour le thème Read the Docs
html_theme = 'sphinx_rtd_theme'

# Options pour le thème Read the Docs
html_theme_options = {
    'collapse_navigation': False,  # Empêche le menu de se refermer
    'navigation_depth': -1,        # Affiche toutes les sections sans limite de profondeur
}


# Ajouter le répertoire `_static` pour les fichiers statiques
html_static_path = ['_static']



# -- Options for EPUB output
epub_show_urls = 'footnote'
