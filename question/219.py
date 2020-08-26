
nums = [1, 5, 9, 1, 5, 8]; k = 2; t = 3
#nums = [1, 2]; k = 0; t = 1

# k : index distance
# t : value difference

if k == 0:
    print False

box = {}

for i in range(len(nums)):

    if nums[i] in box:
        print True

    if i >= k:
        del box[nums[i - k]]

    box[nums[i]] = nums[i]

print False