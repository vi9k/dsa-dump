

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        #     1-> 2 -> 3
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
# 1 -> 2 -> 3 -> insert here
#  pointing next of last node to new node and new node's next will point to null
# need to identify last element
        node = Node(data)
        if not self.head:
            self.insert_at_start(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def print_linked_list(self):
        linked_list = ""
        current_node = self.head
        while current_node:
            # print(self.head.data, "-> ")
            linked_list += f"{current_node.data} -> "
            current_node = current_node.next
        # printing next to last node pointing to None
        linked_list += "None"
        print(linked_list)

    def insert_at(self, index, data):
        node = Node(data)
        current_node = self.head
        count = 0
        while current_node:
            if count == index-1:
                node.next = current_node.next
                current_node.next = node
                break
            current_node = current_node.next
            count =+ 1

    def delete_at(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index-1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            count += 1

    def insert_after_value(self, value, data):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                break
            current_node = current_node.next
        new_node = Node(data, current_node.next)
        current_node.next = new_node

    def remove_by_value(self, value):
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                break
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next
        else:
            print(f"{value} not found in linked list")

    def insert_values(self, data):
        self.head = None
        for ele in data:
            self.insert_at_end(ele)

    def is_circular(self):
        tortaise = self.head.next
        hare = self.head.next.next
        while tortaise != hare and hare.next:
            tortaise = tortaise.next
            hare = hare.next.next
        return hare.next is not None



l1 = Linkedlist()
l1.insert_at_start(1)
l1.insert_at_start(2)
l1.insert_at_start(3)
old = l1.head.next.next
prev = l1.head.next
print(old.data)
new = Node(123, prev)
old.next = new
# l1.print_linked_list()
print(l1.is_circular())
# l1.insert_at_end(4)
# l1.insert_at_end(5)
# l1.insert_at_end(6)
# l1.print_linked_list()
# l1.insert_at(2, 0)
# l1.print_linked_list()
# l1.delete_at(1)
# l1.print_linked_list()
# l1.insert_at_end(12)
# l1.print_linked_list()
# l1.insert_after_value(1, 120)
# l1.print_linked_list()
# l1.insert_after_value(12, 144)
# l1.print_linked_list()
# l1.remove_after_value(120)
# l1.print_linked_list()
# l1.remove_after_value(1)
# l1.print_linked_list()
print()
print()

# ll = Linkedlist()
# ll.insert_values(["banana", "mango", "grapes", "orange"])
# ll.print_linked_list()
# ll.insert_after_value("mango", "apple")  # insert apple after mango
# ll.print_linked_list()
# ll.remove_by_value("orange")  # remove orange from linked list
# ll.print_linked_list()
# ll.remove_by_value("figs")
# ll.print_linked_list()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print_linked_list()


"""
Implement doubly linked list. The only difference with regular linked list is that double linked has prev 
node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this,
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
    
Implement all other methods in regular linked list class and make necessary changes for 
doubly linked list (you need to populate node.prev in all those methods)
"""

class DoubleNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        #   None -> <- 1 -> <- 2 -> <- 3 -> <- None
        if not self.head:
            node = DoubleNode(data, self.head, None)
            self.head = node
        else:
            node = DoubleNode(data=data, next=None, prev=None)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        # 1 -> 2 -> 3 -> insert here
        #  pointing next of last node to new node and new node's next will point to null
        # need to identify last element
        node = DoubleNode(data)
        if not self.head:
            self.insert_at_start(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node

    def print_linked_list(self):
        linked_list = ""
        current_node = self.head
        while current_node:
            # print(self.head.data, "-> ")
            linked_list += f"{current_node.data} -> "
            current_node = current_node.next
        # printing next to last node pointing to None
        linked_list += "None"
        print(linked_list)

    def insert_at(self, index, data):
        node = DoubleNode(data)
        current_node = self.head
        count = 0
        while current_node:
            if count == index - 1:
                node.next = current_node.next
                node.prev = current_node
                current_node.next = node
                break
            current_node = current_node.next
            count = + 1

    def delete_at(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                # current_node.next.prev = None
                break
            current_node = current_node.next
            count += 1

    def insert_after_value(self, value, data):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                break
            current_node = current_node.next
        new_node = Node(data, current_node.next)
        current_node.next = new_node

    def remove_by_value(self, value):
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                break
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next
        else:
            print(f"{value} not found in linked list")

    def insert_values(self, data):
        self.head = None
        for ele in data:
            self.insert_at_end(ele)

    def print_forward(self):
        self.print_linked_list()

    def print_backward(self):
        backward_list = "None "
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        while current_node:
            backward_list += f"<- {current_node.data} "
            current_node = current_node.prev
        print(backward_list)


# l2 = DoublyLinkedList()
# l2.insert_at_start(1)
# l2.insert_at_start(2)
# l2.insert_at_start(3)
# l2.insert_at_end(0)
# l2.insert_at_end(-1)
# l2.print_linked_list()
# l2.insert_at(1, "first")
# l2.print_linked_list()
# l2.delete_at(1)
# l2.print_forward()
# l2.print_backward()
# l2.delete_at(12)