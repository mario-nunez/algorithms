"""Test singly linked implementation"""
import pytest

from dsa.singly_linked_list import LinkedList


@pytest.mark.xfail
def test_singly_linked_list_wrong_initialization():
    """Test singly linked list wrong initializacion"""
    LinkedList(1, 2, 3)
