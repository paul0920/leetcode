
import bisect

##    0   1   2   3   4
a = [10, 20, 30, 40, 50]
a = [10, 20, 20, 30, 40, 50]

# Return index of the 1st bigger element
# 21 can be inserted right after index 1
print bisect.bisect(a, 21)
print bisect.bisect_right(a, 21)
print bisect.bisect_left(a, 21)

print ""

# 20 can be inserted at index 1 or index 2
print bisect.bisect(a, 20)
print bisect.bisect_right(a, 20)
print bisect.bisect_left(a, 20)

print ""


################################################################
# Check 324_median_1.py for the correct binary search template
################################################################


left = 0
right = len(a) - 1
v = 20

while left < right:

    mid = (left + right) / 2

    # 1) v >= a[mid] --> bisect.bisect_right
    # 2) v > a[mid] --> bisect.bisect_left
    if v > a[mid]:
        left = mid + 1

    else:
        right = mid


# 1)                    a[left - 1] <= v < a[left] --> bisect.bisect_right
#                       a[left - 1] <= v < a[right]
#
# 2) a[left - 1] < v <= a[left] --> bisect.bisect_left
#    a[left - 1] < v <= a[right]
print left

