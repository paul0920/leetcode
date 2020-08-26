
#s = 7
#nums = [2, 3, 1, 2, 4, 3]

s = 11
nums = [1, 2, 3, 4, 5]

box = {0: -1}
curr_sum = 0
temp = 0
min_len = len(nums) + 1
j = 0

for i, v in enumerate(nums):

    curr_sum += v
    temp = curr_sum

    if curr_sum - s in box:
        min_len = min(min_len, i - box[curr_sum - s])

    if not curr_sum in box:
        box[curr_sum] = i

    while j <= i and curr_sum >= s:
        min_len = min(min_len, i + 1 - j)
        temp = max(temp, curr_sum)
        curr_sum -= nums[j]
        j += 1

    j = 0
    curr_sum = temp

# return 0 if it's impossible to have a case
print min_len % (len(nums) + 1)