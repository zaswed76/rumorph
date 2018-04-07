# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname
import rumorph
setup(
    name='rumorph',
    version=rumorph.__version__,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
