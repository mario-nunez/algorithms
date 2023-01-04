"""Test singly linked implementation"""
import pytest

from dsa.singly_linked_list import LinkedList


def test_singly_linked_list_initialization():
    """Test singly linked list initializacion"""
    expected_result_sll_empty = []
    expected_result_sll_single = {
        "first_node": {
            "value": 0,
            "next": None
        }
    }
    expected_result_sll_list = {
        "first_node": {
            "value": 0,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "next": 2
        },
        "third_node": {
            "value": 2,
            "next": None
        }
    }
    sll_empty = LinkedList()
    sll_single_value = LinkedList(0)
    sll_list_values = LinkedList([0, 1, 2])
    result_sll_empty = [node for node in sll_empty]
    result_sll_single = [node for node in sll_single_value]
    result_sll_list = [node for node in sll_list_values]

    # test empty initialization
    assert result_sll_empty == expected_result_sll_empty

    # test initialization with a single value
    assert result_sll_single[0].value == expected_result_sll_single["first_node"]["value"]
    assert result_sll_single[0].next == expected_result_sll_single["first_node"]["next"]

    # test initialization with a list of values
    assert result_sll_list[0].value == expected_result_sll_list["first_node"]["value"]
    assert result_sll_list[0].next.value == expected_result_sll_list["first_node"]["next"]
    assert result_sll_list[1].value == expected_result_sll_list["second_node"]["value"]
    assert result_sll_list[1].next.value == expected_result_sll_list["second_node"]["next"]
    assert result_sll_list[2].value == expected_result_sll_list["third_node"]["value"]
    assert result_sll_list[2].next == expected_result_sll_list["third_node"]["next"]


@pytest.mark.xfail
def test_singly_linked_list_wrong_initialization():
    """Test singly linked list wrong initializacion"""
    LinkedList(1, 2, 3)


def test_singly_linked_list_append():
    """Test singly linked list append method"""
    expected_result_sll = {
        "first_node": {
            "value": 0,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "next": None
        }
    }
    sll = LinkedList()
    sll.append(0)
    sll.append(1)
    result_sll = [node for node in sll]

    assert result_sll[0].value == expected_result_sll["first_node"]["value"]
    assert result_sll[0].next.value == expected_result_sll["first_node"]["next"]
    assert result_sll[1].value == expected_result_sll["second_node"]["value"]
    assert result_sll[1].next == expected_result_sll["second_node"]["next"]


def test_singly_linked_list_prepend():
    """Test singly linked list prepend method"""
    expected_result_sll = {
        "first_node": {
            "value": 1,
            "next": 0
        },
        "second_node": {
            "value": 0,
            "next": None
        }
    }
    sll = LinkedList()
    sll.prepend(0)
    sll.prepend(1)
    result_sll = [node for node in sll]

    assert result_sll[0].value == expected_result_sll["first_node"]["value"]
    assert result_sll[0].next.value == expected_result_sll["first_node"]["next"]
    assert result_sll[1].value == expected_result_sll["second_node"]["value"]
    assert result_sll[1].next == expected_result_sll["second_node"]["next"]


def test_singly_linked_list_pop():
    """Test singly linked list pop method"""
    expected_result_sll = []
    expected_result_pop_item1 = 2
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 0
    expected_result_pop_item4 = None
    sll = LinkedList([0, 1, 2])
    result_pop_item1 = sll.pop()
    result_pop_item2 = sll.pop()
    result_pop_item3 = sll.pop()
    result_pop_item4 = sll.pop()
    result_sll = [node for node in sll]

    assert result_sll == expected_result_sll
    assert result_pop_item1.value == expected_result_pop_item1
    assert result_pop_item2.value == expected_result_pop_item2
    assert result_pop_item3.value == expected_result_pop_item3
    assert result_pop_item4 == expected_result_pop_item4


