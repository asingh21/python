class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

#llist.print_list()

forth = Node(4)
temp = llist
forth.next = llist.head
llist.head = forth
llist.print_list()

