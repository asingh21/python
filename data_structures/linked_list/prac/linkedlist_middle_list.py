from linked_list import Node
from linked_list import LinkedList


def get_middle_node(head):
    if not head or head.next is None:
        return head
    slow_ptr = head
    fast_ptr = head
    while (fast_ptr.next and fast_ptr.next.next):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr

if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4, 5]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    middle_node = get_middle_node(head=current_head)
    print(f"Middle node is: {middle_node.data}")
