#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

requires = [
    'nbconvert',
    'jinja2',
    'pandocfilters'
]

setup(
    name='bookbook2',
    version='0.1.0',
    description='Convert ipython notebooks to html/pdf chapters',
    author='Shixiang Wang',
    author_email='w_shixiang@163.com',
    url='https://github.com/ShixiangWang/bookbook2',
    keywords='book converter render',
    packages=["bookbook2"],
    package_dir={'bookbook2': 'bookbook2'},
    package_data={'bookbook2': ['html_index.tpl']},
    include_package_data=True,
    install_requires=requires
)