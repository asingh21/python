from doubly_linked_list import Node
from doubly_linked_list import DoublyLinkedList


def insert_at_beginning(head, data):
    temp = head
    new_node = Node(data)
    new_node.next = temp
    temp.prev = new_node
    head = new_node
    return head


if __name__ == '__main__':
    data_to_insert = 5
    linked_list = DoublyLinkedList()
    llist = [1, 2, 3, 4]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    changed_head = insert_at_beginning(head=current_head, data=data_to_insert)
    linked_list.head = changed_head
    print("Linked list after")
    linked_list.print_list()
