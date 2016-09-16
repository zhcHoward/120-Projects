#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Checks if the string entered by the user is a palindrome. That is that it
# reads the same forwards as backwards like “racecar”

string = input('Please input a string: ')
reversed_string = ''.join(reversed(string))
output = '{} is {}a palindrome'

if string == reversed_string:
    print(output.format(string, ''))
else:
    print(output.format(string, 'not '))

