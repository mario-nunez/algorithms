import pytest

from dsa.queue import Queue


def test_queue_initialization():
    """Test queue initializacion"""
    expected_result_len_queue_empty = 0
    expected_result_len_queue = 1
    queue_empty = Queue()
    queue = Queue(0)
    result_len_queue_empty = queue_empty.length
    result_len_queue = queue.length

    assert result_len_queue_empty == expected_result_len_queue_empty
    assert result_len_queue == expected_result_len_queue


@pytest.mark.xfail
def test_queue_wrong_initialization_list():
    """Test queue wrong initializacion using a list"""
    Queue([1, 2, 3])


@pytest.mark.xfail
def test_queue_wrong_initialization_multiple_values():
    """Test queue wrong initializacion using multiple values"""
    Queue(1, 2, 3)


def test_queue_enqueue():
    """Test queue enqueue method"""
    expected_result_first_len_queue = 1
    expected_result_second_len_queue = 2
    queue = Queue()
    queue.enqueue(0)
    result_first_len_queue = queue.length
    queue.enqueue(1)
    result_second_len_queue = queue.length

    assert result_first_len_queue == expected_result_first_len_queue
    assert result_second_len_queue == expected_result_second_len_queue


def test_queue_dequeue():
    """Test queue dequeue method"""
    expected_result_dequeue_item1 = 0
    expected_result_dequeue_item2 = 1
    expected_result_dequeue_item3 = 2
    expected_result_dequeue_item4 = None
    expected_result_len_queue = 0
    queue = Queue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    result_dequeue_item1 = queue.dequeue()
    result_dequeue_item2 = queue.dequeue()
    result_dequeue_item3 = queue.dequeue()
    result_dequeue_item4 = queue.dequeue()
    result_len_queue = queue.length

    assert result_dequeue_item1.value == expected_result_dequeue_item1
    assert result_dequeue_item2.value == expected_result_dequeue_item2
    assert result_dequeue_item3.value == expected_result_dequeue_item3
    assert result_dequeue_item4 == expected_result_dequeue_item4
    assert result_len_queue == expected_result_len_queue


def test_queue_empty():
    """Test queue empty method"""
    expected_result_empty_queue = True
    expected_result_queue = False
    queue_empty = Queue()
    result_empty_queue = queue_empty.empty()
    queue = Queue(0)
    result_queue = queue.empty()

    assert result_empty_queue == expected_result_empty_queue
    assert result_queue == expected_result_queue


def test_queue_size():
    """Test queue size method"""
    expected_result_size_empty = 0
    expected_result_size1 = 1
    expected_result_size2 = 2
    queue_empty = Queue()
    result_size_empty = queue_empty.size()
    queue = Queue(0)
    result_size1 = queue.size()
    queue.enqueue(1)
    result_size2 = queue.size()

    assert result_size_empty == expected_result_size_empty
    assert result_size1 == expected_result_size1
    assert result_size2 == expected_result_size2


def test_queue_repr():
    """Test queue repr special method"""
    expected_result_queue_empty_repr = "(exit)  (entry)"
    expected_result_queue_repr = "(exit) 0 - 1 (entry)"
    queue_empty = Queue()
    queue = Queue(0)
    queue.enqueue(1)
    result_queue_empty_repr = repr(queue_empty)
    result_queue_repr = repr(queue)

    assert result_queue_empty_repr == expected_result_queue_empty_repr
    assert result_queue_repr == expected_result_queue_repr


def test_queue_node_repr():
    """Test queue node repr special method"""
    expected_result_first_node_repr = "Node(value=0, next=None)"
    expected_result_second_node_repr = "Node(value=1, next=None)"
    queue = Queue(0)
    queue.enqueue(1)
    result_first_node_repr = repr(queue.dequeue())
    result_second_node_repr = repr(queue.dequeue())

    assert result_first_node_repr == expected_result_first_node_repr
    assert result_second_node_repr == expected_result_second_node_repr
