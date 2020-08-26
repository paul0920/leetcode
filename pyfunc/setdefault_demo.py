
# dictionary.setdefault(key name, value)
#
# key name: Required.
# The key name of the item you want to return the value from
#
# value: Optional.
# If the key exists, this parameter has no effect.
# If the key does not exist, this value becomes the key's value
# Default value None


A = [1, 2, 1, 2]
first = {}

for i, v in enumerate(A):
    first.setdefault(v, i)
    print first

print ""

second = {'a': 123}
print second['a']
print second.setdefault('a', 22)
print second.setdefault('b', 22)

print second
