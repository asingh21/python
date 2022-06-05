import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def path_append(root, paths, path):
    if not root:
        return
    path.append(root.data)
    paths.append(path)
    path_append(root.left, path + [root.data], paths)
    path_append(root.right, path + [root.data], paths)
    return paths

def print_all_paths_1(root):
    paths = []
    print path_append(root, [], paths)
    #print "paths: {}".format(paths)

stack = []
def print_all_paths_2(root):
    if not root:
        return
    stack.append(root.data)
    print_all_paths_2(root.left)
    if not root.left and not root.right:
        print stack
    print_all_paths_2(root.right)
    stack.pop()


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

print print_all_paths_2(root)
