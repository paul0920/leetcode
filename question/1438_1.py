import collections

# nums = [10, 1, 2, 4, 7, 2]
# nums = [1 0, 1, 2, 4, 7]
# limit = 5

# nums = [4, 8, 5, 1, 7, 9]

# [4, 8, 5]
nums = [4, 8, 5, 1, 8, 9]
limit = 6

max_stack = collections.deque()
min_stack = collections.deque()
idx = 0

# Start sliding the right bound to the right
for n in nums:

    # max_stack is in decreasing order
    # min_stack is in arising order
    while max_stack and max_stack[-1] < n:
        max_stack.pop()

    while min_stack and min_stack[-1] > n:
        min_stack.pop()

    max_stack.append(n)
    min_stack.append(n)

    print "max:", max_stack
    print "min:", min_stack

    # Check max difference in current window
    if max_stack[0] - min_stack[0] > limit:

        print "max 0:", max_stack[0]
        print "min 0:", min_stack[0]
        print "n:", n, "idx:", idx

        # If meeting the largest or the smallest element
        # in current window, delete it
        if max_stack[0] == nums[idx]:
            max_stack.popleft()

        if min_stack[0] == nums[idx]:
            min_stack.popleft()

        # Move the left bound to the right
        idx += 1

    print "max:", max_stack
    print "min:", min_stack
    print "n:", n, "idx:", idx
    print ""

# right bound - left bound
print len(nums) - idx
