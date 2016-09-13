#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Pig Latin is a game of alterations played on the English language game. To
# create the Pig Latin form of an English word the initial consonant sound is
# transposed to the end of the word and an ay is affixed (Ex.: "banana" would
# yield anana-bay). Read Wikipedia for more information on rules.

string = input('Please enter a string: ')

if string.startswith(('a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U')):
    print(''.join([string, 'yay']))
else:
    print(''.join([string[1:], string[0], 'ay']))