def test_singly_linked_list_pop_first():
    """Test singly linked list pop_first method"""
    expected_result_sll = []
    expected_result_pop_item1 = 0
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 2
    expected_result_pop_item4 = None
    sll = LinkedList([0, 1, 2])
    result_pop_item1 = sll.pop_first()
    result_pop_item2 = sll.pop_first()
    result_pop_item3 = sll.pop_first()
    result_pop_item4 = sll.pop_first()
    result_sll = [node for node in sll]

    assert result_sll == expected_result_sll
    assert result_pop_item1.value == expected_result_pop_item1
    assert result_pop_item2.value == expected_result_pop_item2
    assert result_pop_item3.value == expected_result_pop_item3
    assert result_pop_item4 == expected_result_pop_item4


def test_singly_linked_list_get():
    """Test singly linked list get method"""
    expected_result_empty_item = None
    expected_result_item_nonexistent1 = None
    expected_result_item_nonexistent2 = None
    expected_result_get_item1 = {
        "value": 1,
        "next": 2
    }
    expected_result_get_item2 = {
        "value": 4,
        "next": 5
    }
    sll_empty = LinkedList()
    sll = LinkedList([0, 1, 2, 3, 4, 5])
    result_item_empty = sll_empty.get(0)
    result_item_nonexistent1 = sll.get(-1)
    result_item_nonexistent2 = sll.get(100)
    result_get_item1 = sll.get(1)
    result_get_item2 = sll.get(4)

    assert result_item_empty == expected_result_empty_item
    assert result_item_nonexistent1 == expected_result_item_nonexistent1
    assert result_item_nonexistent2 == expected_result_item_nonexistent2
    assert result_get_item1.value == expected_result_get_item1["value"]
    assert result_get_item1.next.value == expected_result_get_item1["next"]
    assert result_get_item2.value == expected_result_get_item2["value"]
    assert result_get_item2.next.value == expected_result_get_item2["next"]


@pytest.mark.xfail
def test_singly_linked_list_wrong_get():
    """Test singly linked list wrong get method call"""
    sll = LinkedList([0, 1, 2, 3, 4, 5])
    sll.get('random_string')


def test_singly_linked_list_set_value():
    """Test singly linked list set_value method"""
    expected_result_sll_list = {
        "first_node": {
            "value": 0,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "next": None
        }
    }
    expected_result_set = True
    expected_result_set_error = False
    sll = LinkedList([0, 3])
    result_set = sll.set_value(1, 1)
    result_set_error = sll.set_value(100, 1)
    result_sll_list = [node for node in sll]

    assert result_set == expected_result_set
    assert result_set_error == expected_result_set_error
    assert result_sll_list[0].value == expected_result_sll_list["first_node"]["value"]
    assert result_sll_list[0].next.value == expected_result_sll_list["first_node"]["next"]
    assert result_sll_list[1].value == expected_result_sll_list["second_node"]["value"]
    assert result_sll_list[1].next == expected_result_sll_list["second_node"]["next"]


def test_singly_linked_list_insert():
    """Test singly linked list insert method"""
    expected_result_sll_list = {
        "first_node": {
            "value": 0,
            "next": 1
        },
        "second_node": {
            "value": 1,
            "next": 2
        },
        "third_node": {
            "value": 2,
            "next": None
        }
    }
    expected_result_insert1 = True
    expected_result_insert2 = True
    expected_result_insert3 = True
    expected_result_insert_error1 = False
    expected_result_insert_error2 = False
    sll = LinkedList()
    result_insert1 = sll.insert(0, 0)
    result_insert2 = sll.insert(1, 2)
    result_insert3 = sll.insert(1, 1)
    result_insert_error1 = sll.insert(100, 0)
    result_insert_error2 = sll.insert(-1, 0)
    result_sll_list = [node for node in sll]

    assert result_insert1 == expected_result_insert1
    assert result_insert2 == expected_result_insert2
    assert result_insert3 == expected_result_insert3
    assert result_insert_error1 == expected_result_insert_error1
    assert result_insert_error2 == expected_result_insert_error2
    assert result_sll_list[0].value == expected_result_sll_list["first_node"]["value"]
    assert result_sll_list[0].next.value == expected_result_sll_list["first_node"]["next"]
    assert result_sll_list[1].value == expected_result_sll_list["second_node"]["value"]
    assert result_sll_list[1].next.value == expected_result_sll_list["second_node"]["next"]
    assert result_sll_list[2].value == expected_result_sll_list["third_node"]["value"]
    assert result_sll_list[2].next == expected_result_sll_list["third_node"]["next"]


