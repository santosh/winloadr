#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Copyright © 2013 Santosh Kumar <https://twitter.com/sntshk>. All Rights Reserved.
File: winloadr.py
Author : Santosh Kumar <https://twitter.com/sntshk>
Date created: Thu 04 Jul 2013 11:15:28 IST
Description: winloadr is a simple command line download manager for Windows
License: See LICENSE file in the root directory
'''


from __future__ import print_function, division, absolute_import, unicode_literals
import sys
import os
import argparse
import time
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

# {{ Argument parser
parser = argparse.ArgumentParser(
    prog='downloader',
    description='a featureful downloader'
)

parser.add_argument(
    '-o',
    dest='outputfile',
    help='name of the downloaded file, defaults to the remote file'
)

parser.add_argument(
    '-r',
    dest='remotefile',
    help='URL of the file to download'
)

parser.add_argument(
    '-b',
    dest='block_size',
    type=int,
    default=8192,
    # set the upper limit of block_size to its default value
    help='bytes to be downloaded at a time'
)

parser.add_argument(
    '-t',
    dest='time_to_update',
    type=float,
    default=1.0,
    help='no. of secs to update the screen for updates'
)

downloader = parser.parse_args()
# }}

# {{ default local filename
if downloader.outputfile:
    default_output_file = downloader.outputfile
else:
    default_output_file = os.path.split(downloader.remotefile)[-1]
# }}

u = urlopen(downloader.remotefile)
meta = u.info()
file_size_in_bytes  = int(dict(meta.items())['Content-Length'])
print("Downloading: %s Bytes: %i" % (default_output_file, file_size_in_bytes))

try:
    with open(default_output_file, 'wb') as f:
        file_size_dl = 0
        block_size = 8192
        while True:
            buffer = u.read(block_size)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d KB [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size_in_bytes)
            status = status + chr(8)*(len(status)+1)
            print(status, end="\r")
            time.sleep(downloader.time_to_update)
except KeyboardInterrupt:
    sys.exit(0)
# Todo
# Add HTTPError exception
