import importlib.metadata as md
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'sphinxcicdtesting'
copyright = '2025, ER'
author = 'ER'

release  = md.version("sphinxcicdtesting")
release = '0.1'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",           # for Google/NumPy docstrings
    "sphinx_autodoc_typehints",      # for type hints in docs
]

autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# html_theme = 'furo'
# html_theme = 'conestack'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
