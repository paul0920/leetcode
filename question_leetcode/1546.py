
nums = [-1, 3, 5, 1, 4, 2, -9]
target = 6

# nums = [0, 0, 0]
# target = 0


res = 0
seen = {0: 0}
presum = []
presum[:] = nums[:]
presum = [0] + presum

for i in range(1, len(presum)):

    presum[i] += presum[i - 1]
    curr_val = presum[i] - target

    if curr_val in seen:
        res += 1
        seen = {}

    seen[presum[i]] = i

print res
