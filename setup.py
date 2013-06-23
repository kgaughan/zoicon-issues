#!/usr/bin/env python

from setuptools import setup, find_packages

from buildkit import read, read_requirements


setup(
    name='zoicon-issues',
    version='0.1.0',
    description='Issue tracker',
    long_description=read('README'),
    url='https://github.com/kgaughan/zoicon-issues/',
    license='MIT',
    packages=find_packages(exclude='tests'),
    zip_safe=False,
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,

    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ),

    author='Keith Gaughan',
    author_email='k@stereochro.me',
)
