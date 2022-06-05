from linked_list import Node
from linked_list import LinkedList

def find_intersection(head1, head2):
    stack1 , stack2 = [],[]
    t = head1
    while t:
        stack1.append(t)
        t = t.next

    t = head2
    while t:
        stack2.append(t)
        t = t.next

    prev_node = None
    while stack1 and stack2:
        ele1 = stack1.pop()
        ele2 = stack2.pop()
        if ele1 == ele2:
            prev_node = ele1
        else:
            return prev_node

if __name__ == '__main__':

    node11 = Node(data=1)
    node12 = Node(data=2)
    node13 = Node(data=3)
    node14 = Node(data=4)
    node15 = Node(data=5)
    node16 = Node(data=6)
    node17 = Node(data=7)
    node18 = Node(data=8)
    node19 = Node(data=9)

    node21 = Node(data=1)
    node22 = Node(data=2)
    node23 = Node(data=3)
    node24 = Node(data=4)
    node25 = Node(data=5)
    node26 = Node(data=6)

    # creating list1 intersecting at node14
    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node15
    node15.next = node16
    node16.next = node17
    node17.next = node18
    node18.next = node19

    # creating list2 intersecting at node14
    node21.next = node22
    node22.next = node23
    node23.next = node24
    node24.next = node25
    node25.next = node26
    node26.next = node14

    linked_list1 = LinkedList(head=node11)
    linked_list2 = LinkedList(head=node21)
    print("first list")
    linked_list1.print_list()
    print("second list")
    linked_list2.print_list()

    intersecting_node = find_intersection(head1=node11, head2=node21)
    print(f'intersecting node is: {intersecting_node.data}')
