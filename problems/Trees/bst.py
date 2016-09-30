# -*- coding: utf-8 -*-


class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def is_binary_search_tree(self):
        return self.__is_valid(self, float("-infinity"), float("infinity"))

    def __is_valid(self, minimum, maximum):
        if self == None:
            return True
        if self.val <= minimum or self.val >= maximum:
            return False
        solution = self.left.is_valid(minimum, self.val)
        solution = solution and self.right.is_valid(self.val, maximum)

    def search(self, item):
        if self == None:
            return False
        if self.data == item:
            return True
        if item < self.data:
            if self.left == None:
                return False
            else:
                return self.left.search(item)
        if item > self.data:
            if self.right == None:
                return False
            else:
                return self.right.search(item)

    def insert(self, item):
        if self == None:
            self.data = item
        elif self.data:
            if item < self.data:
                if self.left == None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.data:
                if self.right == None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        return self


def reconstruct_bst(preorder, inorder):
        # preorder and inorder are list of elements.
        root = None
        if preorder and inorder:
            root = Node(preorder[0])
            root_index = inorder.index(root.data)
            left_inorder = inorder[0: root_index]
            right_inorder = inorder[root_index + 1:]

            preorder_pos = len(left_inorder)
            left_preorder = preorder[1: preorder_pos + 1]
            right_preorder = preorder[preorder_pos + 1:]

            root.left = reconstruct_bst(left_preorder, left_inorder)
            root.right = reconstruct_bst(right_preorder, right_inorder)
        return root

preorder = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
inorder = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
print reconstruct_bst(preorder, inorder).left.data
print reconstruct_bst(preorder, inorder).right.data
print reconstruct_bst(preorder, inorder).right.right.data
print reconstruct_bst(preorder, inorder).right.left.data


def sorted_list_to_bst(numbers):
    # nlogn
    return sorted_list_to_bst_recurse(numbers, 0, len(numbers) - 1)


def sorted_list_to_bst_recurse(numbers, begin, end):
    if begin > end:
        return
    mid = (begin + end) // 2
    root = Node(numbers[mid])
    root.left = sorted_list_to_bst_recurse(numbers, begin, mid - 1)
    root.right = sorted_list_to_bst_recurse(numbers, mid + 1, end)
    return root

bst = sorted_list_to_bst([1, 2, 3])
print bst.data
print bst.left.data
print bst.right.data

# search item in bst
tree = Node(2)
tree.left = Node(1)
tree.right = Node(3)
print tree.search(4)


#Insert item to bst
tree = Node(2)
tree.left = Node(1)
inserted = tree.insert(3)
print inserted.right.data


