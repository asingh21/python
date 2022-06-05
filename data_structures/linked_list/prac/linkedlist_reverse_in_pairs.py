from linked_list import Node
from linked_list import LinkedList


def reverse_in_pairs(head):
    if head is None:
        return
    temp = head
    prev = None
    while (temp and temp.next):
        if head == temp:
            head = temp.next
        swap_in_pairs(node1=temp, node2=temp.next, prev=prev)
        prev = temp
        temp = temp.next
    return head

def swap_in_pairs(node1, node2, prev):
    temp = node2.next
    node2.next = node1
    node1.next = temp
    if prev:
        prev.next = node2

if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    new_head = reverse_in_pairs(head=current_head)
    new_list = LinkedList(head=new_head)
    print("Linked list after")
    new_list.print_list()
