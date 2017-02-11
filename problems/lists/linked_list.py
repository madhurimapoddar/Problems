# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def print_list(head):
        if head == None:
            return
        while head:
            print head.data
            head = head.next

    def InsertNth(head, data, position):
        new_node = Node(data)
        if position == 0:
            if head == None:
                return Node(data)
            else:
                new_head = Node(data)
                new_head.next = head
                return new_head
        else:
            count = 0
            current = head
            while current:
                if (count + 1 == position):
                    next_temp = current.next
                    current.next = new_node
                    new_node.next = next_temp
                    return head
                current = current.next
                count = count + 1

    def Delete(head, position):
        if head == None:
            return
        if head.next == None and position == 0:
            return
        count = 0
        current = head
        # deleting head
        if position == 0:
            head = head.next
            return head
        while current:
            if count + 1 == position:
                if current.next.next:
                    current.next = current.next.next
                    return head
                else:
                    current.next = None
                    return head
            current = current.next
            count = count + 1

    def ReversePrint(head):
        if head == None:
            return
        items = []
        while head:
            items.append(head.data)
            head = head.next
        items = items[::-1]
        for item in items:
            print item

    def Reverse(self):
        head = self
        if head == None:
            return
        if head.next_node == None:
            return head
        current = Node(head.data)
        nextt = head.next_node
        while nextt:
            head = Node(nextt.data)
            head.next_node = current
            current = head
            nextt = nextt.next_node
        return head

    def CompareLists(headA, headB):
        if bool(headA) ^ bool(headB):
            return 0
        if headA == None and headB == None:
            return 1
        while headA and headB:
            if headA.data != headB.data:
                return 0
            headA = headA.next_node
            headB = headB.next_node
        return 0

    def MergeLists(headA, headB):
        if headA == None and headB == None:
            return
        if headA == None:
            return headB
        if headB == None:
            return headA
        new_head = Node()
        while headA or headB:
            if headA and headB:
                if headA.data <= headB.data:
                    if new_head.data == None:
                        new_head = Node(headA.data)
                        copy_new_head = new_head
                    else:
                        new_head.next = Node(headA.data)
                        new_head = new_head.next
                    headA = headA.next
                else:
                    if new_head.data == None:
                        new_head = Node(headB.data)
                        copy_new_head = new_head
                    else:
                        new_head.next = Node(headB.data)
                        new_head = new_head.next
                    headB = headB.next
            elif headA and not headB:
                new_head.next = headA
                return copy_new_head
            else:
                new_head.next = headB
                return copy_new_head
        return copy_new_head

    def reverse_double_linked_list(self):
        #TODO
        return

    def deletes_nodes_higher_than_value(self, value):
        head = self
        node = self
        prev = None
        while node:
            if node == head and node.data > value:
                temp = node.next_node if node else None
                head = temp
            elif node.data > value:
                temp = node.next_node if node else None
                prev.next_node = temp
            prev = node
            node = node.next_node if node else None

        return head

    def search(self, item):
        start = self
        while start:
            if start.data == item:
                return True
            else:
                start = start.next_node
        return False

    def remove(self, item):
        start = self
        head = self
        prev = None
        while start:
            if start.data == head.data and start.data == item:
                head = start.next_node
                return head
            elif start.data == item:
                temp = start.next_node
                prev.next_node = temp
                return head
            prev = start
            start = start.next_node

    def merge_lists(self, head2):
        # merge two sorted linked lists
        head1 = self
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        # import debug
        # create dummy node to avoid additional checks in loop
        dummy = t = Node()
        while not (head1 is None or head2 is None):
            if head1.data < head2.data:
                # remember current low-node
                current = head1
                # follow ->next
                head1 = head1.next_node
            else:
                # remember current low-node
                current = head2
                # follow ->next
                head2 = head2.next_node

            # only mutate the node AFTER we have followed ->next
            t.next_node = current
            # and make sure we also advance the temp
            t = t.next_node

        t.next_node = head1 or head2

        # return tail of dummy node
        return dummy.next_node

    def insert_at_the_beginning(self, item):
        head = self
        if head == None:
            head = item
            head.next_node = None
        else:
            current_head = head
            head = item
            item.next_node = current_head
        return head

    def insert_at_the_end(self, item):
        head = self
        tail = self
        if head == None:
            return self.insert_at_the_beginning(item)
        else:
            while tail.next_node != None:
                tail = tail.next_node
            tail.next_node = item
            tail.next_node.next_node = None
        return head

    def is_circular(self):
        # http://stackoverflow.com/questions/20353835/fastest-way-to-prove-linked-list-is-circular-in-python
        slow = self
        fast = self
        while fast != None:
            slow = slow.next_node
            if fast.next_node != None:
                fast = fast.next_node.next_node
            else:
                return False

            if slow == fast:
                return True

        return False

    def RemoveDuplicates(head):
        next_node = head.next_node
        current = head
        while current:
            if current.next_node:
                if current.data == next_node.data:
                    current.next_node = next_node.next_node
                    if next_node.next_node:
                        next_node = next_node.next_node.next_node
                    current = current.next_node
                else:
                    current = current.next_node
                    next_node = next_node.next_node
            else:
                copy_head = head
                while copy_head:
                    if head.next_node:
                        if head.data == head.next_node.data:
                            head = head.next_node
                        else:
                            return head
                    copy_head = copy_head.next_node
                return head
        copy_head = head
        while copy_head:
            if head.next_node:
                if head.data == head.next_node.data:
                    head = head.next_node
                else:
                    return head
            copy_head = copy_head.next_node
        return head

    def FindMergeNode(headA, headB):
        a = headA
        b = headB
        n1 = 0
        n2 = 0

        while a is not None:
            a = a.next
            n1 += 1
        while b is not None:
            b = b.next
            n2 += 1
        a = headA
        b = headB

        while n1 > 0 and n2 > 0:
                if n1 > n2:
                    a = a.next
                    n1 -= 1
                if n2 > n1:
                    b = b.next
                    n2 -= 1
                if n1 == n2:
                    if a == b:
                        return a.data
                    else:
                        a = a.next
                        b = b.next
                        n1 -= 1
                        n2 -= 1
        return None


