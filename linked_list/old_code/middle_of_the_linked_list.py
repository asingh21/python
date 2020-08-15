class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, input_list):
        temp = self.head
        if self.head is not None:
            while temp.next:
                temp = temp.next
        for element in input_list:
            if not temp:
                temp = Node(element)
                self.head = temp
            else:
                temp.next = Node(element)
                temp = temp.next

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
        #print ("head is {}".format(self.head.data))

    def get_middle_element(self):
        main = self.head
        reference = self.head
        while reference.next:
            reference = reference.next
            if reference.next:
                reference = reference.next
            else:
                break
            main = main.next
        return main.data

llist = LinkedList()
#llist.push(10)
#llist.push(20)
#llist.push(30)
#llist.push(40)
#llist.push(50)
linked_list_input_list = [10, 20, 30, 40, 50, 60, 70, 80]
llist.create_linked_list(linked_list_input_list)
llist.print_list()
middle_element = llist.get_middle_element()
print("middle element in the list is {}".format(middle_element))
