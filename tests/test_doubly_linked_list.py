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
    """Test doubly linked list append method"""
    expected_result_dll = {
        "first_node": {
            "value": 0,
            "prev": None,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "prev": 0,
            "next": None
        }
    }
    dll = DoublyLinkedList()
    dll.append(0)
    dll.append(1)
    result_dll = [node for node in dll]

    assert result_dll[0].value == expected_result_dll["first_node"]["value"]
    assert result_dll[0].prev == expected_result_dll["first_node"]["prev"]
    assert result_dll[0].next.value == expected_result_dll["first_node"]["next"]
    assert result_dll[1].value == expected_result_dll["second_node"]["value"]
    assert result_dll[1].prev.value == expected_result_dll["second_node"]["prev"]
    assert result_dll[1].next == expected_result_dll["second_node"]["next"]


def test_doubly_linked_list_prepend(empty_dll):
    """Test doubly linked list prepend method"""
    expected_result_dll = {
        "first_node": {
            "value": 1,
            "prev": None,
            "next": 0
        },
        "second_node": {
            "value": 0,
            "prev": 1,
            "next": None
        }
    }
    dll = empty_dll
    dll.prepend(0)
    dll.prepend(1)
    result_dll = [node for node in dll]

    assert result_dll[0].value == expected_result_dll["first_node"]["value"]
    assert result_dll[0].prev == expected_result_dll["first_node"]["prev"]
    assert result_dll[0].next.value == expected_result_dll["first_node"]["next"]
    assert result_dll[1].value == expected_result_dll["second_node"]["value"]
    assert result_dll[1].prev.value == expected_result_dll["second_node"]["prev"]
    assert result_dll[1].next == expected_result_dll["second_node"]["next"]


def test_doubly_linked_list_pop():
    """Test doubly linked list pop method"""
    expected_result_dll = []
    expected_result_pop_item1 = 2
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 0
    expected_result_pop_item4 = None
    dll = DoublyLinkedList([0, 1, 2])
    result_pop_item1 = dll.pop()
    result_pop_item2 = dll.pop()
    result_pop_item3 = dll.pop()
    result_pop_item4 = dll.pop()
    result_dll = [node for node in dll]

    assert result_dll == expected_result_dll
    assert result_pop_item1.value == expected_result_pop_item1
    assert result_pop_item2.value == expected_result_pop_item2
    assert result_pop_item3.value == expected_result_pop_item3
    assert result_pop_item4 == expected_result_pop_item4


def test_doubly_linked_list_pop_first():
    """Test doubly linked list pop_first method"""
    expected_result_dll = []
    expected_result_pop_item1 = 0
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 2
    expected_result_pop_item4 = None
    dll = DoublyLinkedList([0, 1, 2])
    result_pop_item1 = dll.pop_first()
    result_pop_item2 = dll.pop_first()
    result_pop_item3 = dll.pop_first()
    result_pop_item4 = dll.pop_first()
    result_dll = [node for node in dll]

    assert result_dll == expected_result_dll
    assert result_pop_item1.value == expected_result_pop_item1
    assert result_pop_item2.value == expected_result_pop_item2
    assert result_pop_item3.value == expected_result_pop_item3
    assert result_pop_item4 == expected_result_pop_item4


def test_doubly_linked_list_get():
    """Test doubly linked list get method"""
    expected_result_empty_item = None
    expected_result_item_nonexistent1 = None
    expected_result_item_nonexistent2 = None
    expected_result_get_item1 = {
        "value": 1,
        "prev": 0,
        "next": 2
    }
    expected_result_get_item2 = {
        "value": 4,
        "prev": 3,
        "next": 5
    }
    dll_empty = DoublyLinkedList()
    dll = DoublyLinkedList([0, 1, 2, 3, 4, 5])
    result_item_empty = dll_empty.get(0)
    result_item_nonexistent1 = dll.get(-1)
    result_item_nonexistent2 = dll.get(100)
    result_get_item1 = dll.get(1)
    result_get_item2 = dll.get(4)

    assert result_item_empty == expected_result_empty_item
    assert result_item_nonexistent1 == expected_result_item_nonexistent1
    assert result_item_nonexistent2 == expected_result_item_nonexistent2
    assert result_get_item1.value == expected_result_get_item1["value"]
    assert result_get_item1.prev.value == expected_result_get_item1["prev"]
    assert result_get_item1.next.value == expected_result_get_item1["next"]
    assert result_get_item2.value == expected_result_get_item2["value"]
    assert result_get_item2.prev.value == expected_result_get_item2["prev"]
    assert result_get_item2.next.value == expected_result_get_item2["next"]


@pytest.mark.xfail
def test_doubly_linked_list_wrong_get():
    """Test doubly linked list wrong get method call"""
    dll = DoublyLinkedList([0, 1, 2, 3, 4, 5])
    dll.get('random_string')


def test_doubly_linked_list_set_value():
    """Test doubly linked list set_value method"""
    expected_result_dll_list = {
        "first_node": {
            "value": 0,
            "prev": None,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "prev": 0,
            "next": None
        }
    }
    expected_result_set = True
    expected_result_set_error = False
    dll = DoublyLinkedList([0, 3])
    result_set = dll.set_value(1, 1)
    result_set_error = dll.set_value(100, 1)
    result_dll_list = [node for node in dll]

    assert result_set == expected_result_set
    assert result_set_error == expected_result_set_error
    assert result_dll_list[0].value == expected_result_dll_list["first_node"]["value"]
    assert result_dll_list[0].prev == expected_result_dll_list["first_node"]["prev"]
    assert result_dll_list[0].next.value == expected_result_dll_list["first_node"]["next"]
    assert result_dll_list[1].value == expected_result_dll_list["second_node"]["value"]
    assert result_dll_list[1].prev.value == expected_result_dll_list["second_node"]["prev"]
    assert result_dll_list[1].next == expected_result_dll_list["second_node"]["next"]


