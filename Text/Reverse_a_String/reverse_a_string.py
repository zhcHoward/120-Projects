#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Reverse a String – Enter a string and the program will reverse it and print it out.

string = input('Please enter a string: ')
print(string[::-1])
# print(''.join(reversed(string)))  # This is a little slower.

# According to http://stackoverflow.com/questions/931092/reverse-a-string-in-python
# slice is the fastest implementation

