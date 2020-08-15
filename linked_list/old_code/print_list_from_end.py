class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list_from_end(self,something):
        if not something:
            return
        print something.data
        self.print_list_from_end(something.next)
        #print something.data

    def create_linked_list(self, input_list):
        for data in input_list:
            temp = Node(data)
            #temp.set_data(data)
            temp.next = self.head
            self.head = temp
        return self.head

    def print_linked_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

llist = LinkedList()
input_list = [9,8,7,6,5,4,3,2,1]
head = llist.create_linked_list(input_list=input_list)
#print head.data
llist.print_list_from_end(head)
