from linked_list import Node
from linked_list import LinkedList

def insert_node(head, node):
    prev = None
    curr = head
    end = True
    while curr.next:
        if curr.data >= node.data:
            end = False
            break
        prev = curr
        curr = curr.next
    if not prev: head = node

    if end:
        curr.next = node
    else:
        node.next = curr
        if prev: prev.next = node
    return head

if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 5, 6, 7, 8, 9]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    node4 = Node(data=4)

    current_head = insert_node(head=current_head, node=node4)
    linked_list.head = current_head
    print("Linked list after")
    linked_list.print_list()
