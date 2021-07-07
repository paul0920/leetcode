def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    # The key thing is to do one pass from left to right and the other pass from right to left
    distance = []
    prev_index = float("-INF")

    for i, char in enumerate(s):
        if char == c:
            prev_index = i

        distance.append(i - prev_index)

    prev_index = float("INF")

    for i in range(len(s) - 1, -1, -1):
        char = s[i]

        if char == c:
            prev_index = i

        distance[i] = min(distance[i], prev_index - i)

    return distance


s = "loveleetcode"
c = "e"
print shortestToChar(s, c)
