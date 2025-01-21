from math import sqrt


def countDigits(n: int) -> int:
    count = 0
    num = n
    while n > 0:
        digit = n % 10
        if digit and num % digit == 0:
            count += 1
        n = int(n / 10)

    return count

# print(countDigits(660))

def reverseNum(n):
    # Write your code here.
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = (reverse*10)+digit
        n = int(n / 10)

    return reverse

# print(reverseNum(7001))

def check_palindrome(n):
    reverse = reverseNum(n)
    if n == reverse:
        return True
    else:
        return False

# print(check_palindrome(1210))

def check_armstrong_number(n):
    sum = 0
    number = n
    while n>0:
        digit = int(n%10)
        sum += digit ** 3
        n = n/10

    return True if number == sum else False

# print(check_armstrong_number(371))

def all_factors(n):
    factors = []
    for i in range(1, int(sqrt(n))):
        if n%i == 0:
            factors.append(i)
            if n/i != i:
                factors.append(n/i)

    return factors

# print(all_factors(36))

def check_prime(n):
    count = 0
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            count += 1
            if n / i != i:
                count += 1
        if count > 1:
            return False
    return True

# print(check_prime(20))

def check_palindrome_str(s):
    print(len(s))
    reverse = s[::-1]
    print("reversing", reverse == s)
    left = 0
    right = len(s)-1
    while left < right:
        print(f"comparing {s[left]} and {s[right]}")
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# print(check_palindrome_str("aa$%^^%$aa"))

def check_gcd(num1, num2):
    # gcd = 1
    # for i in range(1, min(num1, num2)+1):
    #     if num1 % i == 0 and num2 % i == 0:
    #         gcd = i
    #
    # return gcd
    # original euclidean approach
    while num1>0 and num2>0:
        if num1>num2:
            num1 = num1-num2
        else:
            num2 = num2-num1
    if num1 == 0:
        return num2
    return num1
    # euclidean algorithm iterative approach
    # while num1>0 and num2>0:
    #     if num1>num2:
    #         num1 = num1%num2
    #     else:
    #         num2 = num2%num1
    # if num1 == 0:
    #     return num2
    # return num1

    # euclidean algorithm recursive approach
    # if num1 == 0:
    #     return num2
    # else:
    #     return num1
    # if num1<num2:
    #     return check_gcd(num2%num1, num1)
    # else:
    #     return check_gcd(num1%num2, num2)


# print(check_gcd(77, 77))
# import math
# print(math.gcd(77, 77))

def print_i_times_with_recursion(n):
    def fun(i, n):
        if i<1:
            return
        else:
            print(i)
            fun(i-1, n)
    return fun(n, n)

# print_i_times_with_recursion(10)

def sum_of_n(n):
    # sum = (n*(n+1))/2
    # return sum
    # this is parameterized approach
    # def sum_of_n_recruse_param(i, sum):
    #     if i<1:
    #         return sum
    #     return sum_of_n_recruse_param(i-1, sum+i)
    #
    # return sum_of_n_recruse_param(n, 0)

    def sum_of_n_recurse_functional(n):
        if n==0:
            return 0
        return n + sum_of_n_recurse_functional(n-1)
    return sum_of_n_recurse_functional(n)

# print(sum_of_n(15))

def is_palindrome_num(num):
    reversed = 0
    original_num = num
    while num>0:
        last_digit = num%10
        reversed = (reversed*10)+last_digit
        num = int(num/10)
    return reversed == original_num

def infinite_seq():
    num = 1
    while True:
        yield num
        num += 1

# plaindrome_num = (i for i in infinite_seq() if is_palindrome_num(i))
def log_decorator(add_this):
    def wrapper(*args, **kwargs):
        print("calling function..")
        print(add_this(*args, **kwargs))
        print("call completed..")

    return wrapper

@log_decorator
def add_this(num, to_add):
    return num+to_add

# add_this(5, 10)

def check_highest_repeated_word(s):
    from collections import Counter

    words = s.split(' ')
    counter = Counter(words)
    sorted_word_count = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
    third_frequent_repeated_count = sorted_word_count[2][1]

    return [(word, count) for word, count in sorted_word_count if count == third_frequent_repeated_count]


# print(check_highest_repeated_word("apple banana apple orange banana apple orange orange banana banana"))

def make_even(num):
    if num%2 == 1:
        num += 1
    return num

my_list = [5, 7, 11, 10]
# even_list = map(make_even, my_list)
# even_list = filter(lambda x: x%2==0, my_list)

class Parent:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def greet(self):
        print("hellow from child1")
    # pass

class Child2(Parent):
    def __init__(self, city, name, age, location):
        self.city = city
        super().__init__(name, age, location)

    def greet(self):
        print("Hello from Child2!")
        super().greet()

class GrandChild(Child2, Child1):
    def greet_grandchild(self):
        super().greet()


# grand_child = GrandChild(name="hello", age=26, location="india", city="hyd")
# print(grand_child.city)
# grand_child.greet_grandchild()
# print(GrandChild.mro())

x=1
def func():
    global x
    print(x)
    x=2
# func()
# print(x)

# value = 42.6
# formatted_value = "{:.0f}".format((value))  # The `:d` specifier formats as an integer.
# print(formatted_value)

def insertion_sort(nums):
    for i in range(len(nums)):
        current = i
        while current>0 and nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            current -= 1
    return nums

# print(insertion_sort(nums=[10, 9, 8, 7]))

nested_list = [1, [23,[33], 10, 1], [[[[2], 7, 11]], 8], 0, 9]
# print([a for i in nested_list if isinstance(a, int) a else pass])
def flatten_list(nested_list):
    # flat_list = []
    for item in nested_list:
        if isinstance(item, int):
            # flat_list.append(item)
            yield item
        else:
            # flat_list += flatten_list(item)
            yield from flatten_list(item)
    # return flat_list

# print(flatten_list(nested_list=nested_list))
for ele in flatten_list(nested_list):
    print(ele)