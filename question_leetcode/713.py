
#nums = [10, 5, 2, 6]; k = 100
nums = [1, 1, 8, 1, 9, 1]; k = 6

if k == 0:
    print 0

pd = 1
s = 0
count = 0

for i, v in enumerate(nums):

    pd *= v

    while s <= i and pd >= k:
        pd /= nums[s]
        s += 1

    count += i - s + 1

print count