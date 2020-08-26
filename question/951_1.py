# Iterative version: BFS

import collections

def flipEquiv(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """

    box1 = collections.defaultdict(set)
    box2 = collections.defaultdict(set)

    def find(node, box):

        if not node:
            return box

        q = collections.deque()
        q.append(node)

        while q:

            nd = q.popleft()
            box[nd.val].add(nd.val)

            if nd:

                if nd.left:
                    box[nd.val].add(nd.left.val)
                    q.append(nd.left)

                if nd.right:
                    box[nd.val].add(nd.right.val)
                    q.append(nd.right)

        return box

    # print find(root1, box1)
    # print find(root2, box2)

    return find(root1, box1) == find(root2, box2)
