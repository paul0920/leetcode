
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

dist = {}
res = []

for id, score in items:

    print dist.get(id, [])

    # This is a good way to add more values into the hash table
    # dist.get(id, []) returns [] if id is not found
    dist[id] = dist.get(id, []) + [score]

    print dist

for k, v in dist.items():
    v.sort(reverse=True)
    res.append([k, sum(v[0:5]) / 5])

print res