
nums = [3, 1, 0, -2]; target = 4

nums.sort()
count = 0

for i in range(len(nums) - 2):

    j, k = i + 1, len(nums) - 1

    while j < k:

        total = nums[i] + nums[j] + nums[k]

        if total < target:
            count += k - j
            j += 1

        else:
            k -= 1

print count