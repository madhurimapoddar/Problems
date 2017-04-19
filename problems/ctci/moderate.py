def swap_number_in_place(a, b):
    # swap a number in place without using a temp variable.
    # this can also be done bitwise.
    # with the binary of the two numbers
    # a = a ^ b
    # b = a ^ b
    # a = a ^ b
    a = a - b
    b = a + b
    a = b - a
    return a, b


def word_frequencies(word, book):
    # if this is run once, go through the book and count how many occurences
    # if this is run multiple times, we can do some pre calculation to store
    # words and its frequencies in a dict and lookup the frequency of any word
    # in constant time.
    pass


class Line(object):
    def __init__(self, start, end):
        start_x, start_y = start
        end_x, end_y = end
        self.slope = (end_y - start_y) / (end_x - start_x)
        self.yintercept = end_y - self.slope * end_x


def intersection(point1, point2):
    # given two straight line segments, find point of intersection if any.
    start1, end1 = point1
    start2, end2 = point2
    # assuming start is before end and point1 is before point2. If not, swap.
    if start1.x > end1.x:
        start1.x, end1.x = end1.x, start1.x
        start1.y, end1.y = end1.y, start1.y

    # same for point2
    if start2.x > end2.x:
        start2.x, end2.x = end2.x, start2.x
        start2.y, end2.y = end2.y, start2.y

    # point one is before point 2, so if not swap
    if start1.x > start2.x:
        # swap start1, start2 and end1, end2
        start1.x, start2.x = start2.x, start1.x
        start1.y, start2.y = start2.y, start1.y
        end1.x, end2.x = end2.x, end1.x
        end1.y, end2.y = end2.y, end1.y

    line1 = Line(start1, end1)
    line2 = Line(start2, end2)

    # if the lines are parallel they will intersect if the y intercept is same and start2 is on line1
    if line1.slope == line2.slope:
        if line1.yintercept == line2.yintercept and is_between(start1, start2, end1):
            return start2

    # get intersection coordinate
    x = (line2.yintercept - line1.yintercept) / (line1.slope - line2.slope)
    y = x * line1.slope + line1.yintercept

    # check if intersection point is within range of line segments
    if is_between(start1, x, end1) and is_between(start2, y, end2):
        return x, y


def is_between(start, middle, end):
    return _is_between(start.x, middle.x, end.x) and _is_between(start.y, middle.y, end.y)


def _is_between(start, middle, end):
    if start > end:
        return end <= middle and middle <= start
    return start <= middle and middle <= start


def tic_tac_win_design(board):
    # for every position on the board, have a map for all the winning combinations
    # for each turn check if all the combinations have the same person's turn.
    # there are only 3^9 tictac boards (for size 3X3)
    # if has_one() is called multiple times, we can have the board winning positions mapped
    # in a hash table and check for all the combos
    # if we know the last move, we can calculat, diagonal, row and column that overlaps.
    # look into scaling this to a NXN board
    pass


def factorial_zeroes(num):
    # write an algorithm that counts the number of trailing zeroes in a factorial.
    # cant take simple route since we will exceed bounds of int very quickly
    # A trailing zero is created with multiples of 10 and multiples of tens are created with pairs
    # of 5-multiples and 2-multiples
    # eg: 19! = 2 * ...*5 *...*10 * ....*15*16*...
    # to count the number of zeroes we only need to count the number of 5 multiples and 2 multiples.
    # There will always be more multiples of 2 than 5, so simple counting the number of 5's multiples
    # should be sufficient.
    # there are two cases for multiples of 5, eg 15 and 25. 15 contributes one multiple of 5 and therefore one
    # trailing zero whereas 25 contributes 2 coz it has 2 multiples of 5 (5 * 5).

    # one way - iterate through 2-n and count the number of times 5 goes into each number. if the number is 5,
    # return which power of 5 is it. so 5 =1 , 25 = 2, 125 = 3
    # look below for other way
    count = 0
    for i in range(2, num + 1):
        count += get_factors_of_five(i)
    return count


def factorial_zeroes_another_way(num):
    # We try to count the factors of 5 directly. First count the number of multiples of 5 between 1 - num(which is num/5)
    # and then number of multiples of 25(which is num/25) and number of multiples of 125, so on..
    count = 0
    if num < 0:
        return
    i = 5
    while num / i > 0:
        count += i / 5
        i *= 5
    return count


def get_factors_of_five(num):
    count = 0
    while num % 5 == 0:
        count += 1
        num /= 5
    return count


