
#s = 7
#nums = [2,3,1,2,4,3]

s = 11
nums = [1, 2, 3, 4, 5]

box = {0: -1}
curr_sum = 0
min_len = float("INF")
k = s

for i, v in enumerate(nums):

    curr_sum += v
#    print curr_sum, i, k

    # the range of k increases time complexity
    # it's the bottleneck of the code!
    while s <= k <= sum(nums):

        if curr_sum - k in box:
            min_len = min(min_len, i - box[curr_sum - k])

        k += 1

    k = s
    if not curr_sum in box:
        box[curr_sum] = i

print min_len if min_len != float("INF") else 0