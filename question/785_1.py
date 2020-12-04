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

            if not BFS(i, graph, node_color_lookup):
                return False

    return True


def BFS(i, graph, node_color_lookup):
    q = collections.deque([i])

    while q:

        curr_node = q.popleft()

        for neighbor in graph[curr_node]:

            if neighbor not in node_color_lookup:
                node_color_lookup[neighbor] = node_color_lookup[curr_node] * -1
                q.append(neighbor)

            elif node_color_lookup[neighbor] == node_color_lookup[curr_node]:
                return False

    return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print isBipartite(graph)
