class Node:
    """
    A class to represent a Node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A class to represent a doubly linked list.
    """
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            # allow empty initialization of the doubly linked list
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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Add item to the end"""
        # edge case: empty linked list
        if self.length == 0:
            return None
        temp = self.tail
        # edge case: only one item in the linked list
        if self.length == 1:
            self.head = None
            self.tail = None
        # normal case 
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
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
        


if __name__ == '__main__':

    # test append
    print('\n----- TEST APPEND -----')
    my_doubly_linked_list = DoublyLinkedList()
    print(my_doubly_linked_list)
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    print(my_doubly_linked_list)

    # test pop
    print('\n----- TEST POP -----')
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    print(my_doubly_linked_list)
    print('Pop value extracted:', my_doubly_linked_list.pop())
    print(my_doubly_linked_list)
    print('Pop value extracted:', my_doubly_linked_list.pop())
    print(my_doubly_linked_list)
    print('Pop value extracted:', my_doubly_linked_list.pop())
    print(my_doubly_linked_list)
    print('Pop value extracted:', my_doubly_linked_list.pop())
    print(my_doubly_linked_list)

    # test prepend
    print('\n----- TEST PREPEND -----')
    my_doubly_linked_list = DoublyLinkedList()
