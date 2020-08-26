N = 3
trust = [[1, 2], [2, 3]]

N = 4
trust = [[1, 3], [2, 3], [3, 4]]

if len(trust) < N - 1:
    print -1
    exit()

edge = [0] * (N + 1)

for a, b in trust:
    edge[a] -= 1
    edge[b] += 1

for j in range(1, N + 1):
    if edge[j] == N - 1:
        print j
        exit()

print -1
