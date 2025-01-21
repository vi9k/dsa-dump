from collections import deque

# stack is a data structure which allows these operations and is LIFO type
#  Last In First Out
# push - insert into elements
# pop - remove last inserted
# peek - show the last inserted

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)
        print(f"element {element} pushed into the stack")

    def pop(self):
        if self.stack:
            # return self.stack.pop()
            print(f"pulling/popping {self.stack[-1]} from stack")
            return self.stack.pop()
        else:
            print("stack underflow..., no elements to pop")

    def peek(self):
        if self.stack:
            print(f"top most element is {self.stack[-1]}")
        else:
            print("stack underflow...cannot peek into stack")

    def __len__(self):
        return len(self.stack)



# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(1234)
# my_stack.peek()
# my_stack.pop()
# my_stack.push("hi")
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.peek()

# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_str = ''
    for i in range(len(s)):
        reversed_str=reversed_str+stack.pop()
    return reversed_str

str = "We will conquere COVID-19"

# print(reverse_string(str))
# print(reverse_string(str) == "91-DIVOC ereuqnoc lliw eW")

"""
Write a function in python that checks if parenthesis in the string are balanced or not. Possible parantheses are 
"{}',"()" or "[]". Use Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

"""

def is_balanced(s):
    """
    1. filter out only parenthesis while pushing into stack i.e (, {, [, ], }, )
    2. pop all elements one by one
    3. last element should be closing parenthesis
    4. otherwise it's not balanced
    """
    stack = Stack()
    map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in s:
        if char in "({[":
            stack.push(char)
        if char in ")}]":
            if not len(stack):
                return  False
            if map[char] == stack.pop():
                continue
            else:
                return False
    return True

# print(is_balanced("({a+b})")) # should return True as its balanced
# print(is_balanced("))((a+b}{")) # returns False
# print(is_balanced("((a+b))")) # returns True
# print(is_balanced("))")) # returns False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) # returns True