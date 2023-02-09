"""Implementation of selection sort algorithm"""


import operator


OPS = {
    ">": operator.gt,
    "<": operator.lt,
}


def selection_sort(lst, reverse=False):
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



if __name__ == '__main__':
    print('\n##### TEST SELECTION SORT #####')
    list = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    print('Before list sort:', list)
    list2 = selection_sort(list)
    print('AFTER asc sort:  ', list2)
    list2 = selection_sort(list, True)
    print('AFTER desc sort: ', list2)