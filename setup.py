#! /usr/bin/env python
from setuptools import setup, find_packages
import os

PROJECT_ROOT = os.path.dirname(__file__)
REVISION = '0.0.1'
PROJECT_NAME = 'GFrasca Utilities'
PROJECT_AUTHORS = 'Giulio Frasca'
PROJECT_URL = 'https://github.com/gmfrasca/util'
DESCRIPTION = 'Common Utilities Library for gmfrasca Projects'
PACKAGE_NAME = 'gmfrasca.util'
GLOBAL_ENTRY_POINTS = {
    'console_scripts': [],
    'gui_scripts': []
}

install_requires = [
    'pyyaml'
]

setup(
    name=PACKAGE_NAME,
    version=REVISION,
    author=PROJECT_AUTHORS,
    url=PROJECT_URL,
    description=DESCRIPTION,
    entry_points=GLOBAL_ENTRY_POINTS,
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    install_requires=install_requires,
    license='MIT',
    classifiers=[]
)
