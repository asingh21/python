import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_size_of_binary_tree_iterative(root):
    if not root:
        return
    count = 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        count += 1
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return count

count = 0
def get_size_of_binary_tree_recursive_1(root):
    global count
    if not root:
        return
    count += 1
    get_size_of_binary_tree_recurssive(root.left)
    get_size_of_binary_tree_recurssive(root.right)
    return count

def get_size_of_binary_tree_recursive_2(root):
    if not root:
        return 0
    return get_size_of_binary_tree_recursive_2(root.left) + \
           get_size_of_binary_tree_recursive_2(root.right) + 1



root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print get_size_of_binary_tree_recursive_2(root)
