"""Implementation of a singly linked list"""

class Node:
    """
    A class to represent a Node in a singly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    A class to represent a singly linked list.
    """
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            # allow empty initialization of the linked list
            self.head = None
            self.tail = None

    def append(self, value):
        """Add item to the end"""
        new_node = Node(value)
        # edge case: empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # normal case
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def prepend(self, value):
        """Add item to the beginning"""
        new_node = Node(value)
        # edge case: empty linked list
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        # normal case
        else:
            new_node.next = self.head
            self.head = new_node
        return True

    def pop(self):
        """Remove last item from linked list and return it"""
        # edge case: empty linked list
        if len(self) == 0:
            return None
        # edge case: only one item in the linked list
        elif len(self) == 1:
            temp = self.head
            self.head = None
            self.tail = None
        # normal case
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        return temp.value

    def pop_first(self):
        """Remove first item from linked list and return it"""
        # edge case: empty linked list
        if len(self) == 0:
            return None
        # edge case: only one item in the linked list
        elif len(self) == 1:
            temp = self.head
            temp.next = None
            self.head = None
            self.tail = None
        # normal case
        else:
            temp = self.head
            temp.next = None
            self.head = self.head.next
        return temp.value

    def get(self, index):
        """Get item base on index"""
        if len(self) == 0:
            return None
        elif index not in range(len(self)):
            return None
        else:
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
        if index not in range(len(self)):
            return None
        if index == 0:
            return self.prepend(value)
        if index == len(self):
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        return True

    def remove(self, index):
        """Remove item on a particular index"""
        if index not in range(len(self)):
            return None
        if index == 0:
            return self.pop_first()
        if index == len(self):
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        return temp

    def reverse(self):
        """Reverse linked list"""
        sll_length = len(self)
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(sll_length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def __iter__(self):
        """Allow to iterate over the linked list items"""
        node = self.head
        while node is not None:
            yield node.value
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
    print('\n----- TEST APPEND -----')
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Linked_list:', linked_list)
    print('Linked list head:', linked_list.head.value)
    print('Linked list length:', len(linked_list))

    # test pop
    print('\n----- TEST POP -----')

    linked_list = LinkedList(1)
    linked_list.append(2)

    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop())
    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop())
    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop())
    print('Linked_list:', linked_list)

    # test pop
    print('\n----- TEST POP FIRST -----')

    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop_first())
    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop_first())
    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop_first())
    print('Linked_list:', linked_list)

    print('pop:', linked_list.pop_first())
    print('Linked_list:', linked_list)

    # test prepend
    print('\n----- TEST PREPEND -----')

    linked_list = LinkedList()
    print('Linked_list:', linked_list)
    linked_list.prepend(3)
    linked_list.append(4)
    linked_list.prepend(2)
    linked_list.prepend(1)
    print('Linked_list:', linked_list)

    # test get
    print('\n----- TEST GET -----')
    linked_list = LinkedList(0)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Get item in index 1:', linked_list.get(1))


    # test set
    print('\n----- TEST SET -----')
    linked_list = LinkedList(0)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Set item in index 1:', linked_list.set_value(1, 111))
    print('Linked_list:', linked_list)


    # test insert
    print('\n----- TEST INSERT -----')
    linked_list = LinkedList(0)
    linked_list.append(2)

    print('Insert item in index 1:', linked_list.insert(1, 1))
    print('Linked_list:', linked_list)

    # test remove
    print('\n----- TEST REMOVE -----')
    linked_list = LinkedList(0)
    linked_list.append('1_extra')
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Linked_list before:', linked_list)
    print('Remove item in index 1:', linked_list.remove(1))
    print('Linked_list after:', linked_list)


    # test reverse
    print('\n----- TEST REVERSE -----')
    linked_list = LinkedList(0)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print('Linked_list:', linked_list)
    linked_list.reverse()
    print('Reversed Linked_list after:', linked_list)


if __name__ == '__main__':
    main()
