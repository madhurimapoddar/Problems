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
        import debug
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


# number = Node(data=1)
# number.next_node = Node(data=2)
# number.next_node.next_node = Node(data=3)
# number.next_node.next_node.next_node = Node(data=4)
# print number.deletes_nodes_higher_than_value(0)
# print number.search(5)
# print number.remove(2)


list_one = Node(data=2)
list_one.next_node = Node(data=3)
list_one.next_node.next_node = Node(data=5)

list_two = Node(data=1)
list_two.next_node = Node(data=4)
list_two.next_node.next_node = Node(data=6)

head1 = list_one.merge_lists(list_two)
print head1.data



