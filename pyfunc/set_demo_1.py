nums = [2, 2, 3, 1, 10]

nums1 = set(nums)

# This operation removes element from the set.
# If element does not exist, it raises a KeyError.
# The .remove() operation returns None.
nums1.remove(10)

print nums1



sets = {5, 2, 1, 4, 2, 0}

print sets
# pop() returns and removes a random element
print sets.pop()


d = {'f', 2, 1, 3, 'e'}
e = {2, 3, 4}

# 4 doesn't show up in the result
print d - e
