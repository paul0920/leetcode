arr = [3, 2, 4, 1]
arr = [3, 2, 4, 6, 5, 1]

size = len(arr)
res = []


def flip_array(m, i):
    m[:i + 1] = m[:i + 1][::-1]


for i_cake in range(size, 0, -1):

    pos = arr.index(i_cake)
    if pos + 1 == i_cake:
        continue

    if pos:
        res += [pos + 1]
        flip_array(arr, pos)

    res += [i_cake]
    flip_array(arr, i_cake - 1)

print res
