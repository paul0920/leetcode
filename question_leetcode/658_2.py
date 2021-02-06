def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    if not arr or k == 0:
        return []

    num = sorted(arr, key=lambda ele: abs(ele - x))[:k]
    # print num

    return sorted(num)


arr = [1, 2, 3, 4, 5]
k = 4
x = -1

arr = [1, 2, 3, 4, 5]
k = 2
x = 2
print findClosestElements(arr, k, x)
