"""Test singly linked implementation"""
import pytest

from dsa.singly_linked_list import LinkedList


@pytest.mark.xfail
def test_singly_linked_list_wrong_initialization():
    """Test singly linked list wrong initializacion"""
    LinkedList(1, 2, 3)


def test_singly_linked_list_repr():
    """Test singly linked list repr special method"""
    expected_result_sll_empty_repr = "None"
    expected_result_sll_repr = "0 -> 1 -> None"
    sll_empty = LinkedList()
    sll = LinkedList([0, 1])
    result_sll_empty_repr = repr(sll_empty)
    result_sll_repr = repr(sll)

    assert result_sll_empty_repr == expected_result_sll_empty_repr
    assert result_sll_repr == expected_result_sll_repr


def test_singly_linked_list_node_repr():
    """Test singly linked list node repr special method"""
    expected_result_first_node_repr = "Node(value=0, next=1)"
    expected_result_second_node_repr = "Node(value=1, next=2)"
    expected_result_third_node_repr = "Node(value=2, next=None)"
    sll = LinkedList([0, 1, 2])
    result_first_node_repr = repr(sll.get(0))
    result_second_node_repr = repr(sll.get(1))
    result_third_node_repr = repr(sll.get(2))

    assert result_first_node_repr == expected_result_first_node_repr
    assert result_second_node_repr == expected_result_second_node_repr
    assert result_third_node_repr == expected_result_third_node_repr
