#!/usr/bin/env python

"""Python Scripts Bundle for extra functionalities in Command Line Terminals.

Source: https://github.com/powflix/nimo | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to nimo? | see CONTRIBUTING for more details.

Copyright (C) 2020 Powflix Inc., and its affiliates.
"""

import sys


def fopen():
    """File opening directly."""
    try:
        file = open(sys.argv[1], 'r')

    except Exception:
        print('//Error in file opening,\nIt seems that file does not exit.')
        return 1

    try:
        print('\n')
        flag = 1
        for line in file:
            print('line '+str(flag)+'| '+line, end='')
            flag += 1
        print('')
        file.close()
        return 0

    except Exception:
        print('//Error in file encoding.\n')
        file.close()
        return 1


if __name__ == '__main__':
    sys.exit(fopen())
