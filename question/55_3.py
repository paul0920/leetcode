
nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]

goal = len(nums) - 1
for i in range(len(nums))[::-1]:

    # print i, nums[i], goal

    if i + nums[i] >= goal:
        goal = i

print not goal
