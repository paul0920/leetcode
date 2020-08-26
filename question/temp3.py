inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def pp(self, level=0):
        ret = "\t"*level+repr(self.val)+"\n"
        ret += self.left.pp(level+1)
        ret += self.right.pp(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)  # Line A

    root.right = buildTree(inorder[inorderIndex + 1:], postorder)  # Line B
    # if root.right.val:
    #     print root.right.val
    root.left = buildTree(inorder[:inorderIndex], postorder)  # Line C
    # if root.left.val:
    #     print root.left.val
    # print root.val
    # print ""

    return root

print "***"
print buildTree(inorder, postorder).pp
