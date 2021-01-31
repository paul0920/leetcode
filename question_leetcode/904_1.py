import collections

tree = [1, 2, 3, 2, 2]

h_map = collections.defaultdict(int)
res = 0
start = 0
count = 0

for idx, n in enumerate(tree):

    if not h_map[n]:
        count += 1

    h_map[n] += 1

    while count > 2:

        h_map[tree[start]] -= 1

        if not h_map[tree[start]]:
            count -= 1

        start += 1

    res = max(res, idx - start + 1)

print res