def smallest_difference(numbers1, numbers2):
    # given 2 lists of numbers compute the pair of values(one from each list) with the smallest
    # non negative difference.
    # eg: [1, 3, 15, 11, 2], [23, 127, 235, 19, 8]
    # ans: 3 (11, 8)
    # sort the two arrays and then iterate through the lists by moving forward in the list which has the smaller number
    numbers1.sort()
    numbers2.sort()
    diff = None
    i = 0
    j = 0
    while i in range(len(numbers1)) and j in range(len(numbers2)):
        if diff == None:
            diff = abs(numbers1[i] - numbers2[j])
        else:
            curr_diff = abs(numbers1[i] - numbers2[j])
            if curr_diff < diff:
                diff = curr_diff

        # move forward in the list which had the smaller number
        if numbers1[i] < numbers2[j]:
            i += 1
        else:
            j += 1
    return diff

#print smallest_difference([1, 2, 11, 15], [4, 12, 19, 23, 127, 235])
#print smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])


def number_max(a, b):
    # find max of 2 numbers without using if else of any comparison operator
    pass

smalls = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
              "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
              "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
bigs = ["", "thousand", "million", "billion"]
negative = "negative"


def english_int(num):
    # given an integer print the english phrase that describes the number
    # eg: 1,234 = One thousand, two hundred thirty four.

    # convert number to string
    if num == 0:
        return smalls[0]
    if num < 0:
        return negative + " " + english_int(-1 * num)
    # for a positive integer
    parts = []

    chunk_count = 0
    while num > 0:
        if num % 1000 != 0:
            # thousands, million, billion
            words = convert_by_part(num % 1000)
            words = " ".join(words)
            chunk = words + " " + bigs[chunk_count]
            parts.append(chunk)
        num /= 1000
        chunk_count += 1
    number_in_words = ""

    # parts list contains the in words of the number in reverse order.
    while parts:
        top = parts.pop()
        number_in_words += top
        number_in_words += " "
    return number_in_words


def convert_by_part(num):
    parts = []

    # converts 100s place
    if num >= 100:
        parts.append(smalls[num / 100])
        parts.append(hundred)
        num %= 100

    # convert 10s place
    if num >= 10 and num <= 19:
        parts.append(smalls[num])
    elif num >= 20:
        parts.append(tens[num / 10])
        num %= 10

    # convert 1's place
    if num >= 1 and num <= 9:
        parts.append(smalls[num])
    return parts


#print english_int(5066000000)


def operation(a, b):
    # write methods to implement multiply, subtract and divide operations for integers.
    # The results of all of these are integers. Use only the add operator.
    pass


def operation_subtract(a, b):
    return a + negate(b)


def operation_multiply(a, b):
    # multiplying a times b is adding a to itself b times.
    if a < b:
        return operation_multiply(b, a)  # it is faster is b is less than a
    product = 0
    for i in range(abs(b)):
        product += a
    if b < 0:
        product = negate(product)
    return product


def operation_divide(a, b):
    # x = a/b also means bx = a. Keep adding b x times till you get a
    if b == 0:
        raise ZeroDivisionError
    absa = abs(a)
    absb = abs(b)
    product = 0
    x = 0
    while product + absb <= absa:
        product += absb
        x += 1

    if a < 0 and b < 0 or (a > 0 and b > 0):
        return x
    return negate(x)


def negate(num):
    # flip the sign of a number
    neg = 0
    new_sign = 1 if num < 0 else -1
    while num != 0:
        neg += new_sign
        num += new_sign
    return neg

#print negate(-2)
#print operation_multiply(-2, -3)
#print operation_divide(10, 5)


def living_people(births, deaths, min_year, max_year):
    # given a list of people with their birth and death years implement a method to compute
    # the year with maximum number of people alive.
    # O(PlogP) where P is the number of people
    births = births.sort()
    deaths = deaths.sort()
    current_alive = 0
    max_alive = 0
    max_alive_year = min_year
    birth_index = 0
    death_index = 0
    while birth_index < len(births):
        if births[birth_index] <= deaths[death_index]:  # include birth before death so that we can coutn the person alive that year
            current_alive += 1
            if current_alive > max_alive:
                max_alive = current_alive
                max_alive_year = births[birth_index]
            birth_index += 1  # move forward in the births array
        else:
            current_alive -= 1  # someone died
            death_index += 1  # move forward in the deaths array
    return max_alive_year


def diving_board(k, shorter, longer):
    # 0 of type A, K of type B; 1 of type A, K-1 of type B; 2 of type A, K-2 of type B;..
    # go through unique sets of k planks
    all_lengths = []
    for nshorter in range(k + 1):
        nlonger = k - nshorter
        length = nshorter * shorter + nlonger * longer
        all_lengths.append(length)
    # we want set since we want unique combinations only.
    return list(set(all_lengths))


def xml_encoding():
    pass


def bisect_squares():
    # find line cutting two squares in half
    pass

from collections import defaultdict


