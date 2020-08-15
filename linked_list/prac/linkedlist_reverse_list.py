from linked_list import Node
from linked_list import LinkedList

def reverse_list(head):
    temp = head
    prev = None
    cur = head
    while temp.next:
        temp = temp.next
        cur.next = prev
        prev = cur
        cur = temp
    temp.next = prev
    return temp

if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    current_head = reverse_list(head=current_head)
    linked_list.head = current_head
    print("Linked list after")
    linked_list.print_list()
