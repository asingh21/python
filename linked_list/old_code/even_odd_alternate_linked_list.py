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

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def is_empty(self):
        return len(self.stack_list) == 0

    def stack_length(self):
        return len(self.stack_list)

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, input_list):
        for data in input_list:
            temp = Node()
            temp.set_data(data)
            temp.next = self.head
            self.head = temp

    def create_a_node(self, data):
        temp = Node()
        temp.set_data(data)
        return temp

    def print_linked_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def altenate_even_odd_linked_list(self):
        even_stack = Stack()
        odd_stack = Stack()
        temp = self.head
        while temp:
            if temp.data %2 == 0:
                even_stack.push(temp.data)
            else:
                odd_stack.push(temp.data)
            temp = temp.next
        self.head = None
        count = 0
        prev = None
        while not even_stack.is_empty() or not odd_stack.is_empty():
            if count % 2 == 0:
                if even_stack.is_empty():
                    continue
                temp = self.create_a_node(even_stack.pop())
            else:
                if odd_stack.is_empty():
                    continue
                temp = self.create_a_node(odd_stack.pop())
            count += 1
            temp.next = self.head
            self.head = temp

input_list = [1,2,3,4,5,6]
llist = LinkedList()
llist.create_linked_list(input_list)
llist.print_linked_list()
llist.altenate_even_odd_linked_list()
llist.print_linked_list()
