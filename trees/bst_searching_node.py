class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_searching_node_recursive(root, data):
    if not root or root.data == data:
        return root
    current_node = root.data
    if current_node < data:
        return bst_searching_node_recursive(root.right, data)
    return bst_searching_node_recursive(root.left, data)

def bst_searching_node_itirative(root, data):
    if not root:
        return
    current_node = root
    while current_node:
        if current_node.data == data:
            return current_node
        if current_node.data < data:
            current_node = current_node.right
        else:
            current_node = current_node.left
    return None

root = BinaryTreeNode(8)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(10)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(14)

node = bst_searching_node_itirative(root, 14)
print node.data
