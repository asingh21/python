from linked_list import Node
from linked_list import LinkedList

def n_element_from_end(n_th_element, current_head):
    slow, fast = current_head, current_head
    count = 0
    while fast.next:
        count += 1
        fast = fast.next
        if count < n_th_element:
            continue
        slow = slow.next
    return slow


if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    n_th_element = n_element_from_end(current_head=current_head, n_th_element=4)
    print(f"nth_element from end is {n_th_element.data}")
