# -*- coding: utf-8 -*-
"""
 @Time    : 19/7/29 11:15
 @Author  : CyanZoy
 @File    : setup.py.py
 @Software: PyCharm
 @Describe: 
 """
# !/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time: 2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

import drf_docs

setup(
    name="drf_docs",
    version=drf_docs.__version__,
    keywords=("pip", "pathtool", "timetool", "magetool", "mage"),
    description="api docs",
    long_description="django restframework api docs",
    license="MIT Licence",

    url="https://github.com/fengmm521/pipProject",
    author="mage",
    author_email="mage@woodcol.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)