class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data=None):
        self.__data = data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head
