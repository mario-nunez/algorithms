"""Implementation of insertion sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def insertion_sort(lst: list, reverse: bool = False):
    """Sort a list using insertion sort algorithm"""
    if reverse is True:
        op_order = ">"
    else:
        op_order = "<"

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while OPS[op_order](temp, lst[j]) and j > -1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst
