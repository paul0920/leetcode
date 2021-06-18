import heapq


def mergekSortedArrays(arrays):
    # write your code here
    if not arrays:
        return []

    heap = []
    res = []

    for i_row, array in enumerate(arrays):
        if not array:
            continue

        heapq.heappush(heap, (array[0], i_row, 0))

    while heap:
        num, row, col = heapq.heappop(heap)
        res.append(num)

        if col < len(arrays[row]) - 1:
            heapq.heappush(heap, (arrays[row][col + 1], row, col + 1))

    return res


arrays = [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
]
print mergekSortedArrays(arrays)
