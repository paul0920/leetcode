# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        arr = []
        self.inorder(root, arr)

        for i in range(len(arr) - 1):

            if arr[i] >= arr[i + 1]:
                return False

        return True

    def inorder(self, node, arr):

        if not node:
            return

        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
