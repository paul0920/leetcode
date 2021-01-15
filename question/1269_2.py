def numWays(steps, arrLen):
    """
    :type steps: int
    :type arrLen: int
    :rtype: int
    """
    return dfs(0, steps, arrLen, {})


def dfs(pos, steps, arrLen, memo):
    if (pos, steps) in memo:
        return memo[(pos, steps)]

    if pos < 0 or pos >= arrLen:
        return 0

    if steps == 0:
        if pos == 0:
            return 1

        return 0

    memo[(pos, steps)] = \
        dfs(pos - 1, steps - 1, arrLen, memo) + \
        dfs(pos, steps - 1, arrLen, memo) + \
        dfs(pos + 1, steps - 1, arrLen, memo)

    return memo[(pos, steps)] % (10 ** 9 + 7)


steps = 4
arrLen = 2
steps = 27
arrLen = 2
print numWays(steps, arrLen)
