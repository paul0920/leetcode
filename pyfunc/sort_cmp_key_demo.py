# 179. Largest Number

import functools

nums = [3, 30, 34, 5, 9]

# cmp is old python parameter
print sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1 + n2 > n2 + n1 else (1 if n1 + n2 < n2 + n1 else 0))
print "******"


class comp(str):

    def __lt__(self, b):
        return self + b > b + self


nums = sorted(map(str, nums), key=comp, reverse=False)

print nums
print "******"


def cmp_func(x, y):
    """Sorted by value of concatenated string increasingly."""
    if x + y > y + x:
        return 1
    elif x == y:
        return 0
    else:
        return -1


# Build nums contains all numbers in the String format.
nums = [str(num) for num in nums]

# Sort nums by cmp_func decreasingly.
nums.sort(key=functools.cmp_to_key(cmp_func), reverse=True)

print nums
