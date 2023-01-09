"""Implementation of a stack"""


class Node:
    """
    A class to represent a Node in a stack.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        """Print Node"""
        return (f"Node(value={self.value}, "
                f"next={self.next.value if self.next is not None else None})")


class Stack:
    """
    A class to represent a stack.
    """
    def __init__(self, value=None):
        # allow initialization of the stack with a value
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        # allow empty initialization of the stack
        else:
            self.top = None
            self.height = 0

    def push(self, value):
        """Insert element in the stack"""
        new_node = Node(value)
        # edge case: empty stack
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        """Extract element from the stack"""
        # edge case: empty stack
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def empty(self):
        """Check if the stack is empty"""
        if self.height == 0:
            return True
        return False

    def size(self):
        """Get the size of the stack"""
        return self.height

    def __repr__(self):
        """Print stack"""
        temp = self.top
        stack_items = []
        while temp is not None:
            stack_items.append(str(temp.value))
            temp = temp.next
        return " -> ".join(stack_items)
