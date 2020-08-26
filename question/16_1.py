
nums = [0, 1, 2]; target = 0

nums.sort()

# Be careful of the last index in sum()
# The following is equivalent of nums[0] + nums[1] + nums[2]
sum_min = sum(nums[0:3])

for i in range(len(nums) - 2):

    j, k = i + 1, len(nums) - 1

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    while j < k:

        total = nums[i] + nums[j] + nums[k]

        dis = target - total

        if dis == 0:
            print total

        if abs(dis) < abs(target - sum_min):
            sum_min = total

        if total < target:
            j += 1

        elif total > target:
            k -= 1

print sum_min