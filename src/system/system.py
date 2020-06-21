#!/usr/bin/env python

"""Python Scripts Bundle for extra functionalities in Command Line Terminals.

Source: https://github.com/powflix/nimo | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to nimo? | see CONTRIBUTING for more details.

Copyright (C) 2020 Powflix Inc., and its affiliates.
"""

import platform
import sys


def system():
    """Show system related details."""
    print('\n==============================================================='
          + '===========\nSYSTEM DETAILS\n=================================='
          + '========================================\n')
    print('OS NAME                : '+platform.system()
          + ' '
          + platform.release())
    print('OS VERSION             : '+platform.version())
    print('DEVICE NAME            : '+platform.node())
    print('OS ARCHITECTURE        : '
          + platform.architecture()[0]
          + ' '
          + platform.architecture()[1])
    print('CPU DETAILS            : '+platform.processor())
    print('MACHINE TYPE           : '+platform.machine())

    return 0


if __name__ == '__main__':
    sys.exit(system())
