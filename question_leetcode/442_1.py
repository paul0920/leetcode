
nums = [4, 3, 2, 7, 8, 2, 3, 1]

res = []

for n in nums:

    if nums[abs(n) - 1] < 0:
        res.append(abs(n))

    else:
        nums[abs(n) - 1] *= -1

print res
