
nums = [1, 1, 1]; k = 2

s = 0

# It's important to remember to add [0] in the beginning
# The first element can be evaluated
s_arr = [0]

for i in range(len(nums)):
    s += nums[i]
    s_arr.append(s)

print nums
print s_arr
print ""

count = 0

for i in range(len(s_arr)-1):
    for j in range(i+1, len(s_arr)):

        print i, j, "   ", s_arr[i], s_arr[j]

        if s_arr[j] - s_arr[i] == k:
            count += 1
            print count
            print ""

print count