"""Implementation of selection sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def selection_sort(lst: list, reverse: bool = False):
    """Sort a list using selection sort algorithm"""
    if reverse is True:
        op_order = ">"
    else:
        op_order = "<"
    for i in range(len(lst)-1):
        min_index = i
        # look at everything after 'i' index
        for j in range(i+1, len(lst)):
            if OPS[op_order](lst[j], lst[min_index]):
                min_index = j
        if i != min_index:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst
