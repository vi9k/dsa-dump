from http.cookiejar import cut_port_re
from sys import prefix
from textwrap import shorten
from unittest.mock import right


def remove_duplicates(arr):
    slow_pointer = 0
    for fast_pointer in range(len(arr)):
        if arr[slow_pointer] != arr[fast_pointer]:
            slow_pointer += 1
            arr[slow_pointer] = arr[fast_pointer]

    return arr[:slow_pointer+1]

# arr = [0, 0, 1, 1, 1, 2, 2]
# print(remove_duplicates(arr))

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    return slow_pointer.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

# head = build_list(iter([12, 1]), int)
# print(middle_of_linked_list(head))

"""
Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of 
the non-zero elements. Do this in-place using constant auxiliary space.

Input:

[1, 0, 2, 0, 0, 7]
Output:

[1, 2, 7, 0, 0, 0]
"""

from typing import List, Counter


def move_zeros(nums: List[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE
    slow_pointer = 0
    for fast_pointer in range(len(nums)):
        if nums[fast_pointer] != 0:
            nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
            slow_pointer += 1

    return nums

# in efficient alternate approach
def alternate_move_zeros(nums):
    zeros = [0] * len(nums)
    for index, value in enumerate(nums):
        if value != 0:
            zeros.insert(index, value)
            zeros.pop()

    return zeros

def another_alternate_move_zeros(nums):
    # copy in-place
    i = 0
    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1
    # fill rest with zeros
    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums

# nums = [1, 0, 2, 0, 0, 7]
# nums2 = [0, 1, 0, 3, 0]
# print(move_zeros(nums))
# print(move_zeros(nums2))

# print(alternate_move_zeros(nums))
# print(another_alternate_move_zeros(nums2))

"""
Given an array of integers sorted in ascending order, find two numbers that add up to a given target. 
Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and 
there is only one solution. Do this in O(n) time and with constant auxiliary space.

Input:

arr: a sorted integer array
target: the target sum we want to reach
Sample Input: [2, 3, 4, 5, 8, 11, 18], 8

Sample Output: 1 3
"""

def brute_force_two_sum_sorted(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    for ele in range(len(arr)):
        for j in range(ele, len(arr)):
            if arr[ele] + arr[j] == target:
                return ele, j

# print(brute_force_two_sum_sorted([2, 3, 4, 5, 8, 11, 18], 8))

def two_sum_sorted(arr, target):
    # for fast_pointer in reversed(range(len(arr))):
    #     if arr[slow_pointer] + arr[fast_pointer] < target:
    #         slow_pointer += 1
    #         second = fast_pointer

    left = 0
    right = len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return left, right
        if sum < target:
            left += 1
        else:
            right -= 1

    return []



# print(two_sum_sorted([2, 3, 4, 5, 8, 11, 18], 8))

"""
Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

Input: Do geese see God? Output: True

Input: Was it a car or a cat I saw? Output: True

Input: A brown fox jumping over Output: False

"""

def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    # s = s.replace(" ", "").lower()
    s = ''.join(c for c in s if c.isalnum()).lower()
    palindrome = True
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            palindrome = False
        end -= 1
        start += 1
        if start == end:
            return palindrome

    return palindrome

# print(is_palindrome("A brown fox jumping over Output"))

"""
Given an array representing heights of vertical lines, find the maximum area of water trapped between two lines.

Input: [1,8,6,2,5,4,8,3,7].

Output: 49.
"""

def container_with_most_water(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# print(container_with_most_water([1,8,6,2,5,4,8,3,7]))

"""
Given an array (list) nums consisted of only non-negative integers, 
find the largest sum among all subarrays of length k in nums.

For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 
subarray sum is given by [3, 7, 4] which sums to 14.
"""

def subarray_sum_fixed(nums: List[int], k: int) -> tuple:
    # WRITE YOUR BRILLIANT CODE HERE
    # largest = 0,
    # window_size = k
    # for i in range(len(nums) - window_size):
    #     window_sum = sum(nums[i: window_size+i])
    #     if window_sum > largest[0]:
    #         largest = window_sum, nums[i: window_size+i]
    # return largest

    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)
    return largest


# print(subarray_sum_fixed(nums = [1, 2, 3, 7, 4, 1], k = 3))


"""
Given a string original and a string check, find the starting index of all substrings of original that is an 
anagram of check. The output must be sorted in ascending order.

Parameters
original: A string
check: A string
Result
A list of integers representing the starting indices of all anagrams of check.
Examples
Example 1
Input: original = "cbaebabacd", check = "abc"

Output: [0, 6]

Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".
"""

def find_all_anagrams(original: str, check: str) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    # anagram_index = []
    # for right in range(len(original)):
    #     window = original[right: len(check)+right]
    #     if sorted(list(window)) == sorted(list(check)):
    #         anagram_index.append(right)
    # return anagram_index

    counter = Counter(check)
    window_counter = Counter()
    anagram_index = []
    for right in range(len(original) - len(check)):
        window_counter[original[right]] += 1
        if right >= len(check):
            window_counter[original[right - len(check)]] -= 1
        if window_counter == counter:
            anagram_index.append(right - len(check) + 1)
    return anagram_index

    # original_len, check_len = len(original), len(check)
    # if original_len < check_len:
    #     return []
    #
    # res = []
    # # stores the frequency of each character in the check string
    # check_counter = [0] * 26
    # # stores the frequency of each character in the current window
    # window = [0] * 26
    # a = ord("a")  # ascii value of 'a'
    # # first window
    # for i in range(check_len):
    #     check_counter[ord(check[i]) - a] += 1
    #     window[ord(original[i]) - a] += 1
    # if window == check_counter:
    #     res.append(0)
    #
    # for i in range(check_len, original_len):
    #     ord(original[i]) - a
    #     window[ord(original[i - check_len]) - a] -= 1
    #     window[ord(original[i]) - a] += 1
    #     if window == check_counter:
    #         res.append(i - check_len + 1)
    # return res

# print(find_all_anagrams(original = "nabanabannaabbaanana", check = "banana"))

"""
Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not 
exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).
"""

def subarray_sum_longest(nums: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    largest = 0
    window_sum = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target and left <= right:
            window_sum -= nums[left]
            left += 1
            # print(left)
        largest = max(largest, right-left+1)

    return largest

# print(subarray_sum_longest(nums=[-1, -2, -3, -4, -5], target=-6))

"""
Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: The longest substrings are abc and cab, both of length 3.

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, with a length of 2.
"""
from collections import Counter

def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    window_counter = Counter()
    left = 0
    largest = 0
    for right in range(len(s)):
        window_counter[s[right]] += 1
        while window_counter[s[right]] > 1 and left <= right:
            window_counter[s[left]] -= 1
            left += 1
        largest = max(largest, right-left+1)
    return largest

# print(longest_substring_without_repeating_characters("abccabcabcc"))

"""
This time given a positive integer array nums, we want to find the length of the shortest subarray such that the 
subarray sum is at least target. Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10, 
then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.

We'll assume for this problem that it's guaranteed target will not exceed the sum of all elements in nums.
"""

def subarray_sum_shortest(nums: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    window_sum = 0
    shortest = len(nums)+1
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            shortest = min(shortest, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return shortest

# print(subarray_sum_shortest(nums=[1, 4, 1, 7, 3, 0, 2, 5], target=10))

"""
Given a list of integers cards, your goal is to match a pair of cards, but you can only pick up cards in a 
consecutive manner. What's the minimum number of cards that you need to pick up to make a pair? 
If there are no matching pairs, return -1.

For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s and 
picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match a pair of 3s and 4 consecutive cards to 
match 4s, so you need to pick up at least 4 cards to make a match.
"""

def least_consecutive_cards_to_match(cards: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    match_counter = Counter()
    left = 0
    shortest = len(cards)+1
    for right in range(len(cards)):
        match_counter[cards[right]] += 1
        while match_counter[cards[right]] == 2:
            shortest = min(shortest, right-left+1)
            match_counter[cards[left]] -= 1
            left += 1
    return shortest if shortest<=len(cards)+1 else -1

    # window = Counter()
    # shortest = len(cards) + 1
    # left = 0
    # for right in range(len(cards)):
    #     window[cards[right]] += 1
    #     while window[cards[right]] == 2:
    #         shortest = min(shortest, right - left + 1)
    #         window[cards[left]] -= 1
    #         left += 1
    # return shortest if shortest != len(cards) + 1 else -1

# print(least_consecutive_cards_to_match(cards = [3, 4, 2, 3, 4, 7]))
# print(least_consecutive_cards_to_match(cards = [1, 2, 3, 1, 3, 2]))

"""
Given an array of integers and an integer target, find a subarray that sums to target and return the start and 
end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

def subarray_sum(arr: List[int], target: int) -> List[int]:
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    # prefix_sums = {}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []

    # prefix_sums = [0]
    # for i in arr:
    #     prefix_sums.append(prefix_sums[-1] + i)
    # left = 0
    # for prefix in range(1, len(prefix_sums)):
    #     while prefix_sums[prefix] - prefix_sums[left] > target:
    #         left += 1
    #     if prefix_sums[prefix] - prefix_sums[left] == target:
    #         return [left, prefix]
    # return []



# print(subarray_sum([1, -20, -3, 30, 5, 4], 7))
# print(subarray_sum([0, -20, -3, 30, 5, 4], 0))

""" Find the total number of subarrays that sums up to target."""

def subarray_sum_total(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    prefix_sums = Counter()
    prefix_sums[0] = 1
    count = 0
    current_sum = 0
    for right in arr:
        current_sum += right
        if (current_sum-target) in prefix_sums:
            count += prefix_sums[current_sum-target]
        prefix_sums[current_sum] += 1
    return count

# print(subarray_sum_total([1, 2, 3], 3))
# print(subarray_sum_total([1, -20, -3, 30, 5, 4], 7))

def range_sum(nums, left, right):
    prefix_sums = [0]
    for i in range(len(nums)):
        prefix_sums.append(prefix_sums[-1] + nums[i])
    return prefix_sums[right+1] - prefix_sums[left]

# print(range_sum([1, 2, 3, 4], 1, 3))

def product_of_array_except_self(nums: List[int]) -> List[int]:
    length = len(nums)
    result = [1] * length

    left = 1
    for i in range(length):
        result[i] = left
        left *= nums[i]

    # right = 1
    # for i in reversed(range(length)):
    #     result[0] = right
    #     right *= nums[i]

    right = 1
    for i in reversed(range(length)):
        result[i] *= right
        right *= nums[i]

    return result

print(product_of_array_except_self([1, 2, 3, 4]))