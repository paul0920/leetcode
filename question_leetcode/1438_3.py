import bisect

# nums = [10, 1, 2, 4, 7, 2]
# nums = [1, 0, 1, 2, 4, 7]
# limit = 5

nums = [4, 8, 5, 1, 7, 9]
# nums = [4, 8, 8, 4, 8, 1, 1, 7, 9]
limit = 6

i, L = 0, []
for j in range(len(nums)):

    # keep the sliding window sorted
    bisect.insort(L, nums[j])

    print L

    if L[-1] - L[0] > limit:

        print "idx:", i, "val:", nums[i]
        L.pop(bisect.bisect(L, nums[i]) - 1)
        i += 1

    print L
    print "idx:", i
    print ""

print j - i + 1
