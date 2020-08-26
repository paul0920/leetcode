
A = [0, 6, 5, 2, 2, 5, 1, 9, 4]

L = 1
M = 2

arr = []
arr[:] = A[:]

for i in range(len(arr) - 1):
    arr[i + 1] += arr[i]

arr = [0] + arr

i = L
total = float("-INF")

while i < len(arr):

    j = M

    while j < len(arr):

        if i + M <= j or j + L <= i:
            total = max(total, arr[j] - arr[j - M] + arr[i] - arr[i - L])

        j += 1

    i += 1

print total
