import collections


def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    if not accounts:
        return [[]]

    email_to_name = {}
    email_graph = collections.defaultdict(set)
    visited = set()
    res = []

    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            email_graph[first_email].add(email)  # Use first_email as the hub linking to all nodes
            email_graph[email].add(first_email)
            email_to_name[email] = name
            # Need to track each email's corresponding name since entry point can be any email

    for email in email_graph:
        if email in visited:
            continue

        bfs(email, email_to_name[email], email_graph, visited, res)

    return res


def bfs(email, name, email_graph, visited, res):
    queue = collections.deque([email])
    visited.add(email)
    path = []

    while queue:
        node = queue.popleft()
        path.append(node)

        for next_node in email_graph[node]:
            if next_node in visited:
                continue

            queue.append(next_node)
            visited.add(next_node)

    res.append([name] + sorted(path))


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
print accountsMerge(accounts)
