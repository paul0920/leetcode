
# nums = [1, 2, 3, 4, 5]
nums = [6, 5, 4, 3, 2, 1]
# nums = [1, 1, 1, 4, 6, 6]
# nums = [1, 5, 1, 1, 6, 4]

n = len(nums)

print n, n | 1
print ""

for x in range(10):
    print x, x | 1
print ""

# This lambda mapping only works for LLMSS order, not for SSMLL order
# meaning, > mid: i+=1; k+=1, < mid: j-=1
mapIdx = lambda i: (1 + 2 * i) % (n | 1)

for i in range(n):
    print i, 1 + 2 * i, (1 + 2 * i) % (n | 1)
