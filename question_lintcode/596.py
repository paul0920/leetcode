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
        # write your code here
        min_subtree_sum, subtree, subtree_sum = self.calculate_tree(root)

        return subtree

    def calculate_tree(self, root):
        if not root:
            return float("INF"), root, 0

        min_left_sum, left_tree, left_sum = self.calculate_tree(root.left)
        min_right_sum, right_tree, right_sum = self.calculate_tree(root.right)

        root_sum = left_sum + right_sum + root.val

        if min_left_sum == min(min_left_sum, min_right_sum, root_sum):
            return min_left_sum, left_tree, root_sum

        if min_right_sum == min(min_left_sum, min_right_sum, root_sum):
            return min_right_sum, right_tree, root_sum

        return root_sum, root, root_sum
