from linked_list import Node
from linked_list import LinkedList


def even_odd_list(head):
    temp = head
    while (temp and temp.next):
        temp = temp.next.next
        if not temp:
            return "even"
    return "odd"


if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    ret = even_odd_list(head=current_head)
    print(f"Linked list is {ret}")
