class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def postorder_traversal_iterative(root):
    if not root:
        return
    stack = []
    visited = set()
    node = root
    result = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
    return result


def postorder_traversal_recursive(root, result=[]):
    if not root:
        return
    if result is None:
        result = []
    postorder_traversal_recursive(root.left, result)
    postorder_traversal_recursive(root.right, result)
    result.append(root.data)
    return result

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print postorder_traversal_iterative(root)
