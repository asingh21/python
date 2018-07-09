class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head

        if self.head is None:
            self.head = Node(data)
        else:
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def del_node_first(self):
        temp = self.head
        self.head = temp.next

    def del_node_last(self):
        if self.head is None:
            return
        temp = self.head
        prev = temp
        if temp.next is None:
            self.head = None
        else:
            current = prev.next
            temp = current
            while temp.next:
                prev = current
                current = temp.next
                temp = temp.next
            prev.next = None



llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.del_node_first()
llist.del_node_last()
llist.print_list()
