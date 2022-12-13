class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        """Add node to the end"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def preped(self, value):
        """Add node to the beginning"""
        pass

    def insert(self, value):
        """Insert node"""
        pass

    def __iter__(self):
        """Allow to iterate over the linked list elements"""
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

    linked_list = LinkedList(1)

    linked_list.append(2)
    linked_list.append(3)

    print('Linked_list:', linked_list)
    print('Linked list head:', linked_list.head.value)
    print('Linked list length:', len(linked_list))
    print('Elements of linked list:')
    for node in linked_list:
        print(node)


if __name__ == '__main__':
    main()

