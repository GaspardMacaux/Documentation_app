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
# Paramètres pour la table des matières
html_theme_options = {
    'navigation_depth': 1,  # Limite la profondeur de navigation à 1 niveau
    'collapse_navigation': False,  # Empêche la fermeture automatique des sections
    'sticky_navigation': True,  # Garde la navigation visible pendant le défilement
    'titles_only': True,  # Affiche uniquement les titres dans la barre latérale
}
# Ajouter le répertoire `_static` pour les fichiers statiques
html_static_path = ['_static']
# -- Options for EPUB output
epub_show_urls = 'footnote'