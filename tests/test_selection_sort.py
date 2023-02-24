import pytest

from dsa.selection_sort import selection_sort


def test_selection_sort_asc():
    """Test selection sort ascending method"""
    expected_result_lst_asc_sorted = [0, 1, 2, 3, 4, 4, 5, 5, 6, 15, 23, 37]
    lst = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    result_lst_asc_sorted = selection_sort(lst)
    assert result_lst_asc_sorted == expected_result_lst_asc_sorted


def test_selection_sort_desc():
    """Test selection sort descending method"""
    expected_result_lst_desc_sorted = [37, 23, 15, 6, 5, 5, 4, 4, 3, 2, 1, 0]
    lst = [4, 2, 6, 5, 1, 3, 0, 37, 15, 23, 5, 4]
    result_lst_desc_sorted = selection_sort(lst, True)
    assert result_lst_desc_sorted == expected_result_lst_desc_sorted


@pytest.mark.xfail
def test_selection_sort_wrong_list():
    """Test selection sort method with wrong list"""
    selection_sort([1, 'hi'])


@pytest.mark.xfail
def test_selection_sort_wrong_call():
    """Test selection sort method with wrong call"""
    selection_sort(1)
