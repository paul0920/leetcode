
arr = [6, 2, 4]
# arr = [6, 5, 4, 3, 5, 6]

res = 0

while len(arr) > 1:

    i = arr.index(min(arr))
    # Be careful about the input of min() is an array
    # and it generates the min element of the input array
    res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)

print res
