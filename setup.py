#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests',
    'sanction',
]

test_requirements = [
    'pytest'
]

setup(
    name='python-flipkart',
    version='0.1.0',
    description="Python Flipkart Marketplace API Client",
    long_description=readme + '\n\n' + history,
    author="Fulfi.IO Inc.",
    author_email='help@fulfil.io',
    url='https://github.com/fulfilio/python-flipkart',
    packages=[
        'flipkart',
    ],
    package_dir={'flipkart': 'flipkart'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='python flipkart',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)