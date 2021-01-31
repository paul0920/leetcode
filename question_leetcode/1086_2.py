
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

# The time complexity of "item.sort()" is O(N x logN)
items.sort(reverse=True)

dist = {}
res = []
total = 0
count = 0

for i in range(len(items)):
    if not items[i][0] in dist:
        dist[items[i][0]] = items[i][1]
        count = 0

    elif count < 5:
        dist[items[i][0]] += items[i][1]

    count += 1

for k, v in dist.items():
    res.append([k, v / 5])

print res