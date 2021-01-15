def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    k = len(nums1) + len(nums2)

    if k % 2 == 1:
        return find_kth(nums1, 0, nums2, 0, k // 2 + 1)

    smaller_num = find_kth(nums1, 0, nums2, 0, k // 2)
    bigger_num = find_kth(nums1, 0, nums2, 0, k // 2 + 1)

    return (smaller_num + bigger_num) / 2.0


def find_kth(arr_a, index_a, arr_b, index_b, kth):
    if len(arr_a) == index_a:
        return arr_b[index_b + kth - 1]

    if len(arr_b) == index_b:
        return arr_a[index_a + kth - 1]

    if kth == 1:
        return min(arr_a[index_a], arr_b[index_b])

    half_kth = kth // 2
    if index_a + half_kth <= len(arr_a):
        num_a = arr_a[index_a + half_kth - 1]

    else:
        # num_a = None
        num_a = float("INF")

    if index_b + half_kth <= len(arr_b):
        num_b = arr_b[index_b + half_kth - 1]

    else:
        # num_b = None
        num_b = float("INF")

    # Use "==" to check None instead of "not"
    # if num_b == None or (num_a != None and num_a < num_b):

    # Drop half_kth elements from arr_a and move index_a forward
    if num_a < num_b:
        return find_kth(arr_a, index_a + half_kth, arr_b, index_b, kth - half_kth)

    return find_kth(arr_a, index_a, arr_b, index_b + half_kth, kth - half_kth)


A = [2, 3, 5]
B = [1, 4, 6, 8]

A = [2]
B = [1, 5, 6, 8]
print findMedianSortedArrays(A, B)
