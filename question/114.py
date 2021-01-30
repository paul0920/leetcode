# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, node):
        if not node:
            return None

        left_last_node = self.flatten_and_return_last_node(node.left)
        right_last_node = self.flatten_and_return_last_node(node.right)

        if left_last_node:
            left_last_node.right = node.right
            node.right = node.left
            node.left = None

        return right_last_node or left_last_node or node
