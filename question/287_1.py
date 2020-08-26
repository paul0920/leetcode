
# Depending whether there is 0 in the array,
# the starting point is either from the largest index
# or the smallest index

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once.


# array = [0, 3, 1, 3, 4, 2]
# array = [3, 1, 3, 4, 2]

array = [3, 1, 1, 4, 1, 2]

# slow = len(array) - 1
# fast = len(array) - 1
# finder = len(array) - 1

slow = 0
fast = 0
finder = 0


while True:

    print "slow:", slow, "fast:", fast

    slow = array[slow]
    fast = array[array[fast]]

    print "slow:", slow, "fast:", fast
    print ""

    if slow == fast:
        break

print ""

while True:

    print "slow:", slow, "finder:", finder

    slow = array[slow]
    finder = array[finder]

    print "slow:", slow, "finder:", finder
    print ""

    if slow == finder:
        print "duplicate number:", slow
        break
