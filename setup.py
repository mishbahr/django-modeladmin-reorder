#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import admin_reorder

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = admin_reorder.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-modeladmin-reorder',
    version=version,
    description="""Custom ordering for the apps and models in the admin app.""",
    long_description=readme + '\n\n' + history,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/django-modeladmin-reorder',
    packages=[
        'admin_reorder',
    ],
    include_package_data=True,
    install_requires=[
        'django'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-modeladmin-reorder',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

    ],
)
