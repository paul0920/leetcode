# Time complexity: O(n), n = total nodes

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        inorder = self.get_inorder(root)
        left = self.find_lower_index(inorder, target)
        right = left + 1
        res = []

        for _ in range(k):
            if self.is_left_closer(inorder, left, right, target):
                res.append(inorder[left])
                left -= 1

            else:
                res.append(inorder[right])
                right += 1

        return res

    def get_inorder(self, node):
        stack = []
        res = []

        while node:
            stack.append(node)
            node = node.left

        while stack:
            node = stack[-1]
            res.append(node.val)

            if node.right:
                node = node.right

                while node:
                    stack.append(node)
                    node = node.left

            else:
                node = stack.pop()

                while stack and stack[-1].right == node:
                    node = stack.pop()

        return res

    def find_lower_index(self, nums, target):
        if not nums or target == None:
            return -1

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid

            elif nums[mid] == target:
                right = mid

            else:
                right = mid

        if nums[left] <= target:
            return left

        if nums[right] <= target:
            return right

        return -1

    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False

        if right >= len(nums):
            return True

        return target - nums[left] < nums[right] - target


#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 3, 3, 3, 4, 5]
target = 3

# Just check how binary search works
obj = Solution()
print obj.find_lower_index(nums, target)
