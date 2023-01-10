import pytest

from dsa.stack import Stack


def test_stack_initialization():
    """Test stack initializacion"""
    expected_result_len_stack_empty = 0
    expected_result_len_stack = 1
    expected_result_empty_stack_top = None
    expected_result_stack_top = 0
    stack_empty = Stack()
    stack = Stack(0)
    result_len_stack_empty = stack_empty.height
    result_len_stack = stack.height
    result_empty_stack_top = stack_empty.top
    result_stack_top = stack.top.value

    assert result_len_stack_empty == expected_result_len_stack_empty
    assert result_len_stack == expected_result_len_stack
    assert result_empty_stack_top == expected_result_empty_stack_top
    assert result_stack_top == expected_result_stack_top


@pytest.mark.xfail
def test_stack_wrong_initialization_list():
    """Test stack wrong initializacion using a list"""
    Stack([1, 2, 3])


@pytest.mark.xfail
def test_stack_wrong_initialization_multiple_values():
    """Test stack wrong initializacion using multiple values"""
    Stack(1, 2, 3)


def test_stack_push():
    """Test stack push method"""
    expected_result_first_len_stack = 1
    expected_result_second_len_stack = 2
    stack = Stack()
    stack.push(0)
    result_first_len_stack = stack.height
    stack.push(1)
    result_second_len_stack = stack.height

    assert result_first_len_stack == expected_result_first_len_stack
    assert result_second_len_stack == expected_result_second_len_stack


def test_stack_pop():
    """Test stack pop method"""
    expected_result_pop_item1 = 2
    expected_result_pop_item2 = 1
    expected_result_pop_item3 = 0
    expected_result_pop_item4 = None
    expected_result_len_stack = 0
    stack = Stack(0)
    stack.push(1)
    stack.push(2)
    result_pop_item1 = stack.pop()
    result_pop_item2 = stack.pop()
    result_pop_item3 = stack.pop()
    result_pop_item4 = stack.pop()
    result_len_stack = stack.height

    assert result_pop_item1.value == expected_result_pop_item1
    assert result_pop_item2.value == expected_result_pop_item2
    assert result_pop_item3.value == expected_result_pop_item3
    assert result_pop_item4 == expected_result_pop_item4
    assert result_len_stack == expected_result_len_stack


def test_stack_empty():
    """Test stack empty method"""
    expected_result_empty_stack = True
    expected_result_stack = False
    stack_empty = Stack()
    result_empty_stack = stack_empty.empty()
    stack = Stack(0)
    result_stack = stack.empty()

    assert result_empty_stack == expected_result_empty_stack
    assert result_stack == expected_result_stack


def test_stack_size():
    """Test stack size method"""
    expected_result_size_empty = 0
    expected_result_size1 = 1
    expected_result_size2 = 2
    stack_empty = Stack()
    result_size_empty = stack_empty.size()
    stack = Stack(0)
    result_size1 = stack.size()
    stack.push(1)
    result_size2 = stack.size()

    assert result_size_empty == expected_result_size_empty
    assert result_size1 == expected_result_size1
    assert result_size2 == expected_result_size2


def test_stack_repr():
    """Test stack repr special method"""
    expected_result_stack_empty_repr = "(top)  (bottom)"
    expected_result_stack_repr = "(top) 1 - 0 (bottom)"
    stack_empty = Stack()
    stack = Stack(0)
    stack.push(1)
    result_stack_empty_repr = repr(stack_empty)
    result_stack_repr = repr(stack)

    assert result_stack_empty_repr == expected_result_stack_empty_repr
    assert result_stack_repr == expected_result_stack_repr


def test_stack_node_repr():
    """Test stack node repr special method"""
    expected_result_first_node_repr = "Node(value=1, next=None)"
    expected_result_second_node_repr = "Node(value=0, next=None)"
    stack = Stack(0)
    stack.push(1)
    result_first_node_repr = repr(stack.pop())
    result_second_node_repr = repr(stack.pop())

    assert result_first_node_repr == expected_result_first_node_repr
    assert result_second_node_repr == expected_result_second_node_repr
