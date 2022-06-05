from linked_list import Node
from linked_list import LinkedList

def find_loop(head=Node):

    if head == None or head.next == None:
        return False
    slow_ptr = head.next
    fast_ptr = slow_ptr.next
    while (slow_ptr != fast_ptr):
        slow_ptr = slow_ptr.next
        try:
            fast_ptr = fast_ptr.next.next
        except AttributeError:
            return False
    return slow_ptr


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
    ret = find_loop(head=node1)
    print(f"Loop detected! {ret.data}") if ret else print("no loop")
