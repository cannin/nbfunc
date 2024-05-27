#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import io
import re
import os
from setuptools import find_packages, setup
from nbnofun import __version__

DEPENDENCIES = ['nbconvert', 'ipython']
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "test*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="nbnofun",
    version=__version__,
    author="cannin",
    description="Check Jupyter notebooks in current directory for Python functions; exit with error if found.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cannin/nbnofun",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    entry_points={"console_scripts": ["nbnofun=nbnofun.__main__:main"]},
    zip_safe=False,
    install_requires=DEPENDENCIES,
    #test_suite="tests.test_project",
    python_requires=">=3.10",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: Apache Software License",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
        # "Private :: Do Not Upload"
    ],
)