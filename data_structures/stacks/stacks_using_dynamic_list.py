class Stack(object):
    def __init__(self, limit=5):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        if len(self.stack) >= self.limit:
            print ("Stack overflow! Resizing")
            self.resize()
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return 0
        else:
            self.stack.pop()
            return self.stack

    def peek(self):
        if self.is_empty():
            print ("Stack underflow!")
            return 0
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def resize(self):
        new_stack = list(self.stack)
        self.limit = 2 * self.limit
        self.stack = new_stack

data_stack = Stack()
data_stack.push("1")
data_stack.push("2")
data_stack.push("3")
data_stack.push("4")
data_stack.push("5")
data_stack.push("6")
print data_stack.peek()
print data_stack.pop()
