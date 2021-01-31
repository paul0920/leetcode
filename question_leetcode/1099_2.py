
A = [34,23,1,24,75,33,54,8]; K = 60

# This is bucket sort. Time complexity is O(n), n = len(A)
b = [0] * 1000
for i in A:
    b[i-1] = 1

c = [i+1 for i, v in enumerate(b) if v]

print c

i, j = 0, len(c)-1
ans = 0
while i < j:
    s = c[i] + c[j]

    if s < K:
        ans = max(ans, s)
        i += 1

    else:
        j -= 1

print ans