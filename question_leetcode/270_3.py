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

stack, pred = [], float('-inf')

# To build an inorder traversal iteratively,
# go left as far as you can and add
# all nodes on the way into stack
while stack or root:

    if root:
        print root.val

    while root:
        stack.append(root)
        root = root.left

    print [n.val for n in stack]

    root = stack.pop()

    # If finding the window, return the closest node value
    if pred <= target < root.val:
        print min(pred, root.val, key=lambda x: abs(target - x))
        exit()

    pred = root.val

    print pred
    print ""

    root = root.right

print pred
