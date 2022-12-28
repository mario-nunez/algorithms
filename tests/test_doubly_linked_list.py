from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list():
    """Test doubly linked list methods"""
    # test initialization
    expected_result_empty = []
    expected_result_single = [0]
    expected_result_list = [0, 1, 2]
    dll_empty = DoublyLinkedList()
    dll_single_value = DoublyLinkedList(0)
    dll_list_values = DoublyLinkedList([0, 1, 2])
    result_empty = [node.value for node in dll_empty]
    result_single = [node.value for node in dll_single_value]
    result_list = [node.value for node in dll_list_values]

    assert result_empty == expected_result_empty
    assert result_single == expected_result_single
    assert result_list == expected_result_list

    # test append
    expected_result = [0, 1, 2]
    dll = DoublyLinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    result = [node.value for node in dll]

    assert result == expected_result
