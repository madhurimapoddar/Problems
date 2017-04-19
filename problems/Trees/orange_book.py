import Queue


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder_recurse(self, result):
        # self is root here
        # root, left, right
        # time : O(N)
        # space : O(N)
        if not self:
            return
        result.append(self.data)
        self.preorder_recurse(self.left, result)
        self.preorder_recurse(self.right, result)

    def preorder_iterative(self, result):
        if not self:
            return
        stack = [self]
        while self:
            node = stack.pop()
            if node.right:
                stack.append(node.right.data)
            if node.left:
                stack.append(node.left.data)
            result.append(self.data)

    def inorder_recursive(self, result):
        # time : O(N)
        # space : O(N)
        if not self:
            return
        self.inorder_recursive(self.left, result)
        result.append(self.data)
        self.inorder_recursive(self.right, result)

    def inorder_iterative(self, result):
        # time : O(N)
        # space : O(N)
        if not self:
            return
        node = self
        stack = []
        while node or stack:
            if node:
                # keep going left till you reach end
                stack.append(node)
                node = node.left
            else:
                # last left, record that
                node = stack.pop()
                result.append(node.data)
                # now go right
                node = node.right

    def postorder_recursive(self, result):
        if not self:
            return
        self.postorder_recursive(self.left)
        self.postorder_recursive(self.right)
        result.append(self.data)

    def postorder_iterative(self, result):
        # time : O(N)
        # space : O(N)
        if not self:
            return
        visited = set()
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None

    def level_order(self, result):
        # time : O(N)
        # space : O(N)
        if not self:
            return
        q = Queue.Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            result.append(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def max_in_binary_tree(self):
        # find max in left sub tree,
        # find max in right sub tree
        # compare with root and find max
        # time : O(N)
        # space : O(N)
        # can also be done by level order traversal with same space and time complexity
        global max_data
        if not self:
            return max_data
        if self.data > max_data:
            max_data = self.data
        self.max_in_binary_tree(self.left)
        self.max_in_binary_tree(self.right)
        return max_data

    def search_recursive(self, data):
        # time : O(N)
        # space : O(N)
        if not self:
            return 0
        if self.data == data:
            return 1
        else:
            temp = self.search_recursive(self.left, data)
            if temp == 1:
                return temp
            else:
                return self.search_recursive(self.right, data)

    def size_recursive(self):
        # time : O(N)
        # space : O(N)
        if not self:
            return 0
        return self.size_recursive(self.left) + self.size_recursive(self.right) + 1

    def size_level_order(self):
        # time : O(N)
        # space : O(N)
        if not self:
            return 0
        q = Queue.Queue()
        q.put(self)
        size = 0
        while not q.empty():
            node = q.get()
            size += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return size

    def print_level_order_reverse_order(self):
        # use a stack and a queue.
        # time : O(N)
        # space : O(N)
        if not self:
            return 0
        q = Queue.Queue()
        items = []
        while not q.empty:
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            items.append(node)
        # print in reverse order
        while items:
            item = items.pop()
            print item,

    def delete_binary_tree(self):
        # time : O(N)
        # space : O(N)
        # delete children before root, therefore use post order traversal
        if not self:
            return
        self.delete_binary_tree(self.left)
        self.delete_binary_tree(self.right)
        del self

    def height_recursion(self):
        # also same as max_depth. similar to preorder or DFS
        if not self:
            return 0
        return max(self.height_recursion(self.left), self.height_recursion(self.right)) + 1

    def height_iterative(self):
        # similar to BFS
        height = 0
        current_level = [self]
        while current_level:
            height += 1
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return height

    def deepest_node(self):
        # level order and get the last element
        pass

    def number_of_leaves_in_binary_tree(self):
        # level order and count whose both left and right are empty
        pass

    def number_of_full_nodes_in_binary_tree(self):
        # nodes with both left and right children are called full nodes
        # level order and increase count when both left and right children are present.
        pass

    def number_of_half_nodes_in_binary_tree(self):
        # nodes which have only one child
        q = Queue.Queue()
        node = None
        count = 0
        while not q.empty():
            node = q.get()
            if node.left and not node.right or (node.right and not node.left):
                count += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return count

    def identical_structurally(self, root2):
        pass




x = Tree(1)
x.left = Tree(2)
x.right = Tree(3)
print x.height_iterative()










