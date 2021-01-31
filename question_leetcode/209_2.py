
#s = 7
#nums = [2, 3, 1, 2, 4, 3]

s = 11
nums = [1, 2, 3, 4, 5]

curr_sum = 0
min_len = len(nums) + 1
j = 0

for i, v in enumerate(nums):

    curr_sum += v

    while j <= i and curr_sum >= s:
        min_len = min(min_len, i + 1 - j)
        print i+1-j, curr_sum
        curr_sum -= nums[j]
        j += 1

print min_len % (len(nums) + 1)