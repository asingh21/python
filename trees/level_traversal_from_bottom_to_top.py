import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_traversal_bottom_to_top_iterative(root):
    if not root:
        return
    q = Queue.Queue()
    stack = []
    q.put(root)
    while not q.empty():
        node = q.get()
        stack.append(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return stack[::-1]

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print level_traversal_bottom_to_top_iterative(root)
