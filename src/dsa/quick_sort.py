"""Implementation of quick sort algorithm"""


def swap(lst, idx1, idx2):
    """Swap items within the list"""
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp

def pivot(lst, pivot_idx, end_idx):
    """Separate the list in greater and less than a pivot point, sort the pivot
    point and return the index of the sorted pivot point"""
    swap_idx = pivot_idx
    # Separate the list in greater and less than a pivot point
    for i in range(pivot_idx+1, end_idx+1):
        if lst[i] < lst[pivot_idx]:
            swap_idx += 1
            swap(lst, swap_idx, i)
    # sort the pivot point
    swap(lst, pivot_idx, swap_idx)
    return swap_idx

def quick_sort_helper(lst, first_idx, last_idx):
    """Implement quick sort algorithm"""
    # base case: left index < right index
    if first_idx < last_idx:
        pivot_idx = pivot(lst, first_idx, last_idx)
        quick_sort_helper(lst, first_idx, pivot_idx-1)
        quick_sort_helper(lst, pivot_idx+1, last_idx)
    return lst

def quick_sort(lst: list):
    """Sort a list using quick sort algorithm"""
    return quick_sort_helper(lst, 0, len(lst)-1)
