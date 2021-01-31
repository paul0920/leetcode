
A = [4,-2,2,-4]

c = {}

for i in A:

    if not i in c:
        c[i] = 1

    else:
        c[i] += 1

for i in sorted(c, key=abs):

    if 2 * i in c:
        if c[i] > c[2 * i]:
            print False
            exit()

        c[2 * i] -= c[i]

    elif not 2 * i in c and c[i] >= 1:
        print False
        exit()

print True

# Runtime: 564 ms, faster than 94.17% of Python online submissions for Array of Doubled Pairs.
# Memory Usage: 14.9 MB, less than 100.00% of Python online submissions for Array of Doubled Pairs.