#!/usr/bin/env python

# import os
# import sys
# import glob

from setuptools import setup

data_files = [
    ('share/doc/batinfo', ['AUTHORS', 'README.md'])
]

setup(
    name='batinfo',
    version='0.1.8',
    description="A simple Python lib to retreive battery information",
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/batinfo',
    #download_url='https://s3.amazonaws.com/batinfo/batinfo-0.1.8.tar.gz',
    license="LGPL",
    keywords="lib battery",
    packages=['batinfo'],
    include_package_data=True,
    data_files=data_files,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ]
)
