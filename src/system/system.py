#!/usr/bin/env python
"""System Information Module."""


import platform


def system():
    """Show system related details."""
    print('\n==============================================================='
          + '===========\nSYSTEM DETAILS\n=================================='
          + '========================================\n')
    print('OS NAME                : '+platform.system()+' '+platform.release())
    print('OS VERSION             : '+platform.version())
    print('DEVICE NAME            : '+platform.node())
    print('OS ARCHITECTURE        : '+platform.architecture()
          [0]+' '+platform.architecture()[1])
    print('CPU DETAILS            : '+platform.processor())
    print('MACHINE TYPE           : '+platform.machine())

    return None


if __name__ == '__main__':
    system()
