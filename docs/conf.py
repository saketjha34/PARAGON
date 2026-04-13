# -- Project information -----------------------------------------------------

project = 'PARAGON'
author = 'Jha Saket Sunil'
copyright = '2026, Jha Saket Sunil'
release = 'v0.1.9'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",              # Markdown support
    "sphinx.ext.autodoc",       # Auto docs
    "sphinx.ext.napoleon",      # Google-style docstrings
    "sphinx.ext.viewcode",      # Show source code
    "sphinx.ext.githubpages",   # GitHub Pages support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Allow both .rst and .md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "titles_only": False,
}

html_static_path = ['_static']

# -- Branding / UI -----------------------------------------------------------

html_title = "PARAGON Documentation"
html_short_title = "PARAGON"

html_context = {
    "display_github": True,
    "github_user": "saketjha34",
    "github_repo": "PARAGON",
    "github_version": "main/docs/source/",
}

# -- Custom sidebar ----------------------------------------------------------

html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
    ]
}