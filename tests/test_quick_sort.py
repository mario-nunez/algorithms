import pytest

from dsa.quick_sort import quick_sort


def test_quick_sort_asc():
    """Test quick sort ascending method"""
    expected_result_lst_asc_sorted = [0, 1, 2, 3, 4, 4, 5, 5, 6, 15, 23, 37]
    lst = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    result_lst_asc_sorted = quick_sort(lst)
    assert result_lst_asc_sorted == expected_result_lst_asc_sorted


@pytest.mark.xfail
def test_quick_sort_wrong_list():
    """Test quick sort method with wrong list"""
    result = quick_sort([1, 'hi'])


@pytest.mark.xfail
def test_quick_sort_wrong_call():
    """Test quick sort method with wrong call"""
    result = quick_sort(1)
