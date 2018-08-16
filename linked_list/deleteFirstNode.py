class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def del_node_first(self):
        temp = self.head
        self.head = temp.next

    def del_node_last(self):
        if self.head is None:
            return
        temp = self.head
        prev = temp
        if temp.next is None:
            self.head = None
        else:
            current = prev.next
            temp = current
            while temp.next:
                prev = current
                current = temp.next
                temp = temp.next
            prev.next = None

    def linked_list_length(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def del_node_middle(self, index):
        length = self.linked_list_length()
        if index > length:
            raise "index is out of range.."
        if index == 1:
            self.del_node_first()
        elif index == length:
            self.del_node_last()
        else:
            prev = self.head
            current = prev.next
            after = current.next
            count = 0
            #prev = current
            #current = current.next
            #after = current.next
            while current.next:
                print "prev = {}".format(prev.data)
                print "current = {}".format(current.data)
                print "after = {}".format(after.data)
                count += 1
                if count == index:
                    print "count when break = {}".format(count)
                    print "current node = {}".format(current.data)
                    break
                prev = current
                current = current.next
                after = current.next
            current.next = None
            prev.next = after



llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
#llist.del_node_first()
#llist.del_node_last()
#llist.print_list()
#length = llist.linked_list_length()
#print length
#print "Ankush"
llist.del_node_middle(4)
llist.print_list()
