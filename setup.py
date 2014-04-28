#!/usr/bin/env python
# coding: utf-8

"""
    distutils setup
    ~~~~~~~~~~~~~~~

    :copyleft: 2012 by the django-phpBB3 team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import os
import sys

from setuptools import setup, find_packages

from django_phpBB3 import VERSION_STRING


PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

def long_description():
    readme = open(os.path.join(PACKAGE_ROOT, "README.creole"), "r")
    long_description = readme.read()
    readme.close()
    return long_description

def get_authors():
    f = open(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r")
    authors = [l.strip(" *\r\n") for l in f if l.strip().startswith("*")]
    f.close()
    return authors


setup(
    name='django-phpBB3',
    version=VERSION_STRING,
    description='django database models of phpBB3',
    keywords=["django", "forum", "phpBB3", "phpBB"],
    long_description=long_description(),
    author=get_authors(),
    maintainer="Jens Diemer",
    maintainer_email="django-phpBB3@jensdiemer.de",
    url='https://github.com/jedie/django-phpBB3/',
    download_url='http://pypi.python.org/pypi/django-phpBB3/',
    packages=find_packages(),
    use_2to3=True,
    include_package_data=True, # include package data under svn source control
    install_requires=[
        "Django>=1.4",
    ],
    tests_require=[
        #"django-tools", # https://github.com/jedie/django-tools/
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
#        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
#        "Intended Audience :: Education",
#        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        'Framework :: Django',
        "Topic :: Database :: Front-Ends",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Operating System :: OS Independent",
    ],
#    test_suite = "django_kippo_test_project.runtests.runtests",
)
