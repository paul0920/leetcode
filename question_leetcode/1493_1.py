
# nums = [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
# nums = [0,0,0]

      # 0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,0,0,0,1,1,1,0,1,0]


total = 0
i, j = 0, 0
res = 0

for i in range(len(nums)):

    total += nums[i]
    print "i:", i, "j:", j, "total:", total

    while j < i and total < i - j:
        total -= nums[j]
        j += 1
        print "i:", i, "j:", j, "total:", total, "[adjusting window...]"

    res = max(res, i - j)

    print "i:", i, "j:", j, "total:", total, res
    print ""

print res
