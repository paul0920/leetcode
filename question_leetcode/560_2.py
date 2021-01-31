
# The array can have "0" as the element
nums = [1, 2, 0, 3]; k = 3

s = 0
count = 0

print nums
print ""

for i in range(len(nums)):

    s = 0

    for j in range(i, len(nums)):
        s += nums[j]

        print i, j, "   ", nums[i], nums[j]

        if s == k:
            count += 1
            
            print count
            print ""

print count