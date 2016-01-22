#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-autologin',

    url="https://chris-lamb.co.uk/projects/django-autologin",
    version='0.0.4',
    description="Token generator and processor to provide automatic login links for users",

    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license="BSD",

    packages=find_packages(),
    install_requires=(
        'Django>=1.6.8',
    ),
)
