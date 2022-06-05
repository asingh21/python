import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_deepest_node(root):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return node.data

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

print get_deepest_node(root)
