nums = [-4, -2, 2, 4]
a = 0
b = -1
c = 5

# a = 1
# b = 3
# c = 5

# a = 0
# b = 3
# c = 5


# Use float on "a"
pivot = -b / float(2 * a) if a else 10 * 4
left = 0
right = len(nums) - 1
res = []

while left <= right:

    if abs(nums[left] - pivot) > abs(nums[right] - pivot):
        res += [a * nums[left] ** 2 + b * nums[left] + c]
        left += 1

    else:
        res += [a * nums[right] ** 2 + b * nums[right] + c]
        right -= 1

if a < 0:
    print res
    exit()

elif not a:
    if b < 0:
        print res[::-1]
        exit()

    elif b > 0:
        print res
        exit()

    else:
        print [c for _ in range(len(nums))]
        exit()

else:
    print res[::-1]
    exit()
