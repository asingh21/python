from linked_list import Node
from linked_list import LinkedList


def insert_at_end(head, data):
    temp = head
    while temp.next:
        temp = temp.next
    node_to_insert = Node(data)
    temp.next = node_to_insert


if __name__ == '__main__':
    data_to_insert = 5
    linked_list = LinkedList()
    llist = [1,2,3,4]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    insert_at_end(head=current_head, data=data_to_insert)
    print("Linked list after")
    linked_list.print_list()
