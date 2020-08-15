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

    def nth_from_end(self, n):
        main = self.head
        reference = self.head
        current_element_podition = 0
        while reference:
            if current_element_podition >= n:
                main = main.next
            reference = reference.next
            current_element_podition += 1
        return main.data


llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
linked_list_input_list = [60, 70, 80]
llist.create_linked_list(linked_list_input_list)
llist.print_list()
nth_element_from_end = llist.nth_from_end(3)
print ("Nth element from the end of the linked list is {}".format(nth_element_from_end))
