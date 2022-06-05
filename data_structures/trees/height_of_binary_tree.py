class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height_of_binary_tree_recursive(root):
    if not root:
        return 0
    return max(height_of_binary_tree_recursive(root.left),
               height_of_binary_tree_recursive(root.right)) + 1

def height_of_binary_tree_iterative_1(root):
    if not root:
        return
    stack = []
    max_count = 0
    count = 0
    node = root
    stack.append(node)
    while stack:
        node = stack.pop()
        count += 1
        if node.left:
            stack.append(node.left)
        else:
            max_count = max(max_count, count)
            count -= 1
        if node.right:
            stack.append(node.right)
        else:
            max_count = max(max_count, count)
            count -= 1
    return max_count

def height_of_binary_tree_iterative_2(root):
    if not root:
        return
    stack = []
    stack.append([root, 1])
    depth = 0
    while stack:
        node, count = stack.pop()
        depth = max(count,depth)
        if node.left:
            stack.append([node.left, count+1])
        if node.right:
            stack.append([node.right, count+1])
    return depth

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

print height_of_binary_tree_iterative_2(root)
