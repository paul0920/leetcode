
nums = [1, 2, 1]
nums = [5, 4, 3, 2, 1]
# nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]

n = len(nums)
res = [-1] * n

# If having a stack with reversed nums,
# we only need to loop nums once for a circular array
stack = nums[::-1]
# stack = []

# Loop nums in the reversed sequence
for i in range(n - 1, -1, -1) * 1:
# for i in range(n - 1, -1, -1) * 2:

    print "stack:", stack, nums[i]

    while stack and stack[-1] <= nums[i]:
        stack.pop()
        print "stack checking:", stack

    if stack:
        res[i] = stack[-1]

    print "res:", res

    stack.append(nums[i])

    print "stack:", stack

    if i == 0:
        print "********* Complete One Round *********"

    print ""

print "Final Result:", res
