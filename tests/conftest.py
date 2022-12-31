"""Pytest Fixtures Across Multiple Test Files"""
import pytest

from dsa.doubly_linked_list import DoublyLinkedList


@pytest.fixture(scope="session")
def empty_dll():
    """Initialize an empty doubly linked list"""
    empty_dll = DoublyLinkedList()
    return empty_dll
