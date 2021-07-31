import collections


def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points:
        return 0

    n = len(points)
    max_count = 0

    for i in range(n):
        duplicate_node = 1
        slop_to_count = collections.defaultdict(int)
        curr_count = 0

        for j in range(i + 1, n):
            if points[i] == points[j]:
                duplicate_node += 1
                continue

            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            num = gcd(dx, dy)
            dx /= num
            dy /= num

            slop_to_count[(dx, dy)] += 1
            curr_count = max(curr_count, slop_to_count[(dx, dy)])

        max_count = max(max_count, curr_count + duplicate_node)

    return max_count


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print maxPoints(points)

print gcd(9, 0)
print gcd(0, 0)
