"""Implementation of a queue"""


class Node:
    """
    A class to represent a Node in a queue
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        """Print Node"""
        return (f"Node(value={self.value}, "
                f"next={self.next.value if self.next is not None else None})")


class Queue:
    """
    A class to represent a queue
    """
    def __init__(self, value=None):
        # allow empty initialization of the queue
        if value is None:
            self.first = None
            self.last = None
            self.length = 0
        # allow initialization of the queue with one element
        else:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1

    def enqueue(self, value):
        """Enqueue an item"""
        new_node = Node(value)
        # edge case: empty queue
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """Dequeue an item"""
        # edge case: empty queue
        if self.length == 0:
            return None
        temp = self.first
        # edge case: queue with one element
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def empty(self):
        """Check if the queue is empty"""
        if self.length == 0:
            return True
        return False

    def size(self):
        """Get the size of the queue"""
        return self.length

    def __repr__(self):
        temp = self.first
        queue_items = []
        while temp is not None:
            queue_items.append(str(temp.value))
            temp = temp.next

        return "(exit) " + " - ".join(queue_items) + " (entry)"
