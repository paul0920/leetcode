height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

if len(height) < 3:
    print 0

ht_l, ht_r = 0, 0
left, right = 0, len(height) - 1
vol = 0

while left < right:

    # This is to keep updating the next wall for trapping water
    ht_l, ht_r = max(ht_l, height[left]), max(ht_r, height[right])

    # This is to make sure we have the wall to maintain the water
    if ht_l <= ht_r:
        vol += ht_l - height[left]
        left += 1

    else:
        vol += ht_r - height[right]
        right -= 1

print vol
