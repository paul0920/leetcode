
m = [[1, 2, 3, 4],
     [5, 1, 2, 3],
     [9, 5, 1, 2]]

arr = [r1[:-1] == r2[1:] for r1, r2 in zip(m, m[1:])]

print arr
print all(arr)
print ""



# all values true
l = [1, 3, 4, 5]
print all(l), "a"

# all values false
l = [0, False]
print all(l), "b"

# one false value
l = [1, 3, 4, 0]
print all(l), "c"

# one true value
l = [0, False, 5]
print all(l), "d"

# empty iterable
l = []
print all(l), "e"
