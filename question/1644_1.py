class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def check_valid(root, node):
            if not root:
                return False

            elif root.val == node.val:
                return True

            return check_valid(root.left, node) or check_valid(root.right, node)

        def search_LCA(root, p, q):
            if root in (None, p, q):
                return root

            left = search_LCA(root.left, p, q)
            right = search_LCA(root.right, p, q)

            if left and right:
                return root

            elif not left and right:
                return right

            elif left and not right:
                return left

        if not root or not check_valid(root, p) or not check_valid(root, q):
            return None

        return search_LCA(root, p, q)


root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(2)
obj = Solution()
print obj.lowestCommonAncestor(root, root.right, root.right.right).val
