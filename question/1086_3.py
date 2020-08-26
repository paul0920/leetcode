
import collections

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

# The time complexity of "item.sort()" is O(N x logN)
#items.sort(reverse=True)

dist = collections.defaultdict(list)
res = []

# The time complexity of this is O(N x 5 x log5) = O(N)
# Therefore, do sorting on "items" at the beginning is pricey and inefficient
for id, score in items:
    dist[id].append(score)

    if len(dist[id]) > 5:
        dist[id].sort(reverse=True)
        dist[id].pop()

    print dist

#for i in range(len(items)):
#    dist[items[i][0]].append(items[i][1])

#    if len(dist[items[i][0]]) > 5:
#        dist[items[i][0]].sort(reverse=True)
#        dist[items[i][0]].pop()

res = [[k, sum(dist[k]) // len(dist[k])] for k in dist]

print res