#!/usr/bin/env python

"""Python Scripts Bundle for extra functionalities in Command Line Terminals.

Source: https://github.com/powflix/nimo | see README for more details.
License: GNU General Public License v3 (GPLv3) | see LICENSE for more details.
Contribution: Wanna contribute to nimo? | see CONTRIBUTING for more details.

Copyright (C) 2020 Powflix Inc., and its affiliates.
"""

import datetime
import sys


def dt():
    """Show datetime in Indian Style."""
    load_time = datetime.datetime.now()
    print(load_time.strftime('[%d-%b-%Y %I:%M:%S %p]'))

    return 0


if __name__ == '__main__':
    sys.exit(dt())
