
a = {1, 100, 200, 300}
b = {1, 2, 300}
c = {1, 300}

print a & b & c

print a & b
print a.intersection(b)

print a | b | c


p = set([1])
q = [1, 2, 3, 4]

print p


p |= set(q)

print p