def master_mind(guess, solution):
    # given a guess and solution count number of hits and pseudo hits
    # go through the guess and count the number of hits.
    # when it doesnt match with solution not the color in the solution and
    # its count
    hit_count = 0
    pseudo_hit_count = 0
    unmatched_colors = defaultdict(int)
    for index, color in enumerate(guess):
        if color == solution[index]:
            hit_count += 1
        else:
            # keep track of solution colors that did not match. This is used for counting pseudohits
            unmatched_colors[solution[index]] += 1

    # traverse the guess again and see if any of the guess is a pseudo hit
    for index, color in enumerate(guess):
        if unmatched_colors.get(color) and unmatched_colors[color] > 0 and color != solution[index]:
            pseudo_hit_count += 1
            unmatched_colors[color] -= 1
    return hit_count, pseudo_hit_count


#print master_mind("GGRR", "RGBY")


def sub_sort(integers):
    # given an array of integers write a method to find indices m and n such that if you sorted elements m
    # through n the entire array would be sorted. Minimize n -m, find the smallest such sequence.
    # assuming positive integers
    max_so_far = 0
    prev = 0
    start = 0
    mid_begin_index = 0
    mid_end_index = 0
    while mid_begin_index == 0:
        if integers[start] > max_so_far:
            max_so_far = integers[start]
        if start > 0:
            if integers[start] < prev:
            # keep going back till current integer is larger
                mid_begin_index = start - 1
                while integers[start] < integers[mid_begin_index]:
                    mid_begin_index -= 1
        prev = integers[start]
        start += 1

    start = start - 1  # get it back to where it was. It increments end of the while loop which we dont need for the last time.
    # keep going right from where we stopped, i.e at start till we  find 2 conseutive numbers greater than max_so_far
    while mid_end_index == 0:
        if integers[start + 1] > max_so_far and integers[start + 2] > max_so_far:
            mid_end_index = start
            break
        start += 1
    return mid_begin_index, mid_end_index

print sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])


def contiguous_sequence(integers):
    # given an array of integers both positive and negative. find the contiguous sequence of largest sum
    max_sum = 0
    current_sum = 0
    start = 0
    end = len(integers)
    while start < end:
        current_sum += integers[start]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
        start += 1
    return max_sum
print contiguous_sequence([2, -8, 3, -2, 4, -10])
print contiguous_sequence([-2, -1])


def contiguous_sequence_negative_numbers(integers):
    # given an array of integers both positive and negative. find the contiguous sequence of largest sum
    # this handles all negative numbers
    max_so_far = integers[0]
    current_max = integers[0]
    start = 1
    end = len(integers)
    while start < end:
        current_max = max(integers[start], integers[start] + current_max)
        max_so_far = max(max_so_far, current_max)
        start += 1
    return max_so_far

print contiguous_sequence_negative_numbers([-2, -1])


def pattern_matching():
    pass


def pond_sizes(land):
    # integer matrix representing plot of land where value represents height above sea level.
    # A value of zero indicates water.
    rows = len(land)
    cols = len(land[0])
    visited = [[0 for row in range(rows)] for col in range(cols)]
    pond_sizes = []
    for row_index in range(rows):
        for col_index in range(cols):
            size = compute_size(land, visited, row_index, col_index)
            if size > 0:
                pond_sizes.append(size)
    return pond_sizes


def compute_size(land, visited, row_index, col_index):
    # calculate the size of a possible pond
    if row_index < 0 or col_index < 0 or row_index >= len(land) or col_index >= len(land[0]):
        return 0
    if visited[row_index][col_index] == True or land[row_index][col_index] != 0:
        return 0
    size = 1
    # set visited to true
    visited[row_index][col_index] = True
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            size += compute_size(land, visited, row_index + dr, col_index + dc)
    return size
print pond_sizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]])


def T9():
    pass


import datetime


def max_tv_show_bandwidh(show_details):
    #show details is expected to be something like this
    # [(datetime.time(start_time), datetime.time(end_time), bandwidht), (), ]
    max_bandwidth = 0
    show_details = sorted(show_details, key=lambda x: (x[0], x[1]))
    prev_start_time = None

    for index, show in enumerate(show_details):
        start_time = show[0]
        # we dont want to recalculate for same start time more than once.
        if start_time == prev_start_time:
            continue
        current_bandwidth = show[2]
        if index == 0:
            other_shows = show_details[1:]
        elif index == len(show_details) - 1:
            other_shows = show_details[:len(show_details) - 1]
        else:
            other_shows = show_details[:index] + show_details[index + 1:]

        for other_show in other_shows:
            other_show_start_time = other_show[0]
            other_show_end_time = other_show[1]

            # we dont want to worry about shows that start later.
            # Since we sorted this already, all shows are arranged in increasing order of time.
            if other_show_start_time > start_time:
                break
            # see if the start time falls within the time range of any other show.
            if start_time >= other_show_start_time and start_time < other_show_end_time:
                current_bandwidth += other_show[2]
        max_bandwidth = max(current_bandwidth, max_bandwidth)
        prev_start_time = start_time
    return max_bandwidth

