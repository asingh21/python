from linked_list import Node
from linked_list import LinkedList


def display_from_end(head):
    stack = list()
    temp = head
    while(temp):
        stack.append(temp)
        temp = temp.next
    while (stack):
        node = stack.pop()
        print(f"Node is: {node.data}")

if __name__ == '__main__':
    linked_list = LinkedList()
    llist = [1, 2, 3, 4, 5]
    linked_list.create_linked_list(input_list=llist)
    print("Linked list before")
    linked_list.print_list()
    current_head = linked_list.head
    display_from_end(head=current_head)
