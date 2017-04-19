

def add_without_plus(a, b):
    pass


def letters_and_numbers(array):
    # given an array filled with letters and numbers, find the longest subarray with equal
    # letters and numbers

    # count the number of letters and numbers
    letters_counts = []
    numbers_counts = []
    numbers_count = 0
    letters_count = 0
    for index, item in array:
        if type(item) == str:
            letters_count += 1
            letters_counts[index] = letters_count
        else:
            numbers_count += 1
            numbers_counts[index] = numbers_count

    # find the difference between the two counts. Find pair with matching difference and largest span
    # store the difference in a hash table first time we see it. Each time we see the same difference
    # again we see if the subarray is bigger than the current max.
    diff = []
    difference_map = {}
    for index, item in letters_counts:
        diff[index] = item - numbers_counts[index]

    # build the dictionary
    max_span = [0, 0]  # store start and end index
    for index, item in diff:
        if not difference_map.get(item):
            difference_map[item] = index
        else:
            match = difference_map.get(item)
            distance = index - match
            longest = max_span[1] - max_span[0]
            if distance > longest:
                max_span[1] = index
                max_span[0] = match
    return array[max_span[0] + 1: max_span[1]]


def count_of_twos(n):
    # count the number of 2s between 0-n
    # eg: 25 - 9 (2, 12, 20, 21, 22, 23, 24, 25)
    pass


def baby_names():
    # parse list and initialize equivalence set
    pass





