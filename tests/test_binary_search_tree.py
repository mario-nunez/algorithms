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


def test_bst_insert_recursive():
    """Test binary search tree insert recursive method"""
    expected_result_bst_root = 4
    expected_result_bst_root_left = 1
    expected_result_bst_root_right = 5
    expected_result_bst_root_right_right = 9
    expected_result_bst_root_right_right_right = 19
    expected_result_bst_root_right_right_left = 8
    expected_result_insert_error = None
    bst = BinarySearchTree()
    bst.r_insert(4)
    bst.r_insert(1)
    bst.r_insert(5)
    bst.r_insert(9)
    bst.r_insert(19)
    bst.r_insert(8)
    result_insert_error = bst.r_insert(8)
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


def test_bst_contains_recursive():
    """Test binary search tree contains recursive method"""
    expected_result_contains_correct1 = True
    expected_result_contains_correct2 = True
    expected_result_contains_error1 = False
    expected_result_contains_error2 = False
    bst = BinarySearchTree()
    bst.r_insert(4)
    bst.r_insert(1)
    bst.r_insert(5)
    bst.r_insert(9)
    bst.r_insert(19)
    bst.r_insert(8)
    result_contains_correct1 = bst.r_contains(8)
    result_contains_correct2 = bst.r_contains(19)
    result_contains_error1 = bst.r_contains(88)
    result_contains_error2 = bst.r_contains(0)

    assert result_contains_correct1 == expected_result_contains_correct1
    assert result_contains_correct2 == expected_result_contains_correct2
    assert result_contains_error1 == expected_result_contains_error1
    assert result_contains_error2 == expected_result_contains_error2


def test_bst_delete():
    """Test binary search tree delete method"""

    # Test 0 - Node to delete not in the tree
    expected_result_test = None
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    result_test = my_tree.delete_node(1)
    assert result_test == expected_result_test

    # Test 1 - Node to delete do not have children
    expected_result_test_root = 4
    expected_result_test_root_left = None
    expected_result_test_root_right = 5
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(5)
    my_tree.delete_node(1)
    result_test_root = my_tree.root.value
    result_test_root_left = my_tree.root.left
    result_test_root_right = my_tree.root.right.value

    assert result_test_root == expected_result_test_root
    assert result_test_root_left == expected_result_test_root_left
    assert result_test_root_right == expected_result_test_root_right

    # Test 2 - Node to delete has a child on the right
    expected_result_test_root = 4
    expected_result_test_root_left = 2
    expected_result_test_root_right = 5
    expected_result_test_root_left_right = None
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(5)
    my_tree.r_insert(2)
    my_tree.delete_node(1)
    result_test_root = my_tree.root.value
    result_test_root_left = my_tree.root.left.value
    result_test_root_right = my_tree.root.right.value
    result_test_root_left_right = my_tree.root.left.right

    assert result_test_root == expected_result_test_root
    assert result_test_root_left == expected_result_test_root_left
    assert result_test_root_right == expected_result_test_root_right
    assert result_test_root_left_right == expected_result_test_root_left_right

    # Test 3 - Node to delete has a child on the left
    expected_result_test_root = 4
    expected_result_test_root_left = 1
    expected_result_test_root_right = 5
    expected_result_test_root_right_left = None
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(6)
    my_tree.r_insert(5)
    my_tree.delete_node(6)
    result_test_root = my_tree.root.value
    result_test_root_left = my_tree.root.left.value
    result_test_root_right = my_tree.root.right.value
    result_test_root_right_left = my_tree.root.right.left

    assert result_test_root == expected_result_test_root
    assert result_test_root_left == expected_result_test_root_left
    assert result_test_root_right == expected_result_test_root_right
    assert result_test_root_right_left == expected_result_test_root_right_left

    # Test 4 - Node to delete has a child on the left and on the right (and grandchildren)
    expected_result_test_root = 2
    expected_result_test_root_left = 1
    expected_result_test_root_right = 12
    expected_result_test_right_left = 8
    expected_result_test_right_right = 16
    expected_result_test_right_left_left = 7
    expected_result_test_right_left_right = 9
    expected_result_test_right_right_left = None
    expected_result_test_right_right_right = 20
    my_tree = BinarySearchTree()
    my_tree.r_insert(2)
    my_tree.r_insert(1)
    my_tree.r_insert(10)
    my_tree.r_insert(8)
    my_tree.r_insert(7)
    my_tree.r_insert(9)
    my_tree.r_insert(16)
    my_tree.r_insert(12)
    my_tree.r_insert(20)

    """
    Tree before delete

          2
        /   \
       1    10
          /    \
         8      16
        / \    /  \
       7   9  12  20

    """

    my_tree.delete_node(10)

    result_test_root = my_tree.root.value
    result_test_root_left = my_tree.root.left.value # 1
    result_test_root_right = my_tree.root.right.value # 12
    result_test_right_left = my_tree.root.right.left.value # 8
    result_test_right_right = my_tree.root.right.right.value # 16
    result_test_right_left_left = my_tree.root.right.left.left.value # 7
    result_test_right_left_right = my_tree.root.right.left.right.value # 9
    result_test_right_right_left = my_tree.root.right.right.left # NONE
    result_test_right_right_right = my_tree.root.right.right.right.value # 20

    """
    Tree after delete

           2
         /   \
        1    12
           /    \
         8       16
        / \     /  \
        7  9  NONE  20

    """

    assert result_test_root == expected_result_test_root
    assert result_test_root_left == expected_result_test_root_left
    assert result_test_root_right == expected_result_test_root_right
    assert result_test_right_left == expected_result_test_right_left
    assert result_test_right_right == expected_result_test_right_right
    assert result_test_right_left_left == expected_result_test_right_left_left
    assert result_test_right_left_right == expected_result_test_right_left_right
    assert result_test_right_right_left == expected_result_test_right_right_left
    assert result_test_right_right_right == expected_result_test_right_right_right
