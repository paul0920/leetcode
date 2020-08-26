class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

target = 3.714286


def find(node):
    # This is inorder and the result list is sorted
    return find(node.left) + [node.val] + find(node.right) if node else []


print "This is sorted:", find(root)
print min(find(root), key=lambda x: abs(x - target))
