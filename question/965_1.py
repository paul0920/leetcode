
def isUnivalTree(root):

    # if root.left doesnt' exit, just return True and skip the statement after "or"
    # this statement is very compact and not easy to read
    left_correct = (not root.left or root.val == root.left.val and isUnivalTree(root.left))
    right_correct = (not root.right or root.val == root.right.val and isUnivalTree(root.right))

    return left_correct and right_correct
