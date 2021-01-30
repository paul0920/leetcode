import heapq


def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if not words:
        return ""

    graph = create_graph(words)

    return topological_sort(graph)


def create_graph(words):
    graph = {}

    for word in words:
        for c in word:
            if c not in graph:
                graph[c] = set()

    n = len(words)

    # Create the graph by comparing 2 words next to each other
    for i in range(n - 1):
        min_len = min(len(words[i]), len(words[i + 1]))

        for j in range(min_len):
            if words[i][j] != words[i + 1][j]:
                graph[words[i][j]].add(words[i + 1][j])
                break

            # Check whether the input is valid. For example, ["ab", "a "]
            # "a " should be in the 1st place rather than "ab"
            if j == min_len - 1:
                if len(words[i]) > len(words[i + 1]):
                    return {}

    return graph


def topological_sort(graph):
    indegree = {node: 0 for node in graph}

    # node points to the neighbor
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = [node for node in indegree if not indegree[node]]

    # Remember to heapify first!
    heapq.heapify(queue)
    dict_order = ""

    while queue:

        # Use heap to sort in normal lexicographical order
        node = heapq.heappop(queue)
        dict_order += node

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if not indegree[neighbor]:
                heapq.heappush(queue, neighbor)

    # Need to check the size since there might be a loop among nodes
    if len(dict_order) != len(graph):
        return ""

    return dict_order


words = ["wrt", "wrf", "er", "ett", "rftt"]
# words = ["z", "x"]
# words = ["z", "x", "z"]
print alienOrder(words)
