
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.right = TreeNode(0)


def dfs(node, stack=[]):

    if not node:
        return 2

    l, r = dfs(node.left, stack), dfs(node.right, stack)

    if l == 0 or r == 0:
        stack += [1]
        return 1

    elif l == 1 or r == 1:
        return 2

    else:
        return 0


res = []

if dfs(root, res) == 0:
    print sum(res) + 1
    exit()

print sum(res)
