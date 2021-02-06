# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []

        while stack:
            node = stack.pop()

            if node.right:
                node = node.right

                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                inorder.append(stack[-1].val)

        return inorder[k - 1]
