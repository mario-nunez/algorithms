"""Implementation of merge sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def merge(lst1, lst2, reverse):
    """Merge two sorted list into one single sorted list"""
    combined = []
    i, j = 0, 0
    if reverse is True:
        op_order = ">"
    else:
        op_order = "<"

    # stop loop when one of both lists does not have any items left
    while i < len(lst1) and j < len(lst2):
        if OPS[op_order](lst1[i], lst2[j]):
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
    # add the remaining items
    while i < len(lst1):
        combined.append(lst1[i])
        i += 1
    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    return combined


def merge_sort(lst: list, reverse: bool = False):
    """Sort a list using merge sort algorithm"""
    # base case
    if len(lst) == 1:
        return lst
    mid_index = int(len(lst)/2)
    left = merge_sort(lst[:mid_index], reverse)
    right = merge_sort(lst[mid_index:], reverse)
    return merge(left, right, reverse)
