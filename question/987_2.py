import collections


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


g = collections.defaultdict(list)

def dfs(node, lvl_x, lvl_y):
    if not node:
        return

    g[lvl_x] += [(lvl_y, node.val)]

    if node.left:
        dfs(node.left, lvl_x - 1, lvl_y + 1)

    if node.right:
        dfs(node.right, lvl_x + 1, lvl_y + 1)


dfs(root, 0, 0)
res = []

for idx in sorted(g):
    res += [[val for i, val in sorted(g[idx])]]

print res
