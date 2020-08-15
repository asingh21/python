from linked_list import Node
from linked_list import LinkedList


def delete_at_middle(head, position):
    temp = head
    pos = 0
    while temp.next:
        old_node = temp
        temp = temp.next
        pos += 1
        if position == pos:
            old_node.next = temp.next


if __name__ == '__main__':
    data_to_insert = 3
    linked_list = LinkedList()
    llist = [1, 2, 4, 5]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    delete_at_middle(head=current_head, position=2)
    print("Linked list after")
    linked_list.print_list()
