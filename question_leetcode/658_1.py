def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    if not arr or k == 0:
        return []

    left = find_lower_index(arr, x)
    right = left + 1
    res = []

    for _ in range(k):
        if is_lower_index_closer(arr, left, right, x):
            res.append(arr[left])
            left -= 1

        else:
            res.append(arr[right])
            right += 1

    return sorted(res)


def find_lower_index(arr, x):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2

        if arr[mid] < x:
            left = mid

        elif arr[mid] == x:
            right = mid

        else:
            right = mid

    if arr[left] <= x:
        return left

    if arr[right] <= x:
        return right

    return -1


def is_lower_index_closer(arr, left, right, x):
    if left < 0:
        return False

    if right >= len(arr):
        return True

    return x - arr[left] <= arr[right] - x


arr = [1, 2, 3, 4, 5]
k = 4
x = -1
print findClosestElements(arr, k, x)
