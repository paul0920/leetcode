import heapq

# nums = [10, 1, 2, 4, 7, 2]
# nums = [1, 0, 1, 2, 4, 7]
# limit = 5

nums = [4, 8, 5, 1, 7, 9]
nums = [4, 8, 8, 4, 8, 1, 1, 7, 9]
limit = 6

maxq, minq = [], []
res = i = 0

# j is the right pointer
for j, a in enumerate(nums):

    heapq.heappush(maxq, [-a, j])
    heapq.heappush(minq, [a, j])

    print maxq
    print minq

    # Use while loop
    while -maxq[0][0] - minq[0][0] > limit:

        # i is the left pointer
        i = min(maxq[0][1], minq[0][1]) + 1

        print j, i

        # Use while loop removing all previous values since we already compared them
        while maxq[0][1] < i:

            print "max idx:", maxq[0][1]

            heapq.heappop(maxq)

        # Use while loop removing all previous values since we already compared them
        while minq[0][1] < i:

            print "min idx:", minq[0][1]

            heapq.heappop(minq)

        print maxq
        print minq

    res = max(res, j - i + 1)

    print res
    print ""

print res
