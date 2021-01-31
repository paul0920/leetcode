
nums = [3, 5, 6, 7]
target = 9

nums.sort()
count = 0
l, r = 0, len(nums) - 1

while l <= r:

    if nums[l] + nums[r] <= target:
        count = count + pow(2, r - l, (10**9 + 7))
        l += 1

    else:
        r -= 1

print count % (10**9 + 7)
