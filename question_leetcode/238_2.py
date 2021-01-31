
nums = [1, 2, 3, 4]
nums = [2, 3, 4, 5]


res = [0] * len(nums)
res[0] = 1

for i in range(1, len(nums)):
    res[i] = res[i - 1] * nums[i - 1]

cur_product = 1

# This step merges 2 steps into 1 to get constant space complexity
for i in range(len(nums))[::-1]:
    res[i] = res[i] * cur_product
    cur_product *= nums[i]

print res
