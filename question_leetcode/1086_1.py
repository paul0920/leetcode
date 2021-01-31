
import collections
import heapq

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

# create a dictionary with list type
d = collections.defaultdict(list)

# an easy way to loop a 2D array
for idx, val in items:
    heapq.heappush(d[idx], val)
    print d, "Before"

    if len(d[idx]) > 5:
        # remove the smallest value using "heappop"
        heapq.heappop(d[idx])

    print d, "After"

res = [[i, sum(d[i]) // len(d[i])] for i in d]

print res