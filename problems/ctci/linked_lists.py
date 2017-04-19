# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def remove_dups(self):
        # remove duplicates from an unordered linked list
        head = self
        start = head.next
        items = [head.data]
        prev = head
        while start:
            if start.data in items:
                prev.next = start.next
            else:
                prev = prev.next
            items.append(start.data)
            start = start.next
        return head

    def remove_dups_no_extra_space(self):
        # same as above without using additional items list
        # maintain 2 pointers
        pass

    def kth_to_last(self, k):
        # find kth to the last element in a singly linked list
        head = self
        if not head:
            return
        count = 0
        current = head
        while current:
            count += 1
            if count == k:
                head = current
                return head
            current = current.next
        return "k is larger than the number of items in the list"

    def delete_node(self, node):
        # delete a node from the list
        head = self
        # if node is the head node
        if node.data == head.data:
            head = head.next
            return head

        # if node is any middle node or tail
        current = head.next
        prev = head
        while current:
            if current.next:
                next_node = current.next
            # if its the tail node
            if current.data == node.data:
                if next_node:
                    prev.next = current.next
                else:
                    prev.next = None
                return head
            current = current.next
            prev = prev.next
                # if its the tail node

    def partition(self, x):
        # values smaller than x remain before x and greater remains after.
        head = Node(None)
        tail = Node(None)
        left_half = head
        right_half = tail
        start = self
        while start != None:
            if start.data < x:
                head.next = Node(start.data)
                head = head.next
            else:
                tail.next = Node(start.data)
                tail = tail.next
            start = start.next
        left_half = left_half.next
        right_half = right_half.next
        begin = left_half
        while begin:
            if begin.next == None:
                begin.next = right_half
                break
            begin = begin.next
        return left_half

    def sum_lists(self, node1, node2):
        """Sum two lists and returns the sum as a linked list.
        eg. 7->1->6 and 5->9->2, the numbers are 617 and 295 and the sum is 912.
        Expected output is 2->1->9
        """
        carry = 0
        sum_list = None
        sum_head = None
        while node1 or node2:
            if node1 and node1.data:
                a = node1.data
                node1 = node1.next
            else:
                a = 0
            if node2 and node2.data:
                b = node2.data
                node2 = node2.next
            else:
                    b = 0
            total = a + b + carry
            if not sum_list:
                sum_list = Node(total % 10)
                sum_head = sum_list
            else:
                sum_list.next = Node(total % 10)
                sum_list = sum_list.next
            carry = total / 10
        return sum_head

    def sum_lists_forward_order(self, node1):
        # do the same thing for two lists and call the method above.
        current = node1
        rev_list = None
        while current.next:
            if not rev_list:
                rev_list = Node(current.next.data)
                rev_list.next = Node(current.data)
            else:
                node = Node(current.next.data)
                node.next = rev_list
                rev_list = node
            current = current.next
        return rev_list

    def palindrome(self):
        # determine if a linked list is a palindrome or not.
        # odd length: 2->1->3->1->2
        # even length: 4->3->2->2->3->4
        # using the slow tracker and fast tracker approach and assuming we dont know the length of the lists.
        # when fast tracker's next is none then the length of the list is odd and we skip the middle element
        # when the fast tracker's next next is none, then the length of the list is even and we dont skip any item.
        slow_head = self
        fast_head = self
        first_half_stack = []
        palindrome = True
        while slow_head and fast_head:
            first_half_stack.append(slow_head.data)
            # when list is odd
            if fast_head.next == None:
                first_half_stack.pop()
                slow_head = slow_head.next
                break
            # when list is even
            if fast_head.next.next == None:
                slow_head = slow_head.next
                break
            slow_head = slow_head.next
            fast_head = fast_head.next.next

        while first_half_stack:
            item = first_half_stack.pop()
            if slow_head.data == item:
                slow_head = slow_head.next
            else:
                palindrome = False
                break
        return palindrome

    def intersection(self, a, b):
        # given 2 singly linked lists, find out if the the two lists intersect
        # traverse till the end and get the tails and compare.
        # for the longer list, trim off the excess from the beginning and move forward in
        # both the lists to find intersection node.
        tail_a = a
        tail_b = b
        len_a = 0
        len_b = 0
        # get tail for list a
        while tail_a:
            tail_a = tail_a.next
            len_a += 1

        # get tail for list b
        while tail_b:
            tail_b = tail_b.next
            len_b += 1

        if tail_b != tail_a:
            return False

        # check if the lengths are same. If not, find the difference.
        if len_a != len_b:
            if len_a > len_b:
                diff = len_a - len_b
                longer = a
            else:
                diff = len_b - len_a
                longer = b

        # trim off the excess from the longer list
        if longer == a:
            excess_count = 0
            while excess_count < diff:
                a = a.next
                excess_count += 1

        if longer == b:
            excess_count = 0
            while excess_count < diff:
                b = b.next
                excess_count += 1

        pointer_a = a
        pointer_b = b

        # traverse the lists to see if there is an intersecting node
        while pointer_a and pointer_b:
            if pointer_a == pointer_b:
                return True
            else:
                pointer_a = pointer_a.next
                pointer_b = pointer_b.next
        return False

    def loop_detection(self):
        # given a circular linked list, return the node at the beginning of the loop.
        slow_tracker = self
        fast_tracker = self
        found = False
        while not found:
            slow_tracker = slow_tracker.next
            fast_tracker = fast_tracker.next.next
            if slow_tracker == fast_tracker:
                found = True
                slow_tracker = self
        # find loop node
        found = False
        while not found:
            if slow_tracker == fast_tracker:
                found = True
                return slow_tracker.data
            else:
                slow_tracker = slow_tracker.next
                fast_tracker = fast_tracker.next



# x = Node(4)
# x.next = Node(4)
# x.next.next = Node(5)
# x.next.next.next = Node(6)
# x.remove_dups()
# x.kth_to_last(2)
# y = Node(6)
# x.delete_node(y)

# a = Node(3)
# a.next = Node(5)
# a.next.next = Node(8)
# a.next.next.next = Node(5)
# a.next.next.next.next = Node(10)
# a.next.next.next.next.next = Node(2)
# a.next.next.next.next.next.next = Node(1)

# a.partition(5)


# x = Node(0)
# a = Node(7)
# a.next = Node(1)
# a.next.next = Node(6)
# a.next.next.next = Node(6)

# b = Node(5)
# b.next = Node(9)
# b.next.next = Node(2)
# x.sum_lists(a, b)

# a = Node(6)
# a.next = Node(1)
# a.next.next = Node(7)
# a.sum_lists_forward_order(a)

# a = Node(2)
# a.next = Node(1)
# a.next.next = Node(3)
# a.next.next.next = Node(1)
# a.next.next.next.next = Node(2)
# print a.palindrome()

# a = Node(4)
# a.next = Node(3)
# a.next.next = Node(2)
# a.next.next.next = Node(2)
# a.next.next.next.next = Node(3)
# a.next.next.next.next.next = Node(4)
# print a.palindrome()

# a = Node(2)
# a.next = Node(0)
# print a.palindrome()


# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(3)

# b = Node(6)
# b.next = Node(4)
# b.next.next = a.next

# print a.intersection(a, b)

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)
a.next.next.next.next.next = a.next
print a.loop_detection()
