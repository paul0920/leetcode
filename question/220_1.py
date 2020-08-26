
nums = [1, 5, 9, 1, 5, 8]; k = 2; t = 3
#nums = [1, 2]; k = 0; t = 1

# k : index distance
# t : value difference

if t < 0:
    print False

if k == 0:
    print False

w = t + 1
dist = {}

for i in range(len(nums)):
    box = nums[i] / w

    if box in dist:
        print True

    if box - 1 in dist and abs(nums[i] - dist[box - 1]) < w:
        print True

    if box + 1 in dist and abs(nums[i] - dist[box + 1]) < w:
        print True

    dist[box] = nums[i]

    if i >= k:
        del dist[nums[i - k] / w]

print False