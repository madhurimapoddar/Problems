import heapq
from collections import deque


class Heap(object):
    def __init__(self):
        self.heap_list = [0]  # elements in the heap
        self.size = 0  # size of the heap/ number of elements

    def parent(self, index):
        # parent is at (i-1)/2
        return index / 2

    def left_child(self, index):
        # 1 is added since the array index begins at 0
        # Time complexity : O(1)
        return 2 * index + 1

    def right_child(self, index):
        # Time complexity : O(1)
        return 2 * index + 2

    def get_max(self):
        # this is a maxheap
        # Time complexity : O(1)
        if self.size == 0:
            return -1
        else:
            return self.heap_list[0]

    def get_min(self):
        # this is minheap
        # Time Complexity : O(1)
        if self.size == 0:
            return -1
        else:
            return self.heap_list[0]

    def perc_down(self, index):
        # move down. used for del min
        # Time Complexity : O(logn)
        while(index * 2) <= self.size:
            min_child = self.get_min_child(index)
            if self.heap_list[index] > min_child:
                # swap minchild with current
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[min_child]
                self.heap_list[min_child] = temp
            index = min_child

    def get_min_child(self, index):
        if (index * 2) + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def perc_up(self, index):
        # used for adding to max heap / insert
        # add at the end and then move up to adjust
        # Time Complexity : O(logn)
        # Heap is a complete binary tree.
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                # swap to move up
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    def delete_max(self):
        # delete max from max heap
        # Time complexity : O(logn)
        max_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return max_val

    def delete_min(self):
        # delete min from min heap
        # Time complexity : O(logn)
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return min_val

    def insert(self, item):
        # Time complexity : O(logn)
        self.heap_list.append(item)
        self.size += 1
        self.perc_up(self.size)

    def build_heaps(self, A):
        # if we insert n items it would be O(nlogn)
        # If we start with an entire list, we can build a heap in O(n) time
        # leaf nodes always satisfy the heap property. It should be enough if we
        # heapify the non leaf nodes. First non leaf node will be (size - 1)/2 position.
        # The linear time complexity of building a heap can be shown by computing the sum of the
        # heights of all nodes. Perc down to the nodes in reverse level order.
        i = len(A) // 2
        self. size = len(A)
        self.heap_list = [0] + A[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def heap_sort(self, A):
        # insert all elements from an unsorted array into a heap, then remove them from the root of the
        # heap until its empty. It can be done in place by exchanging first element with the last
        # element and reducing the size by 1. Then heapify the first element. Continue until the number of
        # elements remaining is one.
        # Time complexity : O(nlogn)

        # convert A to a heap
        length = len(A) - 1
        least_parent = length / 2

        for i in range(least_parent, -1, -1):
            self.modified_perc_down(A, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if A[0] > A[i]:
                self.swap(A, 0, i)
                self.modified_perc_down(A, 0, i - 1)

    def modified_perc_down(self, A, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and larger than the left child
            if (largest < last) and (A[largest] > A[largest + 1]):
                largest += 1

            # right child is larger than parent
            if A[largest] > A[first]:
                self.swap(A, largest, first)
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                return

    def swap(A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp

    def find_max_in_min_heap(self):
        # given a min heap the max element will always be at the leaf. the first leaf node
        # is the next of the last nodes parent. Last node is at the size - 1 th location. Parent
        # of last node is (size - 1)/ 2 th location. Therefore next of parent is ((size - 1) / 2) + 1 th
        # location which is (size + 1)/ 2
        # Time complexity : O(n)
        maximum = -1
        for i in range((self.size + 1) // 2, self.size):
            if self.heap_list[i] > maximum:
                maximum = self.heap_list[i]
        return maximum

    def delete_arbitrary_element(self, item):
        # Time complexity = O(n) + O(logn) = O(n)
        # first search
        # then delete min
        pass

    def delete_ith_element(self, i):
        # delete ith element and perform heapify at ith position.
        # Time complexity : O(logn)
        if self.size < i:
            print "Wrong position"
            return
        key = self.heap_list[i]
        self.heap_list[i] = self.heap_list[self.size - 1]
        self.size -= 1
        self.perc_down(i)
        return key

    def find_elements_smaller_than_k(self, k):
        self.find_elements_smaller_than_k_recurse(0, k)

    def find_elements_smaller_than_k_recurse(self, i, k):
        if self.heap_list[i] >= k:
            return
        if self.heap_list[i] < k:
            print self.heap_list[i]
            if i * 2 + 1 < self.size:
                self.find_elements_smaller_than_k_recurse((i * 2 + 1), k)
            if i * 2 + 2 < self.size:
                self.find_elements_smaller_than_k_recurse((i * 2 + 2), k)

    def merge_two_binary_max_heap(self, A, B):
        # size of first heap is m + n
        # size of second heap is n
        # merge, find first non leaf node and start heapifying from that element.
        # Time complexity: O(m + n)
        # First non leaf node is the parents of the last element
        A.append(B)
        self.size = len(A)
        self.heap_list = [0] + A[:]
        first_non_leaf = len(A) // 2
        while(first_non_leaf > 0):
            self.perc_down(first_non_leaf)
            first_non_leaf -= 1
        return A

    def find_kth_smallest_element_in_min_heap(self, collection, k):
        # perform deletion k times from a min heap.
        # Time complexity : O(klogn)
        A = collection[: k]
        self.build_heap(A)
        for i in range(k, len(collection)):
            # compare with current min
            if collection[i] < A[0]:
                # replace
                A[0] = collection[i]
                self.heapify(A, 0, k)
        return A[0]

    def build_heap(self, A):
        n = len(A)
        for i in range(n / 2, -1, -1):
            self.heapify(A, i, n)

    def heapify(self, A, index, max_index):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < max_index and A[left] > A[index]:
            largest = left
        else:
            largest = index
        if right < max_index and A[right] > A[index]:
            largest = right
        if largest != index:
            A[largest], A[index] = A[index], A[largest]
            self.heapify(A, largest, max_index)

    def find_kth_largest_element(self, Horig, k):
        # delete k times from a max heap
        # time complexity : O(klogn)
        pass

    def find_10_max_from_file_with_billions_of_numbers(self):
        # for finding max k elements, heap/pq is the best data structure.
        # One approach: Divide the data into sets of 1000 elements and then make a heap
        # of them. Take 10 elements from each of them one by one and heapsort all the sets
        # of 10 elements and take the top 10 among those.
        # Time complexity : O(n)
        pass

    def merge_k_sorted_lists_with_n_elements_each(self):
        # Explanation here
        pass

    def max_sliding_window(self, nums, k):
        # Time complexity : O(n)
        # Use a dequeue
        dq = deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                print dq
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
                print ans
        return ans


heap = Heap()
print heap.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)























