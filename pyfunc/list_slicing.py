
p1 = ['a', 'b', 'c']
n1 = [1, 2, 3]

p2 = ['a', 'b', 'c']
n2 = [1, 2, 3]

p3 = ['a', 'b', 'c']
n3 = [1, 2, 3]

p1[1:1] = n1[:]
p2[1:2] = n2[:]
p3[1:3] = n3[:]

print "p1[1:1] =", p1
print "p2[1:2] =", p2
print "p3[1:3] =", p3
