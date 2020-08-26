import collections

n = 15
headID = 0
manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]


def dfs(idx):
    if manager[idx] != -1:
        informTime[idx] += dfs(manager[idx])
        manager[idx] = -1

    return informTime[idx]


print max(map(dfs, range(n)))
