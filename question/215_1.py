# Quickselect algorithm
# Average time complexity: O(n)
#   Best case: O(n)
#   Worst case: O(n^2)
# Space complexity: O(1)

import random

nums = [3, 2, 1, 5, 6, 4]
k = 2


# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4


def partition(left, right):

    # This is to randomly select pivot and to prevent from the worst case
    right_seed = random.randint(left, right)
    print "random pivot", right_seed
    nums[right], nums[right_seed] = nums[right_seed], nums[right]
    # This can be turned off and is independent of the rest of the code

    for i, v in enumerate(nums[left:right + 1], left):

        print "index:", i, "R:", right

        # kth largest: >=
        # kth smallest: <=
        if v >= nums[right]:
            print "L:", left, "R:", right, nums

            nums[left], nums[i] = nums[i], nums[left]
            left += 1

            print "L:", left, "R:", right, nums
            print ""

    # translate back into index position
    return left - 1


l, r = 0, len(nums) - 1

# translate k into index position
k = k - 1

while True:

    print "###########################################"
    print "Start partitioning...", nums

    pos = partition(l, r)
    print "End of partitioning...", nums
    print "POS:", pos
    print "###########################################"
    print ""

    if pos < k:
        l = pos + 1

    elif pos > k:
        r = pos - 1

    else:
        print "Kth Largest Element in an Array:", nums[k]
        exit()
