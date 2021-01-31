import bisect

A = [34,23,1,24,75,33,54,8]; K = 60

b = sorted(A)
c = map(lambda x: K - x, sorted(A))

print b
print c

n = 0
x = 0

for i in range(len(b)):
    n = bisect.bisect(b, c[i]) - 1

    if n != -1 and n != i and b[i] + b[n] != K:
        x = max(x, b[i] + b[n])

print x if x != 0 else -1