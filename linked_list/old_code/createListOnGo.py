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

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

llist = LinkedList()
llist.add_node(5)
llist.add_node(10)
llist.add_node(15)
llist.print_linked_list()
