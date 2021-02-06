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
        stack = []

        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack[-1]

            if node.right:
                node = node.right

                while node:
                    stack.append(node)
                    node = node.left

            else:
                node = stack.pop()

                while len(stack) and stack[-1].right == node:
                    node = stack.pop()

        return stack[-1].val
