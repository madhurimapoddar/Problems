# -*- coding: utf-8 -*-
from collections import defaultdict


def char_to_frequence(some_string):
    # https://www.careercup.com/question?id=5657081936871424
    char_freq_dict = defaultdict(int)
    for char in some_string:
        char_freq_dict[char] += 1

    for char, freq in char_freq_dict.items():
        print freq, char,

#char_to_frequence('aaaggbbbbc')


def max_rectangles():
    # https://www.careercup.com/question?id=5754499009347584
    pass


def get_powerset():
    # http://stackoverflow.com/questions/1482308/whats-a-good-way-to-combinate-through-a-set
    # https://www.careercup.com/question?id=4862471882932224
    pass


def make_a_string_palindrome(some_string):
    # https://www.careercup.com/question?id=5708537557680128
    # eg: given string - abc, result - cbabc

    # single letter string will be a palindrome
    if len(some_string) == 1:
        return some_string

    # for strings longer than length 1, first check if its a palindrome or not.
    # if not keep adding letters from the end till it becomes a palindrome
    if is_palindrome(some_string):
        return some_string
    else:
        len_string = len(some_string)
        end = len_string - 1
        left_half = ''
        while True:
            for char in some_string:
                # keep appending letters from the end of the string till it becomes a palindrome.
                left_half = left_half + some_string[end]
                if is_palindrome(left_half + some_string):
                    return left_half + some_string
                else:
                    end -= 1


def is_palindrome(string):
    """Check if a string is a palindrome. Return True if yes or False."""
    start = 0
    end = len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print make_a_string_palindrome('xyayb')


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find_max_sum_aleternate_levels(self):
        # https://www.careercup.com/question?id=5701538572926976
        # traverse level order, keep the items in a list of lists. Sum lists at odd
        # indices and even indeces separately, get max sum.
        levels = [[self]]
        stack = [self]
        while stack:
            next_level = []
            for node in stack:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack = next_level
            if next_level:
                levels.append(next_level)

        node_datas = []
        for level in levels:
            datas = []
            for node in level:
                datas.append(node.data)
            node_datas.append(datas)

        even_level_sum = odd_level_sum = 0
        even = 0
        odd = 1
        while even < len(node_datas) or odd < len(node_datas):
            if even < len(node_datas):
                even_level_sum += sum(node_datas[even])
            if odd < len(node_datas):
                odd_level_sum += sum(node_datas[odd])
            even += 2
            odd += 2
        return max(even_level_sum, odd_level_sum)

tree = Node(4)
tree.left = Node(5)
tree.right = Node(6)
tree.left.left = Node(1)
tree.left.right = Node(1)
tree.right.left = Node(5)
tree.right.right = Node(9)

print tree.find_max_sum_aleternate_levels()


def find_first_index_of_common_char(string1, string2):
    #https://www.careercup.com/question?id=5674342340886528
    count = 0
    len_string_1 = len(string1)
    while count < len(string2):
        if len_string_1 >= count:
            if string2[count] == string1[count]:
                return count
            else:
                count += 1
        else:
            return

print find_first_index_of_common_char("adf6ysh", "123678")


def move_zeroes_to_the_end(numbers):
    # https://www.careercup.com/question?id=5738847481626624
    numbers_count = len(numbers)
    i = 0
    while i < numbers_count:
        if numbers[i] == 0:
            numbers = numbers[: i] + numbers[i + 1:]
            numbers.append(0)
        i += 1
    return numbers

print move_zeroes_to_the_end([1, 3, 0, 8, 12, 0, 4, 0, 7])

