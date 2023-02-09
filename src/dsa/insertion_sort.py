"""Implementation of insertion sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def insertion_sort(lst, reverse=False):
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


if __name__ == '__main__':
    print('\n##### TEST INSERTION SORT #####')
    list = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    print('Before list sort:', list)
    list2 = insertion_sort(list)
    print('AFTER asc sort:  ', list2)
    list2 = insertion_sort(list, True)
    print('AFTER desc sort: ', list2)