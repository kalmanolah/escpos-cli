#!/usr/bin/env python2

"""Setup module."""
from setuptools import setup, find_packages
import os


def read(fname):
    """Read and return the contents of a file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='escpos-cli',
    version='0.0.1',
    description='escpos-cli is a command-line utility for printer stuff using pyxmlescpos',
    long_description=read('README.md'),
    author='Kalman Olah',
    author_email='kalman@inuits.eu',
    url='https://github.com/kalmanolah/escpos-cli',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyxmlescpos'
    ],
    entry_points={
        'console_scripts': [
            'escpos-cli = escpos_cli:main',
        ]
    },
    dependency_links=[
        'git+https://github.com/kalmanolah/py-xml-escpos.git#egg=pyxmlescpos'
    ]
)
