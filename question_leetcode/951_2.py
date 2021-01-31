# Recursive version: DFS

def flipEquiv(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """

    if not root1 or not root2:
        return root1 == root2

    return root1.val == root2.val \
           and (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right) or
                flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))
