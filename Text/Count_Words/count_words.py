#! /usr/bin/env python3
# -*- conding: utf-8 -*-

"""
Usage:
    count_words [options] <content>...

Options:
    -f, --file                      Read string from file.
    -h, --help                      Show this screen.
    --version                       Show version.
"""

from docopt import docopt


# Counts the number of individual words in a string. For added complexity read
# these strings in from a text file and generate a summary.

def count_words(string):
    word_list = string.split()
    return len(word_list)


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0')
    print(args)

    if args['--file']:
        word_num = 0
        for filename in args['<content>']:
            with open(filename, encoding='utf-8') as reader:
                for line in reader:
                    word_num += count_words(line)
    else:
        word_num = len(args['<content>'])

    print(word_num)

