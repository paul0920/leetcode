
nums = [1, 2, 4]
k = 3

nums = [4, 7, 9, 10]
k = 2

def find(idx):
    return nums[idx] - idx - nums[0]


final_idx = len(nums) - 1

# This is to handle cases the kth missing number not in the existing nums
if k > find(final_idx):
    print k + nums[final_idx] - find(final_idx)
    exit()

# Do binary search to find the window between 2 elements
left = 0
right = final_idx

# Return the window: find(left - 1) < k <= find(left)
while left < right:

    mid = (left + right) / 2

    if k > find(mid):
        left = mid + 1

    else:
        right = mid

print k + nums[left - 1] - find(left - 1)
