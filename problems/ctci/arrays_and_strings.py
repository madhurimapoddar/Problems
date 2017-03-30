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


def one_edit_away(string1, string2):
    # check if they are already equal
    if string1 == string2:
        print "True"
        return
    # check if the length of the strings
    if abs(len(string1) - len(string2)) > 1:
        print "False"
        return

    # if we can insert/remove/update to make the strings equal
    len_string1 = len(string1)
    len_string2 = len(string2)

    count_string1 = 0
    count_string2 = 0

    while count_string1 < len_string1 and count_string2 < len_string2:
        if string1[count_string1] == string2[count_string2]:
            count_string1 += 1
            count_string2 += 1
        elif string1[count_string1] != string2[count_string2]:
            # delete the character if the length of the strings differ by one
            if len_string1 > len_string2:
                # strip the mismatched char
                temp = string1[1:count_string1] + string1[count_string1 + 1:]
                return temp == string2

            # if lengths are equal, then replace a character and compare
            else:
                temp = string1[:count_string1] + string2[count_string1] + string1[count_string1 + 1:]
                return temp == string2
    return

print one_edit_away("pale", "bake")
print one_edit_away("pale", "bale")


def string_compressions(my_string):
    # eg: "aabcccccaaa" --> a2b1c5a3
    # if compressed string is not smaller than original, return original string
    copy_my_string = my_string
    char_counts = []
    my_string = list(my_string)
    prev = ''
    count = 0
    while my_string:
        string = my_string.pop()
        if string == prev:
            count += 1
        else:
            if count == 0:
                count += 1
            if prev:
                char_counts.append((prev, count))
                count = 0
        prev = string
        if not my_string:
            char_counts.append((string, count + 1))

    # check if compressed string is longer than original string
    useful_compression = [(x, y) for x, y in char_counts if y > 2]
    compressed_string = ''
    if useful_compression:
        for char, count in useful_compression:
            compressed_string = compressed_string + char + str(count)
        return compressed_string
    return copy_my_string

print string_compressions("abc")


def get_zero_matrix(matrix):
    # given a MxN matrix, if an element is zero, that element's entire row and
    # column are set to zero as well.
    rows = len(matrix)
    zero_col = None
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                # make all the elements in that row zero
                matrix[i] = [0 for col in range(columns)]
                zero_col = j
                break
    # make all the elements in that col zero too
    if zero_col:
        for i in range(rows):
            matrix[i][zero_col] = 0
    return matrix

print get_zero_matrix([[1, 1, 0], [1, 1, 1], [1, 1, 1]])


def string_rotation(s1, s2):
    # check if s2 is a rotation of s1 with only one call to is_substring
    # eg. waterbottle is a rotation of erbottlewat
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 == len_s2:
        s1s1 = s1 + s1
        return s2 in s1s1


print string_rotation("waterbottle", "erbottlewat")

