#!/usr/bin/env python

# Encoding: UTF-8
# Line Endings: LF(Unix)
# Programming Language: Python 3
# Syntax Standard: PEP 8


"""Copyright (C) 2020 Powflix Inc., and its affiliates.

Source: https://github.com/powflix/nimo | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to nimo? | see CONTRIBUTING for more details.
"""


import datetime
import os
import sys


def ltdir():
    """List all hidden files and directories in a sequence."""
    total_files_size = 0

    for root_directory, sub_directories, files in os.walk(os.getcwd()):

        print('\nDIRECTORY OF "'+os.getcwd()+'"\n')
        print('==============================================================='
              + '===========\nType         Last modification time          '
              + 'Name\n======================================================='
              + '===================\n')

        for i in range(0, len(sub_directories)):
            try:
                last_modification_date = datetime.datetime.fromtimestamp(
                    os.stat(str(sub_directories[i])).st_mtime)

                last_modification_date = last_modification_date.strftime(
                    '[%d-%b-%Y %I:%M:%S %p]')

                print('<dir>       '
                      + last_modification_date
                      + '        '
                      + str(sub_directories[i]))

            except FileNotFoundError:
                continue

        for i in range(0, len(files)):
            try:
                last_modification_date = datetime.datetime.fromtimestamp(
                    os.stat(str(files[i])).st_mtime)

                last_modification_date = last_modification_date.strftime(
                    '[%d-%b-%Y %I:%M:%S %p]')

                file_size = float("{0:.2f}".format(
                    os.stat(str(files[i])).st_size/1024))

                total_files_size += file_size

                print('File:       '
                      + last_modification_date
                      + '        '
                      + str(files[i])
                      + '       //[Size = '
                      + str(file_size)
                      + ' Kb'+']')

            except FileNotFoundError:
                continue

        break

    print('\n[Total <dir>]: '+str(len(sub_directories)))

    print('[Total Files]: '
          + str(len(files))
          + '   //[Size = '
          + str(total_files_size)
          + ' Kb]')

    return 0


if __name__ == '__main__':
    sys.exit(ltdir())
