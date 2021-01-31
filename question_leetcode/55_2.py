
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]


max_idx = 0

for idx, n in enumerate(nums):

    # Keep checking whether the current index is beyond
    # the max index that previous elements can reach
    if idx > max_idx:
        print False
        exit()

    max_idx = max(max_idx, idx + n)

print True
