# coding: utf-8
import sys
from setuptools import (
    setup,
    find_packages
)

test_requirements = ['responses',
                     'pytest-cov',
                     'pytest-mock',
                     'pytest>=2.8.0', ]

install_requires = ['six', 'requests']

if sys.version_info == (2, 7):
    install_requires.append('functools32')

setup(
    name='thrall',
    version='0.01',
    description='Maps web-service HTTP Api',
    author='Zoltan Qin',
    author_email='qinzezzhen@outlook.com',
    packages=find_packages(),
    tests_require=test_requirements,
    install_requires=['six', 'functools32', 'requests'],
)