# BFS


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        q = deque([root])

        while q:

            # print stack

            node = q.popleft()

            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)

        return root
