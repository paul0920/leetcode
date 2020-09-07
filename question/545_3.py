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

res = []
visited = set()


def check(node):
    if not node in visited:
        res.append(node.val)
        visited.add(node)


if not root:
    print []
    exit()

check(root)
node = root.left

while node:
    check(node)
    node = node.left or node.right

stack = [root]

while stack:
    node = stack.pop()

    if node.right:
        stack.append(node.right)

    if node.left:
        stack.append(node.left)

    if not node.left and not node.right:
        check(node)

rightmost = [root]
node = root.right

while node:
    rightmost += [node]
    node = node.right or node.left

for node in rightmost[::-1]:
    check(node)

print res
