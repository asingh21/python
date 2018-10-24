class Node(object):
    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def is_empty(self):
        return self.next == None

class Stack(object):
    def __init__(self, data_list=None):
        self.head = None
        if data_list:
            for data in data_list:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

data_list = [1,2,3,4,5,6]
data_stack = Stack(data_list)
print data_stack.peek()
print data_stack.pop()
print data_stack.peek()
