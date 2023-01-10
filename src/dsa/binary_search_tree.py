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
