class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, input_list):
        for data in input_list:
            temp = Node()
            temp.set_data(data)
            temp.next = self.head
            self.head = temp

    def print_linked_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def delete_alternate(self):
        count = -1
        temp = self.head
        prev = None
        while temp:
            count += 1
            if count % 2 != 0:
                prev.next = temp.next
                continue
            prev = temp
            temp = temp.next

llist = LinkedList()
input_list = [9,8,7,6,5,4,3,2,1]
llist.create_linked_list(input_list=input_list)
#llist.print_linked_list()
llist.delete_alternate()
llist.print_linked_list()
