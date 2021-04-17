# BFS

def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    if not arr:
        return 0

    queue = [set()]

    for word in arr:
        if len(word) != len(set(word)):
            continue

        word = set(word)

        for visited_word in queue:
            if word & visited_word:
                continue

            queue.append(visited_word | word)
            # print queue

    return max([len(n) for n in queue])


arr = ["cha", "r", "act", "ers"]
print maxLength(arr)
