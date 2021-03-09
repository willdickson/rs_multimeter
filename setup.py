from setuptools import setup
from setuptools import find_packages
import os

setup(
    name='rs_multimeter', 
    version='0.0.1',
    description='Library for communicating with a (Radio Shack) Micronta type LCD digital multimeter',
    author='Will Dickson', 
    author_email='wbd@caltech', 
    license='MIT', 
    classifiers=[ 
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.7', 
        ], 
    packages=find_packages(exclude=['examples',]),
    )
