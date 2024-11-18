# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os 
import sys
import inspect
import commonmark
import sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tech-interview-prep'
copyright = '2024, applesauce'
author = 'applesauce'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../src'))
sys.path.insert(0, os.path.abspath('../materials'))

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

def linkcode_resolve(domain, info):
    """
    Determine the URL given the domain (e.g., 'py') and info dictionary.
    """
    if domain != 'py':
        return None
    if not info['module']:
        return None

    # Adjust the following variables to match your project's structure and GitHub repo
    github_user = 'KaiErikNiermann'
    github_repo = 'tech-interview-prep'
    github_branch = 'main'  # or the name of your default branch

    # Getting the module or function's source file and line numbers
    try:
        obj = sphinx.util.inspect.safe_getattr(sys.modules[info['module']], info['fullname'])
        source_file = inspect.getsourcefile(obj)
        source_file = os.path.relpath(source_file, start=os.path.dirname(os.path.abspath('.')))
        _, line = inspect.getsourcelines(obj)
    except Exception:
        source_file = None
        line = None

    if source_file and line:
        return f"https://github.com/{github_user}/{github_repo}/blob/{github_branch}/{source_file}#L{line}"
    return None


# renders markdown in docstrings
def docstring(app, what, name, obj, options, lines):
    md  = '\n'.join(lines)
    ast = commonmark.Parser().parse(md)
    rst = commonmark.ReStructuredTextRenderer().render(ast)
    lines.clear()
    lines += rst.splitlines()

def setup(app):
    app.connect('autodoc-process-docstring', docstring)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.linkcode',
    'myst_parser', 
    'sphinx.ext.mathjax', 
    'sphinx_math_dollar'
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']
