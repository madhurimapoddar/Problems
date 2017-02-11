def remove_duplicates(numbers):
    unique = []
    helper_set = set()
    for num in numbers:
        if num not in helper_set:
            unique.append(num)
            helper_set.add(num)
    print unique


def check_two_arrays_same_or_not(array1, array2):
    # give 2 arrays or unordered numbers check whether both
    # arrays have same set of numbers
    # A = [2, 5, 6, 8, 10, 2, 2]
    # B = [2, 5, 5, 8, 10, 5, 6]
    array_1_dict = {}
    for item in array1:
        if item in array_1_dict:
            array_1_dict[item] = array_1_dict[item] + 1
        else:
            array_1_dict[item] = 1

    for item in array2:
        if item in array_1_dict:
            array_1_dict[item] = array_1_dict[item] - 1
        else:
            print "not same"
            break
    if not any(array_1_dict.values()):
        print "Same"
    return


def get_symmetric_pairs(pairs):
    # report all pairs (i, j) and (j, i)
    # [{1, 3}, {2, 6}, {3, 5}, {7, 4}, {5, 3}, {8, 7}]
    # ans: {3,5} and {5, 3}
    # O(n)
    pairs_dict = {}
    for pair in pairs:
        # check if value exists as the key
        # if yes then if its a symmetric pair
        if pair[1] in pairs_dict:
            if pairs_dict[pair[1]] == pair[0]:
                print pair
        if pair[0] not in pairs_dict:
            pairs_dict[pair[0]] = pair[1]
    return

get_symmetric_pairs([(1, 3), (7, 8), (3, 5), (7, 4), (5, 3), (8, 7)])


def does_linked_list_have_loop(node):
    # store data: next
    # if next is already in the dict then there is a loop
    # O(n)
    pass


def remove_chars_from_a_string(string, remove_these_chars):
    # remove specified chars from a string given in another string
    table = {}
    temp = []
    for char in remove_these_chars.lower():
        table[char] = 1
    for char in string.lower():
        if char in table:
            continue
        else:
            temp.append(char)
    print "".join(temp)

remove_chars_from_a_string("careermonk", "ek")


def find_first_non_repeated_char(string):
    char_count_dict = {}
    for char in string:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] = char_count_dict[char] + 1
    for char in string:
        if char_count_dict.get(char) == 1:
            print char
            break

find_first_non_repeated_char("careermonk")


def find_first_repeating_char(string):
    char_count_dict = {}
    for char in string:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            print char
            break

find_first_repeating_char("careermonk")


def get_pairs_that_sum_to_S(numbers, S):
    # given a list of numbers find all pairs that sum to S
    numbers_dict = {}
    for num in numbers:
        if num not in numbers_dict:
            numbers_dict[num] = num
    for num in numbers:
        if S - num in numbers_dict:
            print S - num, num

get_pairs_that_sum_to_S([1, 2, 3, 4, 5, 6, 7], 9)
