import collections

#A = [1, 2, 4, 16, 8, 4]
#A = [0, 0]
#A = [1, 2, 4, 8]
#A = [4, -2, 2, -4]
A = [-4, -6, -1, -2, -1, -1, -3, -8]

c = collections.Counter(A)

for i in sorted(c, key=abs):

    if c[i] > c[2 * i]:
        print False
        exit()

    c[2 * i] -= c[i]

print True