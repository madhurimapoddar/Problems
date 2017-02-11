def find_missing_number(numbers):
    # for a range of 1-n integers, find the missing number
    # eg [1, 2, 4, 6, 3, 7, 8], ans: 5
    found = {}
    for i in range(1, len(numbers) + 1):
        if i in numbers:
            found[i] = 1
        else:
            found[i] = 0

    for number in found:
        if found[number] == 0:
            print number
            return
    print "Nothing is missing"
    return

#find_missing_number([1, 2, 4, 6, 3, 7, 8])


def find_missing_number_using_summation(numbers):
    # better
    # get the sum of all numbers = n*(n + 1)/2
    # Subtract all the numbers from the sum and you will find the missing number
    # time : O(n), space = o(1)
    count = len(numbers) + 1
    total = (count * (count + 1)) / 2
    sum_numbers = sum(numbers)
    print total - sum_numbers

#find_missing_number_using_summation([1, 2, 4, 6, 3, 7, 8])


def find_missing_number_using_xor(numbers):
    # XOR all the array elements, let the result XOR be X
    # XOR all the numbers from 1-n, let XOR be Y
    # XOR X and Y gives the missing
    count = len(numbers)
    X = 0
    for i in range(1, count + 2):
        X = X ^ i
    for i in range(count):
        X = X ^ numbers[i]
    print X

find_missing_number_using_xor([1, 2, 3, 6, 5, 7, 8])


def find_number_occurring_odd_number_of_times(numbers):
    # time : O(n), space: O(1)
    # 2 ^ 2 = 0
    # 2 ^ 2 ^ 2 = 2
    count = len(numbers)
    X = 0
    for i in range(count):
        X = X ^ numbers[i]
    print X

find_number_occurring_odd_number_of_times([1, 2, 3, 2, 3, 1, 3])


def find_two_numbers_that_sum_to_x(numbers, K):
    # given a list of numbers find 2 numbers whose sum = K
    numbers_dict = {}
    for num in numbers:
        if num in numbers_dict:
            numbers_dict[num] += 1
        else:
            numbers_dict[num] = 1

    for num in numbers_dict:
        if K - num in numbers_dict:
            print num, K - num
            return
    print "Doesn't exist"

find_two_numbers_that_sum_to_x([1, 2, 3, 4, 5], 9)


import sys
def find_two_elements_whose_sum_is_closest_to_zero(numbers):
    # sort first
    # maintain 2 indexes, one at the beginning, one at the end
    # maintain 2 variables to keep track of smallest positive sum closed to zero and smallest
    # negative sum closest to zero.
    # if current pair sum > zero and < positive closest, update positive closest
    # if current pair sum is < zero and > negative closest, update negative closest
    # else print the pair
    # Time : O(nlogn)
    numbers.sort()
    count = len(numbers)
    left_index = 0
    right_index = count - 1
    min_left = 1
    min_right = count - 1
    min_sum = sys.maxint
    while(left_index < right_index):
        pair_sum = numbers[left_index] + numbers[right_index]
        if abs(min_sum) > abs(pair_sum):
            min_sum = pair_sum
            min_left = left_index
            min_right = right_index
        if pair_sum < 0:
            left_index += 1
        else:
            right_index -= 1
    print numbers[min_left], numbers[min_right]

find_two_elements_whose_sum_is_closest_to_zero([1, 60, -10, 70, -80, 85])


def find_three_elements_whose_sum_add_to_k(numbers, K):
    # given an array find 3 elements whose sum add to K

    # store sum of all pairs in a dict, sum = key, pair = value
    pass


def find_minimum_in_rotated_sorted_array(numbers):
    # TODO : find O(logN) solution using a variation of binary search
    last = numbers.pop()
    count = len(numbers) - 1
    while numbers:
        second_last = numbers.pop()
        if last > second_last:
            last = second_last
            count = count - 1
        else:
            print count
            break


def find_minimum_in_rotated_sorted_array_log_n_time(numbers):
    mid = 0
    low = 0
    high = len(numbers) - 1
    while numbers[low] >= numbers[high]:
        if high - low <= 1:
            print numbers[high], high
            return
        mid = (low + high) >> 1
        if numbers[mid] == numbers[low]:
            low += 1
        elif numbers[mid] > numbers[low]:
            low = mid
        elif numbers[mid] == numbers[high]:
            high -= 1
        else:
            high = mid
    print numbers[low], low
    return

find_minimum_in_rotated_sorted_array([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14])
find_minimum_in_rotated_sorted_array([1, 2, 3, 4, -3, -2, -1, 0])

find_minimum_in_rotated_sorted_array_log_n_time([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14])



def find_index_where_0_start(array):
    # given an extremely long array that has 1s in the beginning and 0s at the end, find the
    # index where 0s start
    # check the bits at the rate of 2^k where k = 0,1,2,3..n since we are moving at the rate of 2.
    # O(logN)
    pass


def find_element_in_an_array_that_has_been_rotated_unknown_times(numbers, target):
    # the initial array was sorted and then rotated many times
    # eg: find 5 in [15, 16, 19, 20, 1, 3, 4, 5, 7, 10, 14]
    # Time : O(logN)
    # find pivot point and then divide the array into 2 subarrays
    # Call binary search on one of the 2 subarrays
    # if the element is greater than the first element, search left subarray
    # else search right array
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) / 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] >= numbers[left]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

target_index = find_element_in_an_array_that_has_been_rotated_unknown_times([15, 16, 19, 20, 1, 3, 4, 5, 7, 10, 14], 4)
print target_index


