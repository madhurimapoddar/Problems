# -*- coding: utf-8 -*-


class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def inorder_recursive(self):
        # breadth first
        # left, root, right
        left_values = self.left.inorder_recursive() if self.left else []
        right_values = self.right.inorder_recursive() if self.right else []
        return left_values + [self.data] + right_values

    def pre_order_iterative(self):
        # root, left, right
        stack = [self]
        answer = []
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.data)
                # We append right first and then left, since we are using a stack and popping.
                # For pre order left comes before right, and for a stack last in is first out.
                stack.append(node.right)
                stack.append(node.left)
        return answer

    def pre_order_recursive(self):
        # left, root, right
        if self == None:
            return
        if self.data:
            print self.data,
            if self.left:
                self.left.pre_order_recursive()
            if self.right:
                self.right.pre_order_recursive()

    def post_order(self, root):
        # left, right, root
        answer = []
        self.post_order_traversal(root, answer)
        return answer

    def post_order_traversal(self, root, solution):
        if root == None:
            return
        if root.left:
            self.post_order_traversal(root.left, solution)
        if root.right:
            self.post_order_traversal(root.right, solution)
        solution.append(root.data)

    def size(self):
        # total number of nodes in a tree
        nodes = [self]
        all_nodes = [self]
        while nodes:
            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            nodes = next_level
            all_nodes.extend(next_level)
        return len(all_nodes)

    def height(self):
        # also look at formula for height of a complete binary tree
        if self is None:
            return 0
        else:
            return max(self.height(self.left), self.height(self.right)) + 1

    def zigzag(self):
        "print the tree in a zig zag way, "
        roots = [self]
        left_to_right = True
        answer = [self]
        while roots:
            level_answer = []
            for root in roots:
                if left_to_right:
                    if root.left:
                        level_answer.append(root.left)
                    if root.right:
                        level_answer.append(root.right)
                else:
                    if root.right:
                        level_answer.append(root.right)
                    if root.left:
                        level_answer.append(root.left)
            left_to_right = not left_to_right
            roots = level_answer[:: -1]
            answer = answer + level_answer
        return [node.data for node in answer]

    def sum_property(self):
        # For every node, parent value must be equal to sum of left and right children
        roots = [self]
        sum_property = True
        while sum_property and roots:
            next_level = []
            for root in roots:
                children_total = 0
                if root.left:
                    next_level.append(root.left)
                    children_total += root.left.data
                if root.right:
                    next_level.append(root.right)
                    children_total += root.right.data
                if ((root.left or root.right) and (children_total != root.data)):
                    sum_property = False
                    break
            roots = next_level
        return sum_property

    def foldable(self):
        # A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other.
        # An empty tree is considered as foldable.
        if self == None:
            return True
        if self.left and not self.right:
            return False
        if self.right and not self.left:
            return False
        left_half = [self.left]
        right_half = [self.right]
        foldable = True

        while(foldable == True and left_half and right_half):
            current_right = right_half.pop()
            current_left = left_half.pop()

            # if left has both children, right should have both too
            if current_left.left and current_left.right:
                foldable = bool(current_right.left and current_right.right)
            # if right node has both children, left should have both too
            if current_right.left and current_right.right:
                foldable = bool(current_left.left and current_left.right)

            # if left has no children, right should have none too
            if not current_left.left and not current_left.right:
                foldable = bool(current_right.left == None and current_right.right == None)
            # if right has no children, left should have none too
            if not current_right.left and not current_right.right:
                foldable = bool(current_left.left == None and current_left.right == None)

            # if left has left child only, right should have right child only
            if current_left.left and not current_left.right:
                foldable = bool(current_right.right and not current_right.left)
            # if left has right child only, right should have left child only
            if current_left.right and not current_left.left:
                foldable = bool(current_right.left and not current_right.right)

            # if right has only left, left should have right only
            if current_right.left and not current_right.right:
                foldable = bool(current_left.right and not current_left.left)
            # if right has only right, left should have only left
            if current_right.right and not current_right.left:
                foldable = bool(current_left.left and not current_left.right)

            # prepare for next level
            if current_left.left:
                left_half.append(current_left.left)
            if current_left.right:
                left_half.append(current_left.right)
            if current_right.right:
                right_half.append(current_right.right)
            if current_right.left:
                right_half.append(current_right.left)
        return foldable

    def has_path_sum(self, root, summ):
        if root == None:
            return False
        if root.data == summ and (root.left == None and root.right == None):
            return True

        return (self.has_path_sum(root.left, summ - root.data) or self.has_path_sum(root.right, summ - root.data))

    def has_path_sum_queue(self, root, summ):
        pass

    def print_all_paths_binary_tree(self, stack):
        string = str(stack[0].data)
        for i in stack[1:]:
            string += "->" + str(i.data)
        return string

    def binaryTreePaths(self, root):
        if root == None:
            return []

        path = []
        stack = [root]
        pre = None

        while (stack):
            peek = stack[-1]
            if (pre == None or pre.left == peek or pre.right == peek):
                if peek.left:
                    stack.append(peek.left)
                elif peek.right:
                    stack.append(peek.right)
                else:
                    string = self.print_all_paths_binary_tree(stack)
                    path.append(string)
            elif(peek.left == pre and peek.right):
                stack.append(peek.right)
            else:
                stack.remove(peek)
            pre = peek

        return path

    def compare_trees(self, node):
        if node == None and self:
            return False
        if node and not self:
            return False

        if self.data != node.data:
            return False

        result = True
        if self.left is None:
            if node.left:
                return False
        else:
            result = self.left.compare_trees(node.left)

        if result == False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            result = self.right.compare_trees(node.right)

        return result


    # def roottoleaf(root, sb):
    #     if not root:
    #         print(''.join(sb))
    #         return
    #     sb.append(str(root.data)+" ")
    #     roottoleaf(root.left, sb)
    #     if root.right:
    #         roottoleaf(root.right, sb)
    #     sb.pop()


# tree = Node(1)
# tree.left = Node(2)
# tree.right = Node(3)
# tree.left.left = Node(4)
# tree.left.right = Node(5)
# tree.right.left = Node(6)
# tree.right.right = Node(7)
# tree.left.left.left = Node(9)
# tree.left.left.right = Node(10)

# tree = Node(4)
# tree.left = Node(5)
# tree.right = Node(6)
# tree.left.left = Node(7)
# tree.left.right = Node(8)
# tree.right.left = Node(9)
# tree.right.right = Node(10)
# tree.right.right.left = Node(11)

# tree = Node(1)
# tree.left = Node(2)
# tree.right = Node(3)
# tree.left.left = Node(4)
# tree.left.right = Node(5)

# Sum property tree
# tree = Node(10)
# tree.left = Node(8)
# tree.right = Node(2)
# tree.left.left = Node(5)
# tree.left.right = Node(3)
# tree.right.left = Node(2)

#foldable
# tree = Node(10)
# tree.left = Node(7)
# tree.right = Node(15)
# tree. left.right = Node(9)
# tree.right.left = Node(11)


# print tree.inorder_recursive()
# print tree.zigzag()
# print tree.pre_order_iterative()
# print tree.pre_order_recursive()
# print tree.post_order(tree)
# print tree.size()
# print tree.sum_property()
# print tree.foldable()

# tree has a path for a given sum
tree = Node(8)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(2)
print tree.has_path_sum(tree, 11)
print tree.binaryTreePaths(tree)

# Compare
tree2 = Node(8)
tree2.left = Node(2)
tree2.right = Node(3)
tree2.left.left = Node(2)
print tree2.compare_trees(tree)


