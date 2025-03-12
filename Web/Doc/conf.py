import os
import sys
import subprocess
# Call the script to generate index.rst
script_path = os.path.join(os.path.dirname(__file__), 'runindex.py')
subprocess.run(['python3', script_path], check=True)


# conf.py
project = 'Máster'
author = 'Taller 31'

html_title = "Máster"
html_short_title = "Máster"
html_logo = '_static/MMEC.png' 
html_favicon = '_static/MMEC.png' 

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinxemoji.sphinxemoji',
    # ... otras extensiones
]

# Opciones de myst_parser
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

language = 'es'


html_theme = 'sphinx_rtd_theme'
sphinxemoji_style = 'twemoji'

html_theme_options = {
    'logo_only': True,  # Muestra solo el logo y no el nombre del proyecto
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'collapse_navigation': False,  # Deshabilita la navegación colapsable
    'sticky_navigation': True,  # Navegación pegajosa
    'navigation_depth': 2,  # Establece la profundidad de la navegación

}

html_static_path = ['_static']


# Opciones adicionales
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
