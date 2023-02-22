"""Implementation of bubble sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def bubble_sort(lst: list, reverse: bool=False):
    """Sort a list using bubble sort algorithm"""
    if reverse is True:
        op_order = "<"
    else:
        op_order = ">"
    # to sort the list iterate one time less than list's length
    for i in range(len(lst)-1, 0, -1):
        swaped = False
        # one less iteration each time
        for j in range(i):
            # condition depends on sorting order selected
            if OPS[op_order](lst[j], lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                swaped = True
        # no changes sorting an element means that next iterations can be skipped
        if swaped is False:
            break
    return lst
