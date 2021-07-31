
n = 10

i = 2
count = 0
lookup = [0] * n

while i < n:

    if lookup[i] == 0:

        count += 1

        for j in range(i * 2, n, i):
            lookup[j] = 1

    i += 1

print lookup
print count
