
n = 3
k = 2

w = [0, k, k ** 2]
i = 3

while i <= n:
    w.append((w[i - 1] + w[i - 2]) * (k - 1))
    i += 1

print w[n]
