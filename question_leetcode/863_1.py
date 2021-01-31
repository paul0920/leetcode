# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        g = collections.defaultdict(list)

        def connect(parent, child):

            if parent and child:
                g[parent.val] += [child.val]
                g[child.val] += [parent.val]

            for next_node in (child.left, child.right):

                if next_node:
                    connect(child, next_node)

        connect(None, root)
        q = [target.val]
        visited = set([target.val])

        for _ in range(K):

            # Use q1 to store each distance and
            # expand the list comprehension to strip away the complexity
            q1 = []

            for node in q:
                for next_node in g[node]:

                    if next_node not in visited:
                        q1.append(next_node)

            q = q1
            visited |= set(q)

        return q
    