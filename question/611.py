
nums = [2, 2, 3, 4]

# The key idea is to sort the array from
# the largest to the smallest values
nums.sort(reverse=True)
count = 0

for i in range(len(nums) - 2):

    j, k = i + 1, len(nums) - 1

    while j < k:

        s = nums[j] + nums[k]

        if s > nums[i]:
            count += k - j
            j += 1

        else:
            k -= 1

print count