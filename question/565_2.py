nums = [5, 4, 0, 3, 1, 6, 2]

seen = [0] * len(nums)


def finding(arr, idx, t):
    print seen, idx

    if seen[idx]:
        print "FIND", seen, idx
        return 0

    else:
        seen[idx] = 1
        return finding(arr, arr[idx], t) + 1


curr_max = 0

for i in range(len(nums)):
    curr_max = max(curr_max, finding(nums, i, i))
    print ""

print curr_max
