class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bst_min_element_recursive(root):
    if not root.left:
        return root
    else:
        return bst_min_element(root.left)

def bst_min_elemnet_iterative(root):
    if not root:
        return
    current_node = root
    while current_node.left:
        current_node = current_node.left
    return current_node


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(10)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(14)

node = bst_min_elemnet_iterative(root)
print node.data
