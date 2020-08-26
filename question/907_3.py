
# A = [3, 1, 2, 4]
A = [3, 1, 1, 4]
# A = [6, 2, 4, 1, 1, 0, 7]

n, mod = len(A), 10**9 + 7
left, right = [0] * n, [0] * n
s1, s2 = [], []

for i in range(n):

    count = 1

    # Only set "=" and count the same values in either s1 or s2.
    # Otherwise, the group size will be double counted
    while s1 and s1[-1][0] >= A[i]:
        count += s1.pop()[1]
    left[i] = count

    s1.append([A[i], count])
    print left, s1

print ""

for i in range(n)[::-1]:

    count = 1

    # Only set "=" and count the same values in either s1 or s2.
    # Otherwise, the group size will be double counted
    while s2 and s2[-1][0] > A[i]:
        count += s2.pop()[1]
    right[i] = count

    s2.append([A[i], count])
    print right, s2

print sum(a * l * r for a, l, r in zip(A, left, right)) % mod
