def fibo(n):
    # Time : O(n)
    # Bottom up
    # Space : O(n)
    fib_table = []
    for i in range(2, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])
    return fib_table


def fibo_2(n):
    # Space: O(1)
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


fact_table = {}


def factorial(n):
    # Time : O(max(m, n))
    try:
        return fact_table[n]
    except KeyError:
        if n == 0:
            return 1
        else:
            fact_table[n] = n * factorial(n - 1)
            return fact_table[n]


def longest_common_subsequence(X, Y):
    # explanation here: https://www.youtube.com/watch?v=NnD96abizww
    table = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    # row 0 and coloumn 0 are initialized to 0 already
    # construct the matrix for dp
    for i, x in enumerate(x):
        for j, y in enumerate(y):
            if x == y:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])

    # read the substring from the matrix
    # note elements when the movement is diagonal only.
    result = ""
    x, y = len(X), len(Y)
    while x != 0 and y != 0:
        if table[x][y] == table[x - 1][y]:
            x -= 1
        else:
            assert X[x - 1] == Y[y - 1]
            result = X[x - 1] + result
            x -= 1
            y -= 1
    return result


def maximum_contiguous_sum(A):
    # Time : O(n)
    # Space : O(n)
    n = len(A)
    M = [0] * (n + 1)
    if A[0] > 0:
        M[0] = A[0]
    else:
        M[0] = 0
    for i in range(1, n):
        if M[i - 1] + A[i] > 0:
            M[i] = M[i - 1] + A[i]
        else:
            M[i] = 0
    return max(M)


print maximum_contiguous_sum([-2, 3, -16, 100, -4, 5])


def max_sum_no_two_contiguous_numbers(A):
    # Time: O(n)
    # Space : O(n)
    n = len(A)
    M = [0] * (n + 1)
    if A[0] > A[1]:
        M[0] = A[0]
    else:
        M[0] = A[1]
    for i in range(2, n):
        if(M[i - 1] > M[i - 2] + A[i]):
            M[i] = M[i - 1]
        else:
            M[i] = M[i - 2] + A[i]
    return M[n - 1]

print "HI"
print max_sum_no_two_contiguous_numbers([4, 5, 6, 7])


# return max sum such that no two elements are next to each other. Dynamoc programming thief and stolen values.
def find_max_non_adjacent_numbers(houses):
    incl = 0
    excl = 0
    for house in houses:
        temp = incl
        incl = max([temp, excl + house])
        excl = temp
        print temp, incl, excl, house
    return max([incl, excl])

print find_max_non_adjacent_numbers([4, 5, 6, 7])


def knapsack_no_dup(knap_sack_size, items_value, items_weight):
    #https://www.youtube.com/watch?v=8LusJS5-AGo
    num_items = len(items_value)
    M = [[0 for x in range(knap_sack_size + 1)] for x in range(len(items_value))]
    for i in range(1, num_items):
        for j in range(knap_sack_size + 1):
            value = items_value[i]
            weight = items_weight[i]
            if weight > j:
                M[i][j] = M[i - 1][j]
            else:
                M[i][j] = max(M[i - 1][j], (M[i - 1][j - weight] + value))

    return M[num_items - 1][knap_sack_size]


print knapsack_no_dup(50, [60, 100, 120], [10, 20, 30])


def max_sum_longest_increasing_subsequence(arr):
    #https://www.youtube.com/watch?v=99ssGWhLPUE
    # Time : O(n^2)
    # Space : O(n)
    n = len(arr)
    msis = [0 for x in range(n)]
    # Initialize msis values for all indexes
    for i in range(n):
        msis[i] = arr[i]

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                msis[i] = max(msis[i], msis[j] + arr[i])
    return max(msis)

print max_sum_longest_increasing_subsequence([4, 6, 1, 3, 8, 4, 6])


from collections import defaultdict


def longest_increasing_subsequence_n_square(arr):
    n = len(arr)
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1] * n
    posn_values_map = defaultdict(list)
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                if lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    posn_values_map[i].append(arr[j])

    # return length of longest increasing subsequence
    length_of_lis = max(lis)
    index_lis = lis.index(length_of_lis)
    numbers_in_lis = posn_values_map[index_lis]
    numbers_in_lis.append(arr[index_lis])

    return length_of_lis, numbers_in_lis

print "LONGEST INCREASING SUBSEQUENCE"
print longest_increasing_subsequence_n_square([3, 4, -1, 0, 6, 2, 3])
print longest_increasing_subsequence_n_square([10, 22, 9, 33, 21, 50, 41, 60])


def longest_increasing_subsequence_n_log_n(A):
    pass


def longest_palindrome(self):
    pass


def subset_sum(self):
    pass


