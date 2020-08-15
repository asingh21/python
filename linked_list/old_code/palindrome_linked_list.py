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

    def get_palindrome(self, input_list):
        for i in range(len(input_list)/2):
            if input_list[i] != input_list[len(input_list) -1 - i]:
                return False
        return True

    def check_palindrome_linked_list_using_lists(self):
        temp = self.head
        linked_list_elements = []
        while temp:
            linked_list_elements.append(temp.data)
            temp = temp.next
        return self.get_palindrome(linked_list_input_list)

llist = LinkedList()
#llist.push(10)
#llist.push(20)
#llist.push(30)
#llist.push(40)
#llist.push(50)
linked_list_input_list = [10, 20, 30, 40, 40, 30, 20, 10]
llist.create_linked_list(linked_list_input_list)
llist.print_list()
palindrome = llist.check_palindrome_linked_list_using_lists()
if palindrome:
    print ("Linked list is palindrome")
else:
    print ("Not palindrome")
