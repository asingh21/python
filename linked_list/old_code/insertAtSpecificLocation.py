class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def push_node(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def inset_node_specific_location(self, data, location):
        index = 0
        pointer = self.head
        while index < location:
            pointer = pointer.next
            index += 1
        next_node = pointer.next
        inserted_node = Node(data)
        pointer.next = inserted_node
        inserted_node.next = next_node

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.inset_node_specific_location(4, 1)

llist.print_list()