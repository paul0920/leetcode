nums = [5, 4, 0, 3, 1, 6, 2]

seen = [0] * len(nums)
res = 0

for n in nums:

    j = n
    count = 0

    while not seen[j]:
        seen[j] = 1
        count += 1
        j = nums[j]

    res = max(res, count)

print res
