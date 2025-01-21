# insertion sort

def sort_list(unsorted_list):
    for i in range(len(unsorted_list)):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            # swapping two elements where the previous element is greater than current element
            unsorted_list[current], unsorted_list[current-1] = unsorted_list[current-1], unsorted_list[current]
            # decrementing current in order to run the check for previous elements
            current -= 1

    return unsorted_list

print(sort_list([5, 3, 1, 2, 4]))
print(sort_list([19, 7, 88, 65, 52, 2, 45]))

def insertion_sort(nums):
    for i in range(len(nums)):
        current = i
        while current>0 and nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums