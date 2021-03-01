# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key == root.val:
            if not root.right:

                return root.left

            elif not root.left:

                return root.right

            elif root.left and root.right:
                bigger_node = root.right

                while bigger_node.left:
                    bigger_node = bigger_node.left

                root.val = bigger_node.val
                root.right = self.deleteNode(root.right, bigger_node.val)

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            root.right = self.deleteNode(root.right, key)

        return root
