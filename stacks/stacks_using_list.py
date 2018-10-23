class Stack(object):
	def __init__(self, limit=10):
		self.stack = []
		self.limit = limit

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, data):
		if len(self.stack) >= self.limit:
			print("Stack overflow!")
		else:
			self.stack.append(data)
		print("Stack after push {}".format(self.stack))

	def pop(self):
		if self.is_empty():
			print("Stack underflow!")
			return 0
		else:
			return self.stack.pop()

	def peek(self):
		if self.is_empty():
			print("Stack underflow!")
			return 0
		else:
			return self.stack[-1]


	def size(self):
		return len(self.stack)

data_stack = Stack()
data_stack.push("1")
data_stack.push("2")
data_stack.push("5")
data_stack.push("3")
print data_stack.peek()
print data_stack.pop()
print data_stack.peek()
