import collections

A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]


h_map_a = collections.defaultdict(list)
h_map_b = collections.defaultdict(list)

for idx, n in enumerate(A):
    h_map_a[n] += [idx]

for idx, n in enumerate(B):
    h_map_b[n] += [idx]

for i in range(1, 7):

    if len(set(h_map_a[i] + h_map_b[i])) == len(A):
        print len(A) - max(len(h_map_a[i]), len(h_map_b[i]))
        exit()

print -1
