import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_element_iterative(root, search_element):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.data == search_element:
            return True
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return False

def search_element_recursive(root, search_element):
    if not root:
        return False
    if root.data == search_element:
        return True
    else:
        temp = search_element_recursive(root.left, search_element)
        if temp:
            return temp
        else:
            return search_element_recursive(root.right, search_element)

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
print search_element_recursive(root, 6)
