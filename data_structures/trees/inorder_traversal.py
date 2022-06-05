class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def inorder_traversal_iterative(root):
    if not root:
        return
    stack = []
    node = root
    result = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result

def inorder_traversal_recursive(root, result=None):
    if not root:
        return
    if result is None:
        result = []
    inorder_traversal_recursive(root.left, result)
    result.append(root.data)
    inorder_traversal_recursive(root.right, result)
    return result


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print inorder_traversal_recursive(root)
