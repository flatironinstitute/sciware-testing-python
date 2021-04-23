#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

# load README.md contents to use as long_description
with open('README.md') as readme_file:
    readme = readme_file.read()

# load requirements.txt to use as install_requires
with open('requirements.txt', 'r') as f:
    requirements = [l for l in f if l.strip() and not l.startswith('#')]

setup(
    name="sciware-testing-python",
    author="sciware",
    author_email='sciware@flatironinstitute.org',
    url='https://github.com/flatironinstitute/sciware-testing-python',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    version='0.1.0',
    long_description=readme,
    license="Apache Software License 2.0",
    # some (optional) tags
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=requirements,
    packages=find_packages()
)
