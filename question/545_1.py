class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)


def dfs_leftmost(node):

    if not node or not node.left and not node.right:
        return

    res.append(node.val)

    if node.left:
        dfs_leftmost(node.left)

    else:
        dfs_leftmost(node.right)

def dfs_leaves(node):

    if not node:
        return

    if node != root and not node.left and not node.right:
        res.append(node.val)

    dfs_leaves(node.left)
    dfs_leaves(node.right)

def dfs_rightmost(node):

    if not node or not node.left and not node.right:
        return

    if node.right:
        dfs_rightmost(node.right)

    else:
        dfs_rightmost(node.left)

    res.append(node.val)


if not root:
    print []
    exit()

res = [root.val]
dfs_leftmost(root.left)
print res
dfs_leaves(root)
print res
dfs_rightmost(root.right)

print res
