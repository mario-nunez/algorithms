"""Implementation of a binary search tree"""


class Node:
    """
    A class to represent a Node in a binary search tree
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Print Node"""
        return (f"Node(value={self.value}, "
                f"left={self.left.value if self.left is not None else None}, "
                f"right={self.right.value if self.right is not None else None})")


class BinarySearchTree:
    """
    A class to represent a binary search tree
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a node in the binary search tree"""
        new_node = Node(value)
        # edge case: empty tree
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            # edge case: try to insert a value that is already in the tree
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        """Insert method implemented using recursion"""
        # edge case: empty tree
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def contains(self, value):
        """Check if the binary search tree contains a certain value"""
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
           return self.__r_contains(current_node.left, value)
        if value > current_node.value:
           return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        """Contains method implemented using recursion"""
        return self.__r_contains(self.root, value)

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def __delete_node(self, current_node, value):
        # edge case: number to delete not in the tree
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # the node to delete has been found. Four options:
            # 1. Deleting a leaf node
            if current_node.left is None and current_node.right is None:
                return None
            # 2. Deleting a node with opening on the left but a node on the right
            elif current_node.left is None:
                current_node = current_node.right
            # 3. Deleting a node with opening on the right but a node on the left
            elif current_node.right is None:
                current_node = current_node.left
            # 4. Deleting a node with nodes on each side of it
            else:
                # FIXME: if the node has grandchildren, would it work??
                sub_tree_min = self.get_tree_min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def get_tree_min_value(self, current_node):
        """Get the node with the minimun value of a tree"""
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


if __name__ == '__main__':
    
    my_tree = BinarySearchTree()
    print('root:', my_tree.root)

    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    # test recursive contains
    print('BST contains 82:', my_tree.r_contains(82))
    print('BST contains 21:', my_tree.r_contains(21))
    print('BST contains 77:', my_tree.r_contains(77))


    # test recursive insert
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(5)

    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)



    # test delete
    print('\n ----------- TEST DELETE ---------')
    print('TEST 0. Node doesnt exist')
    my_tree.delete_node(9)

    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)

    print('\nTEST 1. Node to delete do not have children')
    my_tree.delete_node(1)

    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left)
    print('root -> right:', my_tree.root.right.value)


    print('\nTEST 2. Node to delete has a child on the right')
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(5)
    my_tree.r_insert(2)

    print('TEST2 BEFORE:')
    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)
    print('root -> left -> right:', my_tree.root.left.right.value)

    my_tree.delete_node(1)

    print('TEST2 AFTER:')
    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)
    print('root -> left -> right:', my_tree.root.left.right)


    print('\nTEST 3. Node to delete has a child on the left')
    my_tree = BinarySearchTree()
    my_tree.r_insert(4)
    my_tree.r_insert(1)
    my_tree.r_insert(6)
    my_tree.r_insert(5)

    print('TEST3 BEFORE:')
    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)
    print('root -> right -> left:', my_tree.root.right.left.value)

    my_tree.delete_node(5)

    print('TEST3 AFTER:')
    print('root:', my_tree.root.value)
    print('root -> left:', my_tree.root.left.value)
    print('root -> right:', my_tree.root.right.value)
    print('root -> right -> left:', my_tree.root.right.left)

    print('\nTEST 4. Node to delete has a child on the left and on the right (and grandchildren)')
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

    print('TEST5 BEFORE:')
    print('root:', my_tree.root.value)
    print('root -> right:', my_tree.root.right.value) # 10
    print('root -> right -> left:', my_tree.root.right.left.value) # 8
    print('root -> right -> right:', my_tree.root.right.right.value) # 16
    print('root -> right -> left -> left:', my_tree.root.right.left.left.value) # 7
    print('root -> right -> left -> right:', my_tree.root.right.left.right.value) # 9
    print('root -> right -> right -> left:', my_tree.root.right.right.left.value) # 12
    print('root -> right -> right -> right:', my_tree.root.right.right.right.value) # 20

    """
        2
        /   \
    1     10
        /    \
        8      16
        / \    /  \
        7   9  12  20

    """

    my_tree.delete_node(10)


    print('TEST5 AFTER:')
    print('root:', my_tree.root.value)
    print('root -> right:', my_tree.root.right.value) # 12
    print('root -> right -> left:', my_tree.root.right.left.value) # 8
    print('root -> right -> right:', my_tree.root.right.right.value) # 16
    print('root -> right -> left -> left:', my_tree.root.right.left.left.value) # 7
    print('root -> right -> left -> right:', my_tree.root.right.left.right.value) # 9
    print('root -> right -> right -> left:', my_tree.root.right.right.left) # NONE
    print('root -> right -> right -> right:', my_tree.root.right.right.right.value) # 20

    """
        2
        /   \
    1     12
        /    \
        8      16
        / \    /  \
        7   9 NONE  20

    """

