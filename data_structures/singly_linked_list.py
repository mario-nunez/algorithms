class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
            return temp.value
        # normal case
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        return temp.value

    def pop_first(self):
        # edge case: empty linked list
        if len(self) == 0:
            return None
        # edge case: only one item in the linked list
        elif len(self) == 1:
            temp = self.head
            temp.next = None
            self.head = None
            self.tail = None
            return temp.value
        # normal case
        else:
            temp = self.head
            temp.next = None
            self.head = self.head.next
            return temp.value

    def insert(self, value):
        """Insert item"""
        pass

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
    
    # test set
    print('\n----- TEST SET -----')



    # test insert
    print('\n----- TEST INSERT -----')





if __name__ == '__main__':
    main()

