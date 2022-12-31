"""Test doubly linked implementation"""
import pytest

from dsa.doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list_initialization():
    """Test doubly linked list initializacion"""
    expected_result_dll_empty = []
    expected_result_dll_single = {
        "first_node": {
            "value": 0,
            "prev": None,
            "next": None
        }
    }
    expected_result_dll_list = {
        "first_node": {
            "value": 0,
            "prev": None,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "prev": 0,
            "next": 2
        },
        "third_node": {
            "value": 2,
            "prev": 1,
            "next": None
        }
    }

    dll_empty = DoublyLinkedList()
    dll_single_value = DoublyLinkedList(0)
    dll_list_values = DoublyLinkedList([0, 1, 2])
    result_dll_empty = [node for node in dll_empty]
    result_dll_single = [node for node in dll_single_value]
    result_dll_list = [node for node in dll_list_values]

    # test empty initialization
    assert result_dll_empty == expected_result_dll_empty

    # test initialization with a single value
    assert result_dll_single[0].value == expected_result_dll_single["first_node"]["value"]
    assert result_dll_single[0].prev == expected_result_dll_single["first_node"]["prev"]
    assert result_dll_single[0].next == expected_result_dll_single["first_node"]["next"]

    # test initialization with a list of values
    assert result_dll_list[0].value == expected_result_dll_list["first_node"]["value"]
    assert result_dll_list[0].prev == expected_result_dll_list["first_node"]["prev"]
    assert result_dll_list[0].next.value == expected_result_dll_list["first_node"]["next"]
    assert result_dll_list[1].value == expected_result_dll_list["second_node"]["value"]
    assert result_dll_list[1].prev.value == expected_result_dll_list["second_node"]["prev"]
    assert result_dll_list[1].next.value == expected_result_dll_list["second_node"]["next"]
    assert result_dll_list[2].value == expected_result_dll_list["third_node"]["value"]
    assert result_dll_list[2].prev.value == expected_result_dll_list["third_node"]["prev"]
    assert result_dll_list[2].next == expected_result_dll_list["third_node"]["next"]


@pytest.mark.xfail
def test_doubly_linked_list_wrong_initialization():
    """Test doubly linked list wrong initializacion"""
    DoublyLinkedList(1, 2, 3)


def test_doubly_linked_list_append():
    """Test doubly linked list append"""
    expected_result = [0, 1, 2]
    dll = DoublyLinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    result = [node.value for node in dll]

    assert result == expected_result


def test_doubly_linked_list_prepend(empty_dll):
    """Test doubly linked list prepend"""
    expected_result = [2, 1, 0]
    dll = empty_dll
    dll.prepend(0)
    dll.prepend(1)
    dll.prepend(2)
    result = [node.value for node in dll]

    assert result == expected_result
