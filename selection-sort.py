# selects index element as min and compares with all elements and updates min_index, finally swaps their positions
# this is repeated till all are sorted

def selection_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        min_index = i
        # identify min_index my comparing with min_index with all elements
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                # updating min_index
                min_index = j
        # swapping min_index with first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list

print(selection_sort([5, 3, 1, 2, 4]))
print(selection_sort([19, 7, 88, 65, 52, 2, 45]))