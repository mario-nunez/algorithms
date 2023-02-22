import pytest

from dsa.insertion_sort import insertion_sort


def test_insertion_sort_asc():
    """Test insertion sort ascending method"""
    expected_result_lst_asc_sorted = [0, 1, 2, 3, 4, 4, 5, 5, 6, 15, 23, 37]
    lst = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    result_lst_asc_sorted = insertion_sort(lst)
    assert result_lst_asc_sorted == expected_result_lst_asc_sorted


def test_insertion_sort_desc():
    """Test insertion sort descending method"""
    expected_result_lst_desc_sorted = [37, 23, 15, 6, 5, 5, 4, 4, 3, 2, 1, 0]
    lst = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    result_lst_desc_sorted = insertion_sort(lst, True)
    assert result_lst_desc_sorted == expected_result_lst_desc_sorted


@pytest.mark.xfail
def test_insertion_sort_wrong_list():
    """Test insertion sort method with wrong list"""
    result = insertion_sort([1, 'hi'])


@pytest.mark.xfail
def test_insertion_sort_wrong_call():
    """Test insertion sort method with wrong call"""
    result = insertion_sort(1)
