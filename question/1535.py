

arr = [2, 1, 3, 5, 4, 6, 7]
# arr = [1, 2, 3, 4, 5, 6, 7]
k = 2

arr = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
k = 1000000000


count = 0
curr = arr[0]

# if k >= len(arr):
#     return max(arr)

for idx in range(1, len(arr)):

    if curr < arr[idx]:
        curr = arr[idx]
        count = 0

    count += 1

    if count == k:
        print curr#, count
        exit()

print curr#, count
