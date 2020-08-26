n = 15
headID = 0
manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

children = [[] for i in xrange(n)]
for i, m in enumerate(manager):
    if m >= 0:
        children[m].append(i)

print children


def dfs(i):

    curr_time = [dfs(j) for j in children[i]] + [0]

    print i, informTime[i], curr_time

    return max(curr_time) + informTime[i]
    # return max([dfs(j) for j in children[i]] or [0]) + informTime[i]


print dfs(headID)
