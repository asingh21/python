from linked_list import Node
from linked_list import LinkedList

def find_loop(head=Node):

    if head == None or head.next == None:
        return
    slow_ptr = head.next
    fast_ptr = slow_ptr.next
    while (slow_ptr != fast_ptr):
        slow_ptr = slow_ptr.next
        try:
            fast_ptr = fast_ptr.next.next
        except AttributeError:
            return False
    # this part of the code will be executed only if there is a loop
    """
    Reason for this algorith to work:
    head = 1
    point at which pointers meet to find the loop = 7
    divide linked list into 3 segments
    segment1 = x = 1..4
    segment2 = y = 5..7
    segment3 = z = 8..9
    slow_ptr travels = x + y
    fast_ptr travels = x + 2y + z
    fast_ptr = 2 * slow_ptr
    x + 2y + z = 2 * (x + y)
    => x = z
    which is basically distance each pointer travels from the current position to loop starting
    And this is represented in the loop below
    """

    slow_ptr = head
    while (slow_ptr != fast_ptr):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    head1 = head2 = slow_ptr
    fast_ptr = slow_ptr.next.next
    slow_ptr = slow_ptr.next
    while (fast_ptr != head1 and fast_ptr.next != head1):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    head2 = slow_ptr.next
    slow_ptr.next = None
    fast_ptr.next = None
    return head1, head2


if __name__ == '__main__':
    node1 = Node(data=1)
    node2 = Node(data=2)
    node3 = Node(data=3)
    node4 = Node(data=4)
    node5 = Node(data=5)
    node6 = Node(data=6)
    node7 = Node(data=7)
    node8 = Node(data=8)
    node9 = Node(data=9)

    # creating circcular linked list`
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node4

    linked_list = LinkedList(head=node1)
    head1, head2 = find_loop(head=node1)
    list1 = LinkedList(head=head1)
    list2 = LinkedList(head=head2)
    list1.print_list()
    list2.print_list()
