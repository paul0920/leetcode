
a = [9, 8, 7, 3, 1, 10, 1]
res = float('inf')

for i in a:

    if min(a) < i < res:
        res = i

print res
