# swaps j+1 elements wih j if j+1 is greater
# keeps swap boolean, if false -> no elements swapped
# list is sorted

def bubble_sort(unsorted_list):
    for i in reversed(range(len(unsorted_list))):
        is_swapped = False
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                is_swapped = True

        if not is_swapped:
            return unsorted_list

    return unsorted_list

print(bubble_sort([5, 3, 1, 2, 4]))
print(bubble_sort([19, 7, 88, 65, 52, 2, 45]))