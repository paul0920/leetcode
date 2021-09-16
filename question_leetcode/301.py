import collections


def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s:
        return [""]

    queue = collections.deque([s])
    visited = {s}
    res = []

    while queue:
        for _ in range(len(queue)):
            curr_s = queue.popleft()

            if is_valid(curr_s):
                res.append(curr_s)

            for i, char in enumerate(curr_s):
                if char not in "()":
                    continue

                next_s = curr_s[:i] + curr_s[i + 1:]

                if next_s in visited:
                    continue

                queue.append(next_s)
                visited.add(next_s)

        if res:
            return res


def is_valid(string):
    if not string:
        return True

    count = 0

    for char in string:
        if char not in "()":
            continue

        if char == "(":
            count += 1

        elif char == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0


s = "(a)())()"
print removeInvalidParentheses(s)
