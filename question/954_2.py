
#A = [1, 2, 4, 16, 8, 4]
#A = [0, 0]
#A = [1, 2, 4, 8]
#A = [4, -2, 2, -4]
A = [-4, -6, -1, -2, -1, -1, -3, -8]

c = {}

for i in A:

    if not i in c:
        c[i] = 1

    else:
        c[i] += 1

for i in sorted(A, key=abs):

    if 2 * i in c:
        if c[i] and c[2 * i]:
            c[i] -= 1
            c[2 * i] -= 1

    elif not 2 * i in c and c[i] >= 1:
        print False
        exit()

for k, v in c.items():
    if v != 0:
        print False
        exit()

print True