print "TV"
print max_tv_show_bandwidh([(datetime.time(13), datetime.time(15), 2),
                      (datetime.time(11), datetime.time(13), 2),
                      (datetime.time(13, 30), datetime.time(14), 5),
                      (datetime.time(10), datetime.time(12), 3),
                      (datetime.time(10), datetime.time(11), 3)])


def strong_and_weak_links(array1, array2):
    strong_links = 0
    weak_links = 0
    shorter_num_frequency_map = defaultdict(int)
    longer_num_frequency_map = defaultdict(int)
    strong_links_count_map = defaultdict(int)

    # iterate over the shorter to find the strong links since we need same number at the same position
    if len(array1) > len(array2):
        shorter = array2
        longer = array1
    else:
        shorter = array1
        longer = array2

    # calculate frequency of each number in the shorter array and strong links
    for index, item in enumerate(shorter):
        if item == longer[index]:
            strong_links += 1
            strong_links_count_map[item] += 1
        shorter_num_frequency_map[item] += 1

    # iterate over the longer array to find the frequency of each number
    for item in longer:
        longer_num_frequency_map[item] += 1

    # iterate over the longer array to calculate the weak links
    for item, frequency in longer_num_frequency_map.items():
        if shorter_num_frequency_map.get(item):
            weak_links += (shorter_num_frequency_map[item] * frequency) - strong_links_count_map.get(item, 0)
    return strong_links, weak_links

print "LINKS"
print strong_and_weak_links([2, 3, 4, 6, 9, 3], [3, 3, 6, 1, 9, 11, 2])
print strong_and_weak_links([2, 3, 4, 6, 9, 12], [3, 3, 6, 1, 9, 11, 2])
print strong_and_weak_links([3, 3, 3], [1, 3, 3, 5, 3])


def sum_swap(array1, array2):
    # given two arrays of integers find a pair than you can swap to give the two arrays the same sum
    # input: [4, 1, 2, 1, 1, 2], [3, 6, 3, 3]
    # output : 1, 3
    # time and space O(N)
    sum_array_1 = sum(array1)
    sum_array_2 = sum(array2)
    difference = abs(sum_array_2 - sum_array_1)

    # convert each array to a dict
    # sum could be found while this instead of doing that separately
    array1_dict = defaultdict(int)
    array2_dict = defaultdict(int)

    for item in array1:
        array1_dict[item] += 1

    for item in array2:
        array2_dict[item] += 1

    # iterate over the shorter array to see if a pair that sums upto the difference can b found.
    for item in array1:
        if array2_dict.get(difference - item):
            return difference - item, item
    return "Pair not found"


print sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])


def t9():
    # create a hash table that maps from a sequence of digits to a list of strings
    # go through each word in the dictionary and convert to its t9 representation. Store each of these in
    # the above hash table.
    # Lookup the number for all possible words.
    pass


def rand7_from_rand5():
    # given a method that generates a random integer from 0-4, write a method
    # that generates a random number between 0-6 (inclusive)
    pass


def pairs_with_sum(integers, summ):
    # all pairs of integers within an array that sum to a specified value
    # time and space : O(n)

    # convert integers to a dict
    intgers_dict = defaultdict(int)
    for integer in integers:
        if not intgers_dict.get(integer):
            intgers_dict[integer] = summ - integer

    # iterate through the dict to see if the difference between  the sum and the integer is also present.
    for item, diff in intgers_dict.items():
        if intgers_dict.get(diff):
            print item, diff


def lru_cache():
    # design a least recently used cache which evicts the least recently used item.
    # the cache should map keys to values.
    # inserting key, value pair: Create a linked list node with a key, value. Insert into the head of the
    # linked list. Insert key - node mapping into the hash table
    # Retrieving value by key: Lookup node in hash table and return. Update most recently used.
    # Finding least recently used: end of the linked list
    # Update most recently used: Move node to front of the linked list.
    # Eviction: remove tail from linked list and key from hash table.
    pass


def calculator():
    # evaluate an arithmetic expression
    # maintain two stacks, one of numbers and one for operators
    # each time we see a number it gets pushed to the number_stack
    # operator gets pushed into the operator stack as long as it has a priority higher than the current top.
    # if priority <= top operators priority then we collapse the top of both stacks.
    # pop 2 elements off the number stack, pop an operator off the operator stack, apply the operator and push
    # the result back to the number stack.
    # At the end we collapse the stack.
    pass






