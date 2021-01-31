
# nums = [1,2,1]
nums = [5, 4, 3, 2, 1]
# nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]

stack = []
res = [-1] * len(nums)

# Loop once, we can get the Next Greater Number of a normal array
# Loop twice, we can get the Next Greater Number of a circular array
for i in range(len(nums)) * 2:

    while stack and nums[stack[-1]] < nums[i]:
        res[stack.pop()] = nums[i]

    stack.append(i)

    # Normal array vs. circular array
    if i == len(nums) - 1:
        print res

print ""
print res
