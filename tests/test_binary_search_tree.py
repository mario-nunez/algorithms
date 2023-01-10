import pytest

from dsa.binary_search_tree import BinarySearchTree


def test_bst_initialization():
    """Test binary search tree initializacion"""
    expected_result_empty_bst_root = None
    bst_empty = BinarySearchTree()
    result_empty_bst_root = bst_empty.root

    assert result_empty_bst_root == expected_result_empty_bst_root


@pytest.mark.xfail
def test_bst_wrong_initialization_single_value():
    """Test binary search tree wrong initializacion using a single value"""
    BinarySearchTree(1)


@pytest.mark.xfail
def test_bst_wrong_initialization_list():
    """Test binary search tree wrong initializacion using a list"""
    BinarySearchTree([1, 2, 3])


@pytest.mark.xfail
def test_bst_wrong_initialization_multiple_values():
    """Test binary search tree wrong initializacion using multiple values"""
    BinarySearchTree(1, 2, 3)


def test_bst_insert():
    """Test binary search tree insert method"""
    expected_result_bst_root = 4
    expected_result_bst_root_left = 1
    expected_result_bst_root_right = 5
    expected_result_bst_root_right_right = 9
    expected_result_bst_root_right_right_right = 19
    expected_result_bst_root_right_right_left = 8
    expected_result_insert_error = False
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(1)
    bst.insert(5)
    bst.insert(9)
    bst.insert(19)
    bst.insert(8)
    result_insert_error = bst.insert(8)
    result_bst_root = bst.root.value
    result_bst_root_left = bst.root.left.value
    result_bst_root_right = bst.root.right.value
    result_bst_root_right_right = bst.root.right.right.value
    result_bst_root_right_right_right = bst.root.right.right.right.value
    result_bst_root_right_right_left = bst.root.right.right.left.value

    assert result_bst_root == expected_result_bst_root
    assert result_bst_root_left == expected_result_bst_root_left
    assert result_bst_root_right == expected_result_bst_root_right
    assert result_bst_root_right_right == expected_result_bst_root_right_right
    assert result_bst_root_right_right_right == expected_result_bst_root_right_right_right
    assert result_bst_root_right_right_left == expected_result_bst_root_right_right_left
    assert result_insert_error == expected_result_insert_error


def test_bst_contains():
    """Test binary search tree contains method"""
    expected_result_contains_correct1 = True
    expected_result_contains_correct2 = True
    expected_result_contains_error1 = False
    expected_result_contains_error2 = False
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(1)
    bst.insert(5)
    bst.insert(9)
    bst.insert(19)
    bst.insert(8)
    result_contains_correct1 = bst.contains(8)
    result_contains_correct2 = bst.contains(19)
    result_contains_error1 = bst.contains(88)
    result_contains_error2 = bst.contains(0)

    assert result_contains_correct1 == expected_result_contains_correct1
    assert result_contains_correct2 == expected_result_contains_correct2
    assert result_contains_error1 == expected_result_contains_error1
    assert result_contains_error2 == expected_result_contains_error2


def test_bst_node_repr():
    """Test binary search tree node repr special method"""
    expected_result_first_node_repr = "Node(value=3, left=None, right=None)"
    bst = BinarySearchTree()
    bst.insert(3)
    result_first_node_repr = repr(bst.root)

    assert result_first_node_repr == expected_result_first_node_repr
