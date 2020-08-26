# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_len = 0

        def find(node):

            if not node:
                return 0

            l_child = find(node.left)
            r_child = find(node.right)

            if node.left and node.left.val == node.val:
                l = l_child + 1

            else:
                l = 0

            if node.right and node.right.val == node.val:
                r = r_child + 1

            else:
                r = 0

            # l + r is current path count toward root node
            self.max_len = max(self.max_len, l + r)

            # Return the larger count between l & r back to the root node
            return max(l, r)

        find(root)

        return self.max_len
