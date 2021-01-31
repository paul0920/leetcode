
nums = [3, 2, 1, 6, 0, 5]


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    if not nums:
        return

    max_num = max(nums)
    max_idx = nums.index(max_num)

    node = TreeNode(max_num)
    node.left = constructMaximumBinaryTree(nums[:max_idx])
    node.right = constructMaximumBinaryTree(nums[max_idx + 1:])

    return node


print constructMaximumBinaryTree(nums)
