
arr = [3, 1, 1, 1, 5, 1, 2, 1]
target = 3

presum = []
presum[:] = arr[:]
presum = [0] + presum
seen = {0: 0}
res = float('INF')
minlen_track = float('INF')
minlen_track_arr = [float('INF')] * len(presum)

for i in range(1, len(presum)):

    # Here uses the 2 sum concept
    presum[i] += presum[i - 1]
    curr_val = presum[i] - target

    if curr_val in seen:

        pre_i = seen[curr_val]
        curr_len = i - pre_i

        # 0 is the dummy element. Also, the constraints of the problem:
        # 1 <= arr[i] <= 1000
        if pre_i > 0:

            # Search the shortest total length of 2 sub arrays
            res = min(res, curr_len + minlen_track_arr[pre_i])

        # Get the smallest length of the sub array
        minlen_track = min(minlen_track, curr_len)

    # This is the shortest sub array until the ith element
    minlen_track_arr[i] = minlen_track

    # print presum
    # print minlen_track_arr, curr_len
    # print ""

    seen[presum[i]] = i

print res if res < float('INF') else -1
