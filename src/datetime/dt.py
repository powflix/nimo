#!/usr/bin/env python
"""Datetime Listing Module."""

import datetime


def dt():
    """Show datetime in Indian Style."""
    load_time = datetime.datetime.now()
    print(load_time.strftime('[%d-%b-%Y %I:%M:%S %p]'))


if __name__ == '__main__':
    dt()
