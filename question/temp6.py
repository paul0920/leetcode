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


if not root: print []

left_bd_nodes = [root]
cur = root.left
while cur:
  left_bd_nodes.append(cur)
  cur = cur.left or cur.right

right_bd_nodes = [root]
cur = root.right
while cur:
  right_bd_nodes.append(cur)
  cur = cur.right or cur.left

leaf_nodes = []
stack = [root]
while stack:
  node = stack.pop()
  if node.right:
    stack.append(node.right)
  if node.left:
    stack.append(node.left)
  if not node.left and not node.right:
    leaf_nodes.append(node)

ans = []
seen = set()
def visit(node):
  if node not in seen:
    seen.add(node)
    ans.append(node.val)

for node in left_bd_nodes: visit(node)
print ans
for node in leaf_nodes: visit(node)
print ans

for node in reversed(right_bd_nodes): visit(node)

print ans