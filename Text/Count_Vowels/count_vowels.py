#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Enter a string and the program counts the number of vowels in the text. For
# added complexity have it report a sum of each vowel found.

from collections import defaultdict


string = input('Please enter a string: ')

vowel_list = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
vowel_sum = defaultdict(int)
for char in string:
    if char in vowel_list:
        vowel_sum[char] += 1

print('Vowel Count:')
for char in sorted(vowel_list):
    print('"{}" sum: {}'.format(char, vowel_sum[char]))

