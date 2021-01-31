# Time complexity: O(n)
# Space complexity: O(n)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(-1)
node.left.left.left = TreeNode(1)
node.left.left.left.left = TreeNode(5)


def find(node, target, curr_sum):

    # Make res & memo global variables to access them later
    global res, memo

    if not node:
        return

    # The following is the method of [560. Subarray Sum Equals K]
    curr_sum += node.val
    pre_sum = curr_sum - target
    res += memo.get(pre_sum, 0)
    memo[curr_sum] = memo.get(curr_sum, 0) + 1

    print curr_sum, pre_sum
    print res, memo
    print ""

    find(node.left, target, curr_sum)
    find(node.right, target, curr_sum)

    # Close the current branch and remove the memo[curr_sum] by 1 time
    memo[curr_sum] -= 1


sum = 5
res = 0
memo = {0: 1}


find(node, sum, 0)

print res
