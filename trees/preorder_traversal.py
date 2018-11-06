class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def pre_order_recursive(root, result=None):
    if not root:
        return
    if result is None:
        result = []
    result.append(root.data)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)
    return result

def pre_order_iterative(root):
    result = []
    stack = []
    if root:
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return result


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(4)
root.left.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
result = pre_order_recursive(root)
print result
