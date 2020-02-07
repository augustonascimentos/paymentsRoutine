#!/usr/bin/env python
from __future__ import unicode_literals
import codecs
import os
import re
from setuptools import setup, find_packages


def read(*parts):
    with codecs.open(os.path.join(*parts), 'r') as fp:
        return fp.read()


def get_version():
    version_file = read('src', '__init__.py')
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', version_file, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


install_requires = [
    'flask==1.1.1',
    'flask-cors==3.0.8',
    'requests==2.22.0',
    'boto3==1.10.27',
    'python-dotenv==0.10.3',
    'marshmallow==2.20.2'
]


setup(
    name='Payments Routine',
    version=get_version(),
    description='This application is part of a payment processing platform',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Augusto Nascimento',
    author_email='augustonascimentos@gmail.com',
    url='https://github.com/augustonascimentos/paymentsRoutine',
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=install_requires,
    include_package_data=True,
    test_suite="tests",
    classifiers=[
    ],
)
