#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, shutil
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='winloadr',
    version=open('VERSION').read().strip(),
    author='Santosh Kumar',
    author_email='sntshkmr60@gmail.com',
    packages=['winloadr'],
    scripts=['bin/winloadr'],
    url='https://github.com/santosh/winloadr',
    zip_safe=False,
    include_package_data=True,
    license=open('LICENSE').read(),
    description='winloadr is a simple command line download manager for Windows',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha'
        'Environment :: Console'
        'Intended Audience :: End Users/Desktop'
        'Intended Audience :: System Administrators'
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)'
        'Natural Language :: English'
        'Operating System :: Microsoft :: Windows'
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python :: 3'
        'Topic :: Internet'
        'Topic :: System'
        'Topic :: Utilities']
    )

if 'install' in sys.argv:
    man_path = '/usr/share/man/man1/'
    if os.path.exists(man_path):
        man_page = "doc/winloadr.1.gz"
        shutil.copy2(man_page, man_path)
        os.chmod(man_path + 'winloadr.1.gz', int('444', 8))
        print("see manual page: man winloadr")

