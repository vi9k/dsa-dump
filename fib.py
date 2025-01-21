

def fibonacci_of(n, cache={0:0, 1:1}):
    keys = {0, 1}
    if n not in keys:
        cache[n] = fibonacci_of(n-1, cache)+fibonacci_of(n-2, cache)

    return cache[n]

# print([fibonacci_of(i) for i in range(51)])

# def fibonacci_iterative(n):
#     fib_sequence = []
#     if n in {0, 1}:
#         return [n]
#     previous, fib_number = 0, 1
#     for i in range(2, n+1):
#         previous, fib_number = fib_number, previous+fib_number
#         fib_sequence.append(fib_number)
#     return fib_sequence

def fibonacci_iterative(n):
    # fib_sequence = []
    if n in {0, 1}:
        return [n]
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_number = fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(fib_number)
    return fib_sequence

# print(fibonacci_iterative(10))

def fibonacci_generator(n):
    previous, fib_number = 0,1
    for i in range(n):
        yield previous
        previous, fib_number = fib_number, previous+fib_number

# print(list(fibonacci_generator(50)))

def max_of(nums):
    max = nums[0]
    for n in nums:
        if n>max:
            max = n
    return max

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print("Maximum value:", max_of(numbers))

def fun():
    yield 1
    yield 2
    yield 3
#
# for i in fun():
#     print(i)

