# Time complexity: O(k + log n), n = total nodes

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
        if not root or k == 0:
            return []

        # Time complexity: O(log n)
        upper_stack = self.get_stack(root, target)
        lower_stack = list(upper_stack)
        res = []

        # Calibrate the index position of each stack
        if upper_stack[-1].val < target:
            self.move_up(upper_stack)

        else:
            self.move_down(lower_stack)

        # Time complexity: O(k)
        for _ in range(k):
            if self.is_lower_index_closer(lower_stack, upper_stack, target):
                res.append(lower_stack[-1].val)
                self.move_down(lower_stack)

            else:
                res.append(upper_stack[-1].val)
                self.move_up(upper_stack)

        return res

    def get_stack(self, node, target):
        if not node:
            return []

        stack = []

        while node:
            stack.append(node)

            if target < node.val:
                node = node.left

            else:
                node = node.right

        return stack

    def move_up(self, stack):
        node = stack[-1]

        if not node.right:
            node = stack.pop()

            while len(stack) and stack[-1].right == node:
                node = stack.pop()

        else:
            node = node.right

            while node:
                stack.append(node)
                node = node.left

    def move_down(self, stack):
        node = stack[-1]

        if not node.left:
            node = stack.pop()

            while len(stack) and stack[-1].left == node:
                node = stack.pop()

        else:
            node = node.left

            while node:
                stack.append(node)
                node = node.right

    def is_lower_index_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False

        if not upper_stack:
            return True

        return target - lower_stack[-1].val < upper_stack[-1].val - target
