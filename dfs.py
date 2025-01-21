"""
Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree,
find its max depth. Here, we define the length of the path to be the number of edges on that path,
not the number of nodes.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # left_depth = 1
    # right_depth = 1
    # cur_node = root
    # if cur_node is None:
    #     return left_depth-1
    # if cur_node.left:
    #     while cur_node.left:
    #         left_depth += 1
    #         cur_node = cur_node.left
    # elif cur_node.right:
    #     while cur_node.right:
    #         right_depth += 1
    #         cur_node = cur_node.right
    #
    # return max(left_depth, right_depth)-1

    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0

"""
In a binary tree, a node is labeled as "visible" if, on the path from the root to that node, 
there isn't any node with a value higher than this node's value.

The root is always "visible" since there are no other nodes between the root and itself. 
Given a binary tree, count the number of "visible" nodes.
"""
from math import inf
def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(root, max_value):
        if not root:
            return 0
        total = 0
        if root.val >= max_value:
            total += 1
        total += dfs(root.left, max(max_value, root.val))
        total += dfs(root.right, max_value)

        return total
    return dfs(root, -inf)

"""
A binary tree is considered balanced if, for every node in the tree, the difference in the height (or depth) of 
its left and right subtrees is at most 1.

In other words, the depth of the two subtrees for every node in the tree differs by no more than one.

The height (or depth) of a tree is defined as the number of edges on the longest path from the root node to 
any leaf node.

Note: An empty tree is considered balanced by definition.

In that case, given a binary tree, determine if it is balanced
"""

def tree_height(tree):
    if tree is None:
        return 0
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1

"""check if a subtree is part of tree - given root node and a sub root node"""

def check_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.val == tree2.val and check_same_tree(tree1.left, tree2.left) and
            check_same_tree(tree1.right, tree2.right))

def check_same_sub_tree(root, sub_root):
    if not root:
        return False
    return (check_same_tree(root, sub_root) or check_same_sub_tree(root.left, sub_root) or
            check_same_sub_tree(root.right, sub_root))

"""invert binary tree"""

def inverted_binary_tree(root):
    if root is None:
        return None
    return Node(root.value, inverted_binary_tree(root.right), inverted_binary_tree(root.left))

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    my_list = [6, 'x', 9, 'x', 11, 'x', 7, 'x', 'x']
    my_another_tree = [11, 'x', 20, 'x', 'x']
    root = build_tree(iter(my_list), int)
    # res = visible_tree_node(root)
    # print(res)
    # print(is_balanced(root))
    print(check_same_sub_tree(root, build_tree(iter(my_another_tree), int)))