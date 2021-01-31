
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.right = TreeNode(2)


def dfs(node, stack=[]):
    if not node:
        return 0

    l = dfs(node.left, stack)
    r = dfs(node.right, stack)

    # The following lines returning results of current layer or one layer below
    # stack += [abs(l + r + node.val - 1)]
    stack += [abs(l) + abs(r)]
    # print node.val

    return l + r + node.val - 1


res = []
dfs(root, res)

print res
print sum(res)
