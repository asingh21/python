import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_no_of_full_nodes(root):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    count = 0
    while not q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
        if node.left and node.right:
            count += 1
    return count

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

print get_no_of_full_nodes(root)
