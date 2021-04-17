nums = [23, 2, 4, 6, 7];
k = 6

if k == 0:
    print any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))

# Hash table saves the locations of mod numbers
box = {0: -1}
curr_sum = 0
curr_sum_mod_k = 0
count = []

for i, n in enumerate(nums):

    curr_sum += n
    curr_sum_mod_k = curr_sum % k

    # Check whether the size of subarray >= 2
    if curr_sum_mod_k in box and i - box[curr_sum_mod_k] > 1:
        count.append([nums[v] for v in range(box[curr_sum_mod_k] + 1, i + 1)])

    elif not curr_sum_mod_k in box:
        box[curr_sum_mod_k] = i

print count
print True if count else False
