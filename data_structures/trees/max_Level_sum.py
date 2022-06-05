import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    q.put(None)
    sum = 0
    total_sum = 0
    while not q.empty():
        node = q.get()
        if node is None:
            total_sum = max(sum, total_sum)
            sum = 0
            if not q.empty():
                q.put(None)
        else:
            sum += node.data
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return total_sum


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

print max_level_sum(root)