def test_singly_linked_list_remove():
    """Test singly linked list remove method"""
    expected_result_sll_list = {
        "first_node": {
            "value": 1,
            "next": 3
        },
        "second_node": {
            "value": 3,
            "next": None
        }
    }
    expected_result_removed_error1 = False
    expected_result_removed_error2 = False
    expected_result_item_removed_last = 4
    expected_result_item_removed_first = 0
    expected_result_item_removed_middle = 2
    sll = LinkedList([0, 1, 2, 3, 4])
    result_removed_error1 = sll.remove(-1)
    result_removed_error2 = sll.remove(100)
    result_item_removed_last = sll.remove(4)
    result_item_removed_first = sll.remove(0)
    result_item_removed_middle = sll.remove(1)
    result_sll_list = [node for node in sll]

    assert result_removed_error1 == expected_result_removed_error1
    assert result_removed_error2 == expected_result_removed_error2
    assert result_item_removed_last.value == expected_result_item_removed_last
    assert result_item_removed_first.value == expected_result_item_removed_first
    assert result_item_removed_middle.value == expected_result_item_removed_middle
    assert result_sll_list[0].value == expected_result_sll_list["first_node"]["value"]
    assert result_sll_list[0].next.value == expected_result_sll_list["first_node"]["next"]
    assert result_sll_list[1].value == expected_result_sll_list["second_node"]["value"]
    assert result_sll_list[1].next == expected_result_sll_list["second_node"]["next"]


def test_singly_linked_list_reverse():
    """Test singly linked list reverse method"""
    expected_result_sll_empty_reversed = []
    expected_result_sll_one_item_reversed = {
        "value": 0,
        "next": None
    }
    expected_result_sll_reversed = {
        "first_node": {
            "value": 3,
            "next": 2
        },
        "second_node": {
            "value": 2,
            "next": 1
        },
        "third_node": {
            "value": 1,
            "next": 0
        },
        "forth_node": {
            "value": 0,
            "next": None
        }
    }
    sll_empty = LinkedList()
    sll_one_item = LinkedList(0)
    sll = LinkedList([0, 1, 2, 3])
    sll_empty.reverse()
    sll_one_item.reverse()
    sll.reverse()
    result_sll_empty_reversed = [node for node in sll_empty]
    result_sll_one_item_reversed = [node for node in sll_one_item]
    result_sll_reversed = [node for node in sll]

    assert result_sll_empty_reversed == expected_result_sll_empty_reversed
    assert result_sll_one_item_reversed[0].value == expected_result_sll_one_item_reversed["value"]
    assert result_sll_one_item_reversed[0].next == expected_result_sll_one_item_reversed["next"]
    assert result_sll_reversed[0].value == expected_result_sll_reversed["first_node"]["value"]
    assert result_sll_reversed[0].next.value == expected_result_sll_reversed["first_node"]["next"]
    assert result_sll_reversed[1].value == expected_result_sll_reversed["second_node"]["value"]
    assert result_sll_reversed[1].next.value == expected_result_sll_reversed["second_node"]["next"]
    assert result_sll_reversed[2].value == expected_result_sll_reversed["third_node"]["value"]
    assert result_sll_reversed[2].next.value == expected_result_sll_reversed["third_node"]["next"]
    assert result_sll_reversed[3].value == expected_result_sll_reversed["forth_node"]["value"]
    assert result_sll_reversed[3].next == expected_result_sll_reversed["forth_node"]["next"]


def test_singly_linked_list_len():
    """Test singly linked list len special method"""
    expected_result_sll_empty_len = 0
    expected_result_sll_len = 4
    sll_empty = LinkedList()
    sll = LinkedList([0, 1, 2, 3])
    result_sll_empty_len = len(sll_empty)
    result_sll_len = len(sll)

    assert result_sll_empty_len == expected_result_sll_empty_len
    assert result_sll_len == expected_result_sll_len


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
