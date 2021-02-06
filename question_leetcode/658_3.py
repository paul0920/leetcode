def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    if not arr or k == 0:
        return []

    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left) // 2

        # if x - arr[mid] > arr[mid + k] - x: 
        if (arr[mid] + arr[mid + k]) / 2.04 < x:
            left = mid + 1

        else:
            right = mid

    return arr[left: left + k]


arr = [1, 2, 3, 4, 5]
k = 4
x = -1

arr = [1, 1, 1, 10, 10, 10]
k = 1
x = 9
print findClosestElements(arr, k, x)
