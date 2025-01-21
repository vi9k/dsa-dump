

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.child = []
#         self.parent = None
#
#     def add_child(self, child):
#         child.parent = self
#         self.child.append(child)

    # def print_tree(self):
    #     prefix = '__'
    #     if not self.parent:
    #         # only root node
    #         prefix = ''
    #     elif self.child:
    #         prefix = '|'+prefix*3
    #     else:
    #         # this is a leaf node, hence no child
    #         prefix = '|'+prefix * 5
    #     print(prefix + self.data)
    #     for child in self.child:
    #         # print(child.data)
    #         child.print_tree()

    # def print_tree(self):
    #     level = self.get_level()
    #     spaces = ' '*level*3
    #     prefix = spaces + "|-" if self.parent else ""
    #     print(prefix + self.data)
    #     for child in self.child:
    #         child.print_tree()
    #
    # def get_level(self):
    #     level = 0
    #     p = self.parent
    #     while p:
    #         level += 1
    #         p = p.parent
    #
    #     return level


# root = TreeNode("Electronics")
#
# laptop = TreeNode("Laptop")
# lenovo = TreeNode("Lenovo")
# laptop.add_child(lenovo)
# mac = TreeNode("MacBook")
# laptop.add_child(mac)
# laptop.add_child(TreeNode("Dell"))
# laptop.add_child(TreeNode("Asus"))
# root.add_child(laptop)
#
# cellphone = TreeNode("Cell Phone")
# cellphone.add_child(TreeNode("iPhone"))
# cellphone.add_child(TreeNode("Google Pixel"))
# cellphone.add_child(TreeNode("Vivo"))
# root.add_child(cellphone)
#
# tv = TreeNode("TV")
# tv.add_child(TreeNode("Samsung"))
# tv.add_child(TreeNode("LG"))
# root.add_child(tv)
#
# root.print_tree()
# print()
# tv.print_tree()
# print(root.get_level())
# print(tv.get_level())
# print(tv.child[0].get_level())

"""
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md#data-structures-exercise-general-tree
Below is the management hierarchy of a company.
Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. 
Here is how your main function should will look like,

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
"""
from dataclasses import dataclass

@dataclass
class Data:
    # data model for holding employee data
    name: str
    designation: str

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self, data: str = "both", lvl: int = None):
        level = self.get_level()
        if lvl < level:
            return
        spaces = ' '*level*3
        prefix = spaces + "|-" if self.parent else ""
        if data == "name":
            print(prefix + self.data.name)
        elif data == "designation":
            print(prefix + self.data.designation)
        elif data == "both":
            print(prefix + self.data.name + f"({self.data.designation})")
        for child in self.child:
            child.print_tree(data, lvl)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

root = TreeNode(Data("Nilupul", "CEO"))

cto = TreeNode(Data("Chinmay", "CTO"))
hr = TreeNode(Data("Gels", "HR Head"))
root.add_child(cto)
root.add_child((hr))

infra_head = TreeNode(Data("Vishwa", "Infrastructure Head"))
app_head = TreeNode(Data("Aamir", "Application Head"))
cto.add_child(infra_head)
cto.add_child(app_head)

cloud_manager = TreeNode(Data("Dhaval", "Cloud Manager"))
app_manager = TreeNode(Data("Abhiith", "App Manager"))
infra_head.add_child(cloud_manager)
infra_head.add_child(app_manager)

recuritment_manager = TreeNode(Data("Peter", "Recruitment Manager"))
policy_manager = TreeNode(Data("Waqas", "Policy Manager"))
hr.add_child(recuritment_manager)
hr.add_child(policy_manager)

# root.print_tree("name") # prints only name hierarchy
# root.print_tree("designation") # prints only designation hierarchy
root.print_tree(lvl=0) # prints both (name and designation) hierarchy
