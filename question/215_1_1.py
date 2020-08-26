# Quick sort algorithm
# Average time complexity: O(n)
#   Best case: O(n)
#   Worst case: O(n^2)
# Space complexity: O(1)

import random

# nums = [3, 2, 1, 5, 6, 4]
# k = 2


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4

def partition(left, right):

    rand_n = random.randint(left,right)
    nums[right], nums[rand_n] = nums[rand_n], nums[right]
    print "Swap", "[", rand_n, "]", "[", right, "]"

    for i, v in enumerate(nums[left:right+1], left):

        if v <= nums[right]:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            
            print nums

    return left - 1

def quicksort(low, high):

    if low < high:

        # pos is the index of the correct place for that element
        pos = partition(low, high)
        print pos
        print ""

        # sort the other 2 sections
        quicksort(low, pos - 1)
        quicksort(pos + 1, high)


l, r = 0, len(nums) - 1

quicksort(l, r)

print "the sorted array:", nums
