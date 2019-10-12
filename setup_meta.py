"""
Creates a distribution alias that just installs pyetheroll.
"""
from setuptools import setup

from setup import setup_params

setup_params.update({"install_requires": ["pyetheroll"], "name": "etheroll"})


setup(**setup_params)
