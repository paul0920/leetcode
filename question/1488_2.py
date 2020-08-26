import collections
import heapq

rains = [1, 2, 0, 0, 2, 1]

#         0   1   2  3   4   5
rains = [10, 20, 20, 0, 20, 10]


# min heap to track the days when flooding would happen (if lake not dried)
nearest = []

# dict to store all rainy days
# use case: to push the subsequent rainy days into the heap for wet lakes
locs = collections.defaultdict(collections.deque)

# result - assume all days are rainy
res = [-1] * len(rains)

# pre-processing - {K: lake, V: list of rainy days}
for i, lake in enumerate(rains):
    locs[lake].append(i)

for i, lake in enumerate(rains):

    print "nearest wet day:", nearest
    # check whether the day, i, is a flooded day
    # the nearest lake got flooded (termination case)
    if nearest and nearest[0] == i:
        print []
        exit()

    # lake got wet
    if lake != 0:

        # pop the wet day. time complexity: O(1)
        locs[lake].popleft()

        # prioritize the next rainy day of this lake
        if locs[lake]:
            nxt = locs[lake][0]
            heapq.heappush(nearest, nxt)
            print "nearest wet day:", nearest

    # a dry day
    else:

        # no wet lake, append an arbitrary value
        if not nearest:
            res[i] = 1

        else:

            # dry the lake that has the highest priority
            # since that lake will be flooded in nearest future otherwise (greedy property)
            next_wet_day = heapq.heappop(nearest)
            wet_lake = rains[next_wet_day]
            res[i] = wet_lake

    print ""

print res
