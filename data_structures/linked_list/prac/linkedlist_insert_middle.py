from linked_list import Node
from linked_list import LinkedList


def insert_at_middle(head, data, position):
    temp = head
    pos = 0
    while temp.next:
        old_node = temp
        new_node = temp.next
        temp = temp.next
        pos += 1
        if position == pos:
            node_to_insert = Node(data)
            old_node.next = node_to_insert
            node_to_insert.next = new_node


if __name__ == '__main__':
    data_to_insert = 3
    linked_list = LinkedList()
    llist = [1, 2, 4, 5]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    insert_at_middle(head=current_head, data=data_to_insert, position=2)
    print("Linked list after")
    linked_list.print_list()
