# -*- coding: utf-8 -*-

from collections import defaultdict
import urllib


def is_unique(my_string):
    # Determine if a string has all unique characters
    char_dict = {}
    for char in my_string:
        if not char_dict.get(char):
            char_dict[char] = 1
        else:
            print "Not Unique"
            break
    print "Unique"


def is_unique_2(my_string):
    # Determine if a string has all unique characters without using any additional data structure.
    # sort the string, O(nlogn)
    my_string = ''.join(sorted(my_string))
    is_unique = True
    length = len(my_string) - 1
    for index in range(length):
        if my_string[index] == my_string[index + 1]:
            is_unique = False
            break
    print is_unique


def check_permutation_1(string1, string2):
    # given 2 strings, see if one is a permutation of the other
    # sort both the strings and compare.
    if len(string1) != len(string2):
        print "Not a permutation"
    else:
        sorted_string_1 = ''.join(sorted(string1))
        sorted_string_2 = ''.join(sorted(string2))
        if sorted_string_1 != sorted_string_2:
            print "Not a permutation"
        else:
            print "Is a permutation"


def check_permutation_2(string1, string2):
    # another way would be to count the characters of both the strings.
    string1_char_count = defaultdict(int)
    string2_char_count = defaultdict(int)

    for char in string1:
        string1_char_count[char] = string1_char_count[char] + 1

    for char in string2:
        string2_char_count[char] = string2_char_count[char] + 1

    if string1_char_count != string2_char_count:
        print "Not a permutation"
    else:
        print "Is a permutation"


def urlify(string):
    # replace all spaces in a string with %20
    # could also use string replace
    # string.replace(" ", "%20")
    print urllib.quote(string)


def palindrome_permutation(string):
    # if a string is a palindrome:
    # a) String is even length
    #    1) each character should have an even count (since palindrome is same when read reverse)
    # b) String is odd length
    #    1) One character will appear odd number of times
    #    2) The others will be even
    string = string.replace(" ", "")
    length = len(string)
    string = string.lower()
    charcter_count_dict = defaultdict(int)
    palindrome = True

    for char in string:
        charcter_count_dict[char] += 1

    # even length string
    if length % 2 == 0:
        for char, count in charcter_count_dict.items():
            if count % 2 != 0:
                palindrome = False
                break
    else:
        odd_char_count = 0
        for char, count in charcter_count_dict.items():
            if count % 2 != 0:
                odd_char_count += 1
            if odd_char_count > 1:
                palindrome = False
                break

    print palindrome


palindrome_permutation("tact coa")
