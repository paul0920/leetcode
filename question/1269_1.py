def numWays(steps, arrLen):
    """
    :type steps: int
    :type arrLen: int
    :rtype: int
    """
    return dfs(0, steps, arrLen)


def dfs(pos, steps, arrLen):
    if pos < 0 or pos >= arrLen:
        return 0

    if steps == 0:
        if pos == 0:
            return 1

        return 0

    return (dfs(pos - 1, steps - 1, arrLen) +
            dfs(pos, steps - 1, arrLen) +
            dfs(pos + 1, steps - 1, arrLen)) % (10 ** 9 + 7)


steps = 4
arrLen = 2
# steps = 27
# arrLen = 2
print numWays(steps, arrLen)
