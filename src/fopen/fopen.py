#!/usr/bin/env python
"""File Opening Module."""


import sys


def fopen():
    """File opening directly."""
    try:
        file = open(sys.argv[1], 'r')

    except Exception:
        print('//Error in file opening,\nIt seems that file does not exit.')
        return None

    try:
        print('\n')
        flag = 1
        for line in file:
            print('line '+str(flag)+'| '+line, end='')
            flag += 1
        print('')
        file.close()
        return None

    except Exception:
        print('//Error in file encoding.\n')
        file.close()
        return None


if __name__ == '__main__':
    sys.exit(fopen())
