#!/usr/bin/env python

from setuptools import setup, find_packages

name = "shingling"

setup(
    name=name,
    version="0.2.1",
    url="http://silpa.org.in/sort",
    license="LGPL-3.0",
    description="A library for making w shingles",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""a w-shingling is a set of unique "shingles"—contiguous subsequences of tokens in a document—that can be used to gauge the similarity of two documents. The w denotes the number of tokens in each shingle in the set.English, Hindi, Malayalam, Kannada, Bengali suported now.""",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools', 'silpa_common'],
    zip_safe=False,
)
