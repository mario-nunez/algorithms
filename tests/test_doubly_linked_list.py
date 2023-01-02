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
    dll = DoublyLinkedList([0, 1, 2])
    pop1 = dll.pop()
    pop2 = dll.pop()
    pop3 = dll.pop()

    result_dll = [node for node in dll]

    assert result_dll == expected_result_dll
    assert pop1.value == expected_result_pop_item1
    assert pop2.value == expected_result_pop_item2
    assert pop3.value == expected_result_pop_item3


def test_doubly_linked_list_pop_first():
    """Test doubly linked list pop_first method"""
    expected_result_dll = []
    expected_result_pop_item1 = 0
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 2
    dll = DoublyLinkedList([0, 1, 2])
    result_pop1 = dll.pop_first()
    result_pop2 = dll.pop_first()
    result_pop3 = dll.pop_first()
    result_dll = [node for node in dll]

    assert result_dll == expected_result_dll
    assert result_pop1.value == expected_result_pop_item1
    assert result_pop2.value == expected_result_pop_item2
    assert result_pop3.value == expected_result_pop_item3


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
        "value": 5,
        "prev": 4,
        "next": None
    }
    dll_empty = DoublyLinkedList()
    dll = DoublyLinkedList([0, 1, 2, 3, 4, 5])
    result_item_empty = dll_empty.get(0)
    result_item_nonexistent1 = dll.get(-1)
    result_item_nonexistent2 = dll.get(100)
    result_item1 = dll.get(1)
    result_item2 = dll.get(5)

    assert result_item_empty == expected_result_empty_item
    assert result_item_nonexistent1 == expected_result_item_nonexistent1
    assert result_item_nonexistent2 == expected_result_item_nonexistent2
    assert result_item1.value == expected_result_get_item1["value"]
    assert result_item1.prev.value == expected_result_get_item1["prev"]
    assert result_item1.next.value == expected_result_get_item1["next"]
    assert result_item2.value == expected_result_get_item2["value"]
    assert result_item2.prev.value == expected_result_get_item2["prev"]
    assert result_item2.next == expected_result_get_item2["next"]


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

    assert result_set ==expected_result_set
    assert result_set_error ==expected_result_set_error
    assert result_dll_list[0].value == expected_result_dll_list["first_node"]["value"]
    assert result_dll_list[0].prev == expected_result_dll_list["first_node"]["prev"]
    assert result_dll_list[0].next.value == expected_result_dll_list["first_node"]["next"]
    assert result_dll_list[1].value == expected_result_dll_list["second_node"]["value"]
    assert result_dll_list[1].prev.value == expected_result_dll_list["second_node"]["prev"]
    assert result_dll_list[1].next == expected_result_dll_list["second_node"]["next"]

