import collections


def shortestPathLength(graph):
    """
    :type graph: List[List[int]]
    :rtype: int
    """
    if not graph:
        return 0

    node_count = len(graph)
    state_count = 1 << node_count
    dp = [[float("INF")] * node_count for _ in range(state_count)]
    q = collections.deque()

    # Initialize the beginning states of each node, dp[state][stay @ node]
    for i in range(node_count):
        state = 1 << i
        dp[state][i] = 0
        q += [(state, i)]

    # Since all edges have equal distance, BFS is already optimal and no need to overwrite
    while q:

        curr_state, curr_node = q.popleft()

        for next_node in graph[curr_node]:

            # Use or to add next_node and generate the next_state
            next_state = curr_state | 1 << next_node

            # It has been visited and must be the shortest route
            if dp[next_state][next_node] != float("INF"):
                continue

            dp[next_state][next_node] = dp[curr_state][curr_node] + 1
            q += [(next_state, next_node)]

    return min(dp[-1])


graph = [[1, 2, 3], [0], [0], [0]]
print shortestPathLength(graph)
