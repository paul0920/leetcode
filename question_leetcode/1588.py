
arr = [1, 4, 2, 5, 3]

res = 0
s = len(arr)

for i in range(s):
    res += arr[i] * (((i + 1) * (s - i) + 1) / 2)

print res
