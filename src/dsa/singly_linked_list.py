"""Implementation of a singly linked list"""


class Node:
    """
    A class to represent a Node in a singly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        """Print Node"""
        return (f"Node(value={self.value}, "
                f"next={self.next.value if self.next is not None else None})")


class LinkedList:
    """
    A class to represent a singly linked list.
    """
    def __init__(self, value=None):
        # allow initialization of the linked list based on a list
        if isinstance(value, list):
            self.length = len(value)
            node = Node(value.pop(0))
            self.head = node
            for item in value:
                node.next = Node(item)
                node = node.next
            self.tail = node
        # allow initialization of the linked list with a value
        elif value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        # allow empty initialization of the linked list
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
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove last item from linked list and return it"""
        # edge case: empty linked list
        if self.length == 0:
            return None
        temp = self.head
        # edge case: only one item in the linked list
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        temp.next = None
        self.length -= 1
        return temp

    def pop_first(self):
        """Remove first item from linked list and return it"""
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
        for _ in range(index):
            temp = temp.next
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
            return None
        # edge case: insert at the beginning
        if index == 0:
            return self.prepend(value)
        # edge case: insert at the end
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Remove item on a particular index"""
        # edge case: index out of range
        if (index < 0) or (index >= self.length):
            return None
        # edge case: remove from the beginning
        if index == 0:
            return self.pop_first()
        # edge case: remove from the end
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """Reverse linked list"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

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
        """Print linked list"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def main():
    """Main test function"""
    # test append
    expected_result = [0, 1, 2]
    dll = LinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    result = [node.value for node in dll]

    assert result == expected_result


if __name__ == '__main__':
    main()
