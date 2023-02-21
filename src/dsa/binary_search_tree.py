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
                sub_tree_min = self.get_tree_min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def get_tree_min_value(self, current_node):
        """Get the node with the minimun value of a tree"""
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
