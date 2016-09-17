#! /usr/bin/env python3
# -*- conding: utf-8 -*-

"""
Usage:
    count_words [--option]... [filename]
    count_words -f FILENAME, --file=FILENAME

Options:
    -f FILENAME, --file FILENAME    Read string from file.
    -h, --help                      Show this screen.
    --version                       Show version.
"""

from docopt import docopt


# Counts the number of individual words in a string. For added complexity read
# these strings in from a text file and generate a summary.

if __name__ == '__main__':
    args = docopt(__doc__, version='1.0')
    print(args)

