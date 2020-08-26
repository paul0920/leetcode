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

def find(node, target, res=[[float('INF'), None]]):
    if not node:
        return None

    if abs(node.val - target) < res[0][0]:
        res = [[abs(node.val - target), node.val]]

    find(node.left, target)
    find(node.right, target)

    return res


print find(root, target)[0][1]
