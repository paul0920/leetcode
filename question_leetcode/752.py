import collections

deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

not_allowed = set(deadends)
q = collections.deque()
q.append(("0000", 0))

while q:

    node, count = q.popleft()
    # print node, count, q

    if node == target:
        print count
        exit()

    # If node is in the not_allowed set, just skip the following process
    elif node in not_allowed:
        continue

    count += 1

    for i in range(4):
        for move in [-1, 1]:

            # Keep in mind Python can handle modulo of negative numbers
            next_digit = (int(node[i]) + move) % 10
            next_node = node[:i] + str(next_digit) + node[i + 1:]

            if not next_node in not_allowed:
                # It's OK to put visited nodes and not allowed nodes in the set()
                # since once the node was visited, it must be the shortest path
                not_allowed.add(node)
                q.append((next_node, count))

print -1
