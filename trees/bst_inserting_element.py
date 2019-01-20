class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_insert_element(root, node):
    if not root:
        root = node
    else:
        if node.data > root.data:
            if not root.right:
                root.right = node
            else:
                bst_insert_element(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                bst_insert_element(root.left, node)

def print_bst(root):
    if not root:
        return
    print_bst(root.left)
    print root.data
    print_bst(root.right)

root = BinaryTreeNode(8)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(10)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(14)
print_bst(root)
node = BinaryTreeNode(2)
print "################"
bst_insert_element(root, node)
print_bst(root)
