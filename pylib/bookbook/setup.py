#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

requires = [
    'nbconvert',
    'jinja2',
    'pandocfilters'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bookbook2',
    version='0.1.0',
    author='Shixiang Wang',
    author_email='w_shixiang@163.com',
    description='Convert ipython notebooks to html or pdf chapters',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ShixiangWang/bookbook2',
    packages=["bookbook2"],
    package_dir={'bookbook2': 'bookbook2'},
    package_data={'bookbook2': ['html_index.tpl']},
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup"
    ]
)