class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data=None):
        self.__data = data


class DoublyLinkedList:
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
                node = Node(element)
                temp.next = node
                node.prev = temp
                temp = temp.next

    def print_list(self):
        temp = self.head
        print("Print forward")
        while temp:
            print(temp.data)
            if not temp.next:
                break
            temp = temp.next
        print("Print backwards")
        while temp:
            print(temp.data)
            temp = temp.prev

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head


if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4]
    linked_list.create_linked_list(input_list=llist)
    linked_list.print_list()