def test_doubly_linked_list_insert():
    """Test doubly linked list insert method"""
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
    expected_result_insert1 = True
    expected_result_insert2 = True
    expected_result_insert3 = True
    expected_result_insert_error1 = False
    expected_result_insert_error2 = False
    dll = DoublyLinkedList()
    result_insert1 = dll.insert(0, 0)
    result_insert2 = dll.insert(1, 2)
    result_insert3 = dll.insert(1, 1)
    result_insert_error1 = dll.insert(100, 0)
    result_insert_error2 = dll.insert(-1, 0)
    result_dll_list = [node for node in dll]

    assert result_insert1 == expected_result_insert1
    assert result_insert2 == expected_result_insert2
    assert result_insert3 == expected_result_insert3
    assert result_insert_error1 == expected_result_insert_error1
    assert result_insert_error2 == expected_result_insert_error2
    assert result_dll_list[0].value == expected_result_dll_list["first_node"]["value"]
    assert result_dll_list[0].prev == expected_result_dll_list["first_node"]["prev"]
    assert result_dll_list[0].next.value == expected_result_dll_list["first_node"]["next"]
    assert result_dll_list[1].value == expected_result_dll_list["second_node"]["value"]
    assert result_dll_list[1].prev.value == expected_result_dll_list["second_node"]["prev"]
    assert result_dll_list[1].next.value == expected_result_dll_list["second_node"]["next"]
    assert result_dll_list[2].value == expected_result_dll_list["third_node"]["value"]
    assert result_dll_list[2].prev.value == expected_result_dll_list["third_node"]["prev"]
    assert result_dll_list[2].next == expected_result_dll_list["third_node"]["next"]


def test_doubly_linked_list_remove():
    """Test doubly linked list remove method"""
    expected_result_dll_list = {
        "first_node": {
            "value": 1,
            "prev": None,
            "next": 3
        },
        "second_node": {
            "value": 3,
            "prev": 1,
            "next": None
        }
    }
    expected_result_removed_error1 = False
    expected_result_removed_error2 = False
    expected_result_item_removed_last = 4
    expected_result_item_removed_first = 0
    expected_result_item_removed_middle = 2
    dll = DoublyLinkedList([0, 1, 2, 3, 4])
    result_removed_error1 = dll.remove(-1)
    result_removed_error2 = dll.remove(100)
    result_item_removed_last = dll.remove(4)
    result_item_removed_first = dll.remove(0)
    result_item_removed_middle = dll.remove(1)
    result_dll_list = [node for node in dll]

    assert result_removed_error1 == expected_result_removed_error1
    assert result_removed_error2 == expected_result_removed_error2
    assert result_item_removed_last.value == expected_result_item_removed_last
    assert result_item_removed_first.value == expected_result_item_removed_first
    assert result_item_removed_middle.value == expected_result_item_removed_middle
    assert result_dll_list[0].value == expected_result_dll_list["first_node"]["value"]
    assert result_dll_list[0].prev == expected_result_dll_list["first_node"]["prev"]
    assert result_dll_list[0].next.value == expected_result_dll_list["first_node"]["next"]
    assert result_dll_list[1].value == expected_result_dll_list["second_node"]["value"]
    assert result_dll_list[1].prev.value == expected_result_dll_list["second_node"]["prev"]
    assert result_dll_list[1].next == expected_result_dll_list["second_node"]["next"]


def test_doubly_linked_list_len():
    """Test doubly linked list len special method"""
    expected_result_dll_empty_len = 0
    expected_result_dll_len = 4
    dll_empty = DoublyLinkedList()
    dll = DoublyLinkedList([0, 1, 2, 3])
    result_dll_empty_len = len(dll_empty)
    result_dll_len = len(dll)

    assert result_dll_empty_len == expected_result_dll_empty_len
    assert result_dll_len == expected_result_dll_len


def test_doubly_linked_list_repr():
    """Test doubly linked list repr special method"""
    expected_result_dll_empty_repr = "None"
    expected_result_dll_repr = "0 <-> 1 <-> None"
    dll_empty = DoublyLinkedList()
    dll = DoublyLinkedList([0, 1])
    result_dll_empty_repr = repr(dll_empty)
    result_dll_repr = repr(dll)

    assert result_dll_empty_repr == expected_result_dll_empty_repr
    assert result_dll_repr == expected_result_dll_repr


def test_doubly_linked_list_node_repr():
    """Test doubly linked list node repr special method"""
    expected_result_first_node_repr = "Node(value=0, prev=None, next=1)"
    expected_result_second_node_repr = "Node(value=1, prev=0, next=2)"
    expected_result_third_node_repr = "Node(value=2, prev=1, next=None)"
    dll = DoublyLinkedList([0, 1, 2])
    result_first_node_repr = repr(dll.get(0))
    result_second_node_repr = repr(dll.get(1))
    result_third_node_repr = repr(dll.get(2))

    assert result_first_node_repr == expected_result_first_node_repr
    assert result_second_node_repr == expected_result_second_node_repr
    assert result_third_node_repr == expected_result_third_node_repr
