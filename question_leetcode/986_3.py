def intervalIntersection(firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(firstList)
    n = len(secondList)
    p1 = 0
    p2 = 0
    res = []

    while p1 < m and p2 < n:
        start_a, end_a = firstList[p1][0], firstList[p1][1]
        start_b, end_b = secondList[p2][0], secondList[p2][1]

        start = max(start_a, start_b)
        end = min(end_a, end_b)

        if start <= end:
            res.append([start, end])

        if end_a < end_b:
            p1 += 1

        else:
            p2 += 1

    return res


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print intervalIntersection(firstList, secondList)
