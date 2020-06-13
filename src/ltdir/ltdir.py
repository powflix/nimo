#!/usr/bin/env python
"""Files Listing Module."""


import datetime
import os


def ltdir():
    """List all hidden files and directories in a sequence."""
    total_files_size = 0

    for root_directry, sub_directories, files in os.walk(os.getcwd()):

        print('\nDIRECTORY OF "'+os.getcwd()+'"\n')
        print('==============================================================='
              + '===========\nType         Last modification time          '
              + 'Name\n======================================================='
              + '===================\n')

        for i in range(0, len(sub_directories)):
            last_modification_date = datetime.datetime.fromtimestamp(
                os.stat(str(sub_directories[i])).st_mtime)
            last_modification_date = last_modification_date.strftime(
                '[%d-%b-%Y %I:%M:%S %p]')
            print('<dir>       '+last_modification_date +
                  '        '+str(sub_directories[i]))

        for i in range(0, len(files)):
            last_modification_date = datetime.datetime.fromtimestamp(
                os.stat(str(files[i])).st_mtime)
            last_modification_date = last_modification_date.strftime(
                '[%d-%b-%Y %I:%M:%S %p]')

            file_size = float("{0:.2f}".format(
                os.stat(str(files[i])).st_size/1024))
            total_files_size += file_size

            print('File:       '+last_modification_date+'        ' +
                  str(files[i])+'       //[Size = '+str(file_size)+' Kb'+']')

        break

    print('\n[Total <dir>]: '+str(len(sub_directories)))
    print('[Total Files]: '+str(len(files)) +
          '   //[Size = '+str(total_files_size)+' Kb]')

    return None


if __name__ == '__main__':
    ltdir()
