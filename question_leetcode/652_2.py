import collections


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        res = []
        structure_to_nodes = collections.defaultdict(list)
        self.search_tree(root, structure_to_nodes)

        for structure, node_list in structure_to_nodes.items():
            if len(node_list) == 1:
                continue

            res.append(node_list[0])

        return res

    def search_tree(self, node, structure_to_nodes):
        if not node:
            return "No"

        structure = str(node.val) + "->" + self.search_tree(node.left, structure_to_nodes) + "->" + self.search_tree(
            node.right, structure_to_nodes)
        structure_to_nodes[structure].append(node)

        return structure
