import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def deleting_node_iterative(root):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    while q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        elif node.right:
            q.put(node.right)
        else:
            del node

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

deleting_node_iterative(root)
print root.data
