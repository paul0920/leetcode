# This is O(n) 1 pass in-place solution
# Lomuto partition algorithm

nums = [2, 0, 2, 1, 1, 0]

i = j = 0
for k in xrange(len(nums)):

    print i, j, k
    print nums

    v = nums[k]
    nums[k] = 2

    print "nums[k]  ", nums

    if v < 2:
        nums[j] = 1
        j += 1

    print "v < 2    ", i, j, k
    print "v < 2    ", nums

    # Use "if". NOT "elif"!!!
    if v == 0:
        nums[i] = 0
        i += 1

    print "v == 0   ", i, j, k
    print "v == 0   ", nums

    print ""
