# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def matching_check(s, t):
            if (not s and t) or (s and not t):
                return False

            elif not s and not t:
                return True

            elif s.val == t.val:
                if matching_check(s.left, t.left) and matching_check(s.right, t.right):
                    return True

                else:
                    return False

        # Compare 2 trees from roots
        if matching_check(s, t):
            return True

        elif not s:
            return False

        # Since roots are not matched, check whether the left child or right child subtrees are the same
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
