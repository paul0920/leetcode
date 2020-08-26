A = [37, 12, 28, 9, 100, 56, 80, 5, 12]

dic = {a: i + 1 for i, a in enumerate(sorted(set(A)))}

print dic
print map(dic.get, A)  # Pick the items in A and get the values from dict. Return the mapping list

b = (1, 2, 3, 4)  # Tuple
r = map(lambda x: x + x, b)

print b
print r
print list(r)

c = ['sat', 'cat', 'mat']
print list(c[0]), list('sat')
t = map(list, c)

print t
print ""


def show(i):
    return i**2


print map(show, range(5))

# Not working!
# map(list, range(5))

print map(list, [range(5)])
