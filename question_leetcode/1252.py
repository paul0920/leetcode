
n = 2
m = 3
indices = [[0, 1], [1, 1]]

odd_count = 0
rows = [0] * n
cols = [0] * m

# Do XOR (^) bit operation
for i, j in indices:
    rows[i] = rows[i] ^ 1
    cols[j] = cols[j] ^ 1
    print rows, cols

for i in range(n):
    for j in range(m):
        if rows[i] ^ cols[j] == 1:
            odd_count += 1

print odd_count