def find_first_occurence_of_a_number_in_a_sorted_array(numbers, target):
    # binary search first occurance
    # time : O(logN)
    high = len(numbers) - 1
    low = 0
    m = 0
    last_found = -1
    while True:
        if low > high:
            print last_found
            return
        m = (low + high) / 2
        if numbers[m] == target:
            last_found = m
            # at this point check if it occurs again in the first half of the array
            high = m - 1
        if numbers[m] < target:
            low = m + 1
        else:
            high = m - 1
    print m

find_first_occurence_of_a_number_in_a_sorted_array([5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 70, 84], 21)


def find_last_occurence_of_a_number_in_a_sorted_array(numbers, target):
    # binary search
    # time : O(logN)
    # mid == high && A[mid] == data || A[mid] == data && A[mid + 1] > data
    high = len(numbers) - 1
    low = 0
    m = 0
    last_found = -1
    while(True):
        if low > high:
            print last_found
            return
        m = (low + high) / 2
        if numbers[m] == target:
            last_found = m
            low = m + 1
        if numbers[m] < target:
            low = m + 1
        else:
            high = m - 1
    print m

find_last_occurence_of_a_number_in_a_sorted_array([5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 70, 84], 21)


def linerar_search_count(numbers, data):
    # given a sorted array of n elements, possibly with duplicates, find the number of occurences of a number
    # binary search
    # O(logN + S) where S is the number of occurences
    # alternate is lastOccurance - firstOccurence + 1
    low = 0
    high = len(numbers) - 1
    found_position = 0
    #import debug
    while(low <= high):
        mid = (low + high) / 2
        if numbers[mid] == data:
            found_position = mid
            break
        elif numbers[mid] < data:
            low = mid + 1
        elif numbers[mid] > data:
            high = mid - 1
    left_count = right_count = 0
    for i in range(0, found_position):
        if numbers[i] == data:
            left_count += 1
    for i in range(found_position + 1, high):
        if numbers[i] == data:
            right_count += 1
    print left_count + 1 + right_count


linerar_search_count([5, 6, 6, 6, 7, 7, 8], 6)


def find_majority_element(numbers):
    # An element is a majority if it appears more than n/2 times
    # time : O(n)
    # dont really get it
    count = 0
    element = -1
    length = len(numbers)
    if length == 0:
        return
    for i in range(length - 1):
        if count == 0:
            element = numbers[i]
            count = 1
        elif element == numbers[i]:
            count += 1
        else:
            count -= 1
    print element
    return

find_majority_element([7, 3, 2, 3, 3, 6, 3])


def find_element_occurring_most_number_of_times(numbers):
    # an array with 2n elements, where n elements are same and
    # remaining are all different. Find the majority element
    # atleast 2 elements will be next to each other
    # or all duplicate will be at a relative distance of 2
    # compare A[i] with A[i+1]
    # or compare A[i] with A[i+2]
    # time : O(N)
    pass


def find_lonely_integer(numbers):
    # given an array  with 2n + 1 integers, n elements appear twice in arbitrary locations.
    # A single element applears only once somewhere. Find the lonely integer.
    res = 0
    for i in range(len(numbers)):
        res = res ^ numbers[i]
    print res

find_lonely_integer([7, 4, 6, 4, 4, 6, 7])


def throwing_eggs_from_n_story_building():
    # divide and conquer chapter
    pass


def local_min_of_array(numbers):
    # an index i such that A[i-1] < A[i] < A[i+1]
    # check middle value at A[n/2] and its right and left neighbors. If A[n/2] is local min the stop,
    # else search in half with smaller neighbor
    # time : O(logN)
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) / 2
        if numbers[mid - 1] < numbers[mid] < numbers[mid + 1]:
            print numbers[mid]
            return
        else:
            if numbers[mid - 1] > numbers[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
    return


def find_element_present_in_2d_array(array):
    # n*n elements, rows and columns in ascending order
    # find an element in O(n) time
    pass


def find_pair_of_indices_in_2d_array(array):
    # n*n elements, find pair of indices i and j such that A[i][j] < A[i+1][j],
    # A[i][j] < A[i][j + 1],
    # A[i][j] < A[i-1][j],
    # A[i][j] < A[i][j -1 1]
    pass


def find_row_with_max_zeros(array):
    # given a n by n matrix, each row starts with 1s and ends with zeros
    # find the row with max zeros
    rows = len(array)
    columns = len(array[0])
    row_with_max_zero = 0
    col = columns - 1
    zero_count = 0
    for i in range(rows):
        while col >= 0:
            if array[i][col] == 0:
                zero_count += 1
                col -= 1
                row_with_max_zero = i
            else:
                break
    print row_with_max_zero, zero_count


find_row_with_max_zeros([[1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]])


def separate_even_and_odd(numbers):
    # input: [12, 34, 45, 9, 8, 90, 3]
    # output: [12, 34, 90, 8, 9, 45, 3]
    # similar to Dutch national flag problem
    # logic is similar to quicksort
    # initialize two index variables, left and right
    # keep incrememnting left until u see an odd number
    # keep decrementing right until u see an even number
    # if left < right swap A[left] and A[right]
    # time: O(N)
    left = 0
    right = len(numbers) - 1
    while left < right:
        while(numbers[left] % 2 == 0 and left < right):
            left += 1
        while(numbers[right] % 2 == 1 and left < right):
            right -= 1

        if left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
    print numbers

separate_even_and_odd([12, 34, 45, 9, 8, 90, 3])


def separate_ones_and_zeroes(numbers):
    # count number of 0s,
    # put 1s in the remaining positions
    # same as separate_even_and_odd
    pass


def sort_0_1_2_in_array(numbers):
    # dutch flag problem
    pass
    














