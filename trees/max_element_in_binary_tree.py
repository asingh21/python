import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_recursive(root, result=None):
    if not root:
        return
    if result is None:
        result = []
    result.append(root.data)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)
    return result

maxData = float("-infinity")
def get_max_element_in_binary_tree_recursive(root):
    global maxData
    if not root:
        return maxData
    if root.data > maxData:
        maxData = root.data
    get_max_element_in_binary_tree(root.left)
    get_max_element_in_binary_tree(root.right)
    return maxData

def get_max_element_in_binary_tree_iterative(root):
    if not root:
        return
    q = Queue.Queue()
    maxData = 0
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.data > maxData:
            maxData = node.data
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return maxData


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
#print max(pre_order_recursive(root))
print get_max_element_in_binary_tree_iterative(root)
