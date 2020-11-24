import collections


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        new_node = Node(node.val)
        lookup = {node: new_node}
        q = collections.deque([node])

        while q:

            curr_node = q.popleft()

            for neighbor in curr_node.neighbors:

                if neighbor not in lookup:
                    lookup[neighbor] = Node(neighbor.val)
                    q += [neighbor]

                lookup[curr_node].neighbors += [lookup[neighbor]]

        return new_node
