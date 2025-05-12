# Configuration file for the Sphinx documentation builder.
# -- Project information
project = 'Cell-Hub'
copyright = '2024, Macaux'
author = 'Macaux'
release = '0.1'
version = '0.1.0'
# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',  # Ajout de MyST-Parser
]

# Définir les extensions de fichiers pour RST et Markdown
source_suffix = ['.rst', '.md']  # Ajout de l'extension .md

# Activer les extensions MyST si nécessaire
myst_enable_extensions = [
    "dollarmath",      # Pour la syntaxe mathématique avec $ et $$
    "colon_fence",     # Pour les blocs de code avec :::
    "smartquotes",     # Pour les guillemets intelligents
    "replacements",    # Pour les remplacements typographiques courants
    "linkify",         # Pour transformer les URLs en liens
    "substitution"     # Pour les substitutions
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