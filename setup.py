# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['black']
install_requires = \
['black']

entry_points = \
{'console_scripts': ['black = black:main']}

setup_kwargs = {
    'name': 'repl-nix-cblack',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