number = Node(data=1)
number.next_node = Node(data=2)
number.next_node.next_node = Node(data=2)
number.next_node.next_node.next_node = Node(data=3)
# print number.deletes_nodes_higher_than_value(0)
# print number.search(5)
# print number.remove(2)

# item = Node(data=5)
# number.insert_at_the_end(item)
#number.next_node.next_node.next_node.next_node = number.next_node
#print number.is_circular()

#number.Reverse()
#number.next_node.next_node.next_node.next_node = Node(data=3)
#number.next_node.next_node.next_node.next_node.next_node = Node(data=4)
#number.RemoveDuplicates()




#list_one = Node(data=2)
#list_one.next_node = Node(data=3)
#list_one.next_node.next_node = Node(data=5)

#list_two = Node(data=1)
#list_two.next_node = Node(data=4)
#list_two.next_node.next_node = Node(data=6)

#head1 = list_one.merge_lists(list_two)
#print head1.data

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def SortedInsert(head, data):
        if head == None:
            return Node(data)
        if head.next == None:
            if head.data >= data:
                temp_head = head
                head.prev = Node(data)
                head = head.prev
                head.next = temp_head
                return head
        current = head
        while current:
            if data < current.data:
                to_insert = Node(data)
                if current.prev:
                    current.prev.next = to_insert
                    to_insert.next = current
                else:
                    current.prev = to_insert
                    head = current.prev
            else:
                if current.next == None and data > current.data:
                    current.next = Node(data)
            copy_current = current
            current = current.next
            if not current:
                return head
            current.prev = copy_current
        return head


def Reverse(head):
        temp = None
        current = head

        # Swap next and prev for all nodes of
        # doubly linked list
        while current:
                temp = current.prev
                current.prev = current.next
                current.next = temp
                current = current.prev

        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            head = temp.prev

        return head

number = Node(2)
number = SortedInsert(number, 1)
number = SortedInsert(number, 4)
number = SortedInsert(number, 3)




