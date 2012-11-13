#!/usr/bin/python
# Filename: setup.py



"""
Easylab is a simple, convenient tool to make the lab easier.
It captures the results as well as the arguments of a program,
stores them in a database, and visualizes them with a simple,
SQL-style query.
"""

import os
import sys


from setuptools import setup, find_packages


setup(
    name = "easylab",
    version = "0.2.0",
    author = "onesuper",
    zip_safe = False,
    packages = find_packages("src"),
    package_dir = {"": "src"},
    url = "http://chengyichao.info/Easylab",
    author_email = "onesuperclark@gmail.com",
    long_description = "make lab a little easier",
    platforms = "Independent",
    license = "MIT",
)
