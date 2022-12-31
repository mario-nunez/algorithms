"""Implementation of a doubly linked list"""


class Node:
    """
    A class to represent a Node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        """Print Node"""
        return (f"Node(value={self.value}, "
                f"prev={self.prev.value if self.prev is not None else None}, "
                f"next={self.next.value if self.next is not None else None})")


class DoublyLinkedList:
    """
    A class to represent a doubly linked list.
    """
    def __init__(self, value=None):
        # allow initialization of the doubly linked list based on a list
        if isinstance(value, list):
            self.length = len(value)
            node = Node(value.pop(0))
            self.head = node
            prev_node = node.prev
            for item in value:
                node.next = Node(item)
                node.prev = prev_node
                prev_node = node
                node = node.next
                node.prev = node.next
            node.prev = prev_node
            self.tail = node
        # allow initialization of the doubly linked list with a value
        elif value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        # allow empty initialization of the doubly linked list
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def append(self, value):
        """Add item to the end"""
        new_node = Node(value)
        # edge case: empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """Add item to the beginning"""
        new_node = Node(value)
        # edge case: empty linked list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        """Pop item from the end"""
        # edge case: empty linked list
        if self.length == 0:
            return None
        temp = self.tail
        # edge case: only one item in the linked list
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        """Pop item from the beginning"""
        # edge case: empty linked list
        if self.length == 0:
            return None
        temp = self.head
        # edge case: only one item in the linked list
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """Get item base on index"""
        # edge case: empty linked list
        if self.length == 0:
            return None
        # edge case: index out of range
        if (index < 0) or (index >= self.length):
            return None
        temp = self.head
        # optimize code depending on the position of the index to get
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """Set item on a particular index"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert item on a particular index"""
        # edge case: index out of range
        if (index < 0) or (index > self.length):
            return False
        # edge case: insert at the beginning
        if index == 0:
            return self.prepend(value)
        # edge case: insert at the end
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Remove item on a particular index"""
        # edge case: index out of range
        if (index < 0) or (index >= self.length):
            return False
        # edge case: remove from the beginning
        if index == 0:
            return self.pop_first()
        # edge case: remove from the end
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def __iter__(self):
        """Allow to iterate over the linked list items"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        """Get linked list number of elements"""
        return len(tuple(iter(self)))

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append('None')
        return ' <-> '.join(nodes)
