import collections

A = [[1,1,0],
    [0,1,0],
    [1,1,0]]
B = [[0,0,0],
    [0,1,1],
    [0,0,1]]


# this is a test
# ggg
N = len(A)

t = 3

for i in range(N**2):
    print i, "  ", i/N, i%N
    print i/N + i%N
    print "*****************"


