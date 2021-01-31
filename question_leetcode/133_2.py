
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

        self.dfs(node, lookup)

        return new_node

    def dfs(self, node, lookup):

        for neighbor in node.neighbors:

            if neighbor not in lookup:
                lookup[neighbor] = Node(neighbor.val)
                self.dfs(neighbor, lookup)

            lookup[node].neighbors += [lookup[neighbor]]
