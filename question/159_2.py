

s = "ecebaa"
# s = "bacc"

h_map = {}
start = 0
count = 0
res = []

for idx, w in enumerate(s):

    h_map[w] = idx

    if len(h_map) > 2:
        start = min(h_map.values())
        h_map.pop(s[start])
        start += 1

    count = max(count, idx - start + 1)
    res.append(s[start:idx+1])

print count
print res
