from linked_list import Node
from linked_list import LinkedList


def merge_linked_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    head3 = None
    temp1 = head1
    temp2 = head2
    if temp1.data <= temp2.data:
        head3 = temp1
        temp1 = temp1.next
    else:
        head3 = temp2
        temp2 = temp2.next

    temp3 = head3
    while (temp1 and temp2):
        if temp1.data <= temp2.data:
            temp = temp1
            temp1 = temp1.next
        else:
            temp = temp2
            temp2 = temp2.next
        temp3.next = temp
        temp3 = temp

    if temp1:
        temp3.next = temp1
    else:
        temp3.next = temp2
    return head3

if __name__ == '__main__':
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    llist1 = [1, 5, 7, 8]
    llist2 = [2, 3, 4, 6]
    linked_list1.create_linked_list(input_list=llist1)
    linked_list2.create_linked_list(input_list=llist2)
    print("First linkedlist")
    linked_list1.print_list()
    print("Second linkedlist")
    linked_list2.print_list()
    head1 = linked_list1.head
    head2 = linked_list2.head
    new_head = merge_linked_lists(head1=head1, head2=head2)
    print("merged list is")
    new_list = LinkedList(head=new_head)
    new_list.print_list()
