"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        subtree, subtree_sum, min_subtree_sum = self.calculate_tree(root)

        return subtree

    def calculate_tree(self, root):
        if not root:
            return root, 0, float("INF")

        left, left_sum, min_left_sum = self.calculate_tree(root.left)
        right, right_sum, min_right_sum = self.calculate_tree(root.right)

        root_sum = left_sum + right_sum + root.val

        if min_left_sum == min(min_left_sum, min_right_sum, root_sum):
            return left, root_sum, min_left_sum

        if min_right_sum == min(min_left_sum, min_right_sum, root_sum):
            return right, root_sum, min_right_sum

        return root, root_sum, root_sum
