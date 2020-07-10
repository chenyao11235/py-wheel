#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2020/07/10 15:29:27
@Desc    :   None
'''

# here put the import lib
from setuptools import setup, find_packages

setup(
    name='wheel',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'grpcio',
    ],
)
