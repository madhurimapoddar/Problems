def check_duplicates_by_sorting(numbers):
    # time : O(nlogn)
    # space : O(1)
    numbers.sort()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[i + 1]:
                print "Duplicate exists"
                return
    print "No duplicate"
    return


def check_who_wins_election(A):
    # given an array of integers [0......n-1], where the integers represent the id of the chosen candidate.
    # give an algorithm to see who wins the election
    # heapsort to sort inplace
    # time : O(nlogn)
    # space : O(1)
    A.sort()
    counter = maxcounter = 0
    candidate = maxcandidate = 0
    for i in range(len(A)):
        if A[i] == candidate:
            counter += 1
        else:
            counter = 1
            candidate = A[i]
        if counter > maxcounter:
            maxcandidate = A[i]
            maxcounter = counter
    print maxcounter, maxcandidate


def find_sum_in_lists(A, B, k):
    # A and B are two arrays of n elements each. Given a number K, find a O(nlogn) algorithm
    # for determining whether there exists a aEA and bEB such that a + b = K
    A.sort()
    for i in range(len(B)):
        c = k - B[i]
        if binary_search(A, c) != -1:
            return 1
    return 0


def binary_search(A, value):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == value:
            return mid
        elif value < A[mid]:
            high = mid
        else:
            low = mid + 1
    return -1


def find_sum_in_3_lists(A, B, C, k):
    # same as above, except 3 lists
    # nlog(n)
    sum_dict = {}
    for item in A:
        if item not in sum_dict:
            sum_dict[item] = k - item
    for key, value in sum_dict.items():
        i = 0
        while i < len(C):
            if value - C[i] in B:
                print key, C[i], value - C[i]
            i += 1
    return


find_sum_in_3_lists([2, 3, 4], [1, 1, 2], [3, 4, 5], 7)


def sort_0_1_2_quick_sort(A, low, high):
    # quick_sort with a pivot of 1
    # quick sort will only use one scan
    # O(n)
    # space: O(1)
    if low < high:
        pivot = partition(A, low, high)
        sort_0_1_2_quick_sort(A, low, pivot - 1)
        sort_0_1_2_quick_sort(A, pivot + 1, high)


def partition(A, low, high):
    pivot = low
    swap(A, pivot, high)
    for i in range(low, high):
        if A[i] <= A[high]:
            swap(A, i, low)
            low += 1
    swap(A, low, high)
    return low


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

A = [0, 1, 1, 0, 2, 1, 2]
sort_0_1_2_quick_sort(A, 0, 6)
print A


def find_number_appearing_max_time_in_an_array(numbers):
    # use a dictionary
    # BST and in order traversal
    # O(n)
    pass


def merge(A, m, B, n):
    # given 2 sorted arrays of size m and n
    # A has m elements but is of size m + n
    # B has n elements and is of size n
    # Merge B into A and the data needs to be sorted
    # O(m + n) and space O(1)
    i = n - 1
    j = k = m - 1
    while k >= 0:
        if (B[i] > A[j] or j < 0):
            A[k] = B[i]
            i -= 1
            if i < 0:
                break
        else:
            A[k] = A[j]
            j -= 1
        k -= 1


def find_element_in_2d_sorted_array(matrix, value):
    # each row and each column are sorted
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    if cols == 0:
        return 0

    i = 0
    j = cols - 1
    # start from end col first row since they are sorted.
    while i < rows and j <= 0:
        if matrix[i][j] == value:
            return 1
        elif matrix[i][j] < value:
            i += 1
        else:
            j -= 1
    return 0


### Running mean/Moving average
def running_mean(l, N):
    sum = 0
    result = list(0 for x in l)

    for i in range(0, N):
        sum = sum + l[i]
        result[i] = sum / (i + 1)

    for i in range(N, len(l)):
        sum = sum - l[i - N] + l[i]
        result[i] = sum / N
    return result

