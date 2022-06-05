class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self, input_element_list=None):
        temp = self.head
        if not self.head:
            while(temp.next):
                temp = temp.next
        for element in input_element_list:
            if not temp:
                temp = Node(element)
                self.head = temp
            else:
                temp.next = Node(element)
                temp = temp.next



llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.print_list()

