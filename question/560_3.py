
# The array can have "0" as the element
nums = [1, 2, -1, 1, 3]; k = 3
nums = [3, 2, 5, 5]; k = 5

d = {0: 1}
cur_sum = 0
res = 0

for i in nums:
    cur_sum += i
    print "i:", i, "cur_sum:", cur_sum

    if cur_sum - k in d:
        res += d[cur_sum - k]
        print "res:", res

    if cur_sum not in d:
        d[cur_sum] = 1

    else:
        d[cur_sum] += 1

    print d
    print ""

print res