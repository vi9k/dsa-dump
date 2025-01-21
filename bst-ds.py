# B-Tree contains only 2 children per parent.
# Can be balanced or unbalanced
from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.data == value:
            return

        if value < self.data:
            # add child to left
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinaryTreeNode(value)
        else:
            # add to right
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinaryTreeNode(value)

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            # search left subtree
            if self.left:
                return self.left.search(value)
            else:
                print(f"{value} not found in tree.")
        else:
            # search right subtree
            if self.right:
                return self.right.search(value)
            else:
                print(f"{value} not found in tree.")

        return False

    def in_order_traversal(self):
        # traverse through all elements in b-tree
        out = []
        # if any left is present keep going left
        if self.left:
            # print(f"visiting node {self.left.data}")
            out += self.left.in_order_traversal()

        # add that left node if nothing there in left
        # print(f"visiting node {self.data}") # for understanding
        out.append(self.data)

        # if any right is present keep going left of that right
        if self.right:
            # print(f"visiting node {self.right.data}") # for understanding
            out += self.right.in_order_traversal()

        return out

    def find_min(self):
        # min = 0
        if self.left:
            min = self.left.find_min()
        else:
            min = self.data

        return min

    def find_max(self):
        if self.right:
            max = self.right.find_max()
        else:
            max = self.data

        return max

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def pre_order_traversal(self):
        out = []
        # first visit root node and store
        out.append(self.data)
        # visit left subtree and find last node
        if self.left:
            # out.append(self.left.data)
            out += self.left.pre_order_traversal()

        # visit right subtree and find last
        if self.right:
            # out.append(self.right.data)
            out += self.right.pre_order_traversal()

        return out

    def post_order_traversal(self):
        out = []
        # first visit left and store
        if self.left:
            out += self.left.post_order_traversal()
        # then visit right and store
        if self.right:
            out += self.right.post_order_traversal()
        # then visit it's root and store
        out.append(self.data)

        return out

    def delete(self, val):
        if val < self.data:
            if self.left:
                return self.left.delete(val)
        elif val > self.data:
            if self.right:
                return self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

    def bfs(self):
        """implements breadth first traversal"""
        from collections import deque

        res = []
        root = self
        queue = deque([root])
        while queue:
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.data)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            res.append(new_level)
        return res

    def zig_zag_bfs(self):
        root = self
        res = []
        queue = deque([root])
        zig_zag = True
        while len(queue)>0:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data) if zig_zag else level.appendleft(node.data)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            zig_zag = not(zig_zag)
            res.append(list(level))
        return res

# helper function to iterate through elements and call add_child method
def build_tree(elements: list):
    root = BinaryTreeNode(elements[0])
    for item in elements[1::]:
        root.add_child(item)
    return root

tree1 = build_tree(["India","Pakistan","Germany", "USA","China","India","UK","USA"])
print(tree1.search("USA"))
print(tree1.search("Russia"))

tree2 = build_tree([20, 44, 957, 83, 3, 67, 33, 23, 88, 21])
print(tree2.search(1))
print(tree2.search(88))
print(tree2.in_order_traversal())
print(f"max element in the tree is {tree2.in_order_traversal()[-1]}")
print(f"min element in the tree is {tree2.in_order_traversal()[0]}")
print(tree2.find_min())
print(tree2.pre_order_traversal())

tree3 = build_tree([10, 20, 60, 30, 70, 40, 50])
print(f"min element in the tree is {tree3.in_order_traversal()[0]}")
print(tree3.find_min())
print(f"max element in the tree is {tree3.in_order_traversal()[-1]}")
print(tree3.find_max())
print(f"sum of all elements are: {sum(tree3.in_order_traversal())}")
print(tree3.calculate_sum())
print(tree3.pre_order_traversal())
print(tree3.post_order_traversal())
print(tree2.post_order_traversal())
print(tree2.bfs())
print(tree2.zig_zag_bfs())