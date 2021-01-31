import collections


def isBipartite(graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """

    if not graph:
        return False

    node_color_lookup = {}

    for i in range(len(graph)):

        if i not in node_color_lookup:
            node_color_lookup[i] = 1

            if not DFS(i, graph, node_color_lookup):
                return False

    return True


def DFS(curr_node, graph, node_color_lookup):

    for neighbor_node in graph[curr_node]:

        if neighbor_node not in node_color_lookup:
            node_color_lookup[neighbor_node] = node_color_lookup[curr_node] * -1
            if not DFS(neighbor_node, graph, node_color_lookup):
                return False

        elif node_color_lookup[neighbor_node] == node_color_lookup[curr_node]:
            return False

    return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print isBipartite(graph)
