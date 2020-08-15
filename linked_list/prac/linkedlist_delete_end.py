from linked_list import Node
from linked_list import LinkedList


def delete_at_end(head):
    temp = head
    second_last_node = None
    while temp.next:
        second_last_node = temp
        temp = temp.next
    print(f"secong_lat_node = {second_last_node.data}")
    if second_last_node:
        second_last_node.next = None


if __name__ == '__main__':
    data_to_insert = 5
    linked_list = LinkedList()
    llist = [1, 2, 3, 4]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    delete_at_end(head=current_head)
    print("Linked list after")
    linked_list.print_list()
