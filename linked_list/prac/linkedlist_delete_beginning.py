from linked_list import Node
from linked_list import LinkedList


def delete_at_beginning(head):
    temp = head
    next_node = temp.next
    temp.next = None
    return next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    changed_head = delete_at_beginning(head=current_head)
    linked_list.head = changed_head
    print("Linked list after")
    linked_list.print_list()
