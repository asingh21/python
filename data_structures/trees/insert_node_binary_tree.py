import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node_binary_tree(root, insert_data):
    if not root:
        return
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        elif node.right:
            q.put(node.left)
        else:
            break
    temp = BinaryTreeNode(insert_data)
    if not node.left:
        node.left = temp
    else:
        node.right = temp

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
insert_node_binary_tree(root, 8)
print inorder_traversal_recursive(root)